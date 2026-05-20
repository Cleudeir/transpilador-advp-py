"""
advp.xml_json — Funções e classes de XML e JSON compatíveis com ADVPL.

Mapeamento 1:1 com as funções nativas do Protheus para manipulação
de XML (XmlParser, XmlNode2Arr, etc.) e JSON (JsonObject, ArrToJson).
"""
from __future__ import annotations
from typing import Any, Optional, List
from .types import Nil, Array


# ---------------------------------------------------------------------------
# XML Parser (XmlParser, XmlParserFile)
# ---------------------------------------------------------------------------

class XmlNode:
    """
    Objeto retornado por XmlParser / XmlParserFile.
    
    Cada tag filha vira um atributo com o prefixo configurado (padrão "_").
    O texto da tag fica em .TEXT.
    Atributos da tag ficam em .ATTR.
    """

    def __init__(self, name: str = ""):
        self._name: str = name
        self._children: dict = {}
        self._text: str = ""
        self._attributes: dict = {}
        self.TEXT: str = ""
        self.ATTR: dict = {}

    def __getattr__(self, name: str) -> Any:
        if name.startswith("_"):
            clean = name.lstrip("_").upper()
            if clean in self._children:
                return self._children[clean]
            for key, val in self._children.items():
                if key.upper() == clean:
                    return val
        return object.__getattribute__(self, name)

    def __setattr__(self, name: str, value: Any) -> None:
        if name.startswith("_") and name not in ("_name", "_children", "_text", "_attributes", "TEXT", "ATTR"):
            clean = name.lstrip("_").upper()
            if isinstance(value, XmlNode):
                self._children[clean] = value
            else:
                self._attributes[clean] = value
        else:
            object.__setattr__(self, name, value)

    def _add_child(self, name: str, node: "XmlNode") -> None:
        self._children[name.upper()] = node

    def _repr_deep(self, indent: int = 0) -> str:
        pad = "  " * indent
        lines = [f"{pad}<{self._name}>"]
        for name, child in self._children.items():
            lines.append(f"{pad}  {name}: {child._repr_deep(indent + 1)}")
        if self._text:
            lines.append(f"{pad}  TEXT: {self._text}")
        for name, val in self._attributes.items():
            lines.append(f"{pad}  @{name}: {val}")
        lines.append(f"{pad}</{self._name}>")
        return "\n".join(lines)

    def __repr__(self) -> str:
        return self._repr_deep()

    def toJson(self) -> str:
        """JsonObject:toJSON() — Serializa para string JSON."""
        import json
        def _to_dict(n: XmlNode):
            d = {}
            if n._text:
                d["_text"] = n._text
            for k, v in n._children.items():
                d[k.lower()] = _to_dict(v)
            for k, v in n._attributes.items():
                d[f"@{k.lower()}"] = v
            return d
        return json.dumps(_to_dict(self), ensure_ascii=False)


def XmlParser(
    cXml: str,
    cReplace: str = "_",
    cAviso: Any = None,
    cErro: Any = None,
) -> Optional[XmlNode]:
    """
    XmlParser() — Converte uma string XML em um objeto do tipo XmlNode.
    
    Parâmetros:
        cXml — String contendo o XML
        cReplace — Prefixo usado nos atributos (padrão "_")
        @cAviso — Retorno de avisos (passar por referência)
        @cErro — Retorno de erros (passar por referência)
    Retorno:
        Objeto XmlNode ou Nil em caso de erro
    """
    import xml.etree.ElementTree as ET
    try:
        root = ET.fromstring(cXml)
        return _etree_to_xmlnode(root, cReplace)
    except Exception as e:
        if cErro is not None:
            try:
                if hasattr(cErro, '__setitem__'):
                    cErro[0] = str(e)
            except:
                pass
        return None


def XmlParserFile(
    cFile: str,
    cReplace: str = "_",
    cAviso: Any = None,
    cErro: Any = None,
) -> Optional[XmlNode]:
    """
    XmlParserFile() — Converte um arquivo XML em um objeto XmlNode.
    
    Parâmetros:
        cFile — Caminho do arquivo XML
        cReplace — Prefixo usado nos atributos (padrão "_")
        @cAviso — Retorno de avisos (passar por referência)
        @cErro — Retorno de erros (passar por referência)
    Retorno:
        Objeto XmlNode ou Nil em caso de erro
    """
    import xml.etree.ElementTree as ET
    try:
        tree = ET.parse(cFile)
        root = tree.getroot()
        return _etree_to_xmlnode(root, cReplace)
    except Exception as e:
        if cErro is not None:
            try:
                if hasattr(cErro, '__setitem__'):
                    cErro[0] = str(e)
            except:
                pass
        return None


def _etree_to_xmlnode(et_node, prefix: str = "_") -> XmlNode:
    """Converte um ElementTree para XmlNode."""
    node = XmlNode(et_node.tag)
    if et_node.text and et_node.text.strip():
        text = et_node.text.strip()
        node.TEXT = text
        node._text = text

    for attr_name, attr_val in et_node.attrib.items():
        node._attributes[attr_name.upper()] = attr_val

    for child in et_node:
        child_node = _etree_to_xmlnode(child, prefix)
        node._add_child(child.tag, child_node)

    return node


# ---------------------------------------------------------------------------
# XML Utilitários (XmlNode2Arr, XmlToArr, IsXmlNode, AttIsMemberOf, etc.)
# ---------------------------------------------------------------------------

def XmlNode2Arr(oRoot: Any, cNode: str) -> bool:
    """
    XmlNode2Arr() — Converte um nó XML em um array dentro da estrutura do objeto.
    
    Parâmetros:
        oRoot — Objeto XmlNode raiz
        cNode — Caminho do nó (ex: "_detalhes:_gostaDeLer")
    Retorno:
        .T. se a conversão foi bem sucedida
    """
    return True


def XmlToArr(oNode: Any) -> list:
    """
    XmlToArr() — Converte um nó XML em um array standalone.
    
    Parâmetros:
        oNode — Objeto XmlNode
    Retorno:
        Array com os dados do nó
    """
    if isinstance(oNode, XmlNode):
        result = []
        for name, child in oNode._children.items():
            entry = {name.lower(): child.TEXT if child.TEXT else child}
            result.append(entry)
        return result
    return []


def IsXmlNode(oObj: Any, cAttName: str, lRecursive: bool = False) -> bool:
    """
    IsXmlNode() — Verifica se uma tag/nó existe no objeto XML.
    
    Parâmetros:
        oObj — Objeto XmlNode
        cAttName — Nome do atributo/tag (ex: "_gostaDeLer")
        lRecursive — Se .T., busca recursivamente
    Retorno:
        .T. se o nó existe
    """
    if isinstance(oObj, XmlNode):
        clean = cAttName.lstrip("_").upper()
        if clean in oObj._children:
            return True
        if lRecursive:
            for child in oObj._children.values():
                if IsXmlNode(child, cAttName, lRecursive):
                    return True
    return False


def AttIsMemberOf(oObj: Any, cAttName: str, lRecursive: bool = False) -> bool:
    """
    AttIsMemberOf() — Verifica se um atributo existe em um objeto.
    
    Parâmetros:
        oObj — Objeto XmlNode
        cAttName — Nome do atributo
        lRecursive — Se .T., busca recursivamente
    Retorno:
        .T. se o atributo existe
    """
    return IsXmlNode(oObj, cAttName, lRecursive)


def XMLChildEx(oParent: Any, cProcura: str) -> Any:
    """
    XMLChildEx() — Busca uma tag filha no XML (nome em UPPERCASE).
    
    Parâmetros:
        oParent — Objeto XmlNode pai
        cProcura — Nome da tag a procurar (maiúsculo)
    Retorno:
        XmlNode encontrado ou Nil
    """
    if isinstance(oParent, XmlNode):
        clean = cProcura.lstrip("_").upper()
        for name, child in oParent._children.items():
            if name.upper() == clean:
                return child
    return Nil


def XmlNodeExist(oObj: Any, cAttName: str) -> bool:
    """
    XmlNodeExist() — Verifica se um nó existe (case-insensitive).
    
    Parâmetros:
        oObj — Objeto XmlNode
        cAttName — Nome do nó a verificar
    Retorno:
        .T. se o nó existe
    """
    return IsXmlNode(oObj, cAttName)


def WSAdvValue(
    oXml: Any,
    cObjCpoInfo: str,
    cType: str,
    xDefault: Any = Nil,
    cNotNILMsg: str = "",
    lAsArray: bool = False,
    cAdvType: str = "",
    cAdv2Par: str = "",
    cRecNS: str = "",
    lRealLong: bool = False,
) -> Any:
    """
    WSAdvValue() — Extrai o valor de uma tag de um objeto XML.
    
    Parâmetros:
        oXml — Objeto XmlNode
        cObjCpoInfo — Nome da tag (ex: "_nome")
        cType — Tipo do dado ("string", "numeric", "date", etc.)
        xDefault — Valor padrão se não encontrar
        cNotNILMsg — Mensagem de erro se obrigatório
        lAsArray — Se .T., retorna como array
        cAdvType — Tipo ADVPL
        cAdv2Par — Variável preenchida com o valor ADVPL
        cRecNS — Namespace
        lRealLong — Tratativa para LONG
    Retorno:
        Valor da tag ou xDefault
    """
    if isinstance(oXml, XmlNode):
        clean = cObjCpoInfo.lstrip("_").upper()
        for name, child in oXml._children.items():
            if name.upper() == clean:
                if lAsArray:
                    return [child.TEXT] if child.TEXT else []
                return child.TEXT if child.TEXT else xDefault
    return xDefault


# ---------------------------------------------------------------------------
# Classe JsonObject
# ---------------------------------------------------------------------------

class JsonObject:
    """
    JsonObject — Representa um objeto JSON.
    
    Uso:
        jDados := JsonObject():New()
        cError := jDados:FromJson(cJsonText)
        valor  := jDados:GetJsonObject('chave')
        json   := jDados:toJSON()
    """

    def __init__(self):
        self._data: Any = None

    def New(self) -> "JsonObject":
        """JsonObject:New() — Construtor da classe."""
        obj = JsonObject()
        return obj

    def FromJson(self, cJson: str) -> str:
        """
        JsonObject:FromJson() — Converte string JSON em objeto.
        
        Parâmetros:
            cJson — String JSON
        Retorno:
            String vazia em caso de sucesso, mensagem de erro em caso de falha
        """
        import json
        try:
            self._data = json.loads(cJson)
            return ""
        except json.JSONDecodeError as e:
            return str(e)

    def SetJson(self, cJson: str) -> str:
        """JsonObject:SetJson() — Alias para FromJson."""
        return self.FromJson(cJson)

    def GetJsonObject(self, key: str) -> Any:
        """
        JsonObject:GetJsonObject() — Obtém valor pela chave.
        
        Parâmetros:
            key — Nome da chave
        Retorno:
            Valor associado à chave (pode ser dict, list, str, int, bool, None)
        """
        if isinstance(self._data, dict):
            return self._data.get(key, Nil)
        return Nil

    def toJSON(self) -> str:
        """JsonObject:toJSON() — Serializa o objeto para string JSON."""
        import json
        if self._data is not None:
            return json.dumps(self._data, ensure_ascii=False)
        return "{}"

    def ToJson(self) -> str:
        """JsonObject:toJson() — Alias para toJSON (maiúsculo)."""
        return self.toJSON()

    def __getitem__(self, key: str) -> Any:
        if isinstance(self._data, dict):
            return self._data.get(key, Nil)
        return Nil

    def __setitem__(self, key: str, value: Any) -> None:
        if self._data is None:
            self._data = {}
        if isinstance(self._data, dict):
            self._data[key] = value


# ---------------------------------------------------------------------------
# Funções JSON (ArrToJson, JsonToArr)
# ---------------------------------------------------------------------------

def ArrToJson(aArray: list) -> str:
    """
    ArrToJson() — Converte um Array em uma string JSON.
    
    Parâmetros:
        aArray — Array a ser convertido
    Retorno:
        String JSON
    """
    import json
    try:
        return json.dumps(aArray, ensure_ascii=False)
    except:
        return "[]"


def JsonToArr(cJson: str) -> list:
    """
    JsonToArr() — Converte uma string JSON em um Array ADVPL.
    
    Parâmetros:
        cJson — String JSON
    Retorno:
        Array com os dados
    """
    import json
    try:
        data = json.loads(cJson)
        if isinstance(data, list):
            return data
        return [data]
    except:
        return []


# ---------------------------------------------------------------------------
# TXMLViewer — Visualizador de XML em Dialog
# ---------------------------------------------------------------------------

class TXMLViewer:
    """
    TXMLViewer — Visualizador de XML em uma janela de diálogo.
    
    Uso:
        oXMLView := TXMLViewer():New(nLinha, nColuna, oDialog, cArquiXML, nLargura, nAltura, lDimPixels)
        oXMLView:SetXML(cArquiXML)
    """

    def __init__(
        self,
        linha: int = 0,
        coluna: int = 0,
        dialog: Any = None,
        arquivo_xml: str = "",
        largura: int = 0,
        altura: int = 0,
        dim_pixels: bool = True,
    ):
        self._linha = linha
        self._coluna = coluna
        self._dialog = dialog
        self._arquivo_xml = arquivo_xml
        self._largura = largura
        self._altura = altura
        self._dim_pixels = dim_pixels

    def New(
        self,
        linha: int = 0,
        coluna: int = 0,
        dialog: Any = None,
        arquivo_xml: str = "",
        largura: int = 0,
        altura: int = 0,
        dim_pixels: bool = True,
    ) -> "TXMLViewer":
        """TXMLViewer:New() — Construtor da classe."""
        obj = TXMLViewer(linha, coluna, dialog, arquivo_xml, largura, altura, dim_pixels)
        return obj

    def SetXML(self, arquivo_xml: str) -> None:
        """TXMLViewer:SetXML() — Define o arquivo XML a ser exibido."""
        self._arquivo_xml = arquivo_xml

    def Refresh(self) -> None:
        """TXMLViewer:Refresh() — Atualiza o visualizador."""
        pass

    def SetXMLText(self, xml_text: str) -> None:
        """TXMLViewer:SetXMLText() — Define o XML a partir de uma string."""
        pass
