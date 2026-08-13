# Esse exemplo faz parte da série do YouTube, Maratona de Exemplos, do canal Terminal de Informação, 
#     caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2024/06/11/criando-um-pincel-para-pintar-um-fundo-de-relatorio-com-tbrush-maratona-advpl-e-tl-471/
# Bibliotecas
# PREPROCESSOR: #Include "TOTVS.ch"
# {Protheus.doc} User Function zExe470
# Classe para exibir imagens em Dialogs no Protheus
# @type Function
# @author Atilio
# @since 02/04/2023
# @see https://tdn.totvs.com/display/tec/TBitmap
# @obs 
# 
#     Esse artigo foi baseado na função zSlider disponível em - https://terminaldeinformacao.com/2020/08/28/como-fazer-um-slideshow-em-advpl/
# 
#     **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
def u_zExe470():
    aArea = GetArea()
    lDimPixels = True
    lCentraliz = True
    bBlocoIni = lambda : None
    # Fontes
    cFontUti = 'Tahoma'
    oFontAno = TFont().New(cFontUti, None, -38)
    oFontSub = TFont().New(cFontUti, None, -20)
    oFontSubN = TFont().New(cFontUti, None, -20, None, True)
    oFontBtn = TFont().New(cFontUti, None, -14)
    Default
    cDirFiles = 'C:\\Users\\danat\\OneDrive\\Trabalho\\Atilio Sistemas\\Workspace_VS\\Local\\Cursos\\Curso_OO\\imgs\\'
    cDirect = Alltrim(cDirFiles)
    aImgs = []
    nImgAtu = 0
    # Janela e componentes
    oDlgCom = None
    oGetImg = None
    cGetImg = ''
    oBmpFoto = None
    # Tamanho da janela
    nJanLarg = 800
    nJanAltu = 600
    # Somente se tiver imagens a exibir
    if not Empty(cDirect) and ExistDir(cDirect):
        # Tratativa para adicionar uma barra no final
        if SubStr(cDirect, Len(cDirect), 1) != '\\':
            cDirect += '\\'

        # Carregando as imagens
        FWMsgRun(None, lambda oSay: fBuscaImg(oSay), 'Processando', 'Buscando imagens da pasta')
        # Se tiver imagens
        if Len(aImgs) > 0:
            nImgAtu = 1
            cGetImg = cDirect + aImgs[nImgAtu]
            # Criando a janela
            oDlgCom = TDialog().New(0, 0, nJanAltu, nJanLarg, 'Slideshow', None, None, None, None, None, None, None, None, lDimPixels)
            # Labels gerais
            oSayModulo = TSay().New(4, 3, lambda : 'TI', oDlgCom, '', oFontAno, None, None, None, True, RGB(149, 179, 215), None, 200, 30, None, None, None, None, None, False, None)
            oSayTitulo = TSay().New(4, 45, lambda : 'Exemplo de Slideshow', oDlgCom, '', oFontSub, None, None, None, True, RGB(31, 73, 125), None, 200, 30, None, None, None, None, None, False, None)
            oSaySubTit = TSay().New(14, 45, lambda : cValToChar(Len(aImgs)) + ' imagens encontradas', oDlgCom, '', oFontSubN, None, None, None, True, RGB(31, 73, 125), None, 300, 30, None, None, None, None, None, False, None)
            # Botão de Sair
            oBtnSair = TButton().New(6, nJanLarg / 2 - 1 - 52 * 1, 'Sair', oDlgCom, lambda : oDlgCom.End(), 50, 18, None, oFontBtn, None, lDimPixels)
            # Botões de navegação
            oBtnEsq = TButton().New(nJanAltu / 4, 3, '<-', oDlgCom, lambda : fChangeImg(-1), 30, 18, None, oFontBtn, None, lDimPixels)
            oBtnDir = TButton().New(nJanAltu / 4, nJanLarg / 2 - 3 - 30, '->', oDlgCom, lambda : fChangeImg(1), 30, 18, None, oFontBtn, None, lDimPixels)
            # Get com a informação da imagem atual
            oGetImg = TGet().New(nJanAltu / 2 - 16, 3, lambda u: ((cGetImg := u) if PCount() > 0 else cGetImg), oDlgCom, nJanLarg / 2 - 3, 13, None, None, None, None, oFontBtn, None, None, lDimPixels)
            oGetImg.lReadOnly = True
            # Imagem atual
            oBmpFoto = TBitmap().New(27, 24, nJanLarg / 2 - 42, nJanAltu / 2 - 48, None, None, None, oDlgCom, None, None, None, None, None, None, None, None, lDimPixels, None, None)
            oBmpFoto.lStretch = True
            oBmpFoto.Load(None, cGetImg)
            oBmpFoto.Refresh()
            # Ativa e exibe a janela
            oDlgCom.Activate(None, None, None, lCentraliz, None, None, bBlocoIni)
        else:
            FWAlertError('Não foi encontrado imagens nesse diretório!', 'Atenção')

    else:
        FWAlertError('Diretório não existe ou inválido!', 'Atenção')

    RestArea(aArea)
    return Static

def fBuscaImg(oSay):
    aExtensoes = ['jpg', 'png', 'bmp']
    nExtAtu = None
    aFiles = None
    cCamFull = None
    nFileAtu = None
    # Percorrendo as extensoes
    return Static

def fChangeImg(nNewPos):
    # Decrementa uma imagem
    if nNewPos == -1:
        nImgAtu -= 1
        # Incrementa uma imagem
    elif nNewPos == 1:
        nImgAtu += 1

    # Se a imagem atual passou da ultima, vai para a primeira
    if nImgAtu > Len(aImgs):
        nImgAtu = 1
        # Se for menor ou igual a zero, vai para a última
    elif nImgAtu <= 0:
        nImgAtu = Len(aImgs)

    # Atualiza o get
    cGetImg = cDirect + aImgs[nImgAtu]
    oGetImg.Refresh()
    # Atualiza a imagem
    oBmpFoto.Load(None, cGetImg)
    oBmpFoto.Refresh()
    return
