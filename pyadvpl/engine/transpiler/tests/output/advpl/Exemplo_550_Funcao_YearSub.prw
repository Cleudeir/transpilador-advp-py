// caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2024/07/21/adicionando-anos-em-uma-data-com-yearsum-maratona-advpl-e-tl-551/
// Bibliotecas
#Include "TOTVS.ch"
// {Protheus.doc} User Function zExe550
// Subtrai anos em uma data
// @type Function
// @author Atilio
// @since 07/04/2023
// Função YearSub
// Parâmetros
// Data a ser processada
// Número de anos a serem subtraídos
// Retorno
// Retorna a nova data com a subtração
// **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
USER FUNCTION zExe550()
    LOCAL aArea, dDataRef, nAnos, dNovaData

    aArea := FWGetArea()
    dDataRef := Date()
    nAnos := 2
    dNovaData := Nil
    // Faz a subtração
    dNovaData := YearSub(dDataRef, nAnos)
    // Exibe a diferença
    FWAlertInfo("Após a subtração de " + cValToChar(nAnos) + " anos, a nova data é " + dToC(dNovaData), "Teste YearSub")
    FWRestArea(aArea)
    RETURN
