"""
advp.protheus — APIs específicas do Protheus/TOTVS.

Stubs para funções de negócio e infraestrutura do Protheus.
"""
from __future__ import annotations
from typing import Any, Callable, Optional, List
from .types import Nil, Array


# ---------------------------------------------------------------------------
# Parâmetros do sistema (SX6)
# ---------------------------------------------------------------------------

def SuperGetMV(param: str, default: Any = None, company: str = "") -> Any:
    """
    SuperGetMV() — Obtém o valor de um parâmetro do SX6.
    Exemplo:
        mv_par01 = SuperGetMV("MV_CFOP")
    """
    return default


def GetMV(param: str, default: Any = None) -> Any:
    """GetMV() — Versão simples do SuperGetMV."""
    return default


def PutMV(param: str, value: Any) -> bool:
    """PutMV() — Grava o valor de um parâmetro no SX6."""
    return True


# ---------------------------------------------------------------------------
# Funções de Numeração (SX5 / SE8)
# ---------------------------------------------------------------------------

def GetSX5Num(table: str, order: str) -> str:
    """GetSX5Num() — Obtém próximo número do SX5."""
    return ""


def GetNewNum(field: str, alias: str = "") -> str:
    """GetNewNum() — Gera o próximo número automático."""
    return ""


def GetNextC(seq: str) -> str:
    """GetNextC() — Próximo código sequencial (letras+números)."""
    return ""


# ---------------------------------------------------------------------------
# Ambiente / Usuário
# ---------------------------------------------------------------------------

def CEMPRESA() -> str:
    """cEmpresa — Código da empresa logada."""
    return "01"


def CFILIAL() -> str:
    """cFilial — Código da filial logada."""
    return "01"


def CUSUARIO() -> str:
    """cUsuario — Usuário logado."""
    return "ADMIN"


def CNOME() -> str:
    """cNome — Nome do usuário logado."""
    return "Administrador"


def RADRetorno(value: Any = Nil) -> None:
    """RADRetorno() — Marca retorno em relatórios RAD."""
    pass


# ---------------------------------------------------------------------------
# Objetos de modelo (FWFormModel)
# ---------------------------------------------------------------------------

class oModel:
    """
    Proxy para FWFormModel do Protheus.

    Permite leitura/escrita de campos do modelo de formulário:
        model = oModel()
        cod = model.getValue("A1_COD")
        model.setValue("A1_NOME", "Cliente Teste")
    """

    def __init__(self):
        self._data: dict = {}
        self._grids: dict = {}

    def getValue(self, field: str) -> Any:
        """oModel:getValue() — Lê o valor de um campo do cabeçalho."""
        return self._data.get(field, "")

    def setValue(self, field: str, value: Any) -> bool:
        """oModel:setValue() — Grava o valor de um campo do cabeçalho."""
        self._data[field] = value
        return True

    def getCell(self, grid: str, row: int, col: str) -> Any:
        """oModel:getCell() — Lê um campo de uma linha da grid."""
        return self._grids.get(grid, {}).get((row, col), "")

    def setCell(self, grid: str, row: int, col: str, value: Any) -> bool:
        """oModel:setCell() — Grava um campo em uma linha da grid."""
        if grid not in self._grids:
            self._grids[grid] = {}
        self._grids[grid][(row, col)] = value
        return True

    def getLineCount(self, grid: str) -> int:
        """oModel:getLineCount() — Número de linhas da grid."""
        rows = {r for r, _ in self._grids.get(grid, {}).keys()}
        return len(rows)

    def addLine(self, grid: str) -> bool:
        """oModel:addLine() — Adiciona linha na grid."""
        return True

    def delLine(self, grid: str) -> bool:
        """oModel:delLine() — Remove linha atual da grid."""
        return True

    def isValidated(self) -> bool:
        """oModel:isValidated() — Verifica se o modelo está validado."""
        return True

    def activate(self, action: int = 3) -> None:
        """oModel:activate() — Ativa o modelo (3=inclusão, 4=alteração, 5=exclusão)."""
        pass

    def deActivate(self) -> None:
        """oModel:deActivate() — Desativa o modelo."""
        pass

    def commitData(self) -> bool:
        """oModel:commitData() — Salva os dados do modelo."""
        return True


# ---------------------------------------------------------------------------
# Relatórios e impressão
# ---------------------------------------------------------------------------

class oReport:
    """Proxy simplificado para FWPrintSetup."""

    def __init__(self, title: str = "Relatório"):
        self.title = title
        self._sections: List[dict] = []

    def init(self) -> None:
        """oReport:Init() — Inicializa o relatório."""
        pass

    def finish(self) -> None:
        """oReport:Finish() — Finaliza o relatório."""
        pass

    def addSection(self, title: str = "") -> "oSection":
        """Adiciona seção ao relatório."""
        s = oSection(title)
        self._sections.append(s)
        return s


class oSection:
    """Seção de um relatório."""

    def __init__(self, title: str = ""):
        self.title = title

    def addTo(self, report: oReport) -> None:
        pass

    def init(self) -> None:
        pass

    def finish(self) -> None:
        pass


# ---------------------------------------------------------------------------
# Browse / Grid (FWBrowse, FWBrwColumn, FWTemporaryTable)
# ---------------------------------------------------------------------------

class FWBrowse:
    """
    FWBrowse — Grid/Browse para exibição de dados em tela.
    
    Uso:
        oBrowse := FWBrowse():New()
        oBrowse:SetAlias("SA1")
        oBrowse:AddColumn("Código", {|o| SA1->A1_COD}, "C", 6, 0)
        oBrowse:AddLegend("SA1->A1_MSBLQL == '1'", "RED", "Bloqueado")
        oBrowse:Activate()
    """

    def __init__(self):
        self._alias: str = ""
        self._query: str = ""
        self._columns: list = []
        self._legends: list = []
        self._filter: str = ""
        self._owner: Any = None
        self._font: Any = None
        self._edit_cell: bool = False
        self._edit_valid: Any = None
        self.lHeaderClick: bool = False
        self.nCol: int = 0
        self.nRow: int = 0

    def New(self) -> "FWBrowse":
        """FWBrowse:New() — Construtor da classe."""
        return FWBrowse()

    def SetAlias(self, alias: str) -> None:
        """FWBrowse:SetAlias() — Define o alias da tabela."""
        self._alias = alias

    def SetQuery(self, query: str) -> None:
        """FWBrowse:SetQuery() — Define a query SQL do browse."""
        self._query = query

    def AddColumn(self, title: str, data_block: Any, data_type: str = "", size: int = 0, decimal: int = 0) -> "FWBrowse":
        """FWBrowse:AddColumn() — Adiciona coluna ao browse."""
        col = FWBrwColumn()
        col.SetTitle(title)
        col.SetData(data_block)
        col.SetType(data_type)
        col.SetSize(size)
        col.SetDecimal(decimal)
        self._columns.append(col)
        return self

    def SetColumns(self, columns: list) -> None:
        """FWBrowse:SetColumns() — Define as colunas do browse a partir de array de FWBrwColumn."""
        self._columns = list(columns)

    def SetFilter(self, filter_expr: str) -> None:
        """FWBrowse:SetFilter() — Define filtro do browse."""
        self._filter = filter_expr

    def SetOwner(self, owner: Any) -> None:
        """FWBrowse:SetOwner() — Define o painel dono do browse."""
        self._owner = owner

    def SetFontBrowse(self, font: Any) -> None:
        """FWBrowse:SetFontBrowse() — Define a fonte do browse."""
        self._font = font

    def SetDataTable(self) -> None:
        """FWBrowse:SetDataTable() — Define que o browse usa tabela de dados."""
        pass

    def SetEditCell(self, edit: bool, valid_block: Any = None) -> None:
        """FWBrowse:SetEditCell() — Habilita edição de células."""
        self._edit_cell = edit
        self._edit_valid = valid_block

    def DisableFilter(self) -> None:
        """FWBrowse:DisableFilter() — Desabilita o filtro."""
        pass

    def DisableConfig(self) -> None:
        """FWBrowse:DisableConfig() — Desabilita a configuração."""
        pass

    def DisableReport(self) -> None:
        """FWBrowse:DisableReport() — Desabilita o relatório."""
        pass

    def DisableSeek(self) -> None:
        """FWBrowse:DisableSeek() — Desabilita a pesquisa."""
        pass

    def DisableSaveConfig(self) -> None:
        """FWBrowse:DisableSaveConfig() — Desabilita salvar configuração."""
        pass

    def AddLegend(self, condition: str, color: str, text: str) -> "FWBrowse":
        """FWBrowse:AddLegend() — Adiciona legenda (condição, cor, descrição)."""
        self._legends.append((condition, color, text))
        return self

    def Activate(self) -> None:
        """FWBrowse:Activate() — Ativa o browse."""
        pass

    def Refresh(self) -> None:
        """FWBrowse:Refresh() — Atualiza o browse."""
        pass

    def GoTop(self) -> None:
        """FWBrowse:GoTop() — Vai ao primeiro registro."""
        pass

    def GoBottom(self) -> None:
        """FWBrowse:GoBottom() — Vai ao último registro."""
        pass

    def Skip(self, n: int = 1) -> None:
        """FWBrowse:Skip() — Avança n registros."""
        pass

    def Eof(self) -> bool:
        """FWBrowse:Eof() — Verifica fim do browse."""
        return True

    def Bof(self) -> bool:
        """FWBrowse:Bof() — Verifica início do browse."""
        return True


class FWBrwColumn:
    """
    FWBrwColumn — Coluna para FWBrowse.
    
    Uso:
        oColumn := FWBrwColumn():New()
        oColumn:SetTitle("Código")
        oColumn:SetData({|| SA1->A1_COD})
        oColumn:SetType("C")
        oColumn:SetSize(6)
    """

    def __init__(self):
        self._data: Any = None
        self._title: str = ""
        self._type: str = ""
        self._size: int = 0
        self._decimal: int = 0
        self._picture: str = ""
        self._edit: bool = False
        self._read_var: str = ""
        self._valid: Any = None

    def New(self) -> "FWBrwColumn":
        """FWBrwColumn:New() — Construtor da classe."""
        return FWBrwColumn()

    def SetData(self, data_block: Any) -> None:
        """FWBrwColumn:SetData() — Define o bloco de dados da coluna."""
        self._data = data_block

    def SetTitle(self, title: str) -> None:
        """FWBrwColumn:SetTitle() — Define o título da coluna."""
        self._title = title

    def SetType(self, data_type: str) -> None:
        """FWBrwColumn:SetType() — Define o tipo da coluna (C, N, D, L)."""
        self._type = data_type

    def SetSize(self, size: int) -> None:
        """FWBrwColumn:SetSize() — Define o tamanho da coluna."""
        self._size = size

    def SetDecimal(self, decimal: int) -> None:
        """FWBrwColumn:SetDecimal() — Define o número de decimais."""
        self._decimal = decimal

    def SetPicture(self, picture: str) -> None:
        """FWBrwColumn:SetPicture() — Define a máscara/picture."""
        self._picture = picture

    def SetEdit(self, edit: bool) -> None:
        """FWBrwColumn:SetEdit() — Habilita/desabilita edição."""
        self._edit = edit

    def SetReadVar(self, var_name: str) -> None:
        """FWBrwColumn:SetReadVar() — Define variável de leitura."""
        self._read_var = var_name

    def SetValid(self, valid_block: Any) -> None:
        """FWBrwColumn:SetValid() — Define bloco de validação."""
        self._valid = valid_block

    def SetField(self, field: str) -> None:
        """FWBrwColumn:SetField() — Define o campo associado."""
        pass

    def SetAlign(self, align: str) -> None:
        """FWBrwColumn:SetAlign() — Define o alinhamento."""
        pass


class FWTemporaryTable:
    """
    FWTemporaryTable — Tabela temporária no Protheus.
    
    Uso:
        oTempTable := FWTemporaryTable():New("TMPSBM")
        oTempTable:SetFields(aFields)
        oTempTable:AddIndex("1", {"XXCODIGO"})
        oTempTable:Create()
        ...
        oTempTable:Delete()
    """

    def __init__(self, alias: str = ""):
        self._alias: str = alias
        self._fields: list = []
        self._indices: list = []

    def New(self, alias: str = "") -> "FWTemporaryTable":
        """FWTemporaryTable:New() — Construtor da classe."""
        obj = FWTemporaryTable(alias)
        return obj

    def SetFields(self, fields: list) -> None:
        """
        FWTemporaryTable:SetFields() — Define os campos.
        
        Cada campo: {nome, tipo, tamanho, decimais}
        """
        self._fields = list(fields)

    def AddIndex(self, order: str, fields: list) -> None:
        """FWTemporaryTable:AddIndex() — Adiciona índice."""
        self._indices.append((order, list(fields)))

    def Create(self) -> None:
        """FWTemporaryTable:Create() — Cria a tabela temporária no banco."""
        pass

    def Delete(self) -> None:
        """FWTemporaryTable:Delete() — Exclui a tabela temporária."""
        pass


# ---------------------------------------------------------------------------
# Model Browse (FWMBrowse / mBrowse)
# ---------------------------------------------------------------------------

class FWMBrowse:
    """
    FWMBrowse — Browse de cadastro com menu de ações (Incluir, Alterar, Excluir).
    
    Uso:
        oBrowse := FWMBrowse():New()
        oBrowse:SetAlias("SBM")
        oBrowse:SetDescription("Grupo de Produtos")
        oBrowse:DisableDetails()
        oBrowse:AddLegend("SBM->BM_PROORI == '1'", "BLACK", "Prioritário")
        oBrowse:Activate()
    """

    def __init__(self):
        self._alias: str = ""
        self._description: str = ""
        self._legends: list = []
        self._disable_details: bool = False

    def New(self) -> "FWMBrowse":
        """FWMBrowse:New() — Construtor da classe."""
        return FWMBrowse()

    def SetAlias(self, alias: str) -> None:
        """FWMBrowse:SetAlias() — Define o alias da tabela."""
        self._alias = alias

    def SetDescription(self, description: str) -> None:
        """FWMBrowse:SetDescription() — Define a descrição do cadastro."""
        self._description = description

    def DisableDetails(self) -> None:
        """FWMBrowse:DisableDetails() — Desabilita detalhes."""
        self._disable_details = True

    def AddLegend(self, condition: str, color: str, text: str) -> "FWMBrowse":
        """FWMBrowse:AddLegend() — Adiciona legenda."""
        self._legends.append((condition, color, text))
        return self

    def Activate(self) -> None:
        """FWMBrowse:Activate() — Ativa o browse."""
        pass

    def Refresh(self) -> None:
        """FWMBrowse:Refresh() — Atualiza o browse."""
        pass


def mBrowse(
    nTop: int = 1,
    nLeft: int = 1,
    nBottom: Any = None,
    nRight: Any = None,
    cAlias: str = "",
    bLine: Any = None,
    cTitle: str = "",
    cFilter: str = "",
    cFields: str = "",
    nCol: int = 0,
    aCores: list = None,
    nWidth: int = 0,
    cSort: str = "",
) -> Any:
    """
    mBrowse() — Função de browse padrão do Protheus.
    
    Parâmetros:
        nTop, nLeft, nBottom, nRight — Posição na tela
        cAlias — Alias da tabela
        bLine — Bloco de código por linha
        cTitle — Título da janela
        cFilter — Filtro
        cFields — Campos
        nCol — Coluna inicial
        aCores — Cores condicionais {{condição, cor}, ...}
        nWidth — Largura
        cSort — Ordenação
    """
    return Nil


# ---------------------------------------------------------------------------
# Browse com Marcação (FWMarkBrowse)
# ---------------------------------------------------------------------------

class FWMarkBrowse:
    """
    FWMarkBrowse — Browse com marcação de registros.
    
    Uso:
        oBrowse := FWMarkBrowse():New()
        oBrowse:SetFieldMark("A1_X_MARCA")
        oBrowse:SetAlias("SA1")
        oBrowse:Activate()
    """

    def __init__(self):
        self._alias: str = ""
        self._field_mark: str = ""
        self._columns: list = []

    def New(self) -> "FWMarkBrowse":
        """FWMarkBrowse:New() — Construtor da classe."""
        return FWMarkBrowse()

    def SetFieldMark(self, field: str) -> None:
        """FWMarkBrowse:SetFieldMark() — Define o campo de marcação."""
        self._field_mark = field

    def SetAlias(self, alias: str) -> None:
        """FWMarkBrowse:SetAlias() — Define o alias da tabela."""
        self._alias = alias

    def AddColumn(self, title: str, data_block: Any, data_type: str = "", size: int = 0, decimal: int = 0) -> "FWMarkBrowse":
        """FWMarkBrowse:AddColumn() — Adiciona coluna."""
        return self

    def Activate(self) -> None:
        """FWMarkBrowse:Activate() — Ativa o browse."""
        pass

def TCSQLQuery(sql: str) -> Any:
    """TCSQLQuery() — Executa uma SQL e retorna resultado."""
    return None


def FWExecView(alias: str, model: oModel, action: int = 3) -> bool:
    """FWExecView() — Abre a view de um cadastro."""
    return True


def ExecAuto(func: Callable, *params: Any) -> bool:
    """ExecAuto() — Executa uma função automática do Protheus."""
    return True




# ---------------------------------------------------------------------------
# Funções de validação CPF/CNPJ
# ---------------------------------------------------------------------------

def ValidCpf(cpf: str) -> bool:
    """ValidCpf() — Valida um CPF."""
    cpf = "".join(c for c in str(cpf) if c.isdigit())
    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return False
    # Dígito verificador 1
    s = sum(int(cpf[i]) * (10 - i) for i in range(9)) % 11
    d1 = 0 if s < 2 else 11 - s
    # Dígito verificador 2
    s = sum(int(cpf[i]) * (11 - i) for i in range(10)) % 11
    d2 = 0 if s < 2 else 11 - s
    return cpf[9] == str(d1) and cpf[10] == str(d2)


def ValidCnpj(cnpj: str) -> bool:
    """ValidCnpj() — Valida um CNPJ."""
    cnpj = "".join(c for c in str(cnpj) if c.isdigit())
    if len(cnpj) != 14 or cnpj == cnpj[0] * 14:
        return False
    weights1 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    weights2 = [6] + weights1
    d1 = sum(int(cnpj[i]) * weights1[i] for i in range(12)) % 11
    d1 = 0 if d1 < 2 else 11 - d1
    d2 = sum(int(cnpj[i]) * weights2[i] for i in range(13)) % 11
    d2 = 0 if d2 < 2 else 11 - d2
    return cnpj[12] == str(d1) and cnpj[13] == str(d2)
