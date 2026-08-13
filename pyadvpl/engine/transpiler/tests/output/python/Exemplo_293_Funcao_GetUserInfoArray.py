# Esse exemplo faz parte da série do YouTube, Maratona de Exemplos, do canal Terminal de Informação, 
#     caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2024/03/14/pegando-a-largura-de-um-texto-com-a-gettextwidth-maratona-advpl-e-tl-292/
# Bibliotecas
# PREPROCESSOR: #Include "TOTVS.ch"
# {Protheus.doc} User Function zExe293
# Busca as informações das threads abertas no slave onde esta rodando a aplicação
# @type  Function
# @author Atilio
# @since 21/02/2023
# @see https://tdn.totvs.com/display/tec/GetUserInfoArray
# @obs 
# 
#     Função GetUserInfoArray
#     Parâmetros
#         + lShowMoreInfo     , Lógico        , Se .T. retorna mais informações (apenas para 4GL)
#     Retorno
#         + aRet              , Array         , Array com as informações
# 
#     **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
def u_zExe293():
    aArea = FWGetArea()
    aThreads = []
    nConexAtu = 1
    cMensagem = ''
    # Pega todos os usuários conectados
    aThreads = GetUserInfoArray()
    # Percorre todas as conexões
    # Mostra a mensagem
    ShowLog(cMensagem)
    FWRestArea(aArea)
    return
