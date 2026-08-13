# Esse exemplo faz parte da série do YouTube, Maratona de Exemplos, do canal Terminal de Informação, 
#     caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2023/08/19/operador-para-soma-ou-incremento-concatenacao-maratona-advpl-e-tl-011/
# Bibliotecas
# PREPROCESSOR: #Include "TOTVS.ch"
# {Protheus.doc} User Function zExe011
# Exemplo de como utilizar os operadores de soma e incremento + (eles também funcionam com atribuição +=)
# @type Function
# @author Atilio
# @since 26/11/2022
# @see https://tdn.engpro.totvs.com.br/display/tec/Operadores+Comuns
# @obs
#     **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
def u_zExe011():
    aArea = FWGetArea()
    nVar1 = 12
    nVar2 = 15
    nResult = 0
    cVar1 = 'Daniel'
    cVar2 = 'Atilio'
    cResult = ''
    # Faz a soma de uma variável com outra
    nResult = nVar1 + nVar2
    nResult += 5
    FWAlertInfo('O resultado é ' + cValToChar(nResult), 'Resultado da Soma')
    # Faz a multiplicação direto pela atribuição (5 * 5)
    cResult = cVar1 + ' ' + cVar2
    cResult += ' aaaa'
    FWAlertInfo('O resultado é ' + cResult, 'Resultado do Incremento')
    FWRestArea(aArea)
    return
