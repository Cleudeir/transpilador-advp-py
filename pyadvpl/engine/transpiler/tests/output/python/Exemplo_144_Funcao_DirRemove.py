# Esse exemplo faz parte da série do YouTube, Maratona de Exemplos, do canal Terminal de Informação, 
#     caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2023/12/30/apagando-uma-pasta-com-a-dirremove-maratona-advpl-e-tl-144/
# Bibliotecas
# PREPROCESSOR: #Include "TOTVS.ch"
# {Protheus.doc} User Function zExe144
# Função que apaga uma pasta
# @type Function
# @author Atilio
# @since 16/12/2022
# @obs 
#     Função DirRemove
#     Parâmetros
#         + Indica o nome da pasta a ser apagada
#         + Compatibilidade
#         + Se .T. será convertido tudo para minúsculo o nome da pasta ou .F. mantém original
#     Retorno
#         + .T. se foi possível apagar a pasta ou .F. se não foi
# 
#     **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
def u_zExe144():
    aArea = FWGetArea()
    cPasta = ''
    # Exclui uma pasta local
    cPasta = 'C:\\spool\\tst1\\'
    if DirRemove(cPasta):
        FWAlertSuccess("A pasta '" + cPasta + "' foi excluida com sucesso", 'Teste 1 DirRemove')
    else:
        FWAlertError("Falha ao excluir a pasta '" + cPasta + "' ", 'Teste 1 DirRemove')

    # Exclui uma pasta dentro da Protheus Data
    cPasta = '\\system\\tst2\\'
    if DirRemove(cPasta):
        FWAlertSuccess("A pasta '" + cPasta + "' foi excluida com sucesso", 'Teste 2 DirRemove')
    else:
        FWAlertError("Falha ao excluir a pasta '" + cPasta + "' ", 'Teste 2 DirRemove')

    FWRestArea(aArea)
    return
