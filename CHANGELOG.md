# Changelog

Todas as mudanças significativas do projeto **pyadvpl — Transpilador de ADVPL para Python**.

Formato: versão (do `pyproject.toml`) + data (UTC) + commits relevantes.

---

## [0.2.1] — (esta versão)

### Mudanças desta versão

- **089b760** — 089b7603cb0aab0425191e26b1de7d84f848ad07 fix: alinhar porta do dashboard no README (5173 -> 8041, D4)
- **4a2fd8d** — 4a2fd8d4f8248457d2816c487e3acd36f6b6f31d fix: alinhar versao do frontend no rodape (2.5.0 -> 0.2.0, D3)
- **06541e1** — 06541e1d73cfce7f082414635ea3f5c6cb7a470f test: atualizar timestamp do relato round-trip (561/561, 89.37%)
- **3f681dd** — 3f681ddf0c5a02d6c2339b03c095e3f9ec7abd82 docs: adicionar CHANGELOG.md com historico dos commits (D4)
- **cdc9db6** — cdc9db63021b372b3618620ba154e31b91d52d5a docs: adicionar bump_version.py para versionamento automatico (D4)Todas as mudanças significativas do projeto **pyadvpl — Transpilador de ADVPL para Python**.

Formato: versão (do `pyproject.toml`) + data (UTC) + commits relevantes.

---

## [0.2.0] — 2026-08-28

### Correções (fix)
- **D3** — Alinhar versão do frontend no rodapé (`2.5.0` → `0.2.0` em `frontend/src/App.tsx`)
- **D4** — Alinhar porta do dashboard no README (`5173` → `8041`)
- **D2** — Remover definições duplicadas de funções em `ui.py`
- **D1** — Exportar `xml_json` no nível superior do pacote `pyadvpl`

### Testes
- Atualizar timestamp do relato round-trip (561/561 @ 89.37% de sucesso)

---

## [0.1.0] — 2026-06-11 a 2026-08-27

### Infraestrutura e CLI
- **CLI** — Implementar comando `pyadvpl test` para rodar a suite localmente
- **CLI** — Implementar comandos de conversão entre Python e ADVPL (`build`, `convert`, `dev`)
- **CLI** — Simplificar imports de pacotes, expor módulos centrais no `pyadvpl`
- **CLI** — Refatorar para remover templates legados e limpar diretórios de exemplo
- **Env** — Adicionar suporte a `.env` (dotenv), atualizar assets do frontend e melhorar config da API
- **Config** — Alterar host padrão da API para `127.0.0.1` (segurança)
- **Config** — Adicionar `.env.*` ao `.gitignore` e excluir `node_modules`
- **Frontend** — Atualizar dependências para Vite 5 e vincular a localhost
- **Frontend** — Atualizar build incremental com cache de hash (`pyadvpl build --incremental`)
- **Testes** — Adicionar arquivo de teste de stubs abrangente (FWBrowse, FWDialogModal, MsNewProcess, FWRest, HttpGet, HttpPost, XmlParser, JsonObject, ArrToJson)
- **Testes** — Suite de +560 exemplos `.prw` cobrindo operadores, funções, classes, transações e SQL

### Transpilação Python → ADVPL
- Declaração automática de variáveis `LOCAL` no topo da função
- Geração de `PRIVATE` e `PUBLIC` além de `LOCAL`
- Mapeamento de acesso a campos (`SA1.A1_NOME` → `SA1->A1_NOME`)
- Mapeamento de métodos de navegação (`sa1.go_top()` → `SA1->( DbGoTop() )`)
- Funções com prefixo `u_`, `static` e `function`
- Estruturas `if/elif/else`, `while`, `for` com `range()`
- Literais de array e acesso por índice
- Expressões binárias e unárias (todos os operadores ADVPL)
- Chamadas de métodos e funções com argumentos posicionais
- Nós de pré-processador (`#include`, `#define`)
- Comentários preservados na saída
- Suporte completo a classes ADVPL (`CLASS`/`METHOD`/`ENDCLASS`)
- Suporte a `BEGIN SEQUENCE` / `RECOVER SEQUENCE` (equivalente ao `try/except`)
- Suporte a `BEGIN TRANSACTION` / `END TRANSACTION` (context manager `Transaction()`)
- Suporte a `BeginSQL` / `EndSQL` (context manager `BeginSQL()`)

### Transpilação ADVPL → Python
- Lexer com todos os operadores específicos do ADVPL (`$`, `&`, `::`, `:=`, `@`, `%`)
- Parser para as estruturas de controle principais
- Gerador Python com mapeamento de tipos e funções
- Suporte a `BEGIN SEQUENCE` / `RECOVER SEQUENCE` (equivalente ao `try/except`)
- Suporte a `BEGIN TRANSACTION` / `END TRANSACTION` (`with Transaction():`)
- Suporte a `BeginSQL` / `EndSQL` com `COLUMN` (`with BeginSQL(alias="...") as sql:`)
- Preservação de modificadores `PRIVATE` e `PUBLIC` na AST

### Biblioteca de Stubs (`pyadvpl/engine/core/`)
- **db** — funções de banco de dados (DbGoTop, DbSeek, DbUseArea, etc.)
- **db** — controle de transações (`Transaction`, `DisarmTransaction`)
- **db** — SQL nativo (`BeginSQL`, `EndSQL`, `sql_eof`, `sql_skip`, `sql_close`)
- **db** — funções SQL (`TCSqlExec`, `TCSQLError`, `TCSQLQuery`, `TCSQLPlan`, `RetSQLName`, `RetSQLCond`, `FormatIn`, `ValToSQL`)
- **ui** — diálogos e mensagens (MsgAlert, MsgYesNo, MsgInfo, etc.)
- **ui** — FWDialogModal (janela de diálogo modal personalizável)
- **ui** — MsNewProcess (processo com barra de progresso / réguas)
- **string** — manipulação de strings (AllTrim, SubStr, Upper, Lower, etc.)
- **math** — funções matemáticas (Abs, Round, Int, Sqrt, etc.)
- **date** — funções de data (Date, CToD, DToC, Month, Year, etc.)
- **array** — funções de array (AAdd, ADel, ASize, ASort, AScan, etc.)
- **protheus** — funções do framework (GetMV, SuperGetMV, Posicione, etc.)
- **protheus** — classes de browse (`FWBrowse`, `FWBrwColumn`, `FWMBrowse`, `FWMarkBrowse`, `FWTemporaryTable`)
- **protheus** — classes de modelo e relatório (`oModel`, `oReport`, `oSection`)
- **protheus** — REST/HTTP client (`FWRest`, `HttpGet`, `HttpPost`, `HttpPut`, `HttpDelete`, `HttpJson`)
- **protheus** — utilitários de área (`FWRestArea`, `RestArea`)
- **xml_json** — parser XML (`XmlParser`, `XmlParserFile`, `XmlNode`, `XmlNode2Arr`, `XmlToArr`, `IsXmlNode`, `AttIsMemberOf`, `XMLChildEx`, `XmlNodeExist`, `WSAdvValue`)
- **xml_json** — JSON (`JsonObject`, `ArrToJson`, `JsonToArr`)
- **xml_json** — visualizador XML (`TXMLViewer`)
- **types** — tipos base (`Nil`, `Array`, `Date`)
