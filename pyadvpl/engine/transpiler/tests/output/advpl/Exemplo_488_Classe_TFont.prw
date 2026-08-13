// caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2024/06/20/criando-campos-em-tela-com-tget-maratona-advpl-e-tl-489/
// Bibliotecas
#Include "TOTVS.ch"
// {Protheus.doc} User Function zExe488
// Classe para modificar as fontes de um objeto instanciado
// @type Function
// @author Atilio
// @since 04/04/2023
// @see https://tdn.totvs.com/display/tec/TFont
// **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
USER FUNCTION zExe488()
    LOCAL aArea, nCorFundo, nJanAltura, nJanLargur, cJanTitulo, lDimPixels, lCentraliz, nObjLinha, nObjColun, nObjLargu, nObjAltur, oDialogPvt, bBlocoIni, oSayObj0, cSayObj0, oFontPad, oSayObj1, cSayObj1, oFontNeg, oSayObj2, cSayObj2, oFontSub, oSayObj3, cSayObj3, oFontIta, oSayObj4, cSayObj4, oFontTudo

    aArea := FWGetArea()
    nCorFundo := RGB(238, 238, 238)
    nJanAltura := 222
    nJanLargur := 404
    cJanTitulo := "Exemplo TFont"
    lDimPixels := .T.
    lCentraliz := .T.
    nObjLinha := 0
    nObjColun := 0
    nObjLargu := 0
    nObjAltur := 0
    oDialogPvt := Nil
    bBlocoIni := Nil
    // Aqui voce pode acionar funcoes customizadas que irao ser acionadas ao abrir a dialog
    // objeto0
    oSayObj0 := Nil
    cSayObj0 := "Tahoma, -12, Normal"
    oFontPad := TFont():New("Tahoma", Nil, - 12)
    // objeto1
    oSayObj1 := Nil
    cSayObj1 := "Tahoma, -12, Negrito"
    oFontNeg := TFont():New("Tahoma", Nil, - 12, Nil, .T.)
    // objeto2
    oSayObj2 := Nil
    cSayObj2 := "Tahoma, -14, Sublinhado"
    oFontSub := TFont():New("Tahoma", Nil, - 14, Nil, .F., Nil, Nil, Nil, Nil, .T.)
    // objeto3
    oSayObj3 := Nil
    cSayObj3 := "Tahoma, -16, Itálico"
    oFontIta := TFont():New("Tahoma", Nil, - 16, Nil, .F., Nil, Nil, Nil, Nil, .F., .T.)
    // objeto4
    oSayObj4 := Nil
    cSayObj4 := "Arial, -10, Tudo"
    oFontTudo := TFont():New("Arial", Nil, - 10, Nil, .T., Nil, Nil, Nil, Nil, .T., .T.)
    // Cria a dialog
    oDialogPvt := TDialog():New(0, 0, nJanAltura, nJanLargur, cJanTitulo, Nil, Nil, Nil, Nil, Nil, nCorFundo, Nil, Nil, lDimPixels)
    // objeto0 - usando a classe TSay
    nObjLinha := 9
    nObjColun := 7
    nObjLargu := 200
    nObjAltur := 20
    oSayObj0 := TSay():New(nObjLinha, nObjColun, Nil, oDialogPvt, Nil, oFontPad, Nil, Nil, Nil, lDimPixels, Nil, Nil, nObjLargu, nObjAltur, Nil, Nil, Nil, Nil, Nil)
    // objeto1 - usando a classe TSay
    nObjLinha := 29
    nObjColun := 7
    nObjLargu := 200
    nObjAltur := 20
    oSayObj1 := TSay():New(nObjLinha, nObjColun, Nil, oDialogPvt, Nil, oFontNeg, Nil, Nil, Nil, lDimPixels, Nil, Nil, nObjLargu, nObjAltur, Nil, Nil, Nil, Nil, Nil)
    // objeto2 - usando a classe TSay
    nObjLinha := 49
    nObjColun := 7
    nObjLargu := 200
    nObjAltur := 20
    oSayObj2 := TSay():New(nObjLinha, nObjColun, Nil, oDialogPvt, Nil, oFontSub, Nil, Nil, Nil, lDimPixels, Nil, Nil, nObjLargu, nObjAltur, Nil, Nil, Nil, Nil, Nil)
    // objeto3 - usando a classe TSay
    nObjLinha := 69
    nObjColun := 7
    nObjLargu := 200
    nObjAltur := 20
    oSayObj3 := TSay():New(nObjLinha, nObjColun, Nil, oDialogPvt, Nil, oFontIta, Nil, Nil, Nil, lDimPixels, Nil, Nil, nObjLargu, nObjAltur, Nil, Nil, Nil, Nil, Nil)
    // objeto4 - usando a classe TSay
    nObjLinha := 89
    nObjColun := 7
    nObjLargu := 200
    nObjAltur := 20
    oSayObj4 := TSay():New(nObjLinha, nObjColun, Nil, oDialogPvt, Nil, oFontTudo, Nil, Nil, Nil, lDimPixels, Nil, Nil, nObjLargu, nObjAltur, Nil, Nil, Nil, Nil, Nil)
    // Ativa e exibe a janela
    oDialogPvt:Activate(Nil, Nil, Nil, lCentraliz, Nil, Nil, bBlocoIni)
    FWRestArea(aArea)
    RETURN
