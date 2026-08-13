// caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2024/07/21/subtraindo-anos-de-uma-data-com-yearsub-maratona-advpl-e-tl-550/
// Bibliotecas
#Include "TOTVS.ch"
// {Protheus.doc} User Function zExe551
// Adiciona anos em uma data
// @type Function
// @author Atilio
// @since 07/04/2023
// Função YearSum
// Parâmetros
// Data a ser processada
// Número de anos a serem adicionados
// Retorno
// Retorna a nova data com a adição
// **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
USER FUNCTION zExe551()
    LOCAL aArea, dDataRef, nAnos, dNovaData

    aArea := FWGetArea()
    dDataRef := Date()
    nAnos := 2
    dNovaData := Nil
    // Faz a adição
    dNovaData := YearSum(dDataRef, nAnos)
    // Exibe a diferença
    FWAlertInfo("Após a soma de " + cValToChar(nAnos) + " anos, a nova data é " + dToC(dNovaData), "Teste YearSum")
    FWRestArea(aArea)
    RETURN
