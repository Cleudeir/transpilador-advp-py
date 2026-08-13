// caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2024/06/26/abrindo-um-relatorio-atraves-da-tpageview-maratona-advpl-e-tl-500/
// Bibliotecas
#Include "TOTVS.ch"
// {Protheus.doc} User Function zExe500
// Abre um relatório para visualização
// @type Function
// @author Atilio
// @since 04/04/2023
// @see https://tdn.totvs.com/display/tec/TPageView
// **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
USER FUNCTION zExe500()
    LOCAL aArea, oDlgRelat, cArqRelat, oPrinter, oTPageView, aTamanho, nJanLarg, nJanAltu, lCentered

    aArea := FWGetArea()
    oDlgRelat := Nil
    cArqRelat := ""
    oPrinter := Nil
    oTPageView := Nil
    aTamanho := MsAdvSize()
    nJanLarg := aTamanho[5]
    nJanAltu := aTamanho[6]
    lCentered := .T.
    // Definindo o arquivo que será aberto
    cArqRelat := "\spool\matr680.prt"
    // Criando um objeto de impressão e setando o arquivo
    oPrinter := TMSPrinter():New()
    oPrinter:SetFile(cArqRelat, .F.)
    oPrinter:SetPortrait()
    oPrinter:SetPaperSize(9)
    // Criando a dialog
    oDlgRelat := TDialog():New(0, 0, nJanAltu, nJanLarg, "Teste de TPageView", Nil, Nil, Nil, Nil, CLR_BLACK, RGB(250, 250, 250), Nil, Nil, .T.)
    // Criando o TPageView
    oTPageView := TPageView():New(0, 0, nJanLarg, nJanAltu, oPrinter, oDlgRelat, oPrinter:nPageWidth() + 200, oPrinter:nPageHeight())
    oTPageView->bLClicked := Nil
    oTPageView->bRClicked := Nil
    oTPageView->Align := CONTROL_ALIGN_ALLCLIENT
    oTPageView->nZoom := 150
    oDlgRelat:Activate(Nil, Nil, Nil, lCentered, Nil, Nil)
    FWRestArea(aArea)
    RETURN
