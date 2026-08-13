// caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2023/08/13/operador-para-continuar-na-proxima-linha-ou-proximo-comando-maratona-advpl-e-tl-005/
// Bibliotecas
#Include "TOTVS.ch"
// {Protheus.doc} User Function zExe005
// Exemplo de como utilizar o operador ; (Ponto e Vírgula), para continuar a execução na próxima linha
// @type Function
// @author Atilio
// @since 26/11/2022
// @obs
// **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
USER FUNCTION zExe005()
    LOCAL aArea, cTexto, aDados

    aArea := FWGetArea()
    cTexto := ""
    aDados := {  }
    // Demonstra a continuação da linha na próxima através do ponto e vírgula
    cTexto := "O rato " + "roeu a roupa " + "do rei de Roma"
    FWAlertInfo(cTexto, "Conteúdo da variável cTexto")
    // Cria um array com vários elementos
    aDados := { "terminaldeinformacao.com", "autumncodemaker.com", "atiliosistemas.com" }
    FWAlertInfo("Tamanho do array: " + cValToChar(Len(aDados)), "Variável aDados")
    FWRestArea(aArea)
    RETURN
