# Esse exemplo faz parte da série do YouTube, Maratona de Exemplos, do canal Terminal de Informação, 
#     caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2024/06/13/preparando-a-execucao-de-uma-query-atraves-das-tcgenqry-e-tcgenqry2-maratona-advpl-e-tl-474/
# Bibliotecas
# PREPROCESSOR: #Include "TOTVS.ch"
# {Protheus.doc} User Function zExe475
# Classe para criar checkbox em uma Dialog
# @type Function
# @author Atilio
# @since 03/04/2023
# @see https://tdn.totvs.com/display/tec/TCheckBox
# @obs 
# 
#     **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
def u_zExe475():
    aArea = FWGetArea()
    nCorFundo = RGB(238, 238, 238)
    nJanAltura = 187
    nJanLargur = 253
    cJanTitulo = 'Exemplo TCheckBox'
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
    oChkObj0 = None
    lChkObj0 = False
    cChkObj0 = 'CheckBox vindo desmarcado'
    # objeto1
    oChkObj1 = None
    lChkObj1 = True
    cChkObj1 = 'CheckBox vindo marcado'
    # objeto2
    oChkObj2 = None
    lChkObj2 = True
    cChkObj2 = 'CheckBox desativado'
    # objeto3
    oBtnObj3 = None
    cBtnObj3 = 'Confirmar'
    bBtnObj3 = lambda : MsgInfo('Primeiro [' + cValToChar(lChkObj0) + '], Segundo [' + cValToChar(lChkObj1) + '], Terceiro [' + cValToChar(lChkObj2) + ']', 'Atencao')
    # Cria a dialog
    oDialogPvt = TDialog().New(0, 0, nJanAltura, nJanLargur, cJanTitulo, None, None, None, None, None, nCorFundo, None, None, lDimPixels)
    # objeto0 - usando a classe TCheckBox
    nObjLinha = 5
    nObjColun = 7
    nObjLargu = 110
    nObjAltur = 15
    oChkObj0 = TCheckBox().New(nObjLinha, nObjColun, cChkObj0, lambda u: ((lChkObj0 := u) if PCount() > 0 else lChkObj0), oDialogPvt, nObjLargu, nObjAltur, None, None, oFontPadrao, None, None, None, None, lDimPixels)
    # objeto1 - usando a classe TCheckBox
    nObjLinha = 25
    nObjColun = 7
    nObjLargu = 110
    nObjAltur = 15
    oChkObj1 = TCheckBox().New(nObjLinha, nObjColun, cChkObj1, lambda u: ((lChkObj1 := u) if PCount() > 0 else lChkObj1), oDialogPvt, nObjLargu, nObjAltur, None, None, oFontPadrao, None, None, None, None, lDimPixels)
    # objeto2 - usando a classe TCheckBox
    nObjLinha = 45
    nObjColun = 7
    nObjLargu = 110
    nObjAltur = 15
    oChkObj2 = TCheckBox().New(nObjLinha, nObjColun, cChkObj2, lambda u: ((lChkObj2 := u) if PCount() > 0 else lChkObj2), oDialogPvt, nObjLargu, nObjAltur, None, None, oFontPadrao, None, None, None, None, lDimPixels)
    oChkObj2.lActive = False
    # objeto3 - usando a classe TButton
    nObjLinha = 70
    nObjColun = 7
    nObjLargu = 110
    nObjAltur = 15
    oBtnObj3 = TButton().New(nObjLinha, nObjColun, cBtnObj3, oDialogPvt, bBtnObj3, nObjLargu, nObjAltur, None, oFontPadrao, None, lDimPixels)
    # Ativa e exibe a janela
    oDialogPvt.Activate(None, None, None, lCentraliz, None, None, bBlocoIni)
    FWRestArea(aArea)
    return
