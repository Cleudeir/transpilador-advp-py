# 🚀 pyadvpl — Transpilador de ADVPL para Python

[![Licença: Comercial/MIT](https://img.shields.io/badge/License-Comercial/MIT-orange.svg)](LICENSE)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![ADVPL](https://img.shields.io/badge/Protheus-ADVPL-green.svg)](https://totvs.com.br/)

O **pyadvpl** é um framework de desenvolvimento moderno que permite escrever código para o ERP **TOTVS Protheus** utilizando **Python**. Ele fornece uma ponte elegante entre a flexibilidade do Python e a robustez do ambiente Protheus, transpilando seu código idiomático diretamente para arquivos `.prw` (ADVPL) prontos para compilação.

---

## 🔥 Principais Funcionalidades

- **💎 Escrita Idiomática**: Escreva Python real, use f-strings, listas, e loops modernos.
- **📦 Biblioteca de Stubs**: Autocomplete completo no VS Code para funções como `MsgAlert`, `DbGoTop`, `SuperGetMV`, etc.
- **🔄 Transpilação Inteligente**: Mapeia automaticamente classes `Table` para acesso via Alias (`SA1->A1_NOME`).
- **⚡ CLI Integrada**: Comandos simplificados como `build`, `convert` e `dev`.
- **🖥️ Dashboard Web**: Interface moderna em React para transpilação em tempo real.
- **🛠️ Auto-Declaração**: O framework detecta suas variáveis e as declara como `LOCAL`, `PRIVATE` ou `PUBLIC` automaticamente no ADVPL gerado.
- **🔒 Transações**: Suporte completo a `BEGIN TRANSACTION` / `END TRANSACTION` via context manager `Transaction()`.
- **🗄️ SQL Nativo**: Suporte a `BeginSQL` / `EndSQL` com `COLUMN` via context manager `BeginSQL()`.

---

## 🛠️ Instalação

### 1. Requisitos

- **Python 3.8+**
- **Node.js & NPM** (apenas para o Dashboard Web)

### 2. Configuração do Framework (Python)

Clone o repositório e configure o ambiente conforme seu sistema:

#### 🐧 Linux / macOS

```bash
git clone https://github.com/Cleudeir/transpilador-advp-py.git
cd transpilador-advp-py
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pip install -e .
```

#### 🪟 Windows

```powershell
git clone https://github.com/Cleudeir/transpilador-advp-py.git
cd transpilador-advp-py
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
pip install -e .
```

### 3. Configuração do Dashboard (Opcional)

Se desejar usar a interface web, instale as dependências do frontend:

```bash
cd frontend
npm install
cd ..
```

### 4. Ambiente de Desenvolvimento (Scripts Rápidos)

Para subir o ambiente completo (Backend + Frontend) de uma só vez:

- **Linux/macOS**: `./dev.sh`
- **Windows**: `dev.bat`

---

## 🧪 Testes

O projeto inclui um sistema de testes de transpiração em lote (bulk round-trip tests) para garantir a precisão:

#### 🐧 Linux / macOS

```bash
./run_bulk_tests.sh
```

#### 🪟 Windows

```powershell
run_bulk_tests.bat
```

---

## 📖 Como Usar

O **pyadvpl** oferece duas formas de trabalho: via **Linha de Comando (CLI)** ou via **Dashboard Web**.

### A. Fluxo Via CLI (Produção)

#### 1. Inicialize um Novo Projeto

Crie a estrutura padrão do projeto:

```bash
pyadvpl init meu_projeto
```

Estrutura gerada:

```text
meu_projeto/
├── pyadvpl.toml # Configurações do projeto
├── src/              # Coloque seus arquivos .py aqui
├── dist/             # Onde o ADVPL gerado será salvo
├── tests/            # Testes unitários para seu código Python
└── ...
```

#### 2. Escreva seu Código

No diretório `meu_projeto/src`, crie seus arquivos `.py`. Exemplo:

```python
from pyadvpl import ui

def u_MinhaFuncao():
    ui.MsgAlert("Olá do Python!")
```

#### 3. Transpile para ADVPL

```bash
pyadvpl build
```

_O comando lê automaticamente a pasta `src/` e gera os arquivos em `dist/`._

---

### B. Conversão de Código Legado (ADVPL -> Python)

O **pyadvpl** permite converter seus arquivos `.prw` antigos para `.py` facilmente.

#### 1. Converta seus arquivos

```bash
# Converte arquivos da pasta legacy/ para src/
pyadvpl convert
```

---

### C. Fluxo Via Dashboard Web (Desenvolvimento)

O dashboard permite colar código Python e ver o ADVPL gerado instantaneamente.

#### 1. Inicie o Backend (API)

```bash
pyadvpl dev
```

_A API rodará por padrão em `http://localhost:8040`._

#### 2. Inicie o Frontend

Em outro terminal:

```bash
cd frontend
npm run dev
```

_Acesse o link gerado (ex: `http://localhost:5173`) para usar a interface._

---

## 🏗️ Arquitetura do Projeto

- **`pyadvpl/engine/`**: O motor principal (Lexer, Parser, Code Generator).
- **`pyadvpl/engine/server.py`**: API FastAPI que serve o motor de transpilação.
- **`pyadvpl/engine/cli.py`**: Interface de comando para automação.
- **`frontend/`**: Aplicação React/Vite para visualização em tempo real.

---

## ⚡ Comparativo: Python vs ADVPL

| Característica     | Python (pyadvpl)           | ADVPL (Gerado)             |
| :----------------- | :------------------------- | :------------------------- |
| **Acesso a Campo** | `SA1.A1_NOME`              | `SA1->A1_NOME`             |
| **Navegação**      | `SA1.go_top()`             | `SA1->( DbGoTop() )`       |
| **Mensagens**      | `ui.MsgAlert("Oi")`        | `MsgAlert("Oi")`           |
| **Loops**          | `for i in range(1, 11)`    | `For nI := 1 To 10`        |
| **Variáveis**      | `LOCAL`, `PRIVATE`, `PUBLIC` | Declarações preservadas  |
| **Transações**     | `with Transaction():`      | `Begin Transaction ... End Transaction` |
| **SQL Nativo**     | `with BeginSQL(alias="Q") as sql:` | `BeginSql Alias "Q" ... EndSql` |

---

## 📝 Exemplos de Uso

### Transações (BEGIN TRANSACTION / END TRANSACTION)

```python
from pyadvpl import db

def u_AtualizaClientes():
    with db.Transaction():
        SA1 = db.Table("SA1")
        SA1.rec_lock(True)
        SA1.A1_NOME = "Novo Nome"
        SA1.unlock()
```

### SQL Nativo (BeginSQL / EndSQL)

```python
from pyadvpl import db

def u_ConsultaClientes():
    nRegs = 0
    with db.BeginSQL(alias="SQL_SA1") as sql:
        sql.column("A1_COD", "CHAR")
        sql.column("A1_NOME", "CHAR")
        sql.query("SELECT A1_COD, A1_NOME FROM SA1 WHERE SA1.D_E_L_E_T_ = ' '")
        
        while not db.sql_eof():
            nRegs += 1
            print(sql.A1_NOME)
            db.sql_skip()
```

### Variáveis PRIVATE e PUBLIC

```python
def u_ExemploVariaveis():
    # PRIVATE: visível na função e em funções chamadas
    private cMsgLog = ""
    
    # PUBLIC: visível globalmente em todo o programa
    public nTotalRegistros = 0
    
    # LOCAL: visível apenas nesta função (declarado automaticamente)
    lSucesso = True
```

---

## 🤝 Como Contribuir

Contribuições são muito bem-vindas! Este documento descreve o estado atual do projeto, as convenções adotadas e as metas para evoluí-lo.

### 1. Configuração do Ambiente de Desenvolvimento

```bash
# 1. Fork e clone
git clone https://github.com/<seu-usuario>/transpilador-advp-py.git
cd transpilador-advp-py

# 2. Ambiente virtual e dependências
python3 -m venv .venv
source .venv/bin/activate          # Linux/macOS
# .venv\Scripts\activate           # Windows
pip install -r requirements.txt
pip install -e .

# 3. (Opcional) Frontend
cd frontend && npm install && cd ..

# 4. Rode os testes de round-trip para verificar a instalação
./run_bulk_tests.sh                 # Linux/macOS
# run_bulk_tests.bat                # Windows
```

### 2. Fluxo de Contribuição

1. Crie uma branch descritiva a partir de `main`:
   ```bash
   git checkout -b feature/minha-feature
   # ou
   git checkout -b fix/bug-que-corrigi
   ```
2. Implemente suas alterações e adicione/atualize os testes correspondentes.
3. Execute os testes de round-trip e confirme que nenhum exemplo regrediu.
4. Faça commit com mensagens claras no padrão:
   ```
   feat: suporte a bloco BEGIN SEQUENCE/END SEQUENCE
   fix: corrigir geração de LOCAL para variáveis de loop
   test: adicionar Exemplo_082_Class ao bulk test
   ```
5. Abra um **Pull Request** descrevendo o problema resolvido e como testou.

### 3. Estrutura do Projeto

| Caminho                                         | Responsabilidade                                                                           |
| :---------------------------------------------- | :----------------------------------------------------------------------------------------- |
| `pyadvpl/engine/transpiler/lexer.py`            | Tokenizador do ADVPL                                                                       |
| `pyadvpl/engine/transpiler/parser.py`           | Construção da AST a partir dos tokens                                                      |
| `pyadvpl/engine/transpiler/advpl_generator.py`  | AST → código ADVPL                                                                         |
| `pyadvpl/engine/transpiler/python_generator.py` | AST → código Python                                                                        |
| `pyadvpl/engine/transpiler/python_to_ast.py`    | Código Python → AST interna                                                                |
| `pyadvpl/engine/core/`                          | Stubs das funções nativas do Protheus (db, ui, string, math, date, array, protheus, types) |
| `pyadvpl/engine/cli.py`                         | CLI (`init`, `build`, `convert`, `dev`)                                                    |
| `pyadvpl/engine/server.py`                      | API FastAPI                                                                                |
| `frontend/`                                     | Dashboard React/Vite                                                                       |
| `pyadvpl/engine/transpiler/tests/input/`        | +560 exemplos `.prw` de referência                                                         |
| `pyadvpl/engine/transpiler/tests/output/`       | Saídas esperadas para os exemplos acima                                                    |

### 4. O Que Já Está Implementado

#### Transpilação Python → ADVPL

- [x] Declaração automática de variáveis `LOCAL` no topo da função
- [x] Geração correta de `PRIVATE` e `PUBLIC` além de `LOCAL`
- [x] Mapeamento de acesso a campos (`SA1.A1_NOME` → `SA1->A1_NOME`)
- [x] Mapeamento de métodos de navegação (`sa1.go_top()` → `SA1->( DbGoTop() )`)
- [x] Funções com prefixo `u_`, `static` e `function`
- [x] Estruturas `if/elif/else`, `while`, `for` com `range()`
- [x] Literais de array e acesso por índice
- [x] Expressões binárias e unárias (todos os operadores ADVPL)
- [x] Chamadas de métodos e funções com argumentos posicionais
- [x] Nós de pré-processador (`#include`, `#define`)
- [x] Comentários preservados na saída
- [x] Suporte completo a classes ADVPL (`CLASS`/`METHOD`/`ENDCLASS`)
- [x] Suporte a `BEGIN SEQUENCE` / `RECOVER SEQUENCE` (equivalente ao `try/except`)
- [x] Suporte a `BEGIN TRANSACTION` / `END TRANSACTION` (context manager `Transaction()`)
- [x] Suporte a `BeginSQL` / `EndSQL` (context manager `BeginSQL()`)

#### Transpilação ADVPL → Python

- [x] Lexer com todos os operadores específicos do ADVPL (`$`, `&`, `::`, `:=`, `@`, `%`)
- [x] Parser para as estruturas de controle principais
- [x] Gerador Python com mapeamento de tipos e funções
- [x] Suporte a `BEGIN SEQUENCE` / `RECOVER SEQUENCE` (equivalente ao `try/except`)
- [x] Suporte a `BEGIN TRANSACTION` / `END TRANSACTION` (`with Transaction():`)
- [x] Suporte a `BeginSQL` / `EndSQL` com `COLUMN` (`with BeginSQL(alias="...") as sql:`)
- [x] Preservação de modificadores `PRIVATE` e `PUBLIC` na AST

#### Biblioteca de Stubs (`pyadvpl/engine/core/`)

- [x] `db` — funções de banco de dados (DbGoTop, DbSeek, DbUseArea, etc.)
- [x] `db` — controle de transações (`Transaction`, `DisarmTransaction`)
- [x] `db` — SQL nativo (`BeginSQL`, `EndSQL`, `sql_eof`, `sql_skip`, `sql_close`)
- [x] `db` — funções SQL (`TCSqlExec`, `TCSQLError`, `TCSQLQuery`, `TCSQLPlan`, `RetSQLName`, `RetSQLCond`, `FormatIn`, `ValToSQL`)
- [x] `ui` — diálogos e mensagens (MsgAlert, MsgYesNo, MsgInfo, etc.)
- [x] `ui` — FWDialogModal (janela de diálogo modal personalizável)
- [x] `ui` — MsNewProcess (processo com barra de progresso / réguas)
- [x] `string` — manipulação de strings (AllTrim, SubStr, Upper, Lower, etc.)
- [x] `math` — funções matemáticas (Abs, Round, Int, Sqrt, etc.)
- [x] `date` — funções de data (Date, CToD, DToC, Month, Year, etc.)
- [x] `array` — funções de array (AAdd, ADel, ASize, ASort, AScan, etc.)
- [x] `protheus` — funções do framework (GetMV, SuperGetMV, Posicione, etc.)
- [x] `protheus` — classes de browse (`FWBrowse`, `FWBrwColumn`, `FWMBrowse`, `FWMarkBrowse`, `FWTemporaryTable`)
- [x] `protheus` — classes de modelo e relatório (`oModel`, `oReport`, `oSection`)
- [x] `types` — tipos base (`Nil`, `Array`, `Date`)

#### Testes

- [x] Suite de +560 exemplos `.prw` cobrindo operadores, funções, classes, transações e SQL do Protheus
- [x] Testes de round-trip em lote (`test_roundtrip_bulk.py`)
- [x] Script `debug_precision.py` para diagnóstico de desvios

### 5. Metas e Roadmap

As contribuições mais necessárias estão marcadas com 🎯 (alta prioridade) ou 💡 (melhoria futura).

#### Transpilador

- 💡 Suporte a codeblocks ADVPL (`{ |x| expr }`) mapeados para lambdas Python
- 💡 Suporte a `#IFDEF` / `#IFNDEF` no pré-processador
- 💡 Preservação de comentários de documentação (`//` e `/* */`) no round-trip
- 💡 Suporte a `STEP` em loops `FOR`

#### Biblioteca de Stubs

- 🎯 Completar stubs de funções REST (`FWRest`, `HttpGet`, `HttpPost`)
- 🎯 Stubs de integração XML (`XmlParser`, `XmlNode2Arr`, `JSONObject`)
- 💡 Adicionar type hints completos e docstrings a todos os stubs existentes
- 💡 Suporte a `TCSqlToArr` e funções de consulta SQL via stub

#### CLI e Dashboard

- 🎯 Comando `pyadvpl test` para rodar a suite de testes localmente
- 🎯 Relatório de cobertura de transpilação (quantos exemplos passam/falham)
- 💡 Modo `watch` no CLI (`pyadvpl dev --watch`) para recompilar ao salvar
- 💡 Plugin VS Code com diagnósticos em tempo real

#### Qualidade e Infraestrutura

- 🎯 Configurar CI/CD (GitHub Actions) com execução automática dos bulk tests
- 🎯 Publicar o pacote no PyPI
- 💡 Adicionar `pre-commit` com `ruff` e `mypy`
- 💡 Criar documentação em MkDocs ou Sphinx

### 6. Convenções de Código

- Linguagem dos comentários e docstrings: **Português Brasileiro**
- Estilo: segue `PEP 8`; use `ruff` para lint
- Novos stubs devem seguir o padrão de `pyadvpl/engine/core/db.py`: função com `pass` e docstring descrevendo o equivalente ADVPL
- Novos testes devem incluir apenas o arquivo `input/*.prw`; o `output/*.py` é gerado automaticamente

---

## 📜 Licença

Este projeto utiliza um modelo de **Licenciamento Dual**:

### 💰 Informações de Uso

- **Uso Comunitário (Gratuito)**: Livre para uso pessoal, estudos, projetos open source e empresas com faturamento anual **inferior a R$ 100.000,00**. Regido pelos termos da [Licença MIT](LICENSE).
- **Uso Comercial (Pago)**: Obrigatório para empresas com faturamento anual **superior a R$ 100.000,00**.

Para adquirir sua licença comercial ou consultar valores, entre em contato via: **cleudeirsilva@gmail.com**.

---

Desenvolvido com ❤️ por [Cleudeir](https://github.com/Cleudeir)
