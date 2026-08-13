# Esse exemplo faz parte da série do YouTube, Maratona de Exemplos, do canal Terminal de Informação, 
#     caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2024/03/08/buscando-o-proximo-alias-disponivel-com-a-getnextalias-maratona-advpl-e-tl-280/
# Bibliotecas
# PREPROCESSOR: #Include "TOTVS.ch"
# {Protheus.doc} User Function zExe281
# Retorna as funções abertas em memória
# @type  Function
# @author Atilio
# @since 21/02/2023
# @see https://tdn.totvs.com/display/tec/GetPrograms
# @obs 
#     
#     Função GetPrograms
#     Parâmetros
#         Função não tem parâmetros
#     Retorno
#         + aRet      , Array      , Array com os programas em AdvPL abertos na memória
# 
#     **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
def u_zExe281():
    aArea = FWGetArea()
    aProgramas = []
    cMensagem = ''
    cPrograma = ''
    # Busca os programas carregados e joga em um array
    aProgramas = GetPrograms()
    # Percorre os programas incrementando a mensagem
    aEval(aProgramas, lambda cPrograma: (cMensagem := cMensagem + cPrograma + CRLF))
    # Exibe uma mensagem com os programas
    ShowLog(cMensagem)
    FWRestArea(aArea)
    return
