# Esse exemplo faz parte da série do YouTube, Maratona de Exemplos, do canal Terminal de Informação, 
#     caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2024/04/02/carregando-uma-imagem-com-a-loadbitmap-maratona-advpl-e-tl-331/
# Bibliotecas
# PREPROCESSOR: #Include "Totvs.ch"
# {Protheus.doc} User Function zExe330
# Valida se o programa esta rodando no SIGAMDI (.T.) ou não (.F.)
# @type Function
# @author Atilio
# @since 12/03/2023
# @obs 
# 
#     Função LjIsMDI
#     Parâmetros
#         Não tem parâmetros
#     Retorno
#         Retorna .T. se estiver rodando via SIGAMDI ou .F. se não
# 
#     **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
def u_zExe330():
    aArea = FWGetArea()
    # Valida se esta rodando em SIGAMDI
    if LjIsMDI():
        FWAlertSuccess('O programa esta rodando via SIGAMDI', 'Teste LjIsMDI')
    else:
        FWAlertError('Não é SIGAMDI', 'Teste LjIsMDI')

    FWRestArea(aArea)
    return
