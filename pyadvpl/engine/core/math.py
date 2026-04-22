"""
advp.math — Funções matemáticas compatíveis com ADVPL.
"""
from __future__ import annotations
import math as _math
from typing import Union

Number = Union[int, float]


def Round(n: Number, decimals: int = 0) -> Number:
    """Round() — Arredonda um número."""
    return round(float(n), decimals)


def Int(n: Number) -> int:
    """Int() — Trunca para inteiro (não arredonda)."""
    return int(float(n))


def Abs(n: Number) -> Number:
    """Abs() — Valor absoluto."""
    return abs(n)


def Sqrt(n: Number) -> float:
    """Sqrt() — Raiz quadrada."""
    return _math.sqrt(float(n))


def Exp(n: Number) -> float:
    """Exp() — e elevado a n."""
    return _math.exp(float(n))


def Log(n: Number) -> float:
    """Log() — Logaritmo natural."""
    return _math.log(float(n))


def Max(a: Number, b: Number) -> Number:
    """Max() — Retorna o maior dos dois valores."""
    return max(a, b)


def Min(a: Number, b: Number) -> Number:
    """Min() — Retorna o menor dos dois valores."""
    return min(a, b)


def Mod(a: Number, b: Number) -> Number:
    """Mod() — Resto da divisão inteira."""
    return a % b


def Floor(n: Number) -> int:
    """Floor() — Arredonda para baixo."""
    return _math.floor(float(n))


def Ceiling(n: Number) -> int:
    """Ceiling() (Protheus: Ceiling) — Arredonda para cima."""
    return _math.ceil(float(n))
