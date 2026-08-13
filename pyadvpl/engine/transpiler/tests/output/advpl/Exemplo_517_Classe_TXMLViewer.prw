// caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2024/07/04/expandindo-e-visualizando-um-xml-atraves-da-txmlviewer-maratona-advpl-e-tl-517/
// Bibliotecas
#Include "TOTVS.ch"
// {Protheus.doc} User Function zExe517
// Realiza a abertura de um XML para ser navegável em uma Dialog
// @type  Function
// @author Atilio
// @since 05/04/2023
// @see https://tdn.totvs.com/display/tec/TXMLViewer
// **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
USER FUNCTION zExe517()
    LOCAL aArea, nCorFundo, nJanAltura, nJanLargur, cJanTitulo, cArquiXML, lDimPixels, lCentraliz, oXMLView, oDialogPvt, nObjLinha, nObjColun, nObjLargu, nObjAltur

    aArea := FWGetArea()
    nCorFundo := RGB(238, 238, 238)
    nJanAltura := 500
    nJanLargur := 500
    cJanTitulo := "Exemplo TXMLViewer"
    cArquiXML := "C:\spool\teste.xml"
    lDimPixels := .T.
    lCentraliz := .T.
    oXMLView := Nil
    oDialogPvt := Nil
    // Cria a dialog
    oDialogPvt := TDialog():New(0, 0, nJanAltura, nJanLargur, cJanTitulo, Nil, Nil, Nil, Nil, Nil, nCorFundo, Nil, Nil, lDimPixels)
    // Cria o visualizador do XML
    nObjLinha := 3
    nObjColun := 3
    nObjLargu := nJanLargur / 2 - 3
    nObjAltur := nJanAltura / 2 - 6
    oXMLView := TXMLViewer():New(nObjLinha, nObjColun, oDialogPvt, cArquiXML, nObjLargu, nObjAltur, lDimPixels)
    oXMLView:SetXML(cArquiXML)
    // Ativa e exibe a janela
    oDialogPvt:Activate(Nil, Nil, Nil, lCentraliz)
    FWRestArea(aArea)
    RETURN
