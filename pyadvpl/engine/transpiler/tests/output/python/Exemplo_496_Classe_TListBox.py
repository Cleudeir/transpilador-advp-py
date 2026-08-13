# Esse exemplo faz parte da série do YouTube, Maratona de Exemplos, do canal Terminal de Informação, 
#     caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2024/06/24/criando-uma-listagem-de-informacoes-com-tlistbox-maratona-advpl-e-tl-496/
# Bibliotecas
# PREPROCESSOR: #Include "TOTVS.ch"
# {Protheus.doc} User Function zExe496
# Cria uma pequena grid em uma Dialog
# @type Function
# @author Atilio
# @since 04/04/2023
# @see https://tdn.totvs.com/display/tec/TListBox
# @obs 
# 
#     **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
def u_zExe496():
    aArea = FWGetArea()
    nCorFundo = RGB(238, 238, 238)
    nJanAltura = 228
    nJanLargur = 318
    cJanTitulo = 'Exemplo TListBox'
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
    oLisObj0 = None
    nLisObj0 = 0
    aLisObj0 = ['YouTube', 'Instagram', 'Twitter', 'Facebook', 'e-Mail']
    # objeto1
    oBtnObj1 = None
    cBtnObj1 = 'Confirmar'
    bBtnObj1 = lambda : MsgYesNo('Você nos segue via "' + aLisObj0[oLisObj0.nAt()] + '"?', 'Dúvida')
    # Cria a dialog
    oDialogPvt = TDialog().New(0, 0, nJanAltura, nJanLargur, cJanTitulo, None, None, None, None, None, nCorFundo, None, None, lDimPixels)
    # objeto0 - usando a classe TListBox
    nObjLinha = 6
    nObjColun = 8
    nObjLargu = 142
    nObjAltur = 80
    oLisObj0 = TListBox().New(nObjLinha, nObjColun, lambda u: ((nLisObj0 := u) if PCount() > 0 else nLisObj0), aLisObj0, nObjLargu, nObjAltur, None, oDialogPvt, None, None, None, lDimPixels, None, None, oFontPadrao)
    # objeto1 - usando a classe TButton
    nObjLinha = 95
    nObjColun = 8
    nObjLargu = 65
    nObjAltur = 15
    oBtnObj1 = TButton().New(nObjLinha, nObjColun, cBtnObj1, oDialogPvt, bBtnObj1, nObjLargu, nObjAltur, None, oFontPadrao, None, lDimPixels)
    # Ativa e exibe a janela
    oDialogPvt.Activate(None, None, None, lCentraliz, None, None, bBlocoIni)
    FWRestArea(aArea)
    return
