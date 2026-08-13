// caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2024/05/01/executando-queries-com-a-plsquery-maratona-advpl-e-tl-388/
// Bibliotecas
#Include "TOTVS.ch"
#Include "POSCSS.ch"
// {Protheus.doc} User Function zExe389
// Retorna o estilo CSS de objetos instanciados
// @type  Function
// @author Atilio
// @since 28/03/2023
// Função PosCSS
// Parâmetros
// Nome da classe do objeto
// Tipo do CSS buscado
// Complementos do CSS para alguns casos
// Retorno
// Retorna o CSS encontrado
// **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
USER FUNCTION zExe389()
    LOCAL aArea, nCorFundo, nJanAltura, nJanLargur, cJanTitulo, lDimPixels, lCentraliz, nObjLinha, nObjColun, nObjLargu, nObjAltur, lPosCSS, cFontNome, oFontPadrao, oDialogPvt, bBlocoIni, oSayInsira, cSayInsira, oGetTexto, cGetTexto, oBtnConf, cBtnObj8, bBtnObj8

    aArea := FWGetArea()
    nCorFundo := RGB(238, 238, 238)
    nJanAltura := 281
    nJanLargur := 358
    cJanTitulo := "Exemplo PosCSS"
    lDimPixels := .T.
    lCentraliz := .T.
    nObjLinha := 0
    nObjColun := 0
    nObjLargu := 0
    nObjAltur := 0
    lPosCSS := FWAlertYesNo("Deseja utilizar o POSCSS?", "Confirma?")
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
    // objeto4
    oBtnConf := Nil
    cBtnObj8 := "Confirmar"
    bBtnObj8 := Nil
    // Cria a dialog
    oDialogPvt := TDialog():New(0, 0, nJanAltura, nJanLargur, cJanTitulo, Nil, Nil, Nil, Nil, Nil, nCorFundo, Nil, Nil, lDimPixels)
    // objeto1 - usando a classe TSay
    nObjLinha := 4
    nObjColun := 4
    nObjLargu := 70
    nObjAltur := 12
    oSayInsira := TSay():New(nObjLinha, nObjColun, Nil, oDialogPvt, Nil, oFontPadrao, Nil, Nil, Nil, lDimPixels, Nil, Nil, nObjLargu, nObjAltur, Nil, Nil, Nil, Nil, Nil)
    If lPosCSS
        oSayInsira:SetCSS(PosCss(GetClassName(oSayInsira), CSS_LABEL_FOCAL, { "16", .F. }))
    EndIf
    // objeto2 - usando a classe TGet
    nObjLinha := 3
    nObjColun := 64
    nObjLargu := 110
    nObjAltur := 15
    oGetTexto := TGet():New(nObjLinha, nObjColun, Nil, oDialogPvt, nObjLargu, nObjAltur, Nil, Nil, Nil, Nil, oFontPadrao, Nil, Nil, lDimPixels)
    If lPosCSS
        oGetTexto:SetCSS(PosCss(GetClassName(oGetTexto), CSS_GET_FOCAL))
    EndIf
    // objeto4 - usando a classe TButton
    nObjLinha := 116
    nObjColun := 2
    nObjLargu := nJanLargur / 2 - 2
    nObjAltur := 15
    oBtnConf := TButton():New(nObjLinha, nObjColun, cBtnObj8, oDialogPvt, bBtnObj8, nObjLargu, nObjAltur, Nil, oFontPadrao, Nil, lDimPixels)
    If lPosCSS
        oBtnConf:SetCSS(PosCss(GetClassName(oBtnConf), CSS_BTN_ATIVO))
    EndIf
    // Ativa e exibe a janela
    oDialogPvt:Activate(Nil, Nil, Nil, lCentraliz, Nil, Nil, bBlocoIni)
    FWRestArea(aArea)
    RETURN Static

FUNCTION fConfirma()
    LOCAL cMensagem

    cMensagem := "teste"
    FWAlertInfo(cMensagem, "Teste PosCSS")
    RETURN
