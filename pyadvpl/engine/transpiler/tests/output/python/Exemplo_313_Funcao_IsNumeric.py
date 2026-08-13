# Esse exemplo faz parte da série do YouTube, Maratona de Exemplos, do canal Terminal de Informação, 
#     caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2024/03/24/validando-se-uma-string-possui-apenas-numeros-com-isnumeric-maratona-advpl-e-tl-313/
# Bibliotecas
# PREPROCESSOR: #Include "Totvs.ch"
# {Protheus.doc} zExe313
# Valida se uma string possui apenas números
# @type  Function
# @author Atilio
# @since 23/02/2023
# @obs 
# 
#     Função IsNumeric
#     Parâmetros
#         Recebe o número a ser validado (no formato Caractere)
#     Retorno
#         Retorna .T. se a string tiver apenas números se não retorna .F.
# 
#     **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
def u_zExe313():
    aArea = FWGetArea()
    cTexto = ''
    # Teste de somente letras
    cTexto = '3.14'
    if IsNumeric(cTexto):
        FWAlertSuccess('O texto possui apenas números', 'Teste 1 IsNumeric')

    # Teste de letras com números
    cTexto = '3.a14'
    if IsNumeric(cTexto):
        FWAlertSuccess('O texto possui apenas números', 'Teste 2 IsNumeric')

    # Teste começando com números
    cTexto = '314'
    if IsNumeric(cTexto):
        FWAlertSuccess('O texto possui apenas números', 'Teste 3 IsNumeric')

    FWRestArea(aArea)
    return
