# Esse exemplo faz parte da série do YouTube, Maratona de Exemplos, do canal Terminal de Informação, 
#     caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2024/06/19/criando-abas-tem-uma-tela-com-tfolder-maratona-advpl-e-tl-487/
# Bibliotecas
# PREPROCESSOR: #Include "TOTVS.ch"
# {Protheus.doc} User Function zExe486
# Classe para criar janelas
# @type Function
# @author Atilio
# @since 04/04/2023
# @see https://tdn.totvs.com/display/tec/TDialog
# @obs 
# 
#     **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
def u_zExe486():
    oDlgAux = None
    nJanAltu = 200
    nJanLarg = 400
    lDimPixels = True
    lCentraliz = True
    bBlocoIni = lambda : None
    cJanTitulo = 'Tela usando TDialog'
    # Cria a dialog
    oDlgAux = TDialog().New(0, 0, nJanAltu, nJanLarg, cJanTitulo, None, None, None, None, None, None, None, None, lDimPixels)
    # Ativa e exibe a janela
    oDlgAux.Activate(None, None, None, lCentraliz, None, None, bBlocoIni)
    return
