// caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2024/03/14/buscando-as-threads-abertas-com-a-getuserinfoarray-maratona-advpl-e-tl-293/
// Bibliotecas
#Include "TOTVS.ch"
// {Protheus.doc} User Function zExe292
// Retorna a largura em pixels de um texto conforme uma fonte
// @type  Function
// @author Atilio
// @since 21/02/2023
// Função GetTextWidth
// Parâmetros
// + Fonte instanciada pela classe TFont
// + Texto a ser avaliado
// Retorno
// Retorna a largura em pixels
// **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
USER FUNCTION zExe292()
    LOCAL aArea, cFontNome, oFontPadrao, cTexto, nLargura

    aArea := FWGetArea()
    cFontNome := "Tahoma"
    oFontPadrao := TFont():New(cFontNome, Nil, - 12)
    cTexto := "Ola mundo 123"
    nLargura := 0
    // Busca a largura em pixels do texto
    nLargura := GetTextWidth(oFontPadrao, cTexto)
    FWAlertInfo("A largura é: " + cValToChar(nLargura), "Teste GetTextWidth")
    FWRestArea(aArea)
    RETURN
