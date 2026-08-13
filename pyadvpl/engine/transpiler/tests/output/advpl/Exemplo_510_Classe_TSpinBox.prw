// caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2024/07/01/criando-um-icone-na-bandeja-do-s-o-com-tsystemtray-maratona-advpl-e-tl-511/
// Bibliotecas
#Include "TOTVS.ch"
// {Protheus.doc} User Function zExe510
// Cria uma caixa de texto com botões ao lado de manipulação
// @type Function
// @author Atilio
// @since 04/04/2023
// @see https://tdn.totvs.com/display/tec/TSpinBox
// **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
USER FUNCTION zExe510()
    LOCAL aArea, nCorFundo, nJanAltura, nJanLargur, cJanTitulo, lDimPixels, lCentraliz, nObjLinha, nObjColun, nObjLargu, nObjAltur, cFontNome, oFontPadrao, oDialogPvt, bBlocoIni, oSpinBox, nSpinBox, oBtnObj1, cBtnObj1, bBtnObj1

    aArea := FWGetArea()
    nCorFundo := RGB(238, 238, 238)
    nJanAltura := 154
    nJanLargur := 318
    cJanTitulo := "Exemplo TSpinBox"
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
    oSpinBox := Nil
    nSpinBox := 10
    // objeto1
    oBtnObj1 := Nil
    cBtnObj1 := "Confirmar"
    bBtnObj1 := Nil
    // Cria a dialog
    oDialogPvt := TDialog():New(0, 0, nJanAltura, nJanLargur, cJanTitulo, Nil, Nil, Nil, Nil, Nil, nCorFundo, Nil, Nil, lDimPixels)
    // objeto0 - usando a classe TSpinBox
    nObjLinha := 7
    nObjColun := 6
    nObjLargu := 145
    nObjAltur := 15
    oSpinBox := TSpinBox():New(nObjLinha, nObjColun, oDialogPvt, Nil, nObjLargu, nObjAltur)
    oSpinBox:setRange(- 30, 30)
    oSpinBox:setStep(5)
    oSpinBox:setValue(nSpinBox)
    // objeto1 - usando a classe TButton
    nObjLinha := 54
    nObjColun := 6
    nObjLargu := 75
    nObjAltur := 15
    oBtnObj1 := TButton():New(nObjLinha, nObjColun, cBtnObj1, oDialogPvt, bBtnObj1, nObjLargu, nObjAltur, Nil, oFontPadrao, Nil, lDimPixels)
    // Ativa e exibe a janela
    oDialogPvt:Activate(Nil, Nil, Nil, lCentraliz, Nil, Nil, bBlocoIni)
    FWRestArea(aArea)
    RETURN
