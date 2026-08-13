# Esse exemplo faz parte da série do YouTube, Maratona de Exemplos, do canal Terminal de Informação, 
#     caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2023/09/24/buscando-a-primeira-ou-ultima-expressao-caractere-com-at-e-rat-maratona-advpl-e-tl-047/
# Bibliotecas
# PREPROCESSOR: #Include "TOTVS.ch"
# {Protheus.doc} User Function zExe047
# Exemplo de função que retorna a primeira ou a última posição de um texto conforme uma busca
# @type Function
# @author Atilio
# @since 30/11/2022
# @see https://tdn.totvs.com/display/tec/At e https://tdn.totvs.com/display/tec/RAt
# @obs 
#     Função At
#     Parâmetros
#         + cPesquisa , Caractere  , Indica a String que será buscada
#         + cDestino  , Caractere  , Indica a String onde será efetuada a busca
#         + nStart    , Numérico   , Indica a partir de qual posição deve iniciar a busca
#     Retorno
#         + nRet      , Numérico   , Retorna a posição encontrada
# 
#     Função RAt
#     Parâmetros
#         + cSearch   , Caractere  , Indica a String que será buscada
#         + cSource   , Caractere  , Indica a String onde será efetuada a busca
#     Retorno
#         + nRet      , Numérico   , Retorna a posição encontrada
# 
#     **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
def u_zExe047():
    aArea = FWGetArea()
    cNome = 'DANIEL DANIEL ATILIO ATILIO'
    cBusca1 = 'IEL'
    cBusca2 = 'ATILIO'
    nPosEnc = 0
    # Busca pelo texto "IEL" dentro da string, a primeira posição que encontrar será mostrada
    nPosEnc = At(cBusca1, cNome)
    if nPosEnc != 0:
        FWAlertInfo('Foi encontrado a busca a partir da posição: ' + cValToChar(nPosEnc), 'Exemplo At')

    # Busca pelo texto "ATILIO" dentro da string, a última posição que encontrar será mostrada
    nPosEnc = RAt(cBusca2, cNome)
    if nPosEnc != 0:
        FWAlertInfo('Foi encontrado a busca a partir da posição: ' + cValToChar(nPosEnc), 'Exemplo RAt')

    FWRestArea(aArea)
    return
