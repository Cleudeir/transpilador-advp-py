// caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2024/04/13/subtraindo-meses-de-uma-data-com-a-monthsub-maratona-advpl-e-tl-353/
// Bibliotecas
#Include "TOTVS.ch"
// {Protheus.doc} User Function zExe353
// Subtrai meses em uma data
// @type Function
// @author Atilio
// @since 26/03/2023
// Função MonthSub
// Parâmetros
// Data a ser processada
// Número de meses a serem subtraídos
// Retorno
// Retorna a nova data com a subtração
// **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
USER FUNCTION zExe353()
    LOCAL aArea, dDataRef, nMeses, dNovaData

    aArea := FWGetArea()
    dDataRef := Date()
    nMeses := 2
    dNovaData := Nil
    // Faz a subtração
    dNovaData := MonthSub(dDataRef, nMeses)
    // Exibe a diferença
    FWAlertInfo("Após a subtração de " + cValToChar(nMeses) + " meses, a nova data é " + dToC(dNovaData), "Teste MonthSub")
    FWRestArea(aArea)
    RETURN
