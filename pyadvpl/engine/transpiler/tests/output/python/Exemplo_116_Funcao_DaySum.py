# Esse exemplo faz parte da série do YouTube, Maratona de Exemplos, do canal Terminal de Informação, 
#     caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2023/12/02/somando-dias-em-uma-data-com-a-daysum-maratona-advpl-e-tl-116/
# Bibliotecas
# PREPROCESSOR: #Include "TOTVS.ch"
# {Protheus.doc} User Function zExe116
# Adiciona dias em uma data
# @type Function
# @author Atilio
# @since 13/12/2022
# @obs 
#     Função DaySum
#     Parâmetros
#         + Data que será processada
#         + Número de dias a serem somados
#     Retorno
#         + Retorna a nova data com a soma
# 
#     **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
def u_zExe116():
    aArea = FWGetArea()
    dDataRef = Date()
    nDias = 10
    dNovaData = None
    # Faz a adição dos dias
    dNovaData = DaySum(dDataRef, nDias)
    # Exibe a diferença
    FWAlertInfo('Após a adição de ' + cValToChar(nDias) + ' dia(s), a nova data é ' + dToC(dNovaData), 'Teste DaySum')
    FWRestArea(aArea)
    return
