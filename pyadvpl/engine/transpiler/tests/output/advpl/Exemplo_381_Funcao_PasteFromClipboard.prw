// caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2024/04/27/simulando-um-ctrlv-com-a-pastefromclipboard-maratona-advpl-e-tl-381/
// Bibliotecas
#Include "TOTVS.ch"
// {Protheus.doc} User Function zExe381
// Busca um conteúdo que esta na clipboard do S.O.
// @type Function
// @author Atilio
// @since 28/03/2023
// @see https://tdn.totvs.com/display/tec/PasteFromClipboard
// Função PasteFromClipboard
// Parâmetros
// Função não tem parâmetros
// Retorno
// Retorna o conteúdo que foi dado Ctrl+C em memória
// **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
USER FUNCTION zExe381()
    LOCAL aArea, cTexto

    aArea := FWGetArea()
    cTexto := ""
    // Busca o valor e mostra
    cTexto := PasteFromClipboard()
    FWAlertInfo("O conteúdo em memória é '" + cTexto + "'", "Teste PasteFromClipboard")
    FWRestArea(aArea)
    RETURN
