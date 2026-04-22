"""
advp.string — Funções de string compatíveis com ADVPL.

Mapeiam 1:1 para as funções de string nativas do ADVPL/AdvPL.
"""
from __future__ import annotations
from typing import Union


# ---------------------------------------------------------------------------
# Funções de manipulação de string
# ---------------------------------------------------------------------------

def AllTrim(s: str) -> str:
    """AllTrim() — Remove espaços do início e do fim."""
    return str(s).strip()


def LTrim(s: str) -> str:
    """LTrim() — Remove espaços do início."""
    return str(s).lstrip()


def RTrim(s: str) -> str:
    """RTrim() — Remove espaços do fim."""
    return str(s).rstrip()


def Upper(s: str) -> str:
    """Upper() — Converte para maiúsculas."""
    return str(s).upper()


def Lower(s: str) -> str:
    """Lower() — Converte para minúsculas."""
    return str(s).lower()


def Len(s) -> int:
    """Len() — Retorna o comprimento da string ou array."""
    return len(s)


def SubStr(s: str, start: int, length: int = -1) -> str:
    """
    SubStr() — Extrai substring.
    ADVPL: índice começa em 1, length opcional.
    """
    s = str(s)
    start = max(1, start) - 1  # convert to 0-based
    if length < 0:
        return s[start:]
    return s[start: start + length]


def Left(s: str, n: int) -> str:
    """Left() — Retorna os n primeiros caracteres."""
    return str(s)[:n]


def Right(s: str, n: int) -> str:
    """Right() — Retorna os n últimos caracteres."""
    return str(s)[-n:] if n > 0 else ""


def At(substr: str, s: str, occurrence: int = 1) -> int:
    """
    At() — Retorna a posição de substr dentro de s.
    ADVPL: retorna posição 1-based, 0 se não encontrado.
    """
    s = str(s)
    substr = str(substr)
    pos = 0
    count = 0
    while True:
        found = s.find(substr, pos)
        if found == -1:
            return 0
        count += 1
        if count == occurrence:
            return found + 1  # 1-based
        pos = found + 1


def RAt(substr: str, s: str) -> int:
    """RAt() — Retorna a última posição de substr dentro de s (1-based)."""
    found = str(s).rfind(str(substr))
    return found + 1 if found >= 0 else 0


def Replicate(s: str, n: int) -> str:
    """Replicate() — Repete a string n vezes."""
    return str(s) * n


def Space(n: int) -> str:
    """Space() — Retorna uma string com n espaços."""
    return " " * n


def PadL(s: str, size: int, pad_char: str = " ") -> str:
    """PadL() — Preenche à direita até atingir o tamanho."""
    return str(s).ljust(size, pad_char)


def PadR(s: str, size: int, pad_char: str = " ") -> str:
    """PadR() — Preenche à esquerda até atingir o tamanho."""
    return str(s).rjust(size, pad_char)


def PadC(s: str, size: int, pad_char: str = " ") -> str:
    """PadC() — Centraliza a string preenchendo dos dois lados."""
    return str(s).center(size, pad_char)


def StrZero(n: Union[int, float], size: int, decimals: int = 0) -> str:
    """StrZero() — Converte número para string com zeros à esquerda."""
    if decimals > 0:
        formatted = f"{float(n):.{decimals}f}"
        integer_part = formatted.replace(".", "").replace("-", "")
        total_size = size + 1 + decimals  # +1 para o ponto decimal
        return str(n).zfill(total_size)
    return str(int(n)).zfill(size)


def Str(n: Union[int, float], size: int = 10, decimals: int = 0) -> str:
    """Str() — Converte número para string com tamanho fixo."""
    if decimals > 0:
        return f"{float(n):{size}.{decimals}f}"
    return f"{int(n):{size}d}"


def Val(s: str) -> Union[int, float]:
    """Val() — Converte string para número."""
    s = str(s).strip()
    try:
        if "." in s or "," in s:
            return float(s.replace(",", "."))
        return int(s)
    except ValueError:
        return 0


def Chr(n: int) -> str:
    """Chr() — Retorna o caractere pelo código ASCII."""
    return chr(n)


def Asc(s: str) -> int:
    """Asc() — Retorna o código ASCII do primeiro caractere."""
    return ord(str(s)[0]) if s else 0


def StrToHex(s: str) -> str:
    """StrToHex() — Converte string para hexadecimal."""
    return s.encode().hex().upper()


def HexToStr(h: str) -> str:
    """HexToStr() — Converte hexadecimal para string."""
    return bytes.fromhex(h).decode()


def CharMix(s1: str, s2: str) -> str:
    """CharMix() — Intercala caracteres de duas strings."""
    result = ""
    for a, b in zip(str(s1), str(s2)):
        result += a + b
    return result


def Occurs(substr: str, s: str) -> int:
    """Occurs() — Conta quantas vezes substr aparece em s."""
    return str(s).count(str(substr))


def IsAlpha(s: str) -> bool:
    """IsAlpha() — Retorna True se o primeiro caractere é letra."""
    return str(s)[:1].isalpha() if s else False


def IsDigit(s: str) -> bool:
    """IsDigit() — Retorna True se o primeiro caractere é dígito."""
    return str(s)[:1].isdigit() if s else False


def IsLower(s: str) -> bool:
    """IsLower() — Retorna True se o primeiro caractere é minúsculo."""
    return str(s)[:1].islower() if s else False


def IsUpper(s: str) -> bool:
    """IsUpper() — Retorna True se o primeiro caractere é maiúsculo."""
    return str(s)[:1].isupper() if s else False


def Transform(value: Union[str, int, float], mask: str) -> str:
    """
    Transform() — Aplica máscara de formatação (simplificado).
    Masks suportadas: "@E", "@!", "999.999.999-99", etc.
    """
    s = str(value)
    if mask.startswith("@!"):
        return s.upper()
    elif mask.startswith("@E"):
        # Número com separador europeu
        try:
            n = float(s.replace(",", "."))
            return f"{n:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
        except ValueError:
            return s
    return s
