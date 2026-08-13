# Esse exemplo faz parte da série do YouTube, Maratona de Exemplos, do canal Terminal de Informação, 
#     caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2024/06/24/montando-e-disparando-emails-com-tmailmessage-e-tmailmanager-maratona-advpl-e-tl-497/
# Bibliotecas
# PREPROCESSOR: #Include "TOTVS.ch"
# {Protheus.doc} User Function zExe497
# Realiza um disparo de e-Mail manualmente
# @type Function
# @author Atilio
# @since 04/04/2023
# @see https://tdn.totvs.com/display/tec/Classe+TMailMessage e https://tdn.totvs.com/display/tec/Classe+TMailManager
# @obs 
# 
#     **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
def u_zExe497():
    aArea = FWGetArea()
    cPara = 'daniel@atiliosistemas.com; contato@atiliosistemas.com'
    cAssunto = ''
    cCorpo = ''
    aAnexos = []
    lExibeHelp = True
    # Monta o corpo do e-Mail
    cCorpo = '<p>Olá.</p>'
    cCorpo += '<p></p>'
    cCorpo += '<p>Esse é um <strong>e-Mail de teste</strong> gerado pelo <font color="red">ERP Protheus</font>.</p>'
    cCorpo += '<p></p>'
    cCorpo += '<p>Data <em>' + dToC(Date()) + '</em> às <em>' + Time() + '</em>.</p>'
    # Faz o disparo via função cusotmizada
    cAssunto = 'Envio de Teste (TMailMessage e TMailManager)'
    lEnvio = fEnvia(cPara, cAssunto, cCorpo, aAnexos, lExibeHelp, True)
    if lEnvio:
        FWAlertSuccess('Sucesso no disparo do e-Mail', 'Teste TMailMessage e TMailManager')
    else:
        FWAlertError('Falha no disparo do e-Mail', 'Teste TMailMessage e TMailManager')

    FWRestArea(aArea)
    return Static

def fEnvia(cPara, cAssunto, cCorpo, aAnexos, lMostraLog, lUsaTLS):
    aArea = FWGetArea()
    nAtual = 0
    lRet = True
    oMsg = None
    oSrv = None
    nRet = 0
    cFrom = Alltrim(GetMV('MV_RELACNT'))
    cUser = SubStr(cFrom, 1, At('@', cFrom) - 1)
    cPass = Alltrim(GetMV('MV_RELPSW'))
    cSrvFull = Alltrim(GetMV('MV_RELSERV'))
    cServer = (SubStr(cSrvFull, 1, At(':', cSrvFull) - 1) if ':' in cSrvFull else cSrvFull)
    nPort = (Val(SubStr(cSrvFull, At(':', cSrvFull) + 1, Len(cSrvFull))) if ':' in cSrvFull else 587)
    nTimeOut = GetMV('MV_RELTIME')
    cLog = ''
    Default
    cPara = ''
    Default
    cAssunto = ''
    Default
    cCorpo = ''
    Default
    aAnexos = []
    Default
    lMostraLog = False
    Default
    lUsaTLS = False
    # Se tiver em branco o destinatário, o assunto ou o corpo do email
    if Empty(cPara) or Empty(cAssunto) or Empty(cCorpo):
        cLog += '001 - Destinatario, Assunto ou Corpo do e-Mail vazio(s)!' + CRLF
        lRet = False

    if lRet:
        # Cria a nova mensagem
        oMsg = TMailMessage().New()
        oMsg.Clear()
        # Define os atributos da mensagem
        oMsg.cFrom = cFrom
        oMsg.cTo = cPara
        oMsg.cSubject = cAssunto
        oMsg.cBody = cCorpo
        # Percorre os anexos
        # Cria servidor para disparo do e-Mail
        oSrv = tMailManager().New()
        # Define se irá utilizar o TLS
        if lUsaTLS:
            oSrv.SetUseTLS(True)

        # Inicializa conexão
        nRet = oSrv.Init('', cServer, cUser, cPass, 0, nPort)
        if nRet != 0:
            cLog += '004 - Nao foi possivel inicializar o servidor SMTP: ' + oSrv.GetErrorString(nRet) + CRLF
            lRet = False

        if lRet:
            # Define o time out
            nRet = oSrv.SetSMTPTimeout(nTimeOut)
            if nRet != 0:
                cLog += "005 - Nao foi possivel definir o TimeOut '" + cValToChar(nTimeOut) + "'" + CRLF

            # Conecta no servidor
            nRet = oSrv.SMTPConnect()
            if nRet != 0:
                cLog += '006 - Nao foi possivel conectar no servidor SMTP: ' + oSrv.GetErrorString(nRet) + CRLF
                lRet = False

            if lRet:
                # Realiza a autenticação do usuário e senha
                nRet = oSrv.SmtpAuth(cFrom, cPass)
                if nRet != 0:
                    cLog += '007 - Nao foi possivel autenticar no servidor SMTP: ' + oSrv.GetErrorString(nRet) + CRLF
                    lRet = False

                if lRet:
                    # Envia a mensagem
                    nRet = oMsg.Send(oSrv)
                    if nRet != 0:
                        cLog += '008 - Nao foi possivel enviar a mensagem: ' + oSrv.GetErrorString(nRet) + CRLF
                        lRet = False


                # Disconecta do servidor
                nRet = oSrv.SMTPDisconnect()
                if nRet != 0:
                    cLog += '009 - Nao foi possivel disconectar do servidor SMTP: ' + oSrv.GetErrorString(nRet) + CRLF




    # Se tiver log de avisos/erros
    if not Empty(cLog):
        cLog = 'zEnvMail - ' + dToC(Date()) + ' ' + Time() + CRLF + 'Funcao - ' + FunName() + CRLF + CRLF + 'Existem mensagens de aviso: ' + CRLF + cLog
        # Se for para mostrar o log visualmente e for processo com interface com o usuário, mostra uma mensagem na tela
        if lMostraLog and not IsBlind():
            Aviso('Log', cLog, ['Ok'], 2)


    FWRestArea(aArea)
    return lRet
