// caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2024/06/12/buscando-qual-e-o-banco-utilizado-atraves-da-tcgetdb-maratona-advpl-e-tl-473/
// Bibliotecas
#Include "TOTVS.ch"
// {Protheus.doc} User Function zExe472
// Classe para criar botões em uma Dialog
// @type Function
// @author Atilio
// @since 03/04/2023
// @see https://tdn.totvs.com/display/tec/TButton
// **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
USER FUNCTION zExe472()
    LOCAL aArea, nCorFundo, nJanAltura, nJanLargur, cJanTitulo, lDimPixels, lCentraliz, nObjLinha, nObjColun, nObjLargu, nObjAltur, cFontNome, oFontPadrao, oDialogPvt, bBlocoIni, oBtnObj0, cBtnObj0, bBtnObj0, oBtnObj1, cBtnObj1, bBtnObj1

    aArea := FWGetArea()
    nCorFundo := RGB(238, 238, 238)
    nJanAltura := 129
    nJanLargur := 242
    cJanTitulo := "Exemplo TButton"
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
    oBtnObj0 := Nil
    cBtnObj0 := "Botão Normal"
    bBtnObj0 := Nil
    // objeto1
    oBtnObj1 := Nil
    cBtnObj1 := "Botão com CSS"
    bBtnObj1 := Nil
    // Cria a dialog
    oDialogPvt := TDialog():New(0, 0, nJanAltura, nJanLargur, cJanTitulo, Nil, Nil, Nil, Nil, Nil, nCorFundo, Nil, Nil, lDimPixels)
    // objeto0 - usando a classe TButton
    nObjLinha := 10
    nObjColun := 10
    nObjLargu := 100
    nObjAltur := 15
    oBtnObj0 := TButton():New(nObjLinha, nObjColun, cBtnObj0, oDialogPvt, bBtnObj0, nObjLargu, nObjAltur, Nil, oFontPadrao, Nil, lDimPixels)
    // objeto1 - usando a classe TButton
    nObjLinha := 35
    nObjColun := 10
    nObjLargu := 100
    nObjAltur := 15
    oBtnObj1 := TButton():New(nObjLinha, nObjColun, cBtnObj1, oDialogPvt, bBtnObj1, nObjLargu, nObjAltur, Nil, oFontPadrao, Nil, lDimPixels)
    oBtnObj1:SetCSS("TButton { font: bold;     background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,stop: 0 #3DAFCC, stop: 1 #0D9CBF);    color: #FFFFFF;     border-width: 1px;     border-style: solid;     border-radius: 3px;     border-color: #369CB5; }TButton:focus {    padding:0px; outline-width:1px; outline-style:solid; outline-color: #51DAFC; outline-radius:3px; border-color:#369CB5;}TButton:hover {    color: #FFFFFF;     background-color : qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,stop: 0 #3DAFCC, stop: 1 #1188A6);    border-width: 1px;     border-style: solid;     border-radius: 3px;     border-color: #369CB5; }TButton:pressed {    color: #FFF;     background-color : qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,stop: 0 #1188A6, stop: 1 #3DAFCC);    border-width: 1px;     border-style: solid;     border-radius: 3px;     border-color: #369CB5; }TButton:disabled {    color: #FFFFFF;     background-color: #4CA0B5; }")
    // Ativa e exibe a janela
    oDialogPvt:Activate(Nil, Nil, Nil, lCentraliz, Nil, Nil, bBlocoIni)
    FWRestArea(aArea)
    RETURN
