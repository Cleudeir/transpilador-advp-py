# Esse exemplo faz parte da série do YouTube, Maratona de Exemplos, do canal Terminal de Informação, 
#     caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2023/09/26/testar-a-pilha-de-chamadas-com-as-funcoes-atisrotina-e-fwisincallstack-maratona-advpl-e-tl-049/
# Bibliotecas
# PREPROCESSOR: #Include "TOTVS.ch"
# {Protheus.doc} User Function zExe049
# Exemplo de função que verifica se esta sendo acionada por alguma função da pilha de chamadas
# @type Function
# @author Atilio
# @since 01/12/2022
# @see https://tdn.totvs.com/pages/releaseview.action?pageId=161349910
# @obs 
#     Função AtIsRotina
#     Parâmetros
#         + Indica o nome da função a ser procurada na pilha de chamadas
#     Retorno
#         + Retorna .T. se encontrou ou .F. se não encontrou
# 
#     Função FWIsInCallStack
#     Parâmetros
#         + Indica o nome da função a ser procurada na pilha de chamadas
#     Retorno
#         + Retorna .T. se encontrou ou .F. se não encontrou
# 
#     **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
def u_zExe049():
    aArea = FWGetArea()
    cFuncBusca = ''
    # Buscando pela AtIsRotina (só funciona se tudo tiver maiúsculo)
    cFuncBusca = 'U_ZMINIFORM'
    if AtIsRotina(cFuncBusca):
        FWAlertInfo('Foi acionado pela função - ' + cFuncBusca, 'Exemplo AtIsRotina')

    # Buscando pela FWIsInCallStack (independe se for maiúscula ou minúscula)
    cFuncBusca = 'u_zMiniForm'
    if FWIsInCallStack(cFuncBusca):
        FWAlertInfo('Foi acionado pela função - ' + cFuncBusca, 'Exemplo FWIsInCallStack')

    FWRestArea(aArea)
    return
