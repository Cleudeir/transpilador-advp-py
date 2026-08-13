# Esse exemplo faz parte da série do YouTube, Maratona de Exemplos, do canal Terminal de Informação, 
#     caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2024/05/08/retorna-o-nome-do-tipo-da-conexao-usada-com-o-banco-atraves-da-rddname-maratona-advpl-e-tl-403/
# Bibliotecas
# PREPROCESSOR: #Include "TOTVS.ch"
# {Protheus.doc} User Function zExe403
# Retorna o nome da conexão usada
# @type Function
# @author Atilio
# @since 28/03/2023
# @see https://tdn.totvs.com/display/tec/RDDName
# @obs 
#     Função RDDName
#     Parâmetros
#         Função não tem parâmetros
#     Retorno
#         + cRet        , Caracere     , Nome do RDD utilizado
# 
#     **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
def u_zExe403():
    aArea = FWGetArea()
    cConexao = ''
    # Busca a conexão RDD e mostra
    cConexao = RDDName()
    FWAlertInfo('O tipo de conexão é ' + cConexao, 'Teste RDDName')
    FWRestArea(aArea)
    return
