# Esse exemplo faz parte da série do YouTube, Maratona de Exemplos, do canal Terminal de Informação, 
#     caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2024/02/17/gerando-um-qrcode-atraves-da-classe-fwqrcode-maratona-advpl-e-tl-241/
# Bibliotecas
# PREPROCESSOR: #Include 'TOTVS.ch'
# {Protheus.doc} User Function zExe241
# Função que gera um QRCode em tela
# @type Function
# @author Atilio
# @since 20/02/2023
# @see https://tdn.totvs.com/display/public/framework/FwQrCode
# @obs 
# 
#     **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
def u_zExe241():
    aArea = FWGetArea()
    nCorFundo = RGB(238, 238, 238)
    nJanAltura = 281
    nJanLargur = 358
    cJanTitulo = 'Exemplo FWQrCode'
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
    # objeto1
    oSayInsira = None
    cSayInsira = 'Insira o Texto:'
    # objeto2
    oGetTexto = None
    cGetTexto = 'https://terminaldeinformacao.com' + Space(200)
    # objeto 3
    oQrCode = None
    # objeto4
    oBtnObj8 = None
    cBtnObj8 = 'Confirmar'
    bBtnObj8 = lambda : fAtualiza()
    # Cria a dialog
    oDialogPvt = TDialog().New(0, 0, nJanAltura, nJanLargur, cJanTitulo, None, None, None, None, None, nCorFundo, None, None, lDimPixels)
    # objeto1 - usando a classe TSay
    nObjLinha = 4
    nObjColun = 4
    nObjLargu = 70
    nObjAltur = 6
    oSayInsira = TSay().New(nObjLinha, nObjColun, lambda : cSayInsira, oDialogPvt, None, oFontPadrao, None, None, None, lDimPixels, None, None, nObjLargu, nObjAltur, None, None, None, None, None)
    # objeto2 - usando a classe TGet
    nObjLinha = 3
    nObjColun = 64
    nObjLargu = 110
    nObjAltur = 10
    oGetTexto = TGet().New(nObjLinha, nObjColun, lambda u: ((cGetTexto := u) if PCount() > 0 else cGetTexto), oDialogPvt, nObjLargu, nObjAltur, None, None, None, None, oFontPadrao, None, None, lDimPixels)
    # objeto3 - usando a classe FWQRCode
    nObjLinha = 19
    nObjColun = 44
    nObjLargu = 180
    nObjAltur = 180
    oQrCode = FwQrCode().New([nObjLinha, nObjColun, nObjLargu, nObjAltur], oDialogPvt, cGetTexto)
    # objeto4 - usando a classe TButton
    nObjLinha = 116
    nObjColun = 2
    nObjLargu = nJanLargur / 2 - 2
    nObjAltur = 15
    oBtnObj8 = TButton().New(nObjLinha, nObjColun, cBtnObj8, oDialogPvt, bBtnObj8, nObjLargu, nObjAltur, None, oFontPadrao, None, lDimPixels)
    # Ativa e exibe a janela
    oDialogPvt.Activate(None, None, None, lCentraliz, None, None, bBlocoIni)
    FWRestArea(aArea)
    return Static

def fAtualiza():
    # Somente se houver texto, irá atualizar na tela
    if not Empty(cGetTexto):
        oQrCode.SetCodeBar(cGetTexto)
        oQrCode.Refresh()

    return
