# Esse exemplo faz parte da série do YouTube, Maratona de Exemplos, do canal Terminal de Informação, 
#     caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2024/06/23/criando-um-teclado-virtual-com-tkeyboard-maratona-advpl-e-tl-495/
# Bibliotecas
# PREPROCESSOR: #Include "TOTVS.ch"
# {Protheus.doc} User Function zExe495
# Cria um teclado virtual em uma Dialog
# @type Function
# @author Atilio
# @since 04/04/2023
# @obs 
# 
#     **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
def u_zExe495():
    aArea = FWGetArea()
    nCorFundo = RGB(238, 238, 238)
    nJanAltura = 251
    nJanLargur = 470
    cJanTitulo = 'Exemplo TKeyboard'
    lDimPixels = True
    lCentraliz = True
    nObjLinha = 0
    nObjColun = 0
    nObjLargu = 0
    nObjAltur = 0
    nTamanText = 50
    cFontNome = 'Tahoma'
    oFontPadrao = TFont().New(cFontNome, None, -12)
    oDialogPvt = None
    bBlocoIni = lambda : None
    # Aqui voce pode acionar funcoes customizadas que irao ser acionadas ao abrir a dialog
    oGetTeste = None
    xGetTeste = Space(nTamanText)
    oKey = None
    # Cria a dialog
    oDialogPvt = TDialog().New(0, 0, nJanAltura, nJanLargur, cJanTitulo, None, None, None, None, None, nCorFundo, None, None, lDimPixels)
    # objeto1 - usando a classe TGet
    nObjLinha = 3
    nObjColun = 3
    nObjLargu = nJanLargur / 2 - 6
    nObjAltur = 10
    oGetTeste = TGet().New(nObjLinha, nObjColun, lambda u: ((xGetTeste := u) if PCount() > 0 else xGetTeste), oDialogPvt, nObjLargu, nObjAltur, None, None, None, None, oFontPadrao, None, None, lDimPixels)
    # Definindo que quando o get for clicado, será vinculado ao teclado virtual
    oGetTeste.bGotFocus = lambda : oKey.SetVars(oGetTeste, nTamanText)
    # Criando o teclado virtual
    nObjLinha = 19
    nObjColun = 3
    oKey = TKeyboard().New(nObjLinha, nObjColun, 2, oDialogPvt)
    # Definindo que ficará vinculado ao get criado anteriomente
    oKey.SetVars(oGetTeste, nTamanText)
    # Definindo uma ação ao clicar no -Enter-
    oKey.SetEnter(lambda : FWAlertInfo(oKey.GetContext(), 'Teste TKeyboard'))
    # Ativa e exibe a janela
    oDialogPvt.Activate(None, None, None, lCentraliz, None, None, bBlocoIni)
    FWRestArea(aArea)
    return
