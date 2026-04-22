"""
advp.array — Funções de array compatíveis com ADVPL.

Complementa a classe Array de advp.types com funções globais.
"""
from __future__ import annotations
from typing import Any, Callable, List, Optional, Union
from .types import Array, Nil


# ---------------------------------------------------------------------------
# Funções globais de array (equivalentes às do ADVPL)
# ---------------------------------------------------------------------------

def aAdd(arr: Array, item: Any) -> Array:
    """aAdd() — Adiciona um elemento ao final do array."""
    if not isinstance(arr, Array):
        arr = Array(arr)
    arr.append(item)
    return arr


def aDel(arr: Array, index: int) -> Array:
    """aDel() — Remove o elemento na posição index (1-based), encurta o array."""
    if 1 <= index <= len(arr):
        del arr[index - 1]  # 0-based internal
    return arr


def aSize(arr: Array, new_size: int) -> Array:
    """aSize() — Redimensiona o array."""
    current = len(arr)
    if new_size > current:
        arr.extend([Nil] * (new_size - current))
    elif new_size < current:
        del arr[new_size:]
    return arr


def aSort(
    arr: Array,
    start: int = 1,
    end: int = -1,
    block: Optional[Callable] = None,
) -> Array:
    """aSort() — Ordena o array."""
    if end < 0:
        end = len(arr)
    # Work on the 0-based slice
    s, e = start - 1, end
    slice_ = arr[s:e]
    if block:
        slice_.sort(key=block)
    else:
        slice_.sort()
    arr[s:e] = slice_
    return arr


def aScan(arr: Array, block: Callable) -> int:
    """aScan() — Busca no array. Retorna índice 1-based ou 0."""
    for i, item in enumerate(arr):
        if block(item):
            return i + 1
    return 0


def aCopy(
    src: Array,
    dst: Array,
    src_start: int = 1,
    count: int = -1,
    dst_start: int = 1,
) -> Array:
    """aCopy() — Copia elementos de src para dst."""
    if count < 0:
        count = len(src) - src_start + 1
    for i in range(count):
        src_idx = src_start - 1 + i
        dst_idx = dst_start - 1 + i
        if src_idx < len(src):
            while len(dst) <= dst_idx:
                dst.append(Nil)
            dst[dst_idx] = src[src_idx]
    return dst


def aClone(arr: Array) -> Array:
    """aClone() — Retorna uma cópia do array."""
    return Array(list(arr))


def aEval(arr: Array, block: Callable) -> Array:
    """aEval() — Executa um bloco para cada elemento."""
    for item in arr:
        block(item)
    return arr


def Len(s) -> int:
    """Len() — Retorna o tamanho do array ou string."""
    return len(s)


def aFill(arr: Array, value: Any, start: int = 1, count: int = -1) -> Array:
    """aFill() — Preenche o array com um valor."""
    if count < 0:
        count = len(arr) - start + 1
    for i in range(start - 1, min(start - 1 + count, len(arr))):
        arr[i] = value
    return arr
