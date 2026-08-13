// caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2023/08/25/operador-para-subtracoes-maratona-advpl-e-tl-017/
// Bibliotecas
#Include "TOTVS.ch"
// {Protheus.doc} User Function zExe017
// Exemplo de como utilizar os operadores de subtração - (ele também funciona com atribuição -=)
// @type Function
// @author Atilio
// @since 26/11/2022
// @see https://tdn.engpro.totvs.com.br/display/tec/Operadores+Comuns
// @obs
// **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
USER FUNCTION zExe017()
    LOCAL aArea, nVar1, nVar2, nResult

    aArea := FWGetArea()
    nVar1 := 12
    nVar2 := 15
    nResult := 0
    // Faz a subtração de uma variável com outra
    nResult := nVar1 - nVar2
    nResult -= 5
    FWAlertInfo("O resultado é " + cValToChar(nResult), "Resultado da Subtração")
    FWRestArea(aArea)
    RETURN
