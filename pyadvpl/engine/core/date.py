"""
advp.date — Funções de data compatíveis com ADVPL.
"""
from __future__ import annotations
from .types import Date
from typing import Union


def CToD(s: str, fmt: str = "%d/%m/%Y") -> Date:
    """CToD() — Converte string para Date."""
    return Date.from_str(s, fmt)


def DToC(d: Date, fmt: str = "%d/%m/%Y") -> str:
    """DToC() — Converte Date para string."""
    if isinstance(d, Date):
        return d.to_str(fmt)
    return ""


def DToS(d: Date) -> str:
    """DToS() — Converte Date para string no formato YYYYMMDD."""
    if isinstance(d, Date):
        return d.to_str("%Y%m%d")
    return "00000000"


def SToD(s: str) -> Date:
    """SToD() — Converte string YYYYMMDD para Date."""
    return Date.from_str(s, "%Y%m%d")


def Month(d: Date) -> int:
    """Month() — Retorna o mês da data."""
    return d.month if isinstance(d, Date) else 0


def Year(d: Date) -> int:
    """Year() — Retorna o ano da data."""
    return d.year if isinstance(d, Date) else 0


def Day(d: Date) -> int:
    """Day() — Retorna o dia da data."""
    return d.day if isinstance(d, Date) else 0


def Today() -> Date:
    """Date() — Retorna a data de hoje (alias de Date.today())."""
    return Date.today()


def Time() -> str:
    """Time() — Retorna a hora atual no formato HH:MM:SS."""
    from datetime import datetime
    return datetime.now().strftime("%H:%M:%S")


def Seconds() -> float:
    """Seconds() — Retorna os segundos desde meia-noite."""
    from datetime import datetime
    now = datetime.now()
    return now.hour * 3600 + now.minute * 60 + now.second + now.microsecond / 1e6


def LastDayOfMonth(d: Date) -> int:
    """LastDayOfMonth() — Retorna o último dia do mês da data."""
    import calendar
    return calendar.monthrange(d.year, d.month)[1]
