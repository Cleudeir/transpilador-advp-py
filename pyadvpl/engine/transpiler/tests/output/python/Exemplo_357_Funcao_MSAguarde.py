# Esse exemplo faz parte da série do YouTube, Maratona de Exemplos, do canal Terminal de Informação, 
#     caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2024/04/15/validando-se-o-dicionario-esta-no-banco-com-mpdicindb-maratona-advpl-e-tl-356/
# Bibliotecas
# PREPROCESSOR: #Include "TOTVS.ch"
# PREPROCESSOR: #Include "TopConn.ch"
# {Protheus.doc} User Function zExe357
# Exibe uma tela de carregamento de rotinas
# @type Function
# @author Atilio
# @since 26/03/2023
# @obs 
#     Função MSAguarde
#     Parâmetros
#         Bloco de código com a execução que será processada
#         Título da janela
#         Mensagem exibida no processamento
#         Define se poderá ser abortado a rotina (.T.) ou não (.F.)
#     Retorno
#         Função não tem retorno
# 
#     **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
def u_zExe357():
    aArea = FWGetArea()
    # Aciona a rotina para processar os registros
    MsAguarde(lambda : fExemplo(), 'Aguarde...', 'Processando Registros...')
    FWRestArea(aArea)
    return Static

def fExemplo():
    aArea = GetArea()
    nAtual = 0
    nTotal = 0
    cQryAux = ''
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
    # Percorre todos os registros da query
    QRY_AUX.DbGoTop()
    while not QRY_AUX.EoF():
        # Incrementa a mensagem na regua
        nAtual += 1
        MsProcTxt('Analisando registro ' + cValToChar(nAtual) + ' de ' + cValToChar(nTotal) + '...')
        Sleep(100)
        QRY_AUX.DbSkip()

    QRY_AUX.DbCloseArea()
    RestArea(aArea)
    return
