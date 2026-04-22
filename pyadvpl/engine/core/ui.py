"""
advp.ui — Funções de interface do usuário compatíveis com ADVPL.

Mapeiam para as funções de diálogo nativas do Protheus.
"""
from __future__ import annotations
from typing import Any, Callable, Optional


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
