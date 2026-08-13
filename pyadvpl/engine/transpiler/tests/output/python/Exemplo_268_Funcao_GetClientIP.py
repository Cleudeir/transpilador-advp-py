# Esse exemplo faz parte da série do YouTube, Maratona de Exemplos, do canal Terminal de Informação, 
#     caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2024/03/02/buscando-o-ip-com-a-funcao-getclientip-maratona-advpl-e-tl-268/
# Bibliotecas
# PREPROCESSOR: #Include "TOTVS.ch"
# {Protheus.doc} User Function zExe268
# Retorna o IP do servidor ou da estação
# @type  Function
# @author Atilio
# @since 21/02/2023
# @see https://tdn.totvs.com/display/tec/GetClientIP
# @obs 
# 
#     Função GetClientIP
#     Parâmetros
#         + lClientSide    , Lógico           , Se .T. retorna o IP do SmartClient ; Se .F. retorna o IP do AppServer
#     Retorno
#         + cRet           , Caractere        , Retorna o IP conforme o lClientSide passado
#     
#     **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
def u_zExe268():
    aArea = FWGetArea()
    cMensagem = ''
    # Busca a informação e exibe
    cMensagem = 'Estou executando no seguinte IP: ' + GetClientIP(False)
    FWAlertInfo(cMensagem, 'Teste GetClientIP')
    FWRestArea(aArea)
    return
