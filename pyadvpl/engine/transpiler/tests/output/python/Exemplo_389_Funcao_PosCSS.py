# Esse exemplo faz parte da série do YouTube, Maratona de Exemplos, do canal Terminal de Informação, 
#     caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2024/05/01/executando-queries-com-a-plsquery-maratona-advpl-e-tl-388/
# Bibliotecas
# PREPROCESSOR: #Include "TOTVS.ch"
# PREPROCESSOR: #Include "POSCSS.ch"
# {Protheus.doc} User Function zExe389
# Retorna o estilo CSS de objetos instanciados
# @type  Function
# @author Atilio
# @since 28/03/2023
# @obs 
# 
#     Função PosCSS
#     Parâmetros
#         Nome da classe do objeto
#         Tipo do CSS buscado
#         Complementos do CSS para alguns casos
#     Retorno
#         Retorna o CSS encontrado
#     
#     **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
def u_zExe389():
    aArea = FWGetArea()
    nCorFundo = RGB(238, 238, 238)
    nJanAltura = 281
    nJanLargur = 358
    cJanTitulo = 'Exemplo PosCSS'
    lDimPixels = True
    lCentraliz = True
    nObjLinha = 0
    nObjColun = 0
    nObjLargu = 0
    nObjAltur = 0
    lPosCSS = FWAlertYesNo('Deseja utilizar o POSCSS?', 'Confirma?')
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
    # objeto4
    oBtnConf = None
    cBtnObj8 = 'Confirmar'
    bBtnObj8 = lambda : fConfirma()
    # Cria a dialog
    oDialogPvt = TDialog().New(0, 0, nJanAltura, nJanLargur, cJanTitulo, None, None, None, None, None, nCorFundo, None, None, lDimPixels)
    # objeto1 - usando a classe TSay
    nObjLinha = 4
    nObjColun = 4
    nObjLargu = 70
    nObjAltur = 12
    oSayInsira = TSay().New(nObjLinha, nObjColun, lambda : cSayInsira, oDialogPvt, None, oFontPadrao, None, None, None, lDimPixels, None, None, nObjLargu, nObjAltur, None, None, None, None, None)
    if lPosCSS:
        oSayInsira.SetCSS(PosCss(GetClassName(oSayInsira), CSS_LABEL_FOCAL, ['16', False]))

    # objeto2 - usando a classe TGet
    nObjLinha = 3
    nObjColun = 64
    nObjLargu = 110
    nObjAltur = 15
    oGetTexto = TGet().New(nObjLinha, nObjColun, lambda u: ((cGetTexto := u) if PCount() > 0 else cGetTexto), oDialogPvt, nObjLargu, nObjAltur, None, None, None, None, oFontPadrao, None, None, lDimPixels)
    if lPosCSS:
        oGetTexto.SetCSS(PosCss(GetClassName(oGetTexto), CSS_GET_FOCAL))

    # objeto4 - usando a classe TButton
    nObjLinha = 116
    nObjColun = 2
    nObjLargu = nJanLargur / 2 - 2
    nObjAltur = 15
    oBtnConf = TButton().New(nObjLinha, nObjColun, cBtnObj8, oDialogPvt, bBtnObj8, nObjLargu, nObjAltur, None, oFontPadrao, None, lDimPixels)
    if lPosCSS:
        oBtnConf.SetCSS(PosCss(GetClassName(oBtnConf), CSS_BTN_ATIVO))

    # Ativa e exibe a janela
    oDialogPvt.Activate(None, None, None, lCentraliz, None, None, bBlocoIni)
    FWRestArea(aArea)
    return Static

def fConfirma():
    cMensagem = 'teste'
    FWAlertInfo(cMensagem, 'Teste PosCSS')
    return
