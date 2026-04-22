"""
advp.types — Tipos base compatíveis com ADVPL.

Estes tipos funcionam em Python puro e são mapeados
1:1 para os tipos nativos do ADVPL ao transpilar.
"""
from __future__ import annotations
from datetime import date as _date
from typing import Any, Iterator


# ---------------------------------------------------------------------------
# Nil — equivalente ao NIL do ADVPL
# ---------------------------------------------------------------------------
class _NilType:
    """Representa o valor NIL do ADVPL (semelhante a None, mas tipado)."""

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __repr__(self) -> str:
        return "Nil"

    def __bool__(self) -> bool:
        return False

    def __eq__(self, other: object) -> bool:
        return other is None or isinstance(other, _NilType)


Nil = _NilType()


# ---------------------------------------------------------------------------
# Date — equivalente ao tipo Date do ADVPL
# ---------------------------------------------------------------------------
class Date:
    """
    Tipo Data do ADVPL.

    Exemplos:
        d = Date(2024, 1, 15)   → equivale a CToD("15/01/2024") no ADVPL
        d = Date.today()        → equivale a Date() no ADVPL
        d = Date.from_str("15/01/2024")  → equivale a CToD("15/01/2024")
    """

    def __init__(self, year: int = 0, month: int = 0, day: int = 0):
        if year == 0 and month == 0 and day == 0:
            self._date = _date.today()
        else:
            self._date = _date(year, month, day)

    @classmethod
    def today(cls) -> "Date":
        """Retorna a data atual — equivale a Date() no ADVPL."""
        return cls()

    @classmethod
    def from_str(cls, s: str, fmt: str = "%d/%m/%Y") -> "Date":
        """CToD equivalente — converte string para Date."""
        from datetime import datetime
        d = datetime.strptime(s, fmt).date()
        obj = cls.__new__(cls)
        obj._date = d
        return obj

    def to_str(self, fmt: str = "%d/%m/%Y") -> str:
        """DToC equivalente — converte Date para string."""
        return self._date.strftime(fmt)

    @property
    def year(self) -> int:
        return self._date.year

    @property
    def month(self) -> int:
        return self._date.month

    @property
    def day(self) -> int:
        return self._date.day

    def __add__(self, days: int) -> "Date":
        from datetime import timedelta
        obj = Date.__new__(Date)
        obj._date = self._date + timedelta(days=days)
        return obj

    def __sub__(self, other) -> int:
        if isinstance(other, Date):
            return (self._date - other._date).days
        from datetime import timedelta
        obj = Date.__new__(Date)
        obj._date = self._date - timedelta(days=other)
        return obj

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Date):
            return self._date == other._date
        return False

    def __lt__(self, other: "Date") -> bool:
        return self._date < other._date

    def __le__(self, other: "Date") -> bool:
        return self._date <= other._date

    def __gt__(self, other: "Date") -> bool:
        return self._date > other._date

    def __ge__(self, other: "Date") -> bool:
        return self._date >= other._date

    def __repr__(self) -> str:
        return f"Date({self.year}, {self.month}, {self.day})"

    def __str__(self) -> str:
        return self.to_str()


# ---------------------------------------------------------------------------
# Array — Array 1-indexed compatível com ADVPL
# ---------------------------------------------------------------------------
class Array(list):
    """
    Array ADVPL-compatível: índice começa em 1 (não em 0 como Python).

    Exemplos:
        a = Array([10, 20, 30])
        a[1]         → 10  (não 20!)
        a[2]         → 20
        a.aAdd(40)   → adiciona ao final
        len(a)       → 3  (ou use Len(a))

    Ao transpilar, é mapeado para o tipo array {} do ADVPL.
    """

    def __init__(self, items=None):
        super().__init__(items or [])

    # --- Acesso 1-based ---
    def __getitem__(self, i):
        if isinstance(i, int):
            if i < 1:
                raise IndexError(f"Índice ADVPL começa em 1. Recebido: {i}")
            return super().__getitem__(i - 1)
        return super().__getitem__(i)

    def __setitem__(self, i, v):
        if isinstance(i, int):
            if i < 1:
                raise IndexError(f"Índice ADVPL começa em 1. Recebido: {i}")
            super().__setitem__(i - 1, v)
        else:
            super().__setitem__(i, v)

    def __iter__(self) -> Iterator[Any]:
        return super().__iter__()

    # --- Funções ADVPL ---
    def aAdd(self, item: Any) -> "Array":
        """aAdd() — adiciona elemento ao final."""
        self.append(item)
        return self

    def aDel(self, index: int) -> "Array":
        """aDel() — remove elemento pelo índice (1-based)."""
        del self[index - 1 + 1]  # convert back to 0-based for internal del
        return self

    def aSize(self, new_size: int) -> "Array":
        """aSize() — redimensiona o array."""
        current = len(self)
        if new_size > current:
            self.extend([Nil] * (new_size - current))
        elif new_size < current:
            del self[new_size:]
        return self

    def aSort(self, start: int = 1, end: int = -1, block=None) -> "Array":
        """aSort() — ordena o array."""
        if block:
            self.sort(key=block)
        else:
            self.sort()
        return self

    def aScan(self, block) -> int:
        """aScan() — busca elemento. Retorna índice (1-based) ou 0."""
        for i, item in enumerate(self):
            if block(item):
                return i + 1
        return 0

    def __repr__(self) -> str:
        return f"Array({list.__repr__(self)})"


# ---------------------------------------------------------------------------
# Funções de Tipo
# ---------------------------------------------------------------------------

def ValType(val: Any) -> str:
    """ValType() — retorna o tipo da variável (C, N, D, L, A, O, U)."""
    if isinstance(val, str): return "C"
    if isinstance(val, (int, float)): return "N"
    if isinstance(val, Date): return "D"
    if isinstance(val, bool): return "L"
    if isinstance(val, Array): return "A"
    if isinstance(val, _NilType): return "U"
    if hasattr(val, "__dict__"): return "O"
    return "U"


def Type(var_name: str) -> str:
    """Type() — retorna o tipo da variável pelo nome."""
    return "U"
