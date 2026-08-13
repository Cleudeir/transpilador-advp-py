# Esse exemplo faz parte da série do YouTube, Maratona de Exemplos, do canal Terminal de Informação, 
#     caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2024/04/19/criando-uma-regua-dupla-com-a-msnewprocess-maratona-advpl-e-tl-364/
# Bibliotecas
# PREPROCESSOR: #Include "TOTVS.ch"
# PREPROCESSOR: #Include "TopConn.ch"
# {Protheus.doc} User Function zExe364
# Abre uma tela de processamento com régua dupla
# @type Function
# @author Atilio
# @since 27/03/2023
# @see https://tdn.totvs.com/display/public/framework/MsNewProcess
# @obs 
# 
#     **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
def u_zExe364():
    aArea = FWGetArea()
    oProcess = None
    # Aciona a rotina para processar os registros
    oProcess = MsNewProcess().New(lambda : fExemplo(oProcess), 'Processando...', 'Aguarde...', True)
    oProcess.Activate()
    FWRestArea(aArea)
    return Static

def fExemplo(oProcess):
    aArea = FWGetArea()
    nAtual = 0
    nTotal = 0
    cQryAux = ''
    nAtu2 = 0
    nTot2 = 90
    # Executa a consulta
    cQryAux = ' SELECT ' + CRLF
    cQryAux += '     BM_GRUPO, ' + CRLF
    cQryAux += '     BM_DESC ' + CRLF
    cQryAux += ' FROM ' + CRLF
    cQryAux += '     ' + RetSQLName('SBM') + ' SBM ' + CRLF
    cQryAux += ' WHERE ' + CRLF
    cQryAux += "     BM_FILIAL = '" + FWxFilial('SBM') + "' " + CRLF
    cQryAux += "     AND SBM.D_E_L_E_T_ = ' ' " + CRLF
    TCQuery
    cQryAux
    New
    Alias
    'QRY_AUX'
    # Conta quantos registros existem, e seta no tamanho da regua
    Count
    To
    nTotal
    oProcess.SetRegua1(nTotal)
    # Percorre todos os registros da query
    QRY_AUX.DbGoTop()
    while not QRY_AUX.EoF():
        # Incrementa a mensagem na regua
        nAtual += 1
        oProcess.IncRegua1('Analisando registro ' + cValToChar(nAtual) + ' de ' + cValToChar(nTotal) + '...')
        # Incrementando a regua 2
        oProcess.SetRegua2(nTot2)
        QRY_AUX.DbSkip()

    QRY_AUX.DbCloseArea()
    FWRestArea(aArea)
    return
