// caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2024/06/24/criando-uma-listagem-de-informacoes-com-tlistbox-maratona-advpl-e-tl-496/
// Bibliotecas
#Include "TOTVS.ch"
// {Protheus.doc} User Function zExe496
// Cria uma pequena grid em uma Dialog
// @type Function
// @author Atilio
// @since 04/04/2023
// @see https://tdn.totvs.com/display/tec/TListBox
// **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
USER FUNCTION zExe496()
    LOCAL aArea, nCorFundo, nJanAltura, nJanLargur, cJanTitulo, lDimPixels, lCentraliz, nObjLinha, nObjColun, nObjLargu, nObjAltur, cFontNome, oFontPadrao, oDialogPvt, bBlocoIni, oLisObj0, nLisObj0, aLisObj0, oBtnObj1, cBtnObj1, bBtnObj1

    aArea := FWGetArea()
    nCorFundo := RGB(238, 238, 238)
    nJanAltura := 228
    nJanLargur := 318
    cJanTitulo := "Exemplo TListBox"
    lDimPixels := .T.
    lCentraliz := .T.
    nObjLinha := 0
    nObjColun := 0
    nObjLargu := 0
    nObjAltur := 0
    cFontNome := "Tahoma"
    oFontPadrao := TFont():New(cFontNome, Nil, - 12)
    oDialogPvt := Nil
    bBlocoIni := Nil
    // Aqui voce pode acionar funcoes customizadas que irao ser acionadas ao abrir a dialog
    // objeto0
    oLisObj0 := Nil
    nLisObj0 := 0
    aLisObj0 := { "YouTube", "Instagram", "Twitter", "Facebook", "e-Mail" }
    // objeto1
    oBtnObj1 := Nil
    cBtnObj1 := "Confirmar"
    bBtnObj1 := Nil
    // Cria a dialog
    oDialogPvt := TDialog():New(0, 0, nJanAltura, nJanLargur, cJanTitulo, Nil, Nil, Nil, Nil, Nil, nCorFundo, Nil, Nil, lDimPixels)
    // objeto0 - usando a classe TListBox
    nObjLinha := 6
    nObjColun := 8
    nObjLargu := 142
    nObjAltur := 80
    oLisObj0 := TListBox():New(nObjLinha, nObjColun, Nil, aLisObj0, nObjLargu, nObjAltur, Nil, oDialogPvt, Nil, Nil, Nil, lDimPixels, Nil, Nil, oFontPadrao)
    // objeto1 - usando a classe TButton
    nObjLinha := 95
    nObjColun := 8
    nObjLargu := 65
    nObjAltur := 15
    oBtnObj1 := TButton():New(nObjLinha, nObjColun, cBtnObj1, oDialogPvt, bBtnObj1, nObjLargu, nObjAltur, Nil, oFontPadrao, Nil, lDimPixels)
    // Ativa e exibe a janela
    oDialogPvt:Activate(Nil, Nil, Nil, lCentraliz, Nil, Nil, bBlocoIni)
    FWRestArea(aArea)
    RETURN
