"""
advp.db — Funções e classes de banco de dados compatíveis com ADVPL.

Mapeamento 1:1 com as funções nativas do Protheus.
"""
from __future__ import annotations
from typing import Any, Optional, List, ContextManager
from contextlib import contextmanager
from .types import Nil, Array


# ---------------------------------------------------------------------------
# Controle de Transações (BEGIN TRANSACTION / END TRANSACTION)
# ---------------------------------------------------------------------------

class Transaction:
    """
    Context manager para controle de transações no Protheus.
    
    Uso:
        with Transaction():
            RecLock('SB1', .T.)
            SB1->B1_COD = "TEST"
            SB1->(MsUnlock())
    
    Equivale a:
        Begin Transaction
            ...
        End Transaction
    """
    
    def __enter__(self):
        """Inicia a transação (Begin Transaction)."""
        pass
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Finaliza a transação (End Transaction).
        Se houver exceção, a transação é automaticamente cancelada (DisarmTransaction).
        """
        if exc_type is not None:
            DisarmTransaction()
        return False


def DisarmTransaction() -> None:
    """DisarmTransaction() — cancela a transação atual."""
    pass


# ---------------------------------------------------------------------------
# SQL Blocks (BeginSQL / EndSQL)
# ---------------------------------------------------------------------------

class BeginSQL:
    """
    Context manager para execução de queries SQL nativas no Protheus.
    
    Uso:
        with BeginSQL(alias="SQL_SB1") as sql:
            sql.column("B1_COD", "CHAR")
            sql.column("B1_DESC", "CHAR")
            sql.query("SELECT B1_COD, B1_DESC FROM %table:SB1% SB1 WHERE SB1.%notDel%")
        
        while not sql_eof():
            print(sql.B1_COD)
            sql_skip()
        sql_close()
    
    Equivale a:
        BeginSql Alias "SQL_SB1"
            COLUMN B1_COD AS CHAR
            COLUMN B1_DESC AS CHAR
            SELECT B1_COD, B1_DESC FROM SB1 SB1 WHERE SB1.D_E_L_E_T_ = ' '
        EndSql
    """
    
    def __init__(self, alias: str = ""):
        self.alias = alias
        self.columns: List[dict] = []
        self.query = ""
        self._results: List[dict] = []
        self._current_row = -1
    
    def __enter__(self):
        """Inicia o bloco SQL (BeginSql)."""
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Finaliza o bloco SQL (EndSql)."""
        return False
    
    def column(self, name: str, col_type: str = "") -> "BeginSQL":
        """Define um coluna com tipo específico."""
        self.columns.append({"name": name, "type": col_type})
        return self
    
    def query(self, sql: str) -> "BeginSQL":
        """Define a query SQL a ser executada."""
        self.query = sql
        return self
    
    def __getattr__(self, name: str) -> Any:
        """Acesso aos campos do resultado (sql.B1_COD → SQL_SB1->B1_COD)."""
        if name.startswith("_"):
            return object.__getattribute__(self, name)
        if self._current_row >= 0 and self._current_row < len(self._results):
            return self._results[self._current_row].get(name, Nil)
        return Nil


def sql_eof() -> bool:
    """Verifica se chegou ao fim do resultado da query SQL."""
    return True


def sql_skip(n: int = 1) -> None:
    """Avança n registros no resultado da query SQL."""
    pass


def sql_close() -> None:
    """Fecha a área de resultado da query SQL."""
    pass


def sql_alias() -> str:
    """Retorna o alias da query SQL atual."""
    return ""


# ---------------------------------------------------------------------------
# Funções SQL (TCSQLExec, TCSQLError, TCSQLQuery)
# ---------------------------------------------------------------------------

def TCSqlExec(statement: str, connection: str = "") -> int:
    """
    TCSqlExec(cStatement) — Executa uma query SQL direta.
    
    Retorna:
        >= 0: Sucesso
        < 0: Erro (use TCSQLError() para detalhes)
    """
    return 0


def TCSQLError() -> str:
    """
    TCSQLError() — Retorna a mensagem de erro do último TCSqlExec.
    """
    return ""


def TCSQLQuery(query: str, connection: str = "") -> Any:
    """
    TCSQLQuery(cQuery) — Executa uma query e retorna o resultado.
    """
    return Nil


def TCSQLPlan(query: str) -> str:
    """
    TCSQLPlan(cQuery) — Retorna o plano de execução da query.
    """
    return ""


def RetSQLName(alias: str) -> str:
    """
    RetSQLName(cAlias) — Retorna o nome real da tabela no banco de dados.
    """
    return alias


def RetSQLCond(condition: str) -> str:
    """
    RetSQLCond(cCondition) — Formata uma condição para uso em SQL.
    """
    return condition


def FormatIn(values: str, separator: str = ",") -> str:
    """
    FormatIn(cValues, cSeparator) — Formata valores para cláusula IN.
    """
    return values


def ValToSQL(value: Any, col_type: str = "C") -> str:
    """
    ValToSQL(xValue, cType) — Converte um valor para formato SQL.
    """
    return ""


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
