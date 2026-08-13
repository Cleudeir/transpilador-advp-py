// caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2024/06/11/criando-um-pincel-para-pintar-um-fundo-de-relatorio-com-tbrush-maratona-advpl-e-tl-471/
// Bibliotecas
#Include "TOTVS.ch"
// {Protheus.doc} User Function zExe470
// Classe para exibir imagens em Dialogs no Protheus
// @type Function
// @author Atilio
// @since 02/04/2023
// @see https://tdn.totvs.com/display/tec/TBitmap
// Esse artigo foi baseado na função zSlider disponível em - https://terminaldeinformacao.com/2020/08/28/como-fazer-um-slideshow-em-advpl/
// **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
USER FUNCTION zExe470()
    LOCAL aArea, lDimPixels, lCentraliz, bBlocoIni, cFontUti, oFontAno, oFontSub, oFontSubN, oFontBtn, cDirFiles, cDirect, aImgs, nImgAtu, oDlgCom, oGetImg, cGetImg, oBmpFoto, nJanLarg, nJanAltu, oSayModulo, oSayTitulo, oSaySubTit, oBtnSair, oBtnEsq, oBtnDir

    aArea := GetArea()
    lDimPixels := .T.
    lCentraliz := .T.
    bBlocoIni := Nil
    // Fontes
    cFontUti := "Tahoma"
    oFontAno := TFont():New(cFontUti, Nil, - 38)
    oFontSub := TFont():New(cFontUti, Nil, - 20)
    oFontSubN := TFont():New(cFontUti, Nil, - 20, Nil, .T.)
    oFontBtn := TFont():New(cFontUti, Nil, - 14)
    Default
    cDirFiles := "C:\Users\danat\OneDrive\Trabalho\Atilio Sistemas\Workspace_VS\Local\Cursos\Curso_OO\imgs\"
    cDirect := Alltrim(cDirFiles)
    aImgs := {  }
    nImgAtu := 0
    // Janela e componentes
    oDlgCom := Nil
    oGetImg := Nil
    cGetImg := ""
    oBmpFoto := Nil
    // Tamanho da janela
    nJanLarg := 800
    nJanAltu := 600
    // Somente se tiver imagens a exibir
    If .NOT. Empty(cDirect) .AND. ExistDir(cDirect)
        // Tratativa para adicionar uma barra no final
        If SubStr(cDirect, Len(cDirect), 1) <> "\"
            cDirect += "\"
        EndIf
        // Carregando as imagens
        FWMsgRun(Nil, Nil, "Processando", "Buscando imagens da pasta")
        // Se tiver imagens
        If Len(aImgs) > 0
            nImgAtu := 1
            cGetImg := cDirect + aImgs[nImgAtu]
            // Criando a janela
            oDlgCom := TDialog():New(0, 0, nJanAltu, nJanLarg, "Slideshow", Nil, Nil, Nil, Nil, Nil, Nil, Nil, Nil, lDimPixels)
            // Labels gerais
            oSayModulo := TSay():New(4, 3, Nil, oDlgCom, "", oFontAno, Nil, Nil, Nil, .T., RGB(149, 179, 215), Nil, 200, 30, Nil, Nil, Nil, Nil, Nil, .F., Nil)
            oSayTitulo := TSay():New(4, 45, Nil, oDlgCom, "", oFontSub, Nil, Nil, Nil, .T., RGB(31, 73, 125), Nil, 200, 30, Nil, Nil, Nil, Nil, Nil, .F., Nil)
            oSaySubTit := TSay():New(14, 45, Nil, oDlgCom, "", oFontSubN, Nil, Nil, Nil, .T., RGB(31, 73, 125), Nil, 300, 30, Nil, Nil, Nil, Nil, Nil, .F., Nil)
            // Botão de Sair
            oBtnSair := TButton():New(6, nJanLarg / 2 - 1 - 52 * 1, "Sair", oDlgCom, Nil, 50, 18, Nil, oFontBtn, Nil, lDimPixels)
            // Botões de navegação
            oBtnEsq := TButton():New(nJanAltu / 4, 3, "<-", oDlgCom, Nil, 30, 18, Nil, oFontBtn, Nil, lDimPixels)
            oBtnDir := TButton():New(nJanAltu / 4, nJanLarg / 2 - 3 - 30, "->", oDlgCom, Nil, 30, 18, Nil, oFontBtn, Nil, lDimPixels)
            // Get com a informação da imagem atual
            oGetImg := TGet():New(nJanAltu / 2 - 16, 3, Nil, oDlgCom, nJanLarg / 2 - 3, 13, Nil, Nil, Nil, Nil, oFontBtn, Nil, Nil, lDimPixels)
            oGetImg->lReadOnly := .T.
            // Imagem atual
            oBmpFoto := TBitmap():New(27, 24, nJanLarg / 2 - 42, nJanAltu / 2 - 48, Nil, Nil, Nil, oDlgCom, Nil, Nil, Nil, Nil, Nil, Nil, Nil, Nil, lDimPixels, Nil, Nil)
            oBmpFoto->lStretch := .T.
            oBmpFoto:Load(Nil, cGetImg)
            oBmpFoto:Refresh()
            // Ativa e exibe a janela
            oDlgCom:Activate(Nil, Nil, Nil, lCentraliz, Nil, Nil, bBlocoIni)
        Else
            FWAlertError("Não foi encontrado imagens nesse diretório!", "Atenção")
        EndIf
    Else
        FWAlertError("Diretório não existe ou inválido!", "Atenção")
    EndIf
    RestArea(aArea)
    RETURN Static

FUNCTION fBuscaImg(oSay)
    LOCAL aExtensoes, nExtAtu, aFiles, cCamFull, nFileAtu

    aExtensoes := { "jpg", "png", "bmp" }
    nExtAtu := Nil
    aFiles := Nil
    cCamFull := Nil
    nFileAtu := Nil
    // Percorrendo as extensoes
    RETURN Static

FUNCTION fChangeImg(nNewPos)
    LOCAL nImgAtu, cGetImg

    // Decrementa uma imagem
    If nNewPos = - 1
        nImgAtu -= 1
        // Incrementa uma imagem
    ElseIf nNewPos = 1
        nImgAtu += 1
    EndIf
    // Se a imagem atual passou da ultima, vai para a primeira
    If nImgAtu > Len(aImgs)
        nImgAtu := 1
        // Se for menor ou igual a zero, vai para a última
    ElseIf nImgAtu <= 0
        nImgAtu := Len(aImgs)
    EndIf
    // Atualiza o get
    cGetImg := cDirect + aImgs[nImgAtu]
    oGetImg:Refresh()
    // Atualiza a imagem
    oBmpFoto:Load(Nil, cGetImg)
    oBmpFoto:Refresh()
    RETURN
