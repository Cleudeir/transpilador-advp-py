# Esse exemplo faz parte da série do YouTube, Maratona de Exemplos, do canal Terminal de Informação, 
#     caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2024/07/13/criando-um-webservice-rest-com-wsrestful-maratona-advpl-e-tl-535/
# Bibliotecas
# PREPROCESSOR: #Include "Totvs.ch"
# PREPROCESSOR: #Include "RESTFul.ch"
# PREPROCESSOR: #Include "TopConn.ch"
# {Protheus.doc} WSRESTFUL zWSProdutos
# Exemplo de Webservice usando REST
# @author Atilio
# @since 07/04/2022
# @version 1.0
# @see https://tdn.totvs.com/display/public/framework/WSRESTFUL
# @obs 
# 
#     **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
WSRESTFUL
zWSProdutos
DESCRIPTION
'WebService Cadastro de Produtos'
# Atributos
WSDATA
id
# AS
STRING
WSDATA
updated_at
# AS
STRING
WSDATA
limit
# AS
INTEGER
WSDATA
page
# AS
INTEGER
# Métodos
WSMETHOD
GET
ID
DESCRIPTION
'Retorna o registro pesquisado'
WSSYNTAX
'/zWSProdutos/get_id?{id}'
PATH
'get_id'
PRODUCES
APPLICATION_JSON
WSMETHOD
GET
ALL
DESCRIPTION
'Retorna todos os registros'
WSSYNTAX
'/zWSProdutos/get_all?{updated_at, limit, page}'
PATH
'get_all'
PRODUCES
APPLICATION_JSON
WSMETHOD
POST
NEW
DESCRIPTION
'Inclusão de registro'
WSSYNTAX
'/zWSProdutos/new'
PATH
'new'
PRODUCES
APPLICATION_JSON
END
WSRESTFUL
# {Protheus.doc} WSMETHOD GET ID
# Busca registro via ID
# @author Atilio
# @since 07/04/2022
# @version 1.0
# @param id, Caractere, String que será pesquisada através do MsSeek
# @obs Codigo gerado automaticamente pelo Autumn Code Maker
# @see http://autumncodemaker.com
WSMETHOD
GET
ID
WSRECEIVE
id
WSSERVICE
zWSProdutos
lRet = True
jResponse = JsonObject().New()
cAliasWS = 'SB1'
# Se o id estiver vazio
if Empty(self.id()):
    # SetRestFault(500, 'Falha ao consultar o registro') //caso queira usar esse comando, você não poderá usar outros retornos, como os abaixo
    self.setStatus(500)
    jResponse['errorId'] = 'ID001'
    jResponse['error'] = 'ID vazio'
    jResponse['solution'] = 'Informe o ID'
else:
    DbSelectArea(cAliasWS)
    cAliasWS.DbSetOrder(1)
    # Se não encontrar o registro
    if not cAliasWS.MsSeek(FWxFilial(cAliasWS) + self.id()):
        # SetRestFault(500, 'Falha ao consultar ID') //caso queira usar esse comando, você não poderá usar outros retornos, como os abaixo
        self.setStatus(500)
        jResponse['errorId'] = 'ID002'
        jResponse['error'] = 'ID não encontrado'
        jResponse['solution'] = 'Código ID não encontrado na tabela ' + cAliasWS
    else:
        # Define o retorno
        jResponse['cod'] = cAliasWS.B1_COD
        jResponse['desc'] = cAliasWS.B1_DESC
        jResponse['tipo'] = cAliasWS.B1_TIPO
        jResponse['um'] = cAliasWS.B1_UM
        jResponse['locpad'] = cAliasWS.B1_LOCPAD
        jResponse['grupo'] = cAliasWS.B1_GRUPO


# Define o retorno
self.SetContentType('application/json')
self.SetResponse(jResponse.toJSON())
return lRet
# {Protheus.doc} WSMETHOD GET ALL
# Busca todos os registros através de paginação
# @author Atilio
# @since 07/04/2022
# @version 1.0
# @param updated_at, Caractere, Data de alteração no formato string 'YYYY-MM-DD' (somente se tiver o campo USERLGA / USERGA na tabela)
# @param limit, Numérico, Limite de registros que irá vir (por exemplo trazer apenas 100 registros)
# @param page, Numérico, Número da página que irá buscar (se existir 1000 registros dividido por 100 terá 10 páginas de pesquisa)
# @obs Codigo gerado automaticamente pelo Autumn Code Maker
# 
#     Poderia ser usado o FWAdapterBaseV2(), mas em algumas versões antigas não existe essa funcionalidade
#     então a paginação foi feita manualmente
# 
# @see http://autumncodemaker.com
WSMETHOD
GET
ALL
WSRECEIVE
updated_at
# ,
limit
# ,
page
WSSERVICE
zWSProdutos
lRet = True
jResponse = JsonObject().New()
cQueryTab = ''
nTamanho = 10
nTotal = 0
nPags = 0
nPagina = 0
nAtual = 0
oRegistro = None
cAliasWS = 'SB1'
# Efetua a busca dos registros
cQueryTab = ' SELECT ' + CRLF
cQueryTab += '     TAB.R_E_C_N_O_ AS TABREC ' + CRLF
cQueryTab += ' FROM ' + CRLF
cQueryTab += '     ' + RetSQLName(cAliasWS) + ' TAB ' + CRLF
cQueryTab += ' WHERE ' + CRLF
cQueryTab += "     TAB.D_E_L_E_T_ = '' " + CRLF
if not Empty(self.updated_at()):
    cQueryTab += "     AND ((CASE WHEN SUBSTRING(B1_USERLGA, 03, 1) != ' ' THEN " + CRLF
    cQueryTab += "        CONVERT(VARCHAR,DATEADD(DAY,((ASCII(SUBSTRING(B1_USERLGA,12,1)) - 50) * 100 + (ASCII(SUBSTRING(B1_USERLGA,16,1)) - 50)),'19960101'),112) " + CRLF
    cQueryTab += "        ELSE '' " + CRLF
    cQueryTab += "     END) >= '" + StrTran(self.updated_at(), '-', '') + "') " + CRLF

cQueryTab += ' ORDER BY ' + CRLF
cQueryTab += '     TABREC ' + CRLF
TCQuery
cQueryTab
New
Alias
'QRY_TAB'
# Se não encontrar registros
if QRY_TAB.EoF():
    # SetRestFault(500, 'Falha ao consultar registros') //caso queira usar esse comando, você não poderá usar outros retornos, como os abaixo
    self.setStatus(500)
    jResponse['errorId'] = 'ALL003'
    jResponse['error'] = 'Registro(s) não encontrado(s)'
    jResponse['solution'] = 'A consulta de registros não retornou nenhuma informação'
else:
    jResponse['objects'] = []
    # Conta o total de registros
    Count
    To
    nTotal
    QRY_TAB.DbGoTop()
    # O tamanho do retorno, será o limit, se ele estiver definido
    if not Empty(self.limit()):
        nTamanho = self.limit()

    # Pegando total de páginas
    nPags = NoRound(nTotal / nTamanho, 0)
    nPags += (1 if nTotal % nTamanho != 0 else 0)
    # Se vier página
    if not Empty(self.page()):
        nPagina = self.page()

    # Se a página vier zerada ou negativa ou for maior que o máximo, será 1
    if nPagina <= 0 or nPagina > nPags:
        nPagina = 1

    # Se a página for diferente de 1, pula os registros
    if nPagina != 1:
        QRY_TAB.DbSkip(nPagina - 1 * nTamanho)

    # Adiciona os dados para a meta
    jJsonMeta = JsonObject().New()
    jJsonMeta['total'] = nTotal
    jJsonMeta['current_page'] = nPagina
    jJsonMeta['total_page'] = nPags
    jJsonMeta['total_items'] = nTamanho
    jResponse['meta'] = jJsonMeta
    # Percorre os registros
    while not QRY_TAB.EoF():
        nAtual += 1
        # Se ultrapassar o limite, encerra o laço
        if nAtual > nTamanho:
            break

        # Posiciona o registro e adiciona no retorno
        DbSelectArea(cAliasWS)
        cAliasWS.DbGoTo(QRY_TAB.TABREC)
        oRegistro = JsonObject().New()
        oRegistro['cod'] = cAliasWS.B1_COD
        oRegistro['desc'] = cAliasWS.B1_DESC
        oRegistro['tipo'] = cAliasWS.B1_TIPO
        oRegistro['um'] = cAliasWS.B1_UM
        oRegistro['locpad'] = cAliasWS.B1_LOCPAD
        oRegistro['grupo'] = cAliasWS.B1_GRUPO
        aAdd(jResponse['objects'], oRegistro)
        QRY_TAB.DbSkip()


QRY_TAB.DbCloseArea()
# Define o retorno
self.SetContentType('application/json')
self.SetResponse(jResponse.toJSON())
return lRet
# {Protheus.doc} WSMETHOD POST NEW
# Cria um novo registro na tabela
# @author Atilio
# @since 07/04/2022
# @version 1.0
# @obs Codigo gerado automaticamente pelo Autumn Code Maker
# 
#     Abaixo um exemplo do JSON que deverá vir no body
#     * 1: Para campos do tipo Numérico, informe o valor sem usar as aspas
#     * 2: Para campos do tipo Data, informe uma string no padrão 'YYYY-MM-DD'
# 
#     {
#         "cod": "conteudo",
#         "desc": "conteudo",
#         "tipo": "conteudo",
#         "um": "conteudo",
#         "locpad": "conteudo",
#         "grupo": "conteudo"
#     }
# 
# @see http://autumncodemaker.com
WSMETHOD
POST
NEW
WSRECEIVE
WSSERVICE
zWSProdutos
lRet = True
aDados = []
jJson = None
cJson = self.GetContent()
cError = ''
nLinha = 0
cDirLog = '\\x_logs\\'
cArqLog = ''
cErrorLog = ''
aLogAuto = []
nCampo = 0
jResponse = JsonObject().New()
cAliasWS = 'SB1'
lMsErroAuto = False
lMsHelpAuto = True
lAutoErrNoFile = True
# Se não existir a pasta de logs, cria
if not ExistDir(cDirLog):
    MakeDir(cDirLog)

# Definindo o conteúdo como JSON, e pegando o content e dando um parse para ver se a estrutura está ok
self.SetContentType('application/json')
jJson = JsonObject().New()
cError = jJson.FromJson(cJson)
# Se tiver algum erro no Parse, encerra a execução
if not Empty(cError):
    # SetRestFault(500, 'Falha ao obter JSON') //caso queira usar esse comando, você não poderá usar outros retornos, como os abaixo
    self.setStatus(500)
    jResponse['errorId'] = 'NEW004'
    jResponse['error'] = 'Parse do JSON'
    jResponse['solution'] = 'Erro ao fazer o Parse do JSON'
else:
    DbSelectArea(cAliasWS)
    # Adiciona os dados do ExecAuto
    aAdd(aDados, ['B1_COD', jJson.GetJsonObject('cod'), None])
    aAdd(aDados, ['B1_DESC', jJson.GetJsonObject('desc'), None])
    aAdd(aDados, ['B1_TIPO', jJson.GetJsonObject('tipo'), None])
    aAdd(aDados, ['B1_UM', jJson.GetJsonObject('um'), None])
    aAdd(aDados, ['B1_LOCPAD', jJson.GetJsonObject('locpad'), None])
    aAdd(aDados, ['B1_GRUPO', jJson.GetJsonObject('grupo'), None])
    # Percorre os dados do execauto
    # Chama a inclusão automática
    MsExecAuto(lambda x, y: MATA010(x, y), aDados, 3)
    # Se houve erro, gera um arquivo de log dentro do diretório da protheus data
    if lMsErroAuto:
        # Monta o texto do Error Log que será salvo
        cErrorLog = ''
        aLogAuto = GetAutoGrLog()
        # Grava o arquivo de log
        cArqLog = 'zWSProdutos_New_' + dToS(Date()) + '_' + StrTran(Time(), ':', '-') + '.log'
        MemoWrite(cDirLog + cArqLog, cErrorLog)
        # Define o retorno para o WebService
        # SetRestFault(500, cErrorLog) //caso queira usar esse comando, você não poderá usar outros retornos, como os abaixo
        self.setStatus(500)
        jResponse['errorId'] = 'NEW005'
        jResponse['error'] = 'Erro na inclusão do registro'
        jResponse['solution'] = 'Nao foi possivel incluir o registro, foi gerado um arquivo de log em ' + cDirLog + cArqLog + ' '
        lRet = False
        # Senão, define o retorno
    else:
        jResponse['note'] = 'Registro incluido com sucesso'


# Define o retorno
self.SetResponse(jResponse.toJSON())
return lRet