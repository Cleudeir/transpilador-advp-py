# Especificação de Funcionalidades — pyadvpl

> **Propósito deste documento:** fornecer a especificação de funcionalidades (features, escopo, critérios de aceite e detalhes técnicos) do projeto **pyadvpl**, extraída diretamente do código-fonte do repositório (`advp-python`), para que a implementação possa prosseguir. Todo o conteúdo foi verificado contra o código no commit `25cfda7` (branch `main`).
>
> **Como usar:** cada funcionalidade (F1–F21) traz status, arquivos-fonte, comportamento verificado e critérios de aceite. As **divergências D1–D7** são inconsistências reais encontradas entre README, código e configuração — são os primeiros candidatos a iteração de implementação. O **roadmap R** lista melhorias planejadas (do README) ainda não implementadas. A **seção 8** define os requisitos de conteúdo do README (o que manter e o que corrigir para ficar consistente com o código).

---

## 1. Visão Geral

O **pyadvpl** é um framework para escrever código **Python** e transpilar para **ADVPL** (ERP TOTVS Protheus), e também converter ADVPL legado de volta para Python. É composto por:

1. **Motor de transpilação** (`pyadvpl/engine/transpiler/`) — lexer, parser e dois geradores (Python ↔ ADVPL).
2. **Biblioteca de stubs** (`pyadvpl/engine/core/`) — assinaturas/funções compatíveis com ADVPL (db, ui, string, math, date, array, protheus, types, xml_json).
3. **CLI** (`pyadvpl/engine/cli.py`) — `init`, `build` (com `--incremental`), `convert`, `dev`/`serve`, `transpile` (legado).
4. **API HTTP** (`pyadvpl/engine/server.py`) — FastAPI com `GET /api/health` e `POST /api/transpile`.
5. **Dashboard web** (`frontend/`) — React + Vite + TypeScript para transpilar em tempo real (ambas as direções).
6. **Infraestrutura** — `dev.sh`/`dev.bat`, PM2 (`ecosystem.config.cjs`), `.env` via `python-dotenv`, scripts de teste em lote.

**Versão declarada:** `0.2.0` (em `pyproject.toml` e `server.py`). O rodapé do frontend exibe "Versão Engine: 2.5.0" — ver **D3**.

**Suíte de testes verificada (executada nesta iteração):**

| Suíte | Resultado |
| --- | --- |
| `pytest pyadvpl/engine/tests/` (CLI incremental) | **12 passed** |
| `python3 -m pyadvpl.engine.transpiler.tests.test_roundtrip_bulk` (round-trip, 561 exemplos `.prw`) | **561/561 sucessos**, precisão média 89.37% |

---

## 2. Arquitetura (verificada)

```
pyadvpl/
├── __init__.py                  # re-exporta core + Nil/Date/Array/Table/MsgAlert
└── engine/
    ├── __init__.py              # re-exporta TODOS os módulos core + classes de conveniência
    ├── cli.py                   # CLI: init, build, convert, dev, transpile
    ├── server.py                # API FastAPI (health, transpile)
    ├── core/                    # stubs ADVPL (9 módulos)
    │   ├── types.py             # Nil, Date, Array, ValType, Type
    │   ├── db.py                # Transaction, BeginSQL, Db*, TCSql*, Table
    │   ├── ui.py                # MsgAlert, MsNewProcess, FWDialogModal, ...
    │   ├── string.py / math.py / date.py / array.py
    │   ├── protheus.py          # oModel, FWBrowse, FWRest, Http*, ...
    │   └── xml_json.py          # XmlParser, JsonObject, TXMLViewer, ...
    └── transpiler/
        ├── lexer.py             # tokenizador ADVPL
        ├── parser.py            # ADVPL → AST
        ├── python_generator.py  # AST → Python
        ├── python_to_ast.py     # Python → AST (via módulo ast stdlib)
        ├── advpl_generator.py   # AST → ADVPL
        └── tests/
            ├── test_roundtrip_bulk.py   # 561 exemplos .prw round-trip
            ├── debug_precision.py
            └── input/ (561 .prw) + output/ (python/ e advpl/)
frontend/                        # React + Vite + TS (porta 8041, proxy /api → 8040)
pyproject.toml                   # nome pyadvpl, versão 0.2.0, entry point cli:main
requirements.txt / .env.example / ecosystem.config.cjs / dev.sh / dev.bat
run_bulk_tests.sh / run_bulk_tests.bat
```

**Fluxo Python → ADVPL (CLI `build`)**: `PythonToAST(code)` (stdlib `ast`) → AST interna → `ADVPLGenerator(ast).generate()` → prefixado com `#Include 'Protheus.ch'`.

**Fluxo ADVPL → Python (CLI `convert`)**: `Lexer(code)` → `ADVPLParser(tokens)` → `PythonGenerator(ast).generate()`.

**API**: `POST /api/transpile` aceita `{"code": str, "direction": "advpl-to-python" | "python-to-advpl"}` e retorna `{"success": bool, "output": str, "error": str|null}`.

---

## 3. Inventário de Funcionalidades

### F1 — Lexer ADVPL
- **Status:** implementado
- **Arquivos:** `pyadvpl/engine/transpiler/lexer.py` (138 linhas)
- **Comportamento verificado:** especificação de tokens com regex (strings com aspas abertas, números, `.T.`/`.F.`, `.AND.`/`.OR.`/`.NOT.`, `::`, `->`, `**`/`^`, `:=`, `+=`/`-=`/`*=`/`/=`, `++`/`--`, `>=`, `<=`, `==`/`=`, `!=`/`<>`, `$`, `&`, `@`, `%`, identificadores Unicode). Palavras-chave mapeadas (`USER`, `FUNCTION`, `LOCAL`, `IF`, `WHILE`, `FOR`, `CLASS`, `BEGINSQL`, `BEGIN/SEQUENCE/RECOVER`, `TRANSACTION`, `COLUMN`, `AS`, ...). Continuação de linha com `;`.
- **Critérios de aceite:**
  - [ ] Tokenizar cada operador/token da especificação sem `LexerError` em entradas válidas.
  - [ ] Identificadores com acentos (Unicode) tokenizados como `IDENTIFIER`.
  - [ ] Comentários `//`, `/* */` e blocos Protheus `/*.../*` preservados como tokens de comentário.

### F2 — Parser ADVPL → AST
- **Status:** implementado
- **Arquivos:** `pyadvpl/engine/transpiler/parser.py` (834 linhas)
- **Comportamento verificado:** constrói AST para `USER/STATIC/FUNCTION`, `CLASS`/`METHOD`, `IF/ELSEIF/ELSE/ENDIF`, `DO CASE/OTHERWISE/ENDCASE`, `WHILE/ENDDO`, `FOR...TO...STEP...NEXT`, `BEGIN SEQUENCE/RECOVER USING/END SEQUENCE`, `BEGIN TRANSACTION/END TRANSACTION`, `BeginSQL...EndSQL` (alias, `COLUMN ... AS`), declarações `LOCAL/PRIVATE/PUBLIC/STATIC` (múltiplas em uma linha), expressões com precedência (or/and/comparison/additive/multiplicative/power/unary), codeblocks `{|params| expr}`, macros `&`, acesso por alias `->`, `::` self, chamadas de método com `:`, `++`/`--` pós-fixados.
- **Critérios de aceite:**
  - [ ] Todos os 561 `.prw` de `tests/input/` parseiam sem `ParserError` (coberto pelo bulk test — 561/561).
  - [ ] Nova construção sintática ADVPL adicionada à gramática preserva round-trip ≥ 85% (padrão atual: 89.37% médio).

### F3 — Gerador Python (AST → Python)
- **Status:** implementado
- **Arquivos:** `pyadvpl/engine/transpiler/python_generator.py` (398 linhas)
- **Comportamento verificado:** gera `def u_X`/`s_X`, métodos como funções `<Classe>_<metodo>(self, ...)` (com comentário `# Method ...`), `if/elif/else`, `try/except Exception as e`, `with Transaction():`, `with BeginSQL(alias=...) as sql:` (com `sql.column(...)` e `sql.query(...)`), `while`, `break`/`continue`, `IIF` → ternário, `$` → `in`, `.AND.` → `and`, `:=` → `=` (walrus em contexto de expressão), atribuição em atributo via `setattr(...) or val`, `ref_()` para `@`, macros → `eval(...)`, codeblocks → `lambda`, alias `->` → `obj.field`, sanitiza palavras-chave Python.
- **Critérios de aceite:**
  - [ ] Saída gerada é Python sintaticamente válido para os 561 exemplos (verificado pelo bulk test).
  - [ ] Alterações no gerador não reduzem a precisão média do round-trip abaixo de 89%.

### F4 — Conversor Python → AST
- **Status:** implementado
- **Arquivos:** `pyadvpl/engine/transpiler/python_to_ast.py` (314 linhas)
- **Comportamento verificado:** usa `ast` stdlib; converte `FunctionDef` (`u_`→USER FUNCTION, `s_`→STATIC FUNCTION), `ClassDef` (com `__init__`→`New`, varre `self.attr` como `DATA`), `If`, `While`, `For` com `range()`, `Try`→`TryStatement`, `With Transaction()`→`TransactionStatement`, `With BeginSQL(alias=...)` (coleta `column()`/`query()`), atribuições, `AugAssign`, f-strings → concatenação de `+`, expressões (`in`→`$`, `and/or`, `not`, subscrito, lista). `x = Table("X")` é ignorado (o acesso a campos vira alias). Namespaces `ui/db/protheus/math/date/array/string/Date/Array` são "stripados" para funções globais. Comentários são preservados via codificação hex (`_advpl_comment_`), com suporte a `# PREPROCESSOR:`.
- **Critérios de aceite:**
  - [ ] Trechos Python do README (transações, SQL, variáveis, browse, REST, XML/JSON) transpilam sem erro.
  - [ ] Comentários `#` no código-fonte Python aparecem como `//` no ADVPL gerado.

### F5 — Gerador ADVPL (AST → ADVPL)
- **Status:** implementado
- **Arquivos:** `pyadvpl/engine/transpiler/advpl_generator.py` (369 linhas)
- **Comportamento verificado:** gera `USER FUNCTION`/`STATIC FUNCTION`/`FUNCTION`; **auto-declaração** de variáveis agrupadas por modificador na ordem `STATIC, PRIVATE, PUBLIC, LOCAL` (parâmetros e `SELF`/`NIL` excluídos); `CLASS ... DATA ... METHOD ... ENDCLASS`; `METHOD ... CLASS ...`; `If/ElseIf/Else/EndIf`; `BEGIN SEQUENCE/RECOVER [USING var]/END SEQUENCE`; `Begin Transaction/End Transaction`; `BeginSql Alias "X"` + `COLUMN A AS TIPO` + query + corpo; `While/EndDo`; `For := ... To ... Next`; mapeamento de métodos de `Table` (`go_top`→`DbGoTop`, `skip`→`DbSkip`, `rec_lock`→`RecLock`, `unlock`→`MsUnlock`, ...) em `ALIAS->( DbXxx() )`; `AliasAccess`→`ALIAS->CAMPO`; `Self`→`::`; operadores (`in`→`$`, `and`→`.AND.`, `or`→`.OR.`, `==`→`=`, `!=`→`<>`, `!`→`.NOT.`); `RETURN Nil` automático no fim de funções sem `RETURN`.
- **Critérios de aceite:**
  - [ ] Saída de `build` inicia com `#Include 'Protheus.ch'`.
  - [ ] Toda variável atribuída sem declaração explícita ganha declaração `LOCAL` no topo da função.

### F6 — Stubs core: `types`
- **Status:** implementado
- **Arquivos:** `pyadvpl/engine/core/types.py` (221 linhas)
- **Conteúdo verificado:** `Nil` (singleton `_NilType`), classe `Date` (com operações de data), `Array(list)` (compat com `A*`), `ValType()`, `Type()`.
- **Critérios de aceite:**
  - [ ] `Nil` é comparável/impressível e usado como valor padrão nos stubs.
  - [ ] `Date` suporta conversão `CToD`/`DToC` e aritmética básica de datas.

### F7 — Stubs core: `db`
- **Status:** implementado
- **Arquivos:** `pyadvpl/engine/core/db.py` (383 linhas)
- **Conteúdo verificado:** `Transaction` (context manager; `__exit__` com exceção chama `DisarmTransaction()`), `DisarmTransaction`, `BeginSQL` (context manager com `column()`, `query()`, acesso a campos via `__getattr__` → `sql.B1_COD`), `sql_eof`/`sql_skip`/`sql_close`/`sql_alias`, `TCSqlExec`/`TCSQLError`/`TCSQLQuery`/`TCSQLPlan`, `RetSQLName`/`RetSQLCond`/`FormatIn`/`ValToSQL`, navegação (`DbGoTop`, `DbGoBottom`, `DbSkip`, `DbSeek`, `DbEof`, `DbBof`, `DbSelectArea`, `DbSetOrder`, `DbCloseArea`, `RecLock`, `MsUnlock`, `RecNo`, `LastRec`, `Alias`, `Select`, `Used`, `OrdSetFocus`), classe `Table` (getters/setters de campo → alias, métodos `go_top`/`go_bottom`/`skip`/`seek`/`eof`/`bof`/`set_order`/`select`/`rec_lock`/`unlock`/`rec_no`/`last_rec`/`count`).
- **Critérios de aceite:**
  - [ ] `from pyadvpl import db` funciona; `Table("SA1").A1_NOME` e `.go_top()` existem.
  - [ ] `with Transaction():` e `with BeginSQL(alias="Q") as sql:` são instanciáveis.

### F8 — Stubs core: `ui`
- **Status:** implementado — **duplicação de definições corrigida (ver D2)**
- **Arquivos:** `pyadvpl/engine/core/ui.py` (377 linhas)
- **Conteúdo verificado:** mensagens (`MsgAlert`, `MsgInfo`, `MsgStop`, `MsgYesNo`, `MsgNoYes`, `MsgOkCancel`, `ConOut`, `FWAlertInfo/Warning/Success/YesNo`, `FWMsgRun`), régua de progresso (`ProcRegua`, `IncRegua`, `ProcAltera`, `SetProcInfo`), classes `MsNewProcess` (linha 93) e `FWDialogModal` (linha 187), `MsAdvSize`, `InputBox`, `ReadVar`. Cada função/classes definida exatamente uma vez (as duplicações de linhas 14–84 foram removidas; a versão canônica fica em 345–451).
- **Critérios de aceite (após correção D2):**
  - [ ] Cada função/classes definida exatamente uma vez no módulo.
  - [ ] Comportamento preservado (as segundas definições são a versão canônica; remover apenas as primeiras).

### F9 — Stubs core: `string`
- **Status:** implementado
- **Arquivos:** `pyadvpl/engine/core/string.py` (212 linhas)
- **Conteúdo verificado:** `AllTrim`, `LTrim`, `RTrim`, `Upper`, `Lower`, `Len`, `SubStr`, `Left`, `Right`, `At`, `RAt`, `Replicate`, `Space`, `PadL`, `PadR`, `PadC`, `StrZero`, `Str`, `Val`, `Chr`, `Asc`, `StrToHex`, `HexToStr`, `CharMix`, `Occurs`, `IsAlpha`, `IsDigit`, `IsLower`, `IsUpper`, `Transform`.
- **Critérios de aceite:**
  - [ ] Comportamento compatível com ADVPL para entradas típicas (ex.: `SubStr("ADVPL", 2, 3)` == `"DVP"` — semântica ADVPL de posição 1-based).

### F10 — Stubs core: `math`
- **Status:** implementado
- **Arquivos:** `pyadvpl/engine/core/math.py` (63 linhas)
- **Conteúdo verificado:** `Round`, `Int`, `Abs`, `Sqrt`, `Exp`, `Log`, `Max`, `Min`, `Mod`, `Floor`, `Ceiling`.
- **Critérios de aceite:** chamáveis e importáveis via `from pyadvpl import math`.

### F11 — Stubs core: `date`
- **Status:** implementado
- **Arquivos:** `pyadvpl/engine/core/date.py` (69 linhas)
- **Conteúdo verificado:** `CToD`, `DToC`, `DToS`, `SToD`, `Month`, `Year`, `Day`, `Today`, `Time`, `Seconds`, `LastDayOfMonth`.
- **Critérios de aceite:** compat com formato `%d/%m/%Y` e 1-based para mês/dia.

### F12 — Stubs core: `array`
- **Status:** implementado
- **Arquivos:** `pyadvpl/engine/core/array.py` (111 linhas)
- **Conteúdo verificado:** `aAdd`, `aDel`, `aSize`, `aSort` (com parâmetros `lNilFirst`, `nType`, `bOrder`), `aScan`, `aCopy`, `aClone`, `aEval`, `Len`, `aFill`.
- **Critérios de aceite:** chamáveis; `aAdd(arr, item)` retorna array com item adicionado.

### F13 — Stubs core: `protheus`
- **Status:** implementado
- **Arquivos:** `pyadvpl/engine/core/protheus.py` (847 linhas)
- **Conteúdo verificado:** parâmetros SX6 (`SuperGetMV`, `GetMV`, `PutMV`), numeração (`GetSX5Num`, `GetNewNum`, `GetNextC`), ambiente (`CEMPRESA`, `CFILIAL`, `CUSUARIO`, `CNOME`, `RADRetorno`), modelo de formulário (`oModel` com `getValue`/`setValue`/`getCell`/`setCell`/`getLineCount`/`addLine`/`delLine`/`isValidated`/`activate`/`deActivate`/`commitData`), relatórios (`oReport`, `oSection`), browses (`FWBrowse`, `FWBrwColumn`, `FWTemporaryTable`, `FWMBrowse`, `mBrowse`, `FWMarkBrowse`), `TCSQLQuery`, `FWExecView`, `ExecAuto`, REST/HTTP (`FWRest` com `Get`/`Post`/`Put`/`Delete` simulados, `HttpGet`, `HttpPost`, `HttpPut`, `HttpDelete`, `HttpJson`), áreas (`FWRestArea`, `RestArea`), validação (`ValidCpf` — implementação real, `ValidCnpj` — implementação real).
- **Critérios de aceite:**
  - [ ] `FWBrowse().New().SetAlias("SA1")` e cadeias de métodos são encadeáveis (retornam self).
  - [ ] `ValidCpf`/`ValidCnpj` validam CPF/CNPJ corretos e rejeitam inválidos (dígitos verificadores).

### F14 — Stubs core: `xml_json`
- **Status:** implementado — **não exportado no pacote top-level (ver D1)**
- **Arquivos:** `pyadvpl/engine/core/xml_json.py` (481 linhas)
- **Conteúdo verificado:** `XmlNode`, `XmlParser`, `XmlParserFile`, `XmlNode2Arr`, `XmlToArr`, `IsXmlNode`, `AttIsMemberOf`, `XMLChildEx`, `XmlNodeExist`, `WSAdvValue`, `JsonObject`, `ArrToJson`, `JsonToArr`, `TXMLViewer`.
- **Critérios de aceite (após correção D1):**
  - [ ] `from pyadvpl import xml_json` funciona (hoje **falha** — ver D1).
  - [ ] `XmlParser(cXml, "_")` e `JsonObject().New().FromJson(...)` funcionam.

### F15 — CLI
- **Status:** implementado
- **Arquivos:** `pyadvpl/engine/cli.py` (244 linhas)
- **Comportamento verificado:** `pyadvpl init <nome>` (copia template `pyadvpl/project/` se existir — **template não encontrado no repo**, cai no caminho "estrutura básica": cria `src/`, `dist/`, `legacy/`, `pyadvpl.toml`, `src/main.py`), `pyadvpl build [input] -o [output] [--incremental]` (default `src/` → `dist/`), `pyadvpl convert [input] -o [output]` (default `legacy/` → `src/`), `pyadvpl dev`/`serve` (uvicorn), `pyadvpl transpile` (legado). Lê `pyadvpl.toml` (`[transpile] input_dir/output_dir`). Encoding: py2adv lê UTF-8 e grava latin-1; adv2py lê latin-1 e grava UTF-8.
- **Critérios de aceite:**
  - [ ] `pyadvpl build` transpila `src/*.py` → `dist/*.prw` com `#Include 'Protheus.ch'`.
  - [ ] `pyadvpl convert` transpila `legacy/*.prw` → `src/*.py`.
  - [ ] `pyadvpl init x` cria projeto funcional (ver D5 para requisito de Python ≥ 3.11 por causa de `tomllib`).

### F16 — Build incremental (`--incremental`)
- **Status:** implementado (commit `25cfda7`; 12 testes dedicados)
- **Arquivos:** `pyadvpl/engine/cli.py` (`file_hash`, `load_cache`, `save_cache`, `process_transpile`), `pyadvpl/engine/tests/test_cli_incremental.py`
- **Comportamento verificado:** cache SHA-256 por arquivo-fonte em `.pyadvpl_cache.json` dentro de `dist/`; pula fontes inalteradas; recompila modificadas, saídas apagadas e fontes removidas (podando o cache); **não cacheia falhas**; `convert` não cria cache; funciona para arquivo único.
- **Critérios de aceite (todos cobertos por 12 testes que passam):**
  - [ ] Primeiro build transpila tudo; segundo build sem alterações não transpila nada.
  - [ ] Modificação de 1 de N arquivos recompila apenas esse arquivo.
  - [ ] Saída apagada é regenerada; fonte removida é podada do cache; falha não é cacheada.

### F17 — API HTTP (FastAPI)
- **Status:** implementado
- **Arquivos:** `pyadvpl/engine/server.py` (117 linhas)
- **Comportamento verificado:** `GET /api/health` → `{"status": "ok", "version": "0.2.0"}`; `POST /api/transpile` com body `{"code": str, "direction": "advpl-to-python" | "python-to-advpl"}` → `{"success": bool, "output": str, "error": str|null}`; CORS configurável por `ALLOWED_ORIGINS` (default `*`); middleware para Chrome Private Network Access (PNA) respondendo 204 ao preflight OPTIONS com `Access-Control-Allow-Private-Network`. Host/porta via `API_HOST`/`API_PORT` (default `127.0.0.1:8040`).
- **Critérios de aceite:**
  - [ ] `GET /api/health` retorna 200 com `status: ok`.
  - [ ] `POST /api/transpile` transpila nas duas direções e retorna erro (não exceção 500) para direção inválida ou código malformado.

### F18 — Dashboard web (frontend)
- **Status:** implementado
- **Arquivos:** `frontend/src/App.tsx`, `frontend/vite.config.ts`, `frontend/package.json`, `frontend/src/index.css`, `frontend/src/main.tsx`
- **Comportamento verificado:** React 18 + Vite 5 + TS; editor de entrada + preview de saída; transpilação com debounce de 600 ms via `POST /api/transpile`; toggle de direção (Python↔ADVPL) que usa a saída como nova entrada; upload de arquivo (`.py`/`.prw`); botões Copiar e Exportar (`.prw`/`.py`); sidebar "Capabilities"; API URL via `VITE_API_URL` (default `/api`) com proxy Vite `/api` → `http://localhost:8040`. Porta do Vite: **8041** (`vite.config.ts`). Rodapé: "Versão Engine: 2.5.0" (ver D3).
- **Critérios de aceite:**
  - [ ] `npm run build` (tsc + vite build) conclui sem erros de tipo.
  - [ ] Com backend em 8040, o dashboard transpila nas duas direções e exibe erro quando a API está indisponível.

### F19 — Infra: ambiente de desenvolvimento
- **Status:** implementado
- **Arquivos:** `dev.sh`, `dev.bat`, `ecosystem.config.cjs` (PM2), `.env.example`, `requirements.txt`, `pyproject.toml`
- **Comportamento verificado:** `dev.sh` mata processos nas portas 8040/8041/3000, sobe backend (`python3 -m pyadvpl.engine.server`) e frontend (`npm run dev -- --host 0.0.0.0`), trap de Ctrl+C. `ecosystem.config.cjs` define apps PM2 `pyadvpl-backend` (python3 -m pyadvpl.engine.server) e `pyadvpl-frontend` (vite), lendo `.env` manualmente, logs em `logs/`. `.env.example` documenta `API_HOST=0.0.0.0`, `API_PORT=8040`, `FRONTEND_PORT=8041`, `ALLOWED_ORIGINS`, `LOG_LEVEL` (ver D6).
- **Critérios de aceite:**
  - [ ] `pm2 start ecosystem.config.cjs` sobe os dois apps e loga em `logs/`.

### F20 — Suite de testes round-trip
- **Status:** implementado (561/561, precisão média 89.37%)
- **Arquivos:** `pyadvpl/engine/transpiler/tests/test_roundtrip_bulk.py`, `tests/input/` (561 `.prw`), `tests/output/python|advpl/`, `run_bulk_tests.sh`, `run_bulk_tests.bat`, `debug_precision.py`
- **Comportamento verificado:** ADVPL → Python → ADVPL, comparando normalizado (comentários removidos, keywords removidas, espaços/pontuação removidos, números normalizados) com `SequenceMatcher`; relatório em `output/_roundtrip_report.txt`.
- **Critérios de aceite:**
  - [ ] Rodando `python3 -m pyadvpl.engine.transpiler.tests.test_roundtrip_bulk`, todos os 561 arquivos reportam `Success`.
  - [ ] Novas features mantêm precisão média ≥ 89%.

### F21 — Testes unitários do CLI
- **Status:** implementado (12 testes passando)
- **Arquivos:** `pyadvpl/engine/tests/test_cli_incremental.py`
- **Critérios de aceite:** `python3 -m pytest pyadvpl/engine/tests/ -q` → 12 passed.

---

## 4. Divergências Encontradas (verificadas nesta iteração)

> Estas são inconsistências reais entre README, código e configuração. São os alvos imediatos de implementação.

### D1 — `from pyadvpl import xml_json` falha (crítico)
- **Evidência:** `pyadvpl/__init__.py` re-exporta `array, date, db, math, protheus, string, types, ui` e `Nil, Date, Array, Table, MsgAlert` — **não exporta `xml_json`**. O `README.md` (linhas ~319 e ~333) usa `from pyadvpl import xml_json`.
- **Verificação executada:** `from pyadvpl import xml_json` → `ImportError: cannot import name 'xml_json' from 'pyadvpl'`.
- **Correção:** adicionar `xml_json` ao bloco `from .engine.core import (...)` em `pyadvpl/__init__.py` (e, por conveniência, exportar `XmlParser`, `JsonObject`, etc., como já faz `pyadvpl/engine/__init__.py`).
- **Critérios de aceite:**
  - [ ] `from pyadvpl import xml_json` funciona.
  - [ ] `from pyadvpl import XmlParser, JsonObject` funciona (paridade com `engine/__init__.py`).
  - [ ] Nenhum teste existente regride.

### D2 — Funções duplicadas em `ui.py` (manutenibilidade)
- **Evidência:** `MsgAlert`, `MsgInfo`, `MsgStop`, `MsgYesNo`, `MsgNoYes`, `MsgOkCancel`, `ConOut`, `FWMsgRun`, `ProcRegua`, `IncRegua`, `ProcAltera`, `SetProcInfo` definidas em 2 grupos (linhas 14–84 e 345–451). As segundas definições são canônicas (sobrescrevem as primeiras).
- **Correção:** remover o primeiro grupo (linhas 14–84), mantendo apenas as versões canônicas em 345–451 (que incluem `InputBox`/`ReadVar`).
- **Critérios de aceite:**
  - [ ] `grep -c '^def MsgAlert' pyadvpl/engine/core/ui.py` → 1.
  - [ ] Todas as funções/classes continuam importáveis e com o mesmo comportamento.
  - [ ] Round-trip e outros testes não regredem.

### D3 — Versão inconsistente (0.2.0 vs 2.5.0)
- **Evidência:** `pyproject.toml` → `version = "0.2.0"`; `server.py` → `version="0.2.0"`; `frontend/src/App.tsx` → "Versão Engine: **2.5.0**".
- **Correção:** alinhar a versão do rodapé do frontend à versão real do pacote (0.2.0) ou centralizar a versão (ex.: importar de `pyadvpl`/metadata).
- **Critérios de aceite:** rodapé do frontend exibe a mesma versão do `pyproject.toml`.

### D4 — Porta do frontend no README (5173 vs 8041)
- **Evidência:** `README.md` diz "Acesse o link gerado (ex: `http://localhost:5173`)"; `vite.config.ts` fixa porta **8041**; `dev.sh`/PM2 usam 8041.
- **Correção:** atualizar README para `http://localhost:8041`.
- **Critérios de aceite:** README, `vite.config.ts` e `dev.sh` referenciam a mesma porta (8041).

### D5 — `requires-python` vs uso de `tomllib` (Python 3.11+)
- **Evidência:** `pyproject.toml` → `requires-python = ">=3.8"`, mas `cli.py` faz `import tomllib` (stdlib somente a partir de **Python 3.11**).
- **Correção (uma das opções):** (a) subir `requires-python` para `>=3.11`; ou (b) trocar `tomllib` por `tomli` com fallback condicional — **nota: a regra do projeto proíbe código de fallback defensivo**, portanto a opção (a) é a preferida, a menos que o usuário decida contrário.
- **Critérios de aceite:** `python3 -c "import tomllib"` disponível no ambiente mínimo declarado, ou `requires-python` atualizado para `>=3.11`.

### D6 — `.env.example` diverge do default de segurança do código
- **Evidência:** commit `bb31c32` mudou o default de `API_HOST` para `127.0.0.1` (segurança), mas `.env.example` ainda documenta `API_HOST=0.0.0.0`.
- **Correção:** atualizar `.env.example` para `API_HOST=127.0.0.1` (ou documentar explicitamente que `0.0.0.0` é para exposição em rede, uso consciente).
- **Critérios de aceite:** `.env.example` reflete o default seguro do código.

### D7 — `pyadvpl test` (roadmap) não implementado
- **Evidência:** `cli.py` não tem subcomando `test`; README lista como 🎯 no roadmap.
- **Implementação:** adicionar subcomando `test` que roda a suíte (ex.: `pytest` + bulk round-trip) e imprime resumo (ex.: precisão média).
- **Critérios de aceite:** `pyadvpl test` executa a suíte e reporta pass/fail + precisão média sem exigir flags.

---

## 5. Roadmap (do README — não implementado)

- **Transpilador**
  - 💡 Codeblocks ADVPL `{ |x| expr }` → lambdas Python (parser já suporta codeblocks; verificar conversão bidirecional completa).
  - 💡 `#IFDEF`/`#IFNDEF` no pré-processador.
  - 💡 Preservação de comentários de documentação no round-trip.
  - 💡 `STEP` em loops `FOR` (parser já lê `STEP`; geradores ainda não emitem/usam).
- **Stubs**
  - 💡 Type hints completos e docstrings em todos os stubs.
  - 💡 `TCSqlToArr` e funções de consulta SQL via stub.
- **CLI/Dashboard**
  - 🎯 `pyadvpl test` (ver **D7**).
  - 🎯 Relatório de cobertura de transpilação (quais exemplos passam/falham).
  - ✅ `pyadvpl build --incremental` — **implementado** (F16).
  - 💡 `pyadvpl dev --watch`.
  - 💡 Plugin VS Code com diagnósticos em tempo real.
- **Qualidade/Infra**
  - 🎯 CI/CD (GitHub Actions) com bulk tests.
  - 🎯 Publicar no PyPI.
  - 💡 `pre-commit` com `ruff` e `mypy`.
  - 💡 Documentação MkDocs/Sphinx.

---

## 6. Convenções do Projeto (do README e do código)

- Comentários e docstrings em **Português Brasileiro**.
- Estilo `PEP 8`; `ruff` para lint (ainda não configurado).
- Novos stubs seguem o padrão de `db.py`: função com `pass` e docstring com o equivalente ADVPL.
- **Regra do projeto: sem código de fallback** (sem `try/except` defensivo, valores padrão, lógica defensiva) — exceção: `__exit__` de `Transaction` e `BeginSQL` usam `return False` por contrato de context manager (comportamento nativo, não fallback).
- Novos testes de transpilação: adicionar apenas `input/*.prw`; o `output/*.py` é gerado automaticamente pelo bulk test.

---

## 7. Resumo Executivo para a Próxima Iteração

| # | Item | Tipo | Esforço estimado |
| --- | --- | --- | --- |
| D1 | Exportar `xml_json` no pacote top-level | Correção (1 linha + teste) | Baixo |
| D2 | Remover funções duplicadas em `ui.py` | Correção (limpeza) | Baixo |
| D3 | Alinhar versão frontend (2.5.0 → 0.2.0) | Correção | Baixo |
| D4 | Atualizar porta 5173 → 8041 no README | Correção (docs) | Baixo |
| D5 | Resolver `tomllib` vs Python 3.8 | Decisão + correção | Médio |
| D6 | Alinhar `.env.example` ao default seguro | Correção (docs) | Baixo |
| D7 | Implementar `pyadvpl test` | Feature (roadmap 🎯) | Médio |
| R | Roadmap restante | Feature (💡) | Variável |

---

## 8. Requisitos de Conteúdo do README (README Content Requirements)

> Esta seção define o que o `README.md` deve conter e os pontos de inconsistência com o código que devem ser corrigidos, verificados nesta iteração (commit `25cfda7`).

### 8.1 Conteúdo obrigatório (já presente no README — manter)

1. **Descrição do projeto** — framework que transpila Python ↔ ADVPL para TOTVS Protheus (✓ §"O **pyadvpl** é...").
2. **Principais funcionalidades** — escrita idiomática, stubs, transpilação inteligente, CLI, dashboard, auto-declaração, transações, SQL nativo, browse, janelas, REST/HTTP, XML/JSON (✓ §"🔥 Principais Funcionalidades").
3. **Instalação** — requisitos (Python + Node), venv, `pip install -r requirements.txt` + `pip install -e .`, frontend `npm install`, scripts `dev.sh`/`dev.bat` (✓).
4. **Testes** — `run_bulk_tests.sh` / `run_bulk_tests.bat` (✓).
5. **Como usar** — CLI (`init`, `build`, `convert`, `dev`) e Dashboard; comparativo Python vs ADVPL; exemplos de uso (transações, SQL, variáveis, browse, diálogo, progresso, REST, XML, JSON) (✓).
6. **Arquitetura** — estrutura de diretórios e responsabilidade de cada caminho (✓).
7. **Contribuição** — setup, fluxo de PR, convenções (✓).
8. **Licença** — dual (MIT comunitário / comercial pago) (✓).

### 8.2 Correções obrigatórias (divergências verificadas)

| ID | O que o README diz | Realidade (código/config) | Ação no README |
| --- | --- | --- | --- |
| D4 | "Acesse o link gerado (ex: `http://localhost:5173`)" | Vite fixa porta **8041** (`frontend/vite.config.ts`) | Atualizar para `http://localhost:8041` |
| D5 | "Python 3.8+" | `cli.py` importa `tomllib` (stdlib **Python 3.11+**) | Após decisão: documentar versão mínima real (≥ 3.11, opção (a) — sem fallback) |
| D6 | `.env.example` documenta `API_HOST=0.0.0.0` | Código default seguro `127.0.0.1` (commit `bb31c32`) | Alinhar `.env.example`; README não documenta o default — adicionar nota se necessário |
| D3 | — (rodapé do frontend "Versão Engine: 2.5.0") | Pacote é `0.2.0` | Corrigir versão no frontend; README não precisa mudar se seguir a versão do pacote |

### 8.3 Critérios de aceite (docs consistentes)

- [ ] `README.md` referencia a porta `8041` para o dashboard (nenhuma menção a `5173`).
- [ ] `README.md` documenta a versão mínima de Python consistente com a decisão D5.
- [ ] `README.md` e `.env.example` refletem o default seguro `API_HOST=127.0.0.1`.
- [ ] Rodapé do frontend exibe a mesma versão do `pyproject.toml` (`0.2.0`).
