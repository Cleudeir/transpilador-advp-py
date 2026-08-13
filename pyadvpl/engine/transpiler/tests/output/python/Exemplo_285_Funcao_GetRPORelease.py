# Esse exemplo faz parte da série do YouTube, Maratona de Exemplos, do canal Terminal de Informação, 
#     caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2024/03/10/buscando-informacoes-de-onde-esta-rodando-o-smartclient-com-getrmtinfo-maratona-advpl-e-tl-284/
# Bibliotecas
# PREPROCESSOR: #Include "TOTVS.ch"
# {Protheus.doc} User Function zExe285
# Retorna a versão do Repositório de Objetos
# @type  Function
# @author Atilio
# @since 21/02/2023
# @obs 
# 
#     Função GetRPORelease
#     Parâmetros
#         Não possui parâmetros
#     Retorno
#         Retorna a versão
#     
#     **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
def u_zExe285():
    aArea = FWGetArea()
    cMensagem = ''
    # Busca a informação e exibe
    cMensagem = 'A versão do RPO é: ' + GetRPORelease()
    FWAlertInfo(cMensagem, 'Teste GetRPORelease')
    FWRestArea(aArea)
    return
