# Esse exemplo faz parte da série do YouTube, Maratona de Exemplos, do canal Terminal de Informação, 
#     caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2024/05/19/buscando-um-tom-de-cor-atraves-da-rgb-maratona-advpl-e-tl-424/
# Bibliotecas
# PREPROCESSOR: #Include "TOTVS.ch"
# {Protheus.doc} User Function zExe424
# Retorna uma cor para ser usada em AdvPL conforme o padrão RGB (Red, Green e Blue)
# @type Function
# @author Atilio
# @since 29/03/2023
# @see https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022454272-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Tabela-de-cores-MSDIALOG
# @obs 
#     Função RGB
#     Parâmetros
#         Recebe o tom em Vermelho (0 a 255)
#         Recebe o tom em Verde (0 a 255)
#         Recebe o tom em Azul (0 a 255)
#     Retorno
#         Retorna a cor em AdvPL para ser utilizada
# 
#     **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
def u_zExe424():
    aArea = FWGetArea()
    nCorUsada = 0
    nJanAltura = 281
    nJanLargur = 358
    cJanTitulo = 'Exemplo RGB'
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
    bBtnObj8 = lambda : FWAlertInfo('Em construção...', 'Teste RGB')
    # Definindo a cor de fundo como um Magenta ou Rosa meio claro
    nCorUsada = RGB(230, 10, 230)
    # Cria a dialog
    oDialogPvt = TDialog().New(0, 0, nJanAltura, nJanLargur, cJanTitulo, None, None, None, None, None, nCorUsada, None, None, lDimPixels)
    # objeto1 - usando a classe TSay
    nObjLinha = 4
    nObjColun = 4
    nObjLargu = 70
    nObjAltur = 12
    oSayInsira = TSay().New(nObjLinha, nObjColun, lambda : cSayInsira, oDialogPvt, None, oFontPadrao, None, None, None, lDimPixels, None, None, nObjLargu, nObjAltur, None, None, None, None, None)
    # objeto2 - usando a classe TGet
    nObjLinha = 3
    nObjColun = 64
    nObjLargu = 110
    nObjAltur = 15
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
    return
