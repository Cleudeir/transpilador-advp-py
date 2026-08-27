"""
advp.ui — Funções de interface do usuário compatíveis com ADVPL.

Mapeiam para as funções de diálogo nativas do Protheus.
"""
from __future__ import annotations
from typing import Any, Callable, Optional


# ---------------------------------------------------------------------------
# Diálogos básicos
# ---------------------------------------------------------------------------


# ---------------------------------------------------------------------------
# MsNewProcess — Processo com barra de progresso
# ---------------------------------------------------------------------------

class MsNewProcess:
    """
    MsNewProcess — Processo com barra de progresso (réguas).
    
    Uso:
        oProcess := MsNewProcess():New({|lEnd| u_Processar(lEnd)}, "Processando", "Aguarde...", .T.)
        oProcess:Activate()
    
    Com régua dupla:
        oProcess:SetRegua1(nTotal)
        oProcess:IncRegua1("Processando...")
        oProcess:SetRegua2(nSubTotal)
        oProcess:IncRegua2("Sub-processo...")
    """

    def __init__(self):
        self._block: Any = None
        self._title: str = ""
        self._message: str = ""
        self._async: bool = False
        self._regua1: int = 0
        self._regua1_current: int = 0
        self._regua2: int = 0
        self._regua2_current: int = 0
        self._text: str = ""

    def New(self, block: Any, title: str = "", message: str = "", async_mode: bool = False) -> "MsNewProcess":
        """MsNewProcess:New() — Construtor da classe.
        
        Parâmetros:
            block — Bloco de código a ser executado {|| ...} ou {|lEnd| ...}
            title — Título da janela
            message — Mensagem exibida
            async_mode — Execução assíncrona (.T.) ou síncrona (.F.)
        """
        obj = MsNewProcess()
        obj._block = block
        obj._title = title
        obj._message = message
        obj._async = async_mode
        return obj

    def Activate(self) -> None:
        """MsNewProcess:Activate() — Ativa e executa o processo."""
        if callable(self._block):
            self._block()

    def SetRegs(self, total: int) -> "MsNewProcess":
        """MsNewProcess:SetRegs() — Define o total de registros para régua simples."""
        self._regua1 = total
        self._regua1_current = 0
        return self

    def IncRegs(self, step: int = 1) -> "MsNewProcess":
        """MsNewProcess:IncRegs() — Incrementa a régua simples."""
        self._regua1_current += step
        return self

    def SetText(self, text: str) -> "MsNewProcess":
        """MsNewProcess:SetText() — Define o texto de status."""
        self._text = text
        return self

    def SetRegua1(self, total: int) -> "MsNewProcess":
        """MsNewProcess:SetRegua1() — Define o total da régua 1."""
        self._regua1 = total
        self._regua1_current = 0
        return self

    def IncRegua1(self, text: str = "") -> "MsNewProcess":
        """MsNewProcess:IncRegua1() — Incrementa a régua 1 com mensagem."""
        self._regua1_current += 1
        if text:
            self._text = text
        return self

    def SetRegua2(self, total: int) -> "MsNewProcess":
        """MsNewProcess:SetRegua2() — Define o total da régua 2."""
        self._regua2 = total
        self._regua2_current = 0
        return self

    def IncRegua2(self, text: str = "") -> "MsNewProcess":
        """MsNewProcess:IncRegua2() — Incrementa a régua 2 com mensagem."""
        self._regua2_current += 1
        if text:
            self._text = text
        return self


# ---------------------------------------------------------------------------
# FWDialogModal — Janela de diálogo modal
# ---------------------------------------------------------------------------

class FWDialogModal:
    """
    FWDialogModal — Janela de diálogo modal personalizável.
    
    Uso:
        oDlg := FWDialogModal():New()
        oDlg:SetTitle("Cadastro")
        oDlg:SetSize(300, 400)
        oDlg:CreateDialog()
        oDlg:AddButton("Confirmar", {|| oDlg:DeActivate()})
        oDlg:Activate()
    
    Com GetPanel:
        oPanel := oDlg:GetPanel()
        oDlg:AddSay(oPanel, 10, 10, "Nome:")
        oDlg:AddGet(oPanel, 10, 100, {|u| Iif(u == Nil, cVar, cVar := u)}, 200, 20)
    """

    def __init__(self):
        self._title: str = ""
        self._height: int = 0
        self._width: int = 0
        self._form_bar: bool = False
        self._buttons: list = []
        self._controls: list = []
        self._created: bool = False

    def New(self) -> "FWDialogModal":
        """FWDialogModal:New() — Construtor da classe."""
        return FWDialogModal()

    def SetTitle(self, title: str) -> "FWDialogModal":
        """FWDialogModal:SetTitle() — Define o título da janela."""
        self._title = title
        return self

    def SetSize(self, height: int, width: int) -> "FWDialogModal":
        """FWDialogModal:SetSize() — Define o tamanho da janela."""
        self._height = height
        self._width = width
        return self

    def EnableFormBar(self, enable: bool = True) -> "FWDialogModal":
        """FWDialogModal:EnableFormBar() — Habilita/desabilita a barra de formulário."""
        self._form_bar = enable
        return self

    def CreateDialog(self) -> "FWDialogModal":
        """FWDialogModal:CreateDialog() — Cria o diálogo."""
        self._created = True
        return self

    def CreateFormBar(self) -> "FWDialogModal":
        """FWDialogModal:CreateFormBar() — Cria a barra de formulário."""
        return self

    def GetPanel(self) -> Any:
        """FWDialogModal:GetPanel() — Retorna o painel principal para adicionar controles."""
        return object()

    def GetPanelMain(self) -> Any:
        """FWDialogModal:GetPanelMain() — Retorna o painel principal (alternativo)."""
        return self.GetPanel()

    def AddButton(
        self,
        prompt: str,
        action: Any,
        name: str = "",
        enabled: bool = True,
        visible: bool = True,
        is_default: bool = False,
        is_cancel: bool = False,
        owner: Any = None,
    ) -> "FWDialogModal":
        """FWDialogModal:AddButton() — Adiciona botão ao diálogo."""
        self._buttons.append({
            "prompt": prompt,
            "action": action,
            "name": name,
            "enabled": enabled,
            "visible": visible,
            "default": is_default,
            "cancel": is_cancel,
        })
        return self

    def AddSay(
        self,
        owner: Any,
        row: int,
        col: int,
        text: str,
        width: int = 0,
        height: int = 0,
    ) -> "FWDialogModal":
        """FWDialogModal:AddSay() — Adiciona texto/label ao diálogo."""
        self._controls.append({
            "type": "say",
            "owner": owner,
            "row": row,
            "col": col,
            "text": text,
            "width": width,
            "height": height,
        })
        return self

    def AddGet(
        self,
        owner: Any,
        row: int,
        col: int,
        var_block: Any,
        width: int = 0,
        height: int = 0,
    ) -> "FWDialogModal":
        """FWDialogModal:AddGet() — Adiciona campo de entrada ao diálogo."""
        self._controls.append({
            "type": "get",
            "owner": owner,
            "row": row,
            "col": col,
            "var_block": var_block,
            "width": width,
            "height": height,
        })
        return self

    def Activate(self) -> None:
        """FWDialogModal:Activate() — Ativa o diálogo (modo modal)."""
        pass

    def DeActivate(self) -> None:
        """FWDialogModal:DeActivate() — Fecha o diálogo."""
        pass


# ---------------------------------------------------------------------------
# Funções de dimensão de janela
# ---------------------------------------------------------------------------

def MsAdvSize() -> list:
    """MsAdvSize() — Retorna as dimensões da tela/área de trabalho.
    
    Retorna array com 8 posições:
        [1] nTop, [2] nLeft, [3] nBottom, [4] nRight,
        [5] nWidth, [6] nHeight, [7] nCenterX, [8] nCenterY
    """
    return [0, 0, 480, 640, 640, 480, 320, 240]


# ---------------------------------------------------------------------------
# Diálogos de entrada
# ---------------------------------------------------------------------------
# Diálogos básicos
# ---------------------------------------------------------------------------

def MsgAlert(msg: str, title: str = "Atenção") -> None:
    """
    MsgAlert() — Exibe uma mensagem de alerta.
    Python: mostra no console. ADVPL: dialog box.
    """
    print(f"[ALERT] {title}: {msg}")


def MsgInfo(msg: str, title: str = "Informação") -> None:
    """MsgInfo() — Exibe uma mensagem informativa."""
    print(f"[INFO] {title}: {msg}")


def MsgStop(msg: str, title: str = "Erro") -> None:
    """MsgStop() — Exibe uma mensagem de erro/parada."""
    print(f"[STOP] {title}: {msg}")


def MsgYesNo(msg: str, title: str = "Confirmação") -> bool:
    """
    MsgYesNo() — Pergunta Sim/Não.
    Python: usa input(). ADVPL: dialog box.
    Retorna True para Sim, False para Não.
    """
    resp = input(f"[YES/NO] {title}: {msg} (s/n): ").strip().lower()
    return resp in ("s", "sim", "y", "yes")


def MsgNoYes(msg: str, title: str = "Confirmação") -> bool:
    """MsgNoYes() — Pergunta Não/Sim (padrão inverso)."""
    return MsgYesNo(msg, title)


def MsgOkCancel(msg: str, title: str = "Confirmação") -> bool:
    """MsgOkCancel() — Pergunta OK/Cancelar."""
    resp = input(f"[OK/CANCEL] {title}: {msg} (ok/c): ").strip().lower()
    return resp in ("ok", "o", "")




def ConOut(*args: Any) -> None:
    """
    ConOut() — Envia mensagens para o console do AppServer.
    Python: print() normal.
    """
    print("[CONOUT]", *args)

# ---------------------------------------------------------------------------
# Funções de processamento
# ---------------------------------------------------------------------------

def FWMsgRun(
    title: str,
    msg: str,
    func: Callable,
    *args: Any,
) -> Any:
    """
    FWMsgRun() — Executa uma função com dialog de progresso.
    Python: executa diretamente com print de status.
    """
    print(f"[RUNNING] {title}: {msg}")
    result = func(*args)
    print(f"[DONE] {title}")
    return result


def ProcRegua(total: int) -> None:
    """ProcRegua() — Inicializa a barra de progresso."""
    print(f"[PROGRESS] Iniciando: 0/{total}")


def IncRegua(current: int = 1) -> None:
    """IncRegua() — Incrementa a barra de progresso."""
    pass


def ProcAltera(msg: str, increment: int = 0) -> None:
    """ProcAltera() — Atualiza a mensagem da barra de progresso."""
    print(f"[PROGRESS] {msg}")


def SetProcInfo(msg: str) -> None:
    """SetProcInfo() — Define o texto de informação do processo."""
    print(f"[INFO] {msg}")


# ---------------------------------------------------------------------------
# Diálogos de entrada
# ---------------------------------------------------------------------------

def InputBox(
    prompt: str,
    title: str = "Entrada",
    default: str = "",
    max_len: int = 100,
) -> str:
    """InputBox() — Solicita entrada de texto ao usuário."""
    resp = input(f"[INPUT] {title}: {prompt} [{default}]: ").strip()
    return resp if resp else default


def ReadVar(var_name: str, default: Any = "") -> Any:
    """ReadVar() — Lê uma variável de entrada do usuário. (Simplificado)"""
    resp = input(f"[READ] {var_name} [{default}]: ").strip()
    return resp if resp else default
