// caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2024/04/14/exibindo-uma-tela-de-logs-com-a-mostraerro-maratona-advpl-e-tl-355/
// Bibliotecas
#Include "TOTVS.ch"
// {Protheus.doc} User Function zExe354
// Adiciona meses em uma data
// @type Function
// @author Atilio
// @since 26/03/2023
// Função MonthSum
// Parâmetros
// Data a ser processada
// Número de meses a serem adicionados
// Retorno
// Retorna a nova data com a adição
// **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
USER FUNCTION zExe354()
    LOCAL aArea, dDataRef, nMeses, dNovaData

    aArea := FWGetArea()
    dDataRef := Date()
    nMeses := 2
    dNovaData := Nil
    // Faz a adição
    dNovaData := MonthSum(dDataRef, nMeses)
    // Exibe a diferença
    FWAlertInfo("Após a soma de " + cValToChar(nMeses) + " meses, a nova data é " + dToC(dNovaData), "Teste MonthSum")
    FWRestArea(aArea)
    RETURN
