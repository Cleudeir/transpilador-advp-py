# Esse exemplo faz parte da série do YouTube, Maratona de Exemplos, do canal Terminal de Informação, 
#     caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2024/06/20/criando-campos-em-tela-com-tget-maratona-advpl-e-tl-489/
# Bibliotecas
# PREPROCESSOR: #Include "TOTVS.ch"
# {Protheus.doc} User Function zExe488
# Classe para modificar as fontes de um objeto instanciado
# @type Function
# @author Atilio
# @since 04/04/2023
# @see https://tdn.totvs.com/display/tec/TFont
# @obs 
# 
#     **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
def u_zExe488():
    aArea = FWGetArea()
    nCorFundo = RGB(238, 238, 238)
    nJanAltura = 222
    nJanLargur = 404
    cJanTitulo = 'Exemplo TFont'
    lDimPixels = True
    lCentraliz = True
    nObjLinha = 0
    nObjColun = 0
    nObjLargu = 0
    nObjAltur = 0
    oDialogPvt = None
    bBlocoIni = lambda : None
    # Aqui voce pode acionar funcoes customizadas que irao ser acionadas ao abrir a dialog
    # objeto0
    oSayObj0 = None
    cSayObj0 = 'Tahoma, -12, Normal'
    oFontPad = TFont().New('Tahoma', None, -12)
    # objeto1
    oSayObj1 = None
    cSayObj1 = 'Tahoma, -12, Negrito'
    oFontNeg = TFont().New('Tahoma', None, -12, None, True)
    # objeto2
    oSayObj2 = None
    cSayObj2 = 'Tahoma, -14, Sublinhado'
    oFontSub = TFont().New('Tahoma', None, -14, None, False, None, None, None, None, True)
    # objeto3
    oSayObj3 = None
    cSayObj3 = 'Tahoma, -16, Itálico'
    oFontIta = TFont().New('Tahoma', None, -16, None, False, None, None, None, None, False, True)
    # objeto4
    oSayObj4 = None
    cSayObj4 = 'Arial, -10, Tudo'
    oFontTudo = TFont().New('Arial', None, -10, None, True, None, None, None, None, True, True)
    # Cria a dialog
    oDialogPvt = TDialog().New(0, 0, nJanAltura, nJanLargur, cJanTitulo, None, None, None, None, None, nCorFundo, None, None, lDimPixels)
    # objeto0 - usando a classe TSay
    nObjLinha = 9
    nObjColun = 7
    nObjLargu = 200
    nObjAltur = 20
    oSayObj0 = TSay().New(nObjLinha, nObjColun, lambda : cSayObj0, oDialogPvt, None, oFontPad, None, None, None, lDimPixels, None, None, nObjLargu, nObjAltur, None, None, None, None, None)
    # objeto1 - usando a classe TSay
    nObjLinha = 29
    nObjColun = 7
    nObjLargu = 200
    nObjAltur = 20
    oSayObj1 = TSay().New(nObjLinha, nObjColun, lambda : cSayObj1, oDialogPvt, None, oFontNeg, None, None, None, lDimPixels, None, None, nObjLargu, nObjAltur, None, None, None, None, None)
    # objeto2 - usando a classe TSay
    nObjLinha = 49
    nObjColun = 7
    nObjLargu = 200
    nObjAltur = 20
    oSayObj2 = TSay().New(nObjLinha, nObjColun, lambda : cSayObj2, oDialogPvt, None, oFontSub, None, None, None, lDimPixels, None, None, nObjLargu, nObjAltur, None, None, None, None, None)
    # objeto3 - usando a classe TSay
    nObjLinha = 69
    nObjColun = 7
    nObjLargu = 200
    nObjAltur = 20
    oSayObj3 = TSay().New(nObjLinha, nObjColun, lambda : cSayObj3, oDialogPvt, None, oFontIta, None, None, None, lDimPixels, None, None, nObjLargu, nObjAltur, None, None, None, None, None)
    # objeto4 - usando a classe TSay
    nObjLinha = 89
    nObjColun = 7
    nObjLargu = 200
    nObjAltur = 20
    oSayObj4 = TSay().New(nObjLinha, nObjColun, lambda : cSayObj4, oDialogPvt, None, oFontTudo, None, None, None, lDimPixels, None, None, nObjLargu, nObjAltur, None, None, None, None, None)
    # Ativa e exibe a janela
    oDialogPvt.Activate(None, None, None, lCentraliz, None, None, bBlocoIni)
    FWRestArea(aArea)
    return
