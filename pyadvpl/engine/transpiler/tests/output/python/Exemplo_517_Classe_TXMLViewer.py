# Esse exemplo faz parte da série do YouTube, Maratona de Exemplos, do canal Terminal de Informação, 
#     caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2024/07/04/expandindo-e-visualizando-um-xml-atraves-da-txmlviewer-maratona-advpl-e-tl-517/
# Bibliotecas
# PREPROCESSOR: #Include "TOTVS.ch"
# {Protheus.doc} User Function zExe517
# Realiza a abertura de um XML para ser navegável em uma Dialog
# @type  Function
# @author Atilio
# @since 05/04/2023
# @see https://tdn.totvs.com/display/tec/TXMLViewer
# @obs 
#     
#     **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
def u_zExe517():
    aArea = FWGetArea()
    nCorFundo = RGB(238, 238, 238)
    nJanAltura = 500
    nJanLargur = 500
    cJanTitulo = 'Exemplo TXMLViewer'
    cArquiXML = 'C:\\spool\\teste.xml'
    lDimPixels = True
    lCentraliz = True
    oXMLView = None
    oDialogPvt = None
    # Cria a dialog
    oDialogPvt = TDialog().New(0, 0, nJanAltura, nJanLargur, cJanTitulo, None, None, None, None, None, nCorFundo, None, None, lDimPixels)
    # Cria o visualizador do XML
    nObjLinha = 3
    nObjColun = 3
    nObjLargu = nJanLargur / 2 - 3
    nObjAltur = nJanAltura / 2 - 6
    oXMLView = TXMLViewer().New(nObjLinha, nObjColun, oDialogPvt, cArquiXML, nObjLargu, nObjAltur, lDimPixels)
    oXMLView.SetXML(cArquiXML)
    # Ativa e exibe a janela
    oDialogPvt.Activate(None, None, None, lCentraliz)
    FWRestArea(aArea)
    return
