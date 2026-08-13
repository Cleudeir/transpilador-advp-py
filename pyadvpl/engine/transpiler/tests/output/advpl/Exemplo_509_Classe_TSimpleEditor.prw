// caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2024/06/30/criando-um-editor-atraves-da-tsimpleeditor-maratona-advpl-e-tl-509/
// Bibliotecas
#Include "TOTVS.ch"
// {Protheus.doc} User Function zExe509
// Cria uma caixa de texto grande para digitação / visualização (com algumas opções como exibir em html)
// @type Function
// @author Atilio
// @since 04/04/2023
// @see https://tdn.totvs.com/display/tec/TSimpleEditor
// **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
USER FUNCTION zExe509()
    LOCAL aArea, nCorFundo, nJanAltura, nJanLargur, cJanTitulo, lDimPixels, lCentraliz, nObjLinha, nObjColun, nObjLargu, nObjAltur, cFontNome, oFontPadrao, oDialogPvt, bBlocoIni, oSimpEdit, cSimpEdit, oBtnObj1, cBtnObj1, bBtnObj1, oPanelEdit

    aArea := FWGetArea()
    nCorFundo := RGB(238, 238, 238)
    nJanAltura := 154
    nJanLargur := 318
    cJanTitulo := "Exemplo TSimpleEditor"
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
    oSimpEdit := Nil
    cSimpEdit := ""
    // objeto1
    oBtnObj1 := Nil
    cBtnObj1 := "Confirmar"
    bBtnObj1 := Nil
    // Cria a dialog
    oDialogPvt := TDialog():New(0, 0, nJanAltura, nJanLargur, cJanTitulo, Nil, Nil, Nil, Nil, Nil, nCorFundo, Nil, Nil, lDimPixels)
    // Monta o texto que será exibido
    cSimpEdit := "<p>Olá.</p>" + CRLF
    cSimpEdit += "<p>Esse é um exemplo de <strong>mensagem em HTML</strong>.</p>" + CRLF
    cSimpEdit += "<p>Note que as <font color="red">tags foram interpretadas</font>.</p>" + CRLF
    // objeto0 - usando a classe TSimpleEditor
    nObjLinha := 7
    nObjColun := 6
    nObjLargu := 145
    nObjAltur := 40
    oPanelEdit := tPanel():New(nObjLinha, nObjColun, "", oDialogPvt, Nil, Nil, Nil, RGB(0, 0, 0), RGB(254, 254, 254), nObjLargu, nObjAltur)
    oSimpEdit := TSimpleEditor():Create(oPanelEdit)
    oSimpEdit->lAutoIndent := .T.
    oSimpEdit->nWidth := oPanelEdit:nWidth()
    oSimpEdit->nHeight := oPanelEdit:nHeight()
    oSimpEdit:TextFormat(1)
    // 1=Html; 2=Plain Text
    oSimpEdit:TextSize(11)
    oSimpEdit:Load(cSimpEdit)
    oSimpEdit:Refresh()
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
