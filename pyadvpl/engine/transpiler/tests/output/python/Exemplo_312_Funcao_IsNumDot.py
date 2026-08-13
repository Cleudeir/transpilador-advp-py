# Esse exemplo faz parte da série do YouTube, Maratona de Exemplos, do canal Terminal de Informação, 
#     caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2024/03/24/validando-se-na-string-possui-apenas-numero-e-ponto-com-isnumdot-maratona-advpl-e-tl-312/
# Bibliotecas
# PREPROCESSOR: #Include "Totvs.ch"
# {Protheus.doc} zExe312
# Valida se uma string possui apenas número e ponto
# @type  Function
# @author Atilio
# @since 23/02/2023
# @obs 
# 
#     Função IsNumDot
#     Parâmetros
#         Recebe o número a ser validado (no formato Caractere)
#     Retorno
#         Retorna .T. se a string tiver apenas número ou "." se não retorna .F.
# 
#     **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
def u_zExe312():
    aArea = FWGetArea()
    cTexto = ''
    # Teste de somente letras
    cTexto = '3.14'
    if IsNumDot(cTexto):
        FWAlertSuccess('O texto possui apenas números ou pontos', 'Teste 1 IsNumDot')

    # Teste de letras com números
    cTexto = '3.a14'
    if IsNumDot(cTexto):
        FWAlertSuccess('O texto possui apenas números ou pontos', 'Teste 2 IsNumDot')

    # Teste começando com números
    cTexto = '314'
    if IsNumDot(cTexto):
        FWAlertSuccess('O texto possui apenas números ou pontos', 'Teste 3 IsNumDot')

    FWRestArea(aArea)
    return
