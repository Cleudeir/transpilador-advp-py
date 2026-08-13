// caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2024/06/13/preparando-a-execucao-de-uma-query-atraves-das-tcgenqry-e-tcgenqry2-maratona-advpl-e-tl-474/
// Bibliotecas
#Include "TOTVS.ch"
// {Protheus.doc} User Function zExe475
// Classe para criar checkbox em uma Dialog
// @type Function
// @author Atilio
// @since 03/04/2023
// @see https://tdn.totvs.com/display/tec/TCheckBox
// **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
USER FUNCTION zExe475()
    LOCAL aArea, nCorFundo, nJanAltura, nJanLargur, cJanTitulo, lDimPixels, lCentraliz, nObjLinha, nObjColun, nObjLargu, nObjAltur, cFontNome, oFontPadrao, oDialogPvt, bBlocoIni, oChkObj0, lChkObj0, cChkObj0, oChkObj1, lChkObj1, cChkObj1, oChkObj2, lChkObj2, cChkObj2, oBtnObj3, cBtnObj3, bBtnObj3

    aArea := FWGetArea()
    nCorFundo := RGB(238, 238, 238)
    nJanAltura := 187
    nJanLargur := 253
    cJanTitulo := "Exemplo TCheckBox"
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
    oChkObj0 := Nil
    lChkObj0 := .F.
    cChkObj0 := "CheckBox vindo desmarcado"
    // objeto1
    oChkObj1 := Nil
    lChkObj1 := .T.
    cChkObj1 := "CheckBox vindo marcado"
    // objeto2
    oChkObj2 := Nil
    lChkObj2 := .T.
    cChkObj2 := "CheckBox desativado"
    // objeto3
    oBtnObj3 := Nil
    cBtnObj3 := "Confirmar"
    bBtnObj3 := Nil
    // Cria a dialog
    oDialogPvt := TDialog():New(0, 0, nJanAltura, nJanLargur, cJanTitulo, Nil, Nil, Nil, Nil, Nil, nCorFundo, Nil, Nil, lDimPixels)
    // objeto0 - usando a classe TCheckBox
    nObjLinha := 5
    nObjColun := 7
    nObjLargu := 110
    nObjAltur := 15
    oChkObj0 := TCheckBox():New(nObjLinha, nObjColun, cChkObj0, Nil, oDialogPvt, nObjLargu, nObjAltur, Nil, Nil, oFontPadrao, Nil, Nil, Nil, Nil, lDimPixels)
    // objeto1 - usando a classe TCheckBox
    nObjLinha := 25
    nObjColun := 7
    nObjLargu := 110
    nObjAltur := 15
    oChkObj1 := TCheckBox():New(nObjLinha, nObjColun, cChkObj1, Nil, oDialogPvt, nObjLargu, nObjAltur, Nil, Nil, oFontPadrao, Nil, Nil, Nil, Nil, lDimPixels)
    // objeto2 - usando a classe TCheckBox
    nObjLinha := 45
    nObjColun := 7
    nObjLargu := 110
    nObjAltur := 15
    oChkObj2 := TCheckBox():New(nObjLinha, nObjColun, cChkObj2, Nil, oDialogPvt, nObjLargu, nObjAltur, Nil, Nil, oFontPadrao, Nil, Nil, Nil, Nil, lDimPixels)
    oChkObj2->lActive := .F.
    // objeto3 - usando a classe TButton
    nObjLinha := 70
    nObjColun := 7
    nObjLargu := 110
    nObjAltur := 15
    oBtnObj3 := TButton():New(nObjLinha, nObjColun, cBtnObj3, oDialogPvt, bBtnObj3, nObjLargu, nObjAltur, Nil, oFontPadrao, Nil, lDimPixels)
    // Ativa e exibe a janela
    oDialogPvt:Activate(Nil, Nil, Nil, lCentraliz, Nil, Nil, bBlocoIni)
    FWRestArea(aArea)
    RETURN
