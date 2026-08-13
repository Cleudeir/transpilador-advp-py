# Esse exemplo faz parte da série do YouTube, Maratona de Exemplos, do canal Terminal de Informação, 
#     caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2023/08/25/operador-para-subtracoes-maratona-advpl-e-tl-017/
# Bibliotecas
# PREPROCESSOR: #Include "TOTVS.ch"
# {Protheus.doc} User Function zExe017
# Exemplo de como utilizar os operadores de subtração - (ele também funciona com atribuição -=)
# @type Function
# @author Atilio
# @since 26/11/2022
# @see https://tdn.engpro.totvs.com.br/display/tec/Operadores+Comuns
# @obs
#     **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
def u_zExe017():
    aArea = FWGetArea()
    nVar1 = 12
    nVar2 = 15
    nResult = 0
    # Faz a subtração de uma variável com outra
    nResult = nVar1 - nVar2
    nResult -= 5
    FWAlertInfo('O resultado é ' + cValToChar(nResult), 'Resultado da Subtração')
    FWRestArea(aArea)
    return
