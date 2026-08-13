# Esse exemplo faz parte da série do YouTube, Maratona de Exemplos, do canal Terminal de Informação, 
#     caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2024/06/26/abrindo-um-relatorio-atraves-da-tpageview-maratona-advpl-e-tl-500/
# Bibliotecas
# PREPROCESSOR: #Include "TOTVS.ch"
# {Protheus.doc} User Function zExe500
# Abre um relatório para visualização
# @type Function
# @author Atilio
# @since 04/04/2023
# @see https://tdn.totvs.com/display/tec/TPageView
# @obs 
# 
#     **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
def u_zExe500():
    aArea = FWGetArea()
    oDlgRelat = None
    cArqRelat = ''
    oPrinter = None
    oTPageView = None
    aTamanho = MsAdvSize()
    nJanLarg = aTamanho[5]
    nJanAltu = aTamanho[6]
    lCentered = True
    # Definindo o arquivo que será aberto
    cArqRelat = '\\spool\\matr680.prt'
    # Criando um objeto de impressão e setando o arquivo
    oPrinter = TMSPrinter().New()
    oPrinter.SetFile(cArqRelat, False)
    oPrinter.SetPortrait()
    oPrinter.SetPaperSize(9)
    # Criando a dialog
    oDlgRelat = TDialog().New(0, 0, nJanAltu, nJanLarg, 'Teste de TPageView', None, None, None, None, CLR_BLACK, RGB(250, 250, 250), None, None, True)
    # Criando o TPageView
    oTPageView = TPageView().New(0, 0, nJanLarg, nJanAltu, oPrinter, oDlgRelat, oPrinter.nPageWidth() + 200, oPrinter.nPageHeight())
    oTPageView.bLClicked = lambda : Iif(oTPageView.nZoom() < 200, (setattr(oTPageView, 'nZoom', getattr(oTPageView, 'nZoom') + 25) or getattr(oTPageView, 'nZoom')), None, None)
    oTPageView.bRClicked = lambda : Iif(oTPageView.nZoom() > 25, (setattr(oTPageView, 'nZoom', getattr(oTPageView, 'nZoom') - 25) or getattr(oTPageView, 'nZoom')), None, None)
    oTPageView.Align = CONTROL_ALIGN_ALLCLIENT
    oTPageView.nZoom = 150
    oDlgRelat.Activate(None, None, None, lCentered, lambda : True, None)
    FWRestArea(aArea)
    return
