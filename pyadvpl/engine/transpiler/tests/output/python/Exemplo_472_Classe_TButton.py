# Esse exemplo faz parte da série do YouTube, Maratona de Exemplos, do canal Terminal de Informação, 
#     caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2024/06/12/buscando-qual-e-o-banco-utilizado-atraves-da-tcgetdb-maratona-advpl-e-tl-473/
# Bibliotecas
# PREPROCESSOR: #Include "TOTVS.ch"
# {Protheus.doc} User Function zExe472
# Classe para criar botões em uma Dialog
# @type Function
# @author Atilio
# @since 03/04/2023
# @see https://tdn.totvs.com/display/tec/TButton
# @obs 
# 
#     **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
def u_zExe472():
    aArea = FWGetArea()
    nCorFundo = RGB(238, 238, 238)
    nJanAltura = 129
    nJanLargur = 242
    cJanTitulo = 'Exemplo TButton'
    lDimPixels = True
    lCentraliz = True
    nObjLinha = 0
    nObjColun = 0
    nObjLargu = 0
    nObjAltur = 0
    cFontNome = 'Tahoma'
    oFontPadrao = TFont().New(cFontNome, None, -12)
    oDialogPvt = None
    bBlocoIni = lambda : None
    # Aqui voce pode acionar funcoes customizadas que irao ser acionadas ao abrir a dialog
    # objeto0
    oBtnObj0 = None
    cBtnObj0 = 'Botão Normal'
    bBtnObj0 = lambda : MsgInfo('Coloque sua funcao aqui', 'Atencao objeto0')
    # objeto1
    oBtnObj1 = None
    cBtnObj1 = 'Botão com CSS'
    bBtnObj1 = lambda : MsgInfo('Coloque sua funcao aqui', 'Atencao objeto1')
    # Cria a dialog
    oDialogPvt = TDialog().New(0, 0, nJanAltura, nJanLargur, cJanTitulo, None, None, None, None, None, nCorFundo, None, None, lDimPixels)
    # objeto0 - usando a classe TButton
    nObjLinha = 10
    nObjColun = 10
    nObjLargu = 100
    nObjAltur = 15
    oBtnObj0 = TButton().New(nObjLinha, nObjColun, cBtnObj0, oDialogPvt, bBtnObj0, nObjLargu, nObjAltur, None, oFontPadrao, None, lDimPixels)
    # objeto1 - usando a classe TButton
    nObjLinha = 35
    nObjColun = 10
    nObjLargu = 100
    nObjAltur = 15
    oBtnObj1 = TButton().New(nObjLinha, nObjColun, cBtnObj1, oDialogPvt, bBtnObj1, nObjLargu, nObjAltur, None, oFontPadrao, None, lDimPixels)
    oBtnObj1.SetCSS('TButton { font: bold;     background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,stop: 0 #3DAFCC, stop: 1 #0D9CBF);    color: #FFFFFF;     border-width: 1px;     border-style: solid;     border-radius: 3px;     border-color: #369CB5; }TButton:focus {    padding:0px; outline-width:1px; outline-style:solid; outline-color: #51DAFC; outline-radius:3px; border-color:#369CB5;}TButton:hover {    color: #FFFFFF;     background-color : qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,stop: 0 #3DAFCC, stop: 1 #1188A6);    border-width: 1px;     border-style: solid;     border-radius: 3px;     border-color: #369CB5; }TButton:pressed {    color: #FFF;     background-color : qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,stop: 0 #1188A6, stop: 1 #3DAFCC);    border-width: 1px;     border-style: solid;     border-radius: 3px;     border-color: #369CB5; }TButton:disabled {    color: #FFFFFF;     background-color: #4CA0B5; }')
    # Ativa e exibe a janela
    oDialogPvt.Activate(None, None, None, lCentraliz, None, None, bBlocoIni)
    FWRestArea(aArea)
    return
