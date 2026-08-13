// caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2024/05/19/buscando-um-tom-de-cor-atraves-da-rgb-maratona-advpl-e-tl-424/
// Bibliotecas
#Include "TOTVS.ch"
// {Protheus.doc} User Function zExe424
// Retorna uma cor para ser usada em AdvPL conforme o padrão RGB (Red, Green e Blue)
// @type Function
// @author Atilio
// @since 29/03/2023
// @see https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022454272-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Tabela-de-cores-MSDIALOG
// Função RGB
// Parâmetros
// Recebe o tom em Vermelho (0 a 255)
// Recebe o tom em Verde (0 a 255)
// Recebe o tom em Azul (0 a 255)
// Retorno
// Retorna a cor em AdvPL para ser utilizada
// **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
USER FUNCTION zExe424()
    LOCAL aArea, nCorUsada, nJanAltura, nJanLargur, cJanTitulo, lDimPixels, lCentraliz, nObjLinha, nObjColun, nObjLargu, nObjAltur, cFontNome, oFontPadrao, oDialogPvt, bBlocoIni, oSayInsira, cSayInsira, oGetTexto, cGetTexto, oBtnConf, cBtnObj8, bBtnObj8

    aArea := FWGetArea()
    nCorUsada := 0
    nJanAltura := 281
    nJanLargur := 358
    cJanTitulo := "Exemplo RGB"
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
    // Definindo a cor de fundo como um Magenta ou Rosa meio claro
    nCorUsada := RGB(230, 10, 230)
    // Cria a dialog
    oDialogPvt := TDialog():New(0, 0, nJanAltura, nJanLargur, cJanTitulo, Nil, Nil, Nil, Nil, Nil, nCorUsada, Nil, Nil, lDimPixels)
    // objeto1 - usando a classe TSay
    nObjLinha := 4
    nObjColun := 4
    nObjLargu := 70
    nObjAltur := 12
    oSayInsira := TSay():New(nObjLinha, nObjColun, Nil, oDialogPvt, Nil, oFontPadrao, Nil, Nil, Nil, lDimPixels, Nil, Nil, nObjLargu, nObjAltur, Nil, Nil, Nil, Nil, Nil)
    // objeto2 - usando a classe TGet
    nObjLinha := 3
    nObjColun := 64
    nObjLargu := 110
    nObjAltur := 15
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
    RETURN
