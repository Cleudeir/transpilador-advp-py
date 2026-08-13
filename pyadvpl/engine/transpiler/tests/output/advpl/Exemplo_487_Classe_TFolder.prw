// caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2024/06/19/criando-telas-com-a-tdialog-maratona-advpl-e-tl-486/
// Bibliotecas
#Include "TOTVS.ch"
// {Protheus.doc} User Function zExe487
// Classe para criar abas dentro de uma Dialog
// @type Function
// @author Atilio
// @since 04/04/2023
// @see https://tdn.totvs.com/display/tec/TFolder
// **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
USER FUNCTION zExe487()
    LOCAL aArea, nCorFundo, nJanAltura, nJanLargur, cJanTitulo, lDimPixels, lCentraliz, nObjLinha, nObjColun, nObjLargu, nObjAltur, cFontNome, oFontPadrao, oDialogPvt, bBlocoIni, oBtnObj0, cBtnObj0, bBtnObj0, oSayObj1A, cSayObj1A, oGetObj2A, xGetObj2A, oSayObj1B, cSayObj1B, oGetObj2B, xGetObj2B, oSayObj1C, cSayObj1C, oGetObj2C, xGetObj2C, oFolder, aAbas

    aArea := FWGetArea()
    nCorFundo := RGB(238, 238, 238)
    nJanAltura := 248
    nJanLargur := 655
    cJanTitulo := "Exemplo TFolder"
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
    cBtnObj0 := "Confirmar"
    bBtnObj0 := Nil
    // objeto1
    oSayObj1A := Nil
    cSayObj1A := "Campo A:"
    // objeto2
    oGetObj2A := Nil
    xGetObj2A := Space(10)
    // Se o get for data para inicilizar use dToS(''), se for numerico inicie com 0
    // objeto1
    oSayObj1B := Nil
    cSayObj1B := "Campo B:"
    // objeto2
    oGetObj2B := Nil
    xGetObj2B := Space(10)
    // Se o get for data para inicilizar use dToS(''), se for numerico inicie com 0
    // objeto1
    oSayObj1C := Nil
    cSayObj1C := "Campo C:"
    // objeto2
    oGetObj2C := Nil
    xGetObj2C := Space(10)
    // Se o get for data para inicilizar use dToS(''), se for numerico inicie com 0
    // Abas
    oFolder := Nil
    aAbas := { "Cadastro", "Complemento", "Outros" }
    // Cria a dialog
    oDialogPvt := TDialog():New(0, 0, nJanAltura, nJanLargur, cJanTitulo, Nil, Nil, Nil, Nil, Nil, nCorFundo, Nil, Nil, lDimPixels)
    // objeto0 - usando a classe TButton
    nObjLinha := 106
    nObjColun := 5
    nObjLargu := 75
    nObjAltur := 15
    oBtnObj0 := TButton():New(nObjLinha, nObjColun, cBtnObj0, oDialogPvt, bBtnObj0, nObjLargu, nObjAltur, Nil, oFontPadrao, Nil, lDimPixels)
    // Cria as abas
    oFolder := TFolder():New(1, 1, aAbas, Nil, oDialogPvt, Nil, Nil, Nil, lDimPixels, Nil, nJanLargur / 2 - 1, nJanAltura / 2 - 30)
    // Aba 1
    // objeto1 - usando a classe TSay
    nObjLinha := 7
    nObjColun := 2
    nObjLargu := 28
    nObjAltur := 6
    oSayObj1A := TSay():New(nObjLinha, nObjColun, Nil, oFolder:aDialogs()[1], Nil, oFontPadrao, Nil, Nil, Nil, lDimPixels, Nil, Nil, nObjLargu, nObjAltur, Nil, Nil, Nil, Nil, Nil)
    // objeto2 - usando a classe TGet
    nObjLinha := 5
    nObjColun := 37
    nObjLargu := 50
    nObjAltur := 10
    oGetObj2A := TGet():New(nObjLinha, nObjColun, Nil, oFolder:aDialogs()[1], nObjLargu, nObjAltur, Nil, Nil, Nil, Nil, oFontPadrao, Nil, Nil, lDimPixels)
    oGetObj2A->Picture := "@!"
    // Mascara / Picture do campo
    // Aba 2
    // objeto1 - usando a classe TSay
    nObjLinha := 7
    nObjColun := 2
    nObjLargu := 28
    nObjAltur := 6
    oSayObj1B := TSay():New(nObjLinha, nObjColun, Nil, oFolder:aDialogs()[2], Nil, oFontPadrao, Nil, Nil, Nil, lDimPixels, Nil, Nil, nObjLargu, nObjAltur, Nil, Nil, Nil, Nil, Nil)
    // objeto2 - usando a classe TGet
    nObjLinha := 5
    nObjColun := 37
    nObjLargu := 100
    nObjAltur := 10
    oGetObj2B := TGet():New(nObjLinha, nObjColun, Nil, oFolder:aDialogs()[2], nObjLargu, nObjAltur, Nil, Nil, Nil, Nil, oFontPadrao, Nil, Nil, lDimPixels)
    oGetObj2B->Picture := "@!"
    // Mascara / Picture do campo
    // Aba 3
    // objeto1 - usando a classe TSay
    nObjLinha := 7
    nObjColun := 2
    nObjLargu := 28
    nObjAltur := 6
    oSayObj1C := TSay():New(nObjLinha, nObjColun, Nil, oFolder:aDialogs()[3], Nil, oFontPadrao, Nil, Nil, Nil, lDimPixels, Nil, Nil, nObjLargu, nObjAltur, Nil, Nil, Nil, Nil, Nil)
    // objeto2 - usando a classe TGet
    nObjLinha := 5
    nObjColun := 37
    nObjLargu := 150
    nObjAltur := 10
    oGetObj2C := TGet():New(nObjLinha, nObjColun, Nil, oFolder:aDialogs()[3], nObjLargu, nObjAltur, Nil, Nil, Nil, Nil, oFontPadrao, Nil, Nil, lDimPixels)
    oGetObj2C->Picture := "@!"
    // Mascara / Picture do campo
    // Ativa e exibe a janela
    oDialogPvt:Activate(Nil, Nil, Nil, lCentraliz, Nil, Nil, bBlocoIni)
    FWRestArea(aArea)
    RETURN
