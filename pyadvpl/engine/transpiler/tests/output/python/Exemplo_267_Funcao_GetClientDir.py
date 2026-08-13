# Esse exemplo faz parte da série do YouTube, Maratona de Exemplos, do canal Terminal de Informação, 
#     caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2024/03/01/buscando-a-pasta-do-smartclient-com-a-getclientdir-maratona-advpl-e-tl-267/
# Bibliotecas
# PREPROCESSOR: #Include "TOTVS.ch"
# {Protheus.doc} User Function zExe267
# Retorna a pasta onde o Protheus esta executando (smartclient.exe)
# @type  Function
# @author Atilio
# @since 21/02/2023
# @see https://tdn.totvs.com/display/tec/GetClientDir
# @obs 
# 
#     Função GetClientDir
#     Parâmetros
#         Não tem Parâmetros
#     Retorno
#         + cRet           , Caractere        , Retorna a pasta do SmartClient
#     
#     **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
def u_zExe267():
    aArea = FWGetArea()
    cMensagem = ''
    # Busca a pasta e exibe
    cMensagem = 'Estou executando em - ' + GetClientDir()
    FWAlertInfo(cMensagem, 'Teste GetClientDir')
    FWRestArea(aArea)
    return
