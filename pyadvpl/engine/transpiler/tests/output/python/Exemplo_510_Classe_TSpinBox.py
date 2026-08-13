# Esse exemplo faz parte da série do YouTube, Maratona de Exemplos, do canal Terminal de Informação, 
#     caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2024/07/01/criando-um-icone-na-bandeja-do-s-o-com-tsystemtray-maratona-advpl-e-tl-511/
# Bibliotecas
# PREPROCESSOR: #Include "TOTVS.ch"
# {Protheus.doc} User Function zExe510
# Cria uma caixa de texto com botões ao lado de manipulação
# @type Function
# @author Atilio
# @since 04/04/2023
# @see https://tdn.totvs.com/display/tec/TSpinBox
# @obs 
# 
#     **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
def u_zExe510():
    aArea = FWGetArea()
    nCorFundo = RGB(238, 238, 238)
    nJanAltura = 154
    nJanLargur = 318
    cJanTitulo = 'Exemplo TSpinBox'
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
    oSpinBox = None
    nSpinBox = 10
    # objeto1
    oBtnObj1 = None
    cBtnObj1 = 'Confirmar'
    bBtnObj1 = lambda : MsgInfo('O valor é:' + CRLF + CRLF + cValToChar(nSpinBox), 'Atenção')
    # Cria a dialog
    oDialogPvt = TDialog().New(0, 0, nJanAltura, nJanLargur, cJanTitulo, None, None, None, None, None, nCorFundo, None, None, lDimPixels)
    # objeto0 - usando a classe TSpinBox
    nObjLinha = 7
    nObjColun = 6
    nObjLargu = 145
    nObjAltur = 15
    oSpinBox = TSpinBox().New(nObjLinha, nObjColun, oDialogPvt, lambda x: (nSpinBox := x), nObjLargu, nObjAltur)
    oSpinBox.setRange(-30, 30)
    oSpinBox.setStep(5)
    oSpinBox.setValue(nSpinBox)
    # objeto1 - usando a classe TButton
    nObjLinha = 54
    nObjColun = 6
    nObjLargu = 75
    nObjAltur = 15
    oBtnObj1 = TButton().New(nObjLinha, nObjColun, cBtnObj1, oDialogPvt, bBtnObj1, nObjLargu, nObjAltur, None, oFontPadrao, None, lDimPixels)
    # Ativa e exibe a janela
    oDialogPvt.Activate(None, None, None, lCentraliz, None, None, bBlocoIni)
    FWRestArea(aArea)
    return
