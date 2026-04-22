"""
advp.db — Funções e classes de banco de dados compatíveis com ADVPL.

Mapeamento 1:1 com as funções nativas do Protheus.
"""
from __future__ import annotations
from typing import Any, Optional
from .types import Nil, Array


# ---------------------------------------------------------------------------
# Funções de navegação de cursor (mapeiam diretamente para ADVPL)
# ---------------------------------------------------------------------------

def DbGoTop() -> None:
    """DbGoTop() — move o cursor para o primeiro registro."""
    pass  # stub: comportamento real no Protheus


def DbGoBottom() -> None:
    """DbGoBottom() — move o cursor para o último registro."""
    pass


def DbSkip(n: int = 1) -> None:
    """DbSkip(n) — avança n registros."""
    pass


def DbSeek(key: Any, soft: bool = False, order: int = 0) -> bool:
    """DbSeek() — posiciona o cursor pela chave."""
    return False


def DbEof() -> bool:
    """DbEof() — retorna True se estiver no fim do arquivo."""
    return True


def DbBof() -> bool:
    """DbBof() — retorna True se estiver no início do arquivo."""
    return True


def DbSelectArea(alias: str) -> None:
    """DbSelectArea() — seleciona a área de trabalho pelo alias."""
    pass


def DbSetOrder(order: int) -> None:
    """DbSetOrder() — define o índice ativo."""
    pass


def DbCloseArea() -> None:
    """DbCloseArea() — fecha a área de trabalho atual."""
    pass


def RecLock(alias: str, new: bool = False) -> bool:
    """RecLock() — trava o registro para edição."""
    return True


def MsUnlock() -> None:
    """MsUnlock() — libera o travamento do registro."""
    pass


def RecNo() -> int:
    """RecNo() — retorna o número do registro atual."""
    return 0


def LastRec() -> int:
    """LastRec() — retorna o número do último registro."""
    return 0


def Alias() -> str:
    """Alias() — retorna o alias da área de trabalho atual."""
    return ""


def Select(alias: str) -> int:
    """Select() — retorna o número da área de trabalho pelo alias."""
    return 0


def Used() -> bool:
    """Used() — retorna True se a área de trabalho está em uso."""
    return False


def OrdSetFocus(order: str) -> None:
    """OrdSetFocus() — define o índice pelo nome."""
    pass




# ---------------------------------------------------------------------------
# Classe Table — Abstração de tabela Protheus em Python
# ---------------------------------------------------------------------------

class Table:
    """
    Abstração de uma tabela Protheus.

    Permite escrever acesso a campos de forma pythônica:
        SA1 = Table("SA1")
        SA1.go_top()
        while not SA1.eof():
            nome = SA1.A1_NOME   # → SA1->A1_NOME no ADVPL
            SA1.skip()

    Ao transpilar, o acesso a atributos é convertido para
    a notação de alias ADVPL: ALIAS->CAMPO
    """

    def __init__(self, alias: str):
        object.__setattr__(self, "_alias", alias.upper())
        object.__setattr__(self, "_fields", {})

    @property
    def alias(self) -> str:
        return object.__getattribute__(self, "_alias")

    # --- Getters/Setters de campo (Alias->Campo) ---
    def __getattr__(self, name: str) -> Any:
        if name.startswith("_"):
            return object.__getattribute__(self, name)
        # No transpilador: SA1.A1_NOME → SA1->A1_NOME
        fields = object.__getattribute__(self, "_fields")
        return fields.get(name, Nil)

    def __setattr__(self, name: str, value: Any) -> None:
        if name.startswith("_"):
            object.__setattr__(self, name, value)
            return
        # No transpilador: SA1.A1_NOME = "X" → SA1->A1_NOME := "X"
        fields = object.__getattribute__(self, "_fields")
        fields[name] = value

    # --- Métodos de navegação ---
    def go_top(self) -> None:
        """DbGoTop() nesta área de trabalho."""
        pass

    def go_bottom(self) -> None:
        """DbGoBottom() nesta área de trabalho."""
        pass

    def skip(self, n: int = 1) -> None:
        """DbSkip(n) nesta área de trabalho."""
        pass

    def seek(self, key: Any, soft: bool = False, order: int = 0) -> bool:
        """DbSeek() nesta área de trabalho."""
        return False

    def eof(self) -> bool:
        """DbEof() nesta área de trabalho."""
        return True

    def bof(self) -> bool:
        """DbBof() nesta área de trabalho."""
        return True

    def set_order(self, order: int) -> None:
        """DbSetOrder() nesta área de trabalho."""
        pass

    def select(self) -> None:
        """DbSelectArea() desta tabela."""
        pass

    def rec_lock(self, new: bool = False) -> bool:
        """RecLock() nesta área de trabalho."""
        return True

    def unlock(self) -> None:
        """MsUnlock() nesta área de trabalho."""
        pass

    def rec_no(self) -> int:
        """RecNo() nesta área de trabalho."""
        return 0

    def last_rec(self) -> int:
        """LastRec() nesta área de trabalho."""
        return 0

    def count(self) -> int:
        """Retorna o número de registros da tabela."""
        return 0

    def __repr__(self) -> str:
        return f"Table('{self.alias}')"
