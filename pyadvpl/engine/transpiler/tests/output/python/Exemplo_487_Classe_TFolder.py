# Esse exemplo faz parte da série do YouTube, Maratona de Exemplos, do canal Terminal de Informação, 
#     caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2024/06/19/criando-telas-com-a-tdialog-maratona-advpl-e-tl-486/
# Bibliotecas
# PREPROCESSOR: #Include "TOTVS.ch"
# {Protheus.doc} User Function zExe487
# Classe para criar abas dentro de uma Dialog
# @type Function
# @author Atilio
# @since 04/04/2023
# @see https://tdn.totvs.com/display/tec/TFolder
# @obs 
# 
#     **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
def u_zExe487():
    aArea = FWGetArea()
    nCorFundo = RGB(238, 238, 238)
    nJanAltura = 248
    nJanLargur = 655
    cJanTitulo = 'Exemplo TFolder'
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
    cBtnObj0 = 'Confirmar'
    bBtnObj0 = lambda : MsgInfo('Primeira Aba (Campo A): ' + xGetObj2A + ', Segunda Aba (Campo B): ' + xGetObj2B + ', Terceira Aba (Campo C): ' + xGetObj2C, 'Atencao objeto0')
    # objeto1
    oSayObj1A = None
    cSayObj1A = 'Campo A:'
    # objeto2
    oGetObj2A = None
    xGetObj2A = Space(10)
    # Se o get for data para inicilizar use dToS(''), se for numerico inicie com 0
    # objeto1
    oSayObj1B = None
    cSayObj1B = 'Campo B:'
    # objeto2
    oGetObj2B = None
    xGetObj2B = Space(10)
    # Se o get for data para inicilizar use dToS(''), se for numerico inicie com 0
    # objeto1
    oSayObj1C = None
    cSayObj1C = 'Campo C:'
    # objeto2
    oGetObj2C = None
    xGetObj2C = Space(10)
    # Se o get for data para inicilizar use dToS(''), se for numerico inicie com 0
    # Abas
    oFolder = None
    aAbas = ['Cadastro', 'Complemento', 'Outros']
    # Cria a dialog
    oDialogPvt = TDialog().New(0, 0, nJanAltura, nJanLargur, cJanTitulo, None, None, None, None, None, nCorFundo, None, None, lDimPixels)
    # objeto0 - usando a classe TButton
    nObjLinha = 106
    nObjColun = 5
    nObjLargu = 75
    nObjAltur = 15
    oBtnObj0 = TButton().New(nObjLinha, nObjColun, cBtnObj0, oDialogPvt, bBtnObj0, nObjLargu, nObjAltur, None, oFontPadrao, None, lDimPixels)
    # Cria as abas
    oFolder = TFolder().New(1, 1, aAbas, None, oDialogPvt, None, None, None, lDimPixels, None, nJanLargur / 2 - 1, nJanAltura / 2 - 30)
    # Aba 1
    # objeto1 - usando a classe TSay
    nObjLinha = 7
    nObjColun = 2
    nObjLargu = 28
    nObjAltur = 6
    oSayObj1A = TSay().New(nObjLinha, nObjColun, lambda : cSayObj1A, oFolder.aDialogs()[1], None, oFontPadrao, None, None, None, lDimPixels, None, None, nObjLargu, nObjAltur, None, None, None, None, None)
    # objeto2 - usando a classe TGet
    nObjLinha = 5
    nObjColun = 37
    nObjLargu = 50
    nObjAltur = 10
    oGetObj2A = TGet().New(nObjLinha, nObjColun, lambda u: ((xGetObj2A := u) if PCount() > 0 else xGetObj2A), oFolder.aDialogs()[1], nObjLargu, nObjAltur, None, None, None, None, oFontPadrao, None, None, lDimPixels)
    oGetObj2A.Picture = '@!'
    # Mascara / Picture do campo
    # Aba 2
    # objeto1 - usando a classe TSay
    nObjLinha = 7
    nObjColun = 2
    nObjLargu = 28
    nObjAltur = 6
    oSayObj1B = TSay().New(nObjLinha, nObjColun, lambda : cSayObj1B, oFolder.aDialogs()[2], None, oFontPadrao, None, None, None, lDimPixels, None, None, nObjLargu, nObjAltur, None, None, None, None, None)
    # objeto2 - usando a classe TGet
    nObjLinha = 5
    nObjColun = 37
    nObjLargu = 100
    nObjAltur = 10
    oGetObj2B = TGet().New(nObjLinha, nObjColun, lambda u: ((xGetObj2B := u) if PCount() > 0 else xGetObj2B), oFolder.aDialogs()[2], nObjLargu, nObjAltur, None, None, None, None, oFontPadrao, None, None, lDimPixels)
    oGetObj2B.Picture = '@!'
    # Mascara / Picture do campo
    # Aba 3
    # objeto1 - usando a classe TSay
    nObjLinha = 7
    nObjColun = 2
    nObjLargu = 28
    nObjAltur = 6
    oSayObj1C = TSay().New(nObjLinha, nObjColun, lambda : cSayObj1C, oFolder.aDialogs()[3], None, oFontPadrao, None, None, None, lDimPixels, None, None, nObjLargu, nObjAltur, None, None, None, None, None)
    # objeto2 - usando a classe TGet
    nObjLinha = 5
    nObjColun = 37
    nObjLargu = 150
    nObjAltur = 10
    oGetObj2C = TGet().New(nObjLinha, nObjColun, lambda u: ((xGetObj2C := u) if PCount() > 0 else xGetObj2C), oFolder.aDialogs()[3], nObjLargu, nObjAltur, None, None, None, None, oFontPadrao, None, None, lDimPixels)
    oGetObj2C.Picture = '@!'
    # Mascara / Picture do campo
    # Ativa e exibe a janela
    oDialogPvt.Activate(None, None, None, lCentraliz, None, None, bBlocoIni)
    FWRestArea(aArea)
    return
