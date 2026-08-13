# Esse exemplo faz parte da série do YouTube, Maratona de Exemplos, do canal Terminal de Informação, 
#     caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2024/03/01/buscando-a-classe-de-um-objeto-com-a-getclassname-maratona-advpl-e-tl-266/
# Bibliotecas
# PREPROCESSOR: #Include "TOTVS.ch"
# {Protheus.doc} User Function zExe266
# Retorna o nome da classe de um objeto
# @type  Function
# @author Atilio
# @since 21/02/2023
# @see https://tdn.totvs.com/display/tec/GetClassName
# @obs 
# 
#     Função GetClassName
#     Parâmetros
#         + oObjeto        , Objeto           , Variável com o objeto instanciado de uma classe
#     Retorno
#         + cClassName     , Caractere        , Nome da classe usada no Objeto
#     
#     **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
def u_zExe266():
    aArea = FWGetArea()
    nCorFundo = RGB(238, 238, 238)
    nJanAltura = 281
    nJanLargur = 358
    cJanTitulo = 'Exemplo GetClassName'
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
    nObjAltur = 6
    oSayInsira = TSay().New(nObjLinha, nObjColun, lambda : cSayInsira, oDialogPvt, None, oFontPadrao, None, None, None, lDimPixels, None, None, nObjLargu, nObjAltur, None, None, None, None, None)
    # objeto2 - usando a classe TGet
    nObjLinha = 3
    nObjColun = 64
    nObjLargu = 110
    nObjAltur = 10
    oGetTexto = TGet().New(nObjLinha, nObjColun, lambda u: ((cGetTexto := u) if PCount() > 0 else cGetTexto), oDialogPvt, nObjLargu, nObjAltur, None, None, None, None, oFontPadrao, None, None, lDimPixels)
    # objeto4 - usando a classe TButton
    nObjLinha = 116
    nObjColun = 2
    nObjLargu = nJanLargur / 2 - 2
    nObjAltur = 15
    oBtnConf = TButton().New(nObjLinha, nObjColun, cBtnObj8, oDialogPvt, bBtnObj8, nObjLargu, nObjAltur, None, oFontPadrao, None, lDimPixels)
    # Ativa e exibe a janela
    oDialogPvt.Activate(None, None, None, lCentraliz, None, None, bBlocoIni)
    FWRestArea(aArea)
    return Static

def fConfirma():
    cMensagem = ''
    # Busca a classe dos objetos em tela
    cMensagem += 'oDialogPvt: ' + GetClassName(oDialogPvt) + CRLF
    cMensagem += 'oSayInsira: ' + GetClassName(oSayInsira) + CRLF
    cMensagem += 'oGetTexto: ' + GetClassName(oGetTexto) + CRLF
    cMensagem += 'oBtnConf: ' + GetClassName(oBtnConf)
    FWAlertInfo(cMensagem, 'Teste GetClassName')
    return
