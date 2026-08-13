# Esse exemplo faz parte da série do YouTube, Maratona de Exemplos, do canal Terminal de Informação, 
#     caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2024/06/29/realizando-tratativas-com-try-catch-maratona-advpl-e-tl-506/
# Bibliotecas
# PREPROCESSOR: #Include "TOTVS.ch"
# {Protheus.doc} User Function zExe507
# Cria labels de texto dentro de uma dialog
# @type Function
# @author Atilio
# @since 04/04/2023
# @see https://tdn.totvs.com/display/tec/TSay
# @obs 
# 
#     **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
def u_zExe507():
    aArea = FWGetArea()
    nCorFundo = RGB(238, 238, 238)
    nJanAltura = 222
    nJanLargur = 404
    cJanTitulo = 'Exemplo TSay'
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
    oSayObj0 = None
    cSayObj0 = 'Label comum'
    # objeto1
    oSayObj1 = None
    cSayObj1 = '<h3>Label html - <font color="blue">teste</font></h3>'
    # objeto2
    oSayObj2 = None
    cSayObj2 = 'Label com cores'
    # objeto3
    oSayObj3 = None
    cSayObj3 = 'Label com CSS'
    # objeto4
    oSayObj4 = None
    cSayObj4 = 'Label com clique'
    # Cria a dialog
    oDialogPvt = TDialog().New(0, 0, nJanAltura, nJanLargur, cJanTitulo, None, None, None, None, None, nCorFundo, None, None, lDimPixels)
    # objeto0 - usando a classe TSay
    nObjLinha = 9
    nObjColun = 7
    nObjLargu = 180
    nObjAltur = 15
    oSayObj0 = TSay().New(nObjLinha, nObjColun, lambda : cSayObj0, oDialogPvt, None, oFontPadrao, None, None, None, lDimPixels, None, None, nObjLargu, nObjAltur, None, None, None, None, None)
    # objeto1 - usando a classe TSay
    nObjLinha = 29
    nObjColun = 7
    nObjLargu = 180
    nObjAltur = 15
    oSayObj1 = TSay().New(nObjLinha, nObjColun, lambda : cSayObj1, oDialogPvt, None, oFontPadrao, None, None, None, lDimPixels, None, None, nObjLargu, nObjAltur, None, None, None, None, None, True)
    # objeto2 - usando a classe TSay
    nObjLinha = 49
    nObjColun = 7
    nObjLargu = 180
    nObjAltur = 15
    oSayObj2 = TSay().New(nObjLinha, nObjColun, lambda : cSayObj2, oDialogPvt, None, oFontPadrao, None, None, None, lDimPixels, RGB(255, 0, 0), None, nObjLargu, nObjAltur, None, None, None, None, None)
    # objeto3 - usando a classe TSay
    nObjLinha = 69
    nObjColun = 7
    nObjLargu = 180
    nObjAltur = 15
    oSayObj3 = TSay().New(nObjLinha, nObjColun, lambda : cSayObj3, oDialogPvt, None, oFontPadrao, None, None, None, lDimPixels, None, None, nObjLargu, nObjAltur, None, None, None, None, None)
    oSayObj3.SetCSS('background-color: #FF0000; color: #0D0D0D}')
    # objeto4 - usando a classe TSay
    nObjLinha = 89
    nObjColun = 7
    nObjLargu = 180
    nObjAltur = 15
    oSayObj4 = TSay().New(nObjLinha, nObjColun, lambda : cSayObj4, oDialogPvt, None, oFontPadrao, None, None, None, lDimPixels, None, None, nObjLargu, nObjAltur, None, None, None, None, None)
    oSayObj4.bLClicked = lambda : FWAlertInfo('Clique com o botão esquerdo do Mouse', 'bLClicked')
    oSayObj4.bRClicked = lambda : FWAlertInfo('Clique com o botão direito do Mouse', 'bRClicked')
    # oSayObj4:bLDblClick := {|| FWAlertInfo("Duplo clique com o botão esquerdo do Mouse", "bLDblClick")}
    # Ativa e exibe a janela
    oDialogPvt.Activate(None, None, None, lCentraliz, None, None, bBlocoIni)
    FWRestArea(aArea)
    return
