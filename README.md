# 🚀 pyadvpl — O Futuro do Protheus com Python

[![Licença: Comercial/MIT](https://img.shields.io/badge/License-Comercial/MIT-orange.svg)](LICENSE)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![ADVPL](https://img.shields.io/badge/Protheus-ADVPL-green.svg)](https://totvs.com.br/)

O **pyadvpl** é um framework de desenvolvimento moderno que permite escrever código para o ERP **TOTVS Protheus** utilizando **Python**. Ele fornece uma ponte elegante entre a flexibilidade do Python e a robustez do ambiente Protheus, transpilando seu código idiomático diretamente para arquivos `.prw` (ADVPL) prontos para compilação.

---

## 🔥 Principais Funcionalidades

- **💎 Escrita Idiomática**: Escreva Python real, use f-strings, listas, e loops modernos.
- **📦 Biblioteca de Stubs**: Autocomplete completo no VS Code para funções como `MsgAlert`, `DbGoTop`, `SuperGetMV`, etc.
- **🔄 Transpilação Inteligente**: Mapeia automaticamente classes `Table` para acesso via Alias (`SA1->A1_NOME`).
- **⚡ CLI Integrada**: Comando `pyadvpl` para inicializar projetos, transpilar e subir o dashboard.
- **🖥️ Dashboard Web**: Interface moderna em React para transpilação em tempo real e testes rápidos.
- **🛠️ Auto-Declaração**: O framework detecta suas variáveis e as declara como `LOCAL` automaticamente no ADVPL gerado.

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
O projeto inclui um sistema de testes de transpiração em lote (bulk round-trip tests) para garantir a precisão da transpiração:

```bash
# Rodar testes em lote (ADVPL -> Python -> ADVPL)
./run_bulk_tests.sh  # ou run_bulk_tests.bat no Windows
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
pyadvpl transpile src/ -o dist/
```

---

### B. Fluxo Via Dashboard Web (Desenvolvimento)

O dashboard permite colar código Python e ver o ADVPL gerado instantaneamente.

#### 1. Inicie o Backend (API)
```bash
pyadvpl serve
```
*A API rodará por padrão em `http://localhost:8040`.*

#### 2. Inicie o Frontend
Em outro terminal:
```bash
cd frontend
npm run dev
```
*Acesse o link gerado (ex: `http://localhost:5173`) para usar a interface.*

---

## 🏗️ Arquitetura do Projeto

- **`pyadvpl/engine/`**: O motor principal (Lexer, Parser, Code Generator).
- **`pyadvpl/engine/server.py`**: API FastAPI que serve o motor de transpilação.
- **`pyadvpl/engine/cli.py`**: Interface de comando para automação.
- **`frontend/`**: Aplicação React/Vite para visualização em tempo real.

---

## ⚡ Comparativo: Python vs ADVPL

| Característica | Python (pyadvpl) | ADVPL (Gerado) |
| :--- | :--- | :--- |
| **Acesso a Campo** | `SA1.A1_NOME` | `SA1->A1_NOME` |
| **Navegação** | `SA1.go_top()` | `SA1->( DbGoTop() )` |
| **Mensagens** | `ui.MsgAlert("Oi")` | `MsgAlert("Oi")` |
| **Loops** | `for i in range(1, 11)` | `For nI := 1 To 10` |
| **Variáveis** | Globais/Locais automáticas | `LOCAL` declaradas no topo |

---

## 🤝 Contribuição

1. Faça um **Fork**.
2. Crie uma branch (`git checkout -b feature/NovaFeature`).
3. Faça o **Commit** (`git commit -m 'Add NovaFeature'`).
4. Envie para o **Branch** (`git push origin feature/NovaFeature`).
5. Abra um **Pull Request**.

---

## 📜 Licença

Este projeto utiliza um modelo de **Licenciamento Dual**:

- **Uso Comunitário (Gratuito)**: Livre para uso pessoal, estudos, projetos open source e empresas com faturamento anual **inferior a R$ 100.000,00**. Regido pelos termos da [Licença MIT](LICENSE).
- **Uso Comercial (Pago)**: Obrigatório para empresas com faturamento anual **superior a R$ 100.000,00**.

### 💰 Informações de Uso

- **Gratuito**: Uso livre para empresas e desenvolvedores com faturamento anual **inferior a R$ 100.000,00**.
- **Pago**: Licença obrigatória para empresas com faturamento anual **superior a R$ 100.000,00**.

Para adquirir sua licença comercial ou consultar valores, entre em contato via: **cleudeirsilva@gmail.com**.

---

Desenvolvido com ❤️ por [Cleudeir](https://github.com/Cleudeir)
