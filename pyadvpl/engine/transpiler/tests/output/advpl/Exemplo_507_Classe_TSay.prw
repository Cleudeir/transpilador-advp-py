// caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2024/06/29/realizando-tratativas-com-try-catch-maratona-advpl-e-tl-506/
// Bibliotecas
#Include "TOTVS.ch"
// {Protheus.doc} User Function zExe507
// Cria labels de texto dentro de uma dialog
// @type Function
// @author Atilio
// @since 04/04/2023
// @see https://tdn.totvs.com/display/tec/TSay
// **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
USER FUNCTION zExe507()
    LOCAL aArea, nCorFundo, nJanAltura, nJanLargur, cJanTitulo, lDimPixels, lCentraliz, nObjLinha, nObjColun, nObjLargu, nObjAltur, cFontNome, oFontPadrao, oDialogPvt, bBlocoIni, oSayObj0, cSayObj0, oSayObj1, cSayObj1, oSayObj2, cSayObj2, oSayObj3, cSayObj3, oSayObj4, cSayObj4

    aArea := FWGetArea()
    nCorFundo := RGB(238, 238, 238)
    nJanAltura := 222
    nJanLargur := 404
    cJanTitulo := "Exemplo TSay"
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
    oSayObj0 := Nil
    cSayObj0 := "Label comum"
    // objeto1
    oSayObj1 := Nil
    cSayObj1 := "<h3>Label html - <font color="blue">teste</font></h3>"
    // objeto2
    oSayObj2 := Nil
    cSayObj2 := "Label com cores"
    // objeto3
    oSayObj3 := Nil
    cSayObj3 := "Label com CSS"
    // objeto4
    oSayObj4 := Nil
    cSayObj4 := "Label com clique"
    // Cria a dialog
    oDialogPvt := TDialog():New(0, 0, nJanAltura, nJanLargur, cJanTitulo, Nil, Nil, Nil, Nil, Nil, nCorFundo, Nil, Nil, lDimPixels)
    // objeto0 - usando a classe TSay
    nObjLinha := 9
    nObjColun := 7
    nObjLargu := 180
    nObjAltur := 15
    oSayObj0 := TSay():New(nObjLinha, nObjColun, Nil, oDialogPvt, Nil, oFontPadrao, Nil, Nil, Nil, lDimPixels, Nil, Nil, nObjLargu, nObjAltur, Nil, Nil, Nil, Nil, Nil)
    // objeto1 - usando a classe TSay
    nObjLinha := 29
    nObjColun := 7
    nObjLargu := 180
    nObjAltur := 15
    oSayObj1 := TSay():New(nObjLinha, nObjColun, Nil, oDialogPvt, Nil, oFontPadrao, Nil, Nil, Nil, lDimPixels, Nil, Nil, nObjLargu, nObjAltur, Nil, Nil, Nil, Nil, Nil, .T.)
    // objeto2 - usando a classe TSay
    nObjLinha := 49
    nObjColun := 7
    nObjLargu := 180
    nObjAltur := 15
    oSayObj2 := TSay():New(nObjLinha, nObjColun, Nil, oDialogPvt, Nil, oFontPadrao, Nil, Nil, Nil, lDimPixels, RGB(255, 0, 0), Nil, nObjLargu, nObjAltur, Nil, Nil, Nil, Nil, Nil)
    // objeto3 - usando a classe TSay
    nObjLinha := 69
    nObjColun := 7
    nObjLargu := 180
    nObjAltur := 15
    oSayObj3 := TSay():New(nObjLinha, nObjColun, Nil, oDialogPvt, Nil, oFontPadrao, Nil, Nil, Nil, lDimPixels, Nil, Nil, nObjLargu, nObjAltur, Nil, Nil, Nil, Nil, Nil)
    oSayObj3:SetCSS("background-color: #FF0000; color: #0D0D0D}")
    // objeto4 - usando a classe TSay
    nObjLinha := 89
    nObjColun := 7
    nObjLargu := 180
    nObjAltur := 15
    oSayObj4 := TSay():New(nObjLinha, nObjColun, Nil, oDialogPvt, Nil, oFontPadrao, Nil, Nil, Nil, lDimPixels, Nil, Nil, nObjLargu, nObjAltur, Nil, Nil, Nil, Nil, Nil)
    oSayObj4->bLClicked := Nil
    oSayObj4->bRClicked := Nil
    // oSayObj4:bLDblClick := {|| FWAlertInfo("Duplo clique com o botão esquerdo do Mouse", "bLDblClick")}
    // Ativa e exibe a janela
    oDialogPvt:Activate(Nil, Nil, Nil, lCentraliz, Nil, Nil, bBlocoIni)
    FWRestArea(aArea)
    RETURN
