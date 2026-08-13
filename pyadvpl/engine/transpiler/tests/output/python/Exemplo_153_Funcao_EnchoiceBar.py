# Esse exemplo faz parte da série do YouTube, Maratona de Exemplos, do canal Terminal de Informação, 
#     caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2024/01/04/validando-se-uma-expressao-esta-vazia-com-a-funcao-empty-maratona-advpl-e-tl-152/
# Bibliotecas
# PREPROCESSOR: #Include "TOTVS.ch"
# {Protheus.doc} User Function zExe153
# Cria uma barra na tela com botões como Confirmar, Cancelar e Outras Ações
# @type Function
# @author Atilio
# @since 18/12/2022
# @obs 
#     Função EnchoiceBar
#     Parâmetros
#         + Nome da Dialog que a EnchoiceBar será vinculada
#         + Ação ao clicar no botão Confirmar
#         + Ação ao clicar no botão Cancelar
#         + Se for .T. mostra uma mensagem de deseja realmente excluir
#         + Botões do Outras Ações
#         + Número do Recno que será posicionado da tabela
#         + Tabela de onde esta sendo feito as operações
#         + Ativa a função Mashups no Outras Ações
#     Retorno
#         Função não tem retorno
# 
#     **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
def u_zExe153():
    aArea = FWGetArea()
    nJanAltu = 200
    nJanLarg = 600
    lDimPixels = True
    lCentraliz = True
    bBlocoOk = lambda : [(lOk := True), oDlgAux.End()]
    bBlocoCan = lambda : [(lOk := False), oDlgAux.End()]
    aOutrasAc = [['BMP', lambda : Alert('Cliquei no 1'), 'Botão 1'], ['BMP', lambda : Alert('Cliquei no 2'), 'Botão 2']]
    bBlocoIni = lambda : EnchoiceBar(oDlgAux, bBlocoOk, bBlocoCan, None, aOutrasAc)
    cJanTitulo = 'Tela usando TDialog com EnchoiceBar'
    oDlgAux = None
    lOk = False
    # Cria a dialog
    oDlgAux = TDialog().New(0, 0, nJanAltu, nJanLarg, cJanTitulo, None, None, None, None, None, None, None, None, lDimPixels)
    # Ativa e exibe a janela
    oDlgAux.Activate(None, None, None, lCentraliz, None, None, bBlocoIni)
    # Se o retorno for positivo, foi clicado no botão Confirmar ao invés do Cancelar
    if lOk:
        FWAlertSuccess('Foi clicado no botão Confirmar!', 'OK')

    FWRestArea(aArea)
    return
