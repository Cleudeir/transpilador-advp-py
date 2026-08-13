# Esse exemplo faz parte da série do YouTube, Maratona de Exemplos, do canal Terminal de Informação, 
#     caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2024/06/25/criando-um-campo-com-multiplas-linhas-atraves-da-tmultiget-maratona-advpl-e-tl-499/
# Bibliotecas
# PREPROCESSOR: #Include "TOTVS.ch"
# {Protheus.doc} User Function zExe499
# Cria uma caixa de texto grande para digitação / visualização
# @type Function
# @author Atilio
# @since 04/04/2023
# @see https://tdn.totvs.com/display/tec/TMultiGet
# @obs 
# 
#     **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
def u_zExe499():
    aArea = FWGetArea()
    nCorFundo = RGB(238, 238, 238)
    nJanAltura = 154
    nJanLargur = 318
    cJanTitulo = 'Exemplo TMultiGet'
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
    oMulObj0 = None
    cMulObj0 = ''
    # objeto1
    oBtnObj1 = None
    cBtnObj1 = 'Confirmar'
    bBtnObj1 = lambda : MsgInfo('O texto digitado foi:' + CRLF + CRLF + cMulObj0, 'Atenção')
    # Cria a dialog
    oDialogPvt = TDialog().New(0, 0, nJanAltura, nJanLargur, cJanTitulo, None, None, None, None, None, nCorFundo, None, None, lDimPixels)
    # objeto0 - usando a classe TMultiGet
    nObjLinha = 7
    nObjColun = 6
    nObjLargu = 145
    nObjAltur = 40
    oMulObj0 = TMultiGet().New(nObjLinha, nObjColun, lambda u: ((cMulObj0 := u) if PCount() > 0 else cMulObj0), oDialogPvt, nObjLargu, nObjAltur, oFontPadrao, None, None, None, None, lDimPixels, None, None, None, None, None, None, None, None, None, None, True)
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
