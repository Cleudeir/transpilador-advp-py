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
# Funções de Consulta SQL (APSDU / ExecAuto)
# ---------------------------------------------------------------------------

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
