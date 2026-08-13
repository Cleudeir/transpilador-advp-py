# Esse exemplo faz parte da série do YouTube, Maratona de Exemplos, do canal Terminal de Informação, 
#     caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2024/07/14/buscando-o-modo-de-compartilhamento-de-uma-tabela-com-x2modacess-maratona-advpl-e-tl-537/
# Bibliotecas
# PREPROCESSOR: #Include "TOTVS.ch"
# PREPROCESSOR: #Include "APWebSrv.ch"
# {Protheus.doc} WsService zWSClientes
# Exemplo de WebService usando SOAP
# @author Atilio
# @since 07/04/2022
# @version 1.0
# @see https://tdn.totvs.com/display/tec/WSSERVICE
# @obs 
# 
#     **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
WsService
zWSClientes
Description
'WebService com funcoes de clientes'
# Atributos
WsData
cViewRece
# as
String
WsData
cViewSend
# as
String
WsData
cNewRece
# as
String
WsData
cNewSend
# as
String
# Métodos
WsMethod
ViewCli
Description
'Metodo para visualizar clientes'
WsMethod
NewCli
Description
'Metodo para incluir clientes'
EndWsService
# {Protheus.doc} WsMethod ViewCli
# Visualiza as informações de um cliente
# @author Atilio
# @since 03/06/2022
# @param cViewRece, Caractere, Estrutura xml com o código do cliente ou cnpj / cpf
# @obs Será retornado um XML com os dados do cadastro
WsMethod
ViewCli
WsReceive
cViewRece
WsSend
cViewSend
WsService
zWSClientes
aArea = FWGetArea()
lRet = True
cBusca = Alltrim(self.cViewRece())
nIndice = 0
cCGC = ''
cMascCPF = '@R 999.999.999-99'
cMascCNPJ = '@R 99.999.999/9999-99'
# Retira pontos, hífens e barras da busca (para o caso se o usuário digitou o cpf ou cnpj com esses caracteres)
cBusca = StrTran(cBusca, '.', '')
cBusca = StrTran(cBusca, '/', '')
cBusca = StrTran(cBusca, '-', '')
# Se o tamanho da busca for de 14 caracteres, é um CNPJ. Ou se for 11 caracteres, é um CPF
if Len(cBusca) == 14 or Len(cBusca) == 11:
    nIndice = 3
    # A1_FILIAL + A1_CGC
    # Senão, irá usar o índice padrão, por código e loja do cliente
else:
    nIndice = 1
    # A1_FILIAL + A1_COD + A1_LOJA

# Tenta posicionar no cliente
DbSelectArea('SA1')
SA1.DbSetOrder(nIndice)
if SA1.MsSeek(FWxFilial('SA1') + cBusca):
    cCGC = Alltrim(SA1.A1_CGC)
    self.cViewSend = '{' + CRLF
    self.cViewSend += ' "dados":{' + CRLF
    self.cViewSend += '  "status":"Cliente encontrado",' + CRLF
    self.cViewSend += '  "codigo":"' + SA1.A1_COD + SA1.A1_LOJA + '",' + CRLF
    if Len(cCGC) == 14:
        self.cViewSend += '  "cnpj":"' + Alltrim(Transform(cCGC, cMascCNPJ)) + '",' + CRLF
    elif Len(cCGC) == 11:
        self.cViewSend += '  "cpf":"' + Alltrim(Transform(cCGC, cMascCPF)) + '",' + CRLF

    self.cViewSend += '  "nome":"' + Alltrim(SA1.A1_NOME) + '",' + CRLF
    self.cViewSend += '  "email":"' + Alltrim(SA1.A1_EMAIL) + '",' + CRLF
    self.cViewSend += '  "site":"' + Alltrim(SA1.A1_HPAGE) + '"' + CRLF
    self.cViewSend += ' }' + CRLF
    self.cViewSend += '}' + CRLF
else:
    self.cViewSend = '{' + CRLF
    self.cViewSend += ' "dados":{' + CRLF
    self.cViewSend += '  "status":"Cliente nao encontrado com a chave fornecida"' + CRLF
    self.cViewSend += ' }' + CRLF
    self.cViewSend += '}' + CRLF

FWRestArea(aArea)
return lRet
# {Protheus.doc} WsMethod NewCli
# Cadastra um novo cliente
# @author Atilio
# @since 03/06/2022
# @param cNewRece, Caractere, XML com os campos obrigatórios do cadastro de clientes
# @obs Será retornado um XML com a informação de sucesso ou falha na inclusão
WsMethod
NewCli
WsReceive
cNewRece
WsSend
cNewSend
WsService
zWSClientes
aArea = FWGetArea()
lRet = True
jJsonRece = None
cError = ''
jResponse = JsonObject().New()
cDirLog = '\\x_logs\\'
nLinha = None
aDados = []
lMsHelpAuto = True
lAutoErrNoFile = True
lMsErroAuto = False
# Recebe o texto e transforma em objeto
jJsonRece = JsonObject().New()
cError = jJsonRece.FromJson(self.cNewRece())
# Se tiver algum erro no Parse, encerra a execução
if not Empty(cError) or Len(self.cNewRece()) < 20:
    jResponse['errorId'] = 'NEW001'
    jResponse['error'] = 'Parse do JSON'
    jResponse['solution'] = 'Erro ao fazer o Parse do JSON'
else:
    # Se algum dos campos estiver vazio
    if Empty(jJsonRece.GetJsonObject('cod')) or Empty(jJsonRece.GetJsonObject('loja')) or Empty(jJsonRece.GetJsonObject('nome')) or Empty(jJsonRece.GetJsonObject('nreduz')) or Empty(jJsonRece.GetJsonObject('tipo')) or Empty(jJsonRece.GetJsonObject('end')) or Empty(jJsonRece.GetJsonObject('mun')) or Empty(jJsonRece.GetJsonObject('est')):
        jResponse['errorId'] = 'NEW002'
        jResponse['error'] = 'Campo(s) obrigatorio(s)'
        jResponse['solution'] = 'Existem campos que nao foram enviados, revise a estrutura do seu JSON'
    else:
        # Adiciona no array
        aAdd(aDados, ['A1_COD', jJsonRece.GetJsonObject('cod'), None])
        aAdd(aDados, ['A1_LOJA', jJsonRece.GetJsonObject('loja'), None])
        aAdd(aDados, ['A1_NOME', jJsonRece.GetJsonObject('nome'), None])
        aAdd(aDados, ['A1_NREDUZ', jJsonRece.GetJsonObject('nreduz'), None])
        aAdd(aDados, ['A1_TIPO', jJsonRece.GetJsonObject('tipo'), None])
        aAdd(aDados, ['A1_END', jJsonRece.GetJsonObject('end'), None])
        aAdd(aDados, ['A1_MUN', jJsonRece.GetJsonObject('mun'), None])
        aAdd(aDados, ['A1_EST', jJsonRece.GetJsonObject('est'), None])
        # Chama a inclusão automática
        MsExecAuto(lambda x, y: CRMA980(x, y), aDados, 3)
        # Se houve erro, gera um arquivo de log dentro do diretório da protheus data
        if lMsErroAuto:
            # Monta o texto do Error Log que será salvo
            cErrorLog = ''
            aLogAuto = GetAutoGrLog()
            # Grava o arquivo de log
            cArqLog = 'zWSClientes_New_' + dToS(Date()) + '_' + StrTran(Time(), ':', '-') + '.log'
            MemoWrite(cDirLog + cArqLog, cErrorLog)
            # Define o retorno para o WebService
            jResponse['errorId'] = 'NEW003'
            jResponse['error'] = 'Erro na inclusao do registro'
            jResponse['solution'] = 'Nao foi possivel incluir o registro, foi gerado um arquivo de log em ' + cDirLog + cArqLog + ' '
            # Senão, define a mensagem de retorno
        else:
            jResponse['note'] = 'Registro incluido com sucesso'



# Agora pega o json da Resposta e joga para o retorno do WS
self.cNewSend = jResponse.toJSON()
FWRestArea(aArea)
return lRet