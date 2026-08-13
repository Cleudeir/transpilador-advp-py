// caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2024/02/17/gerando-um-qrcode-atraves-da-classe-fwqrcode-maratona-advpl-e-tl-241/
// Bibliotecas
#Include 'TOTVS.ch'
// {Protheus.doc} User Function zExe241
// Função que gera um QRCode em tela
// @type Function
// @author Atilio
// @since 20/02/2023
// @see https://tdn.totvs.com/display/public/framework/FwQrCode
// **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
USER FUNCTION zExe241()
    LOCAL aArea, nCorFundo, nJanAltura, nJanLargur, cJanTitulo, lDimPixels, lCentraliz, nObjLinha, nObjColun, nObjLargu, nObjAltur, cFontNome, oFontPadrao, oDialogPvt, bBlocoIni, oSayInsira, cSayInsira, oGetTexto, cGetTexto, oQrCode, oBtnObj8, cBtnObj8, bBtnObj8

    aArea := FWGetArea()
    nCorFundo := RGB(238, 238, 238)
    nJanAltura := 281
    nJanLargur := 358
    cJanTitulo := "Exemplo FWQrCode"
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
    // objeto1
    oSayInsira := Nil
    cSayInsira := "Insira o Texto:"
    // objeto2
    oGetTexto := Nil
    cGetTexto := "https://terminaldeinformacao.com" + Space(200)
    // objeto 3
    oQrCode := Nil
    // objeto4
    oBtnObj8 := Nil
    cBtnObj8 := "Confirmar"
    bBtnObj8 := Nil
    // Cria a dialog
    oDialogPvt := TDialog():New(0, 0, nJanAltura, nJanLargur, cJanTitulo, Nil, Nil, Nil, Nil, Nil, nCorFundo, Nil, Nil, lDimPixels)
    // objeto1 - usando a classe TSay
    nObjLinha := 4
    nObjColun := 4
    nObjLargu := 70
    nObjAltur := 6
    oSayInsira := TSay():New(nObjLinha, nObjColun, Nil, oDialogPvt, Nil, oFontPadrao, Nil, Nil, Nil, lDimPixels, Nil, Nil, nObjLargu, nObjAltur, Nil, Nil, Nil, Nil, Nil)
    // objeto2 - usando a classe TGet
    nObjLinha := 3
    nObjColun := 64
    nObjLargu := 110
    nObjAltur := 10
    oGetTexto := TGet():New(nObjLinha, nObjColun, Nil, oDialogPvt, nObjLargu, nObjAltur, Nil, Nil, Nil, Nil, oFontPadrao, Nil, Nil, lDimPixels)
    // objeto3 - usando a classe FWQRCode
    nObjLinha := 19
    nObjColun := 44
    nObjLargu := 180
    nObjAltur := 180
    oQrCode := FwQrCode():New({ nObjLinha, nObjColun, nObjLargu, nObjAltur }, oDialogPvt, cGetTexto)
    // objeto4 - usando a classe TButton
    nObjLinha := 116
    nObjColun := 2
    nObjLargu := nJanLargur / 2 - 2
    nObjAltur := 15
    oBtnObj8 := TButton():New(nObjLinha, nObjColun, cBtnObj8, oDialogPvt, bBtnObj8, nObjLargu, nObjAltur, Nil, oFontPadrao, Nil, lDimPixels)
    // Ativa e exibe a janela
    oDialogPvt:Activate(Nil, Nil, Nil, lCentraliz, Nil, Nil, bBlocoIni)
    FWRestArea(aArea)
    RETURN Static

FUNCTION fAtualiza()
    // Somente se houver texto, irá atualizar na tela
    If .NOT. Empty(cGetTexto)
        oQrCode:SetCodeBar(cGetTexto)
        oQrCode:Refresh()
    EndIf
    RETURN
