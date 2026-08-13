// caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2024/03/01/buscando-a-classe-de-um-objeto-com-a-getclassname-maratona-advpl-e-tl-266/
// Bibliotecas
#Include "TOTVS.ch"
// {Protheus.doc} User Function zExe266
// Retorna o nome da classe de um objeto
// @type  Function
// @author Atilio
// @since 21/02/2023
// @see https://tdn.totvs.com/display/tec/GetClassName
// Função GetClassName
// Parâmetros
// + oObjeto        , Objeto           , Variável com o objeto instanciado de uma classe
// Retorno
// + cClassName     , Caractere        , Nome da classe usada no Objeto
// **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
USER FUNCTION zExe266()
    LOCAL aArea, nCorFundo, nJanAltura, nJanLargur, cJanTitulo, lDimPixels, lCentraliz, nObjLinha, nObjColun, nObjLargu, nObjAltur, cFontNome, oFontPadrao, oDialogPvt, bBlocoIni, oSayInsira, cSayInsira, oGetTexto, cGetTexto, oBtnConf, cBtnObj8, bBtnObj8

    aArea := FWGetArea()
    nCorFundo := RGB(238, 238, 238)
    nJanAltura := 281
    nJanLargur := 358
    cJanTitulo := "Exemplo GetClassName"
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
    nObjAltur := 6
    oSayInsira := TSay():New(nObjLinha, nObjColun, Nil, oDialogPvt, Nil, oFontPadrao, Nil, Nil, Nil, lDimPixels, Nil, Nil, nObjLargu, nObjAltur, Nil, Nil, Nil, Nil, Nil)
    // objeto2 - usando a classe TGet
    nObjLinha := 3
    nObjColun := 64
    nObjLargu := 110
    nObjAltur := 10
    oGetTexto := TGet():New(nObjLinha, nObjColun, Nil, oDialogPvt, nObjLargu, nObjAltur, Nil, Nil, Nil, Nil, oFontPadrao, Nil, Nil, lDimPixels)
    // objeto4 - usando a classe TButton
    nObjLinha := 116
    nObjColun := 2
    nObjLargu := nJanLargur / 2 - 2
    nObjAltur := 15
    oBtnConf := TButton():New(nObjLinha, nObjColun, cBtnObj8, oDialogPvt, bBtnObj8, nObjLargu, nObjAltur, Nil, oFontPadrao, Nil, lDimPixels)
    // Ativa e exibe a janela
    oDialogPvt:Activate(Nil, Nil, Nil, lCentraliz, Nil, Nil, bBlocoIni)
    FWRestArea(aArea)
    RETURN Static

FUNCTION fConfirma()
    LOCAL cMensagem

    cMensagem := ""
    // Busca a classe dos objetos em tela
    cMensagem += "oDialogPvt: " + GetClassName(oDialogPvt) + CRLF
    cMensagem += "oSayInsira: " + GetClassName(oSayInsira) + CRLF
    cMensagem += "oGetTexto: " + GetClassName(oGetTexto) + CRLF
    cMensagem += "oBtnConf: " + GetClassName(oBtnConf)
    FWAlertInfo(cMensagem, "Teste GetClassName")
    RETURN
