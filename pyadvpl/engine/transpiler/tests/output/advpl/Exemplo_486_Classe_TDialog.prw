// caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2024/06/19/criando-abas-tem-uma-tela-com-tfolder-maratona-advpl-e-tl-487/
// Bibliotecas
#Include "TOTVS.ch"
// {Protheus.doc} User Function zExe486
// Classe para criar janelas
// @type Function
// @author Atilio
// @since 04/04/2023
// @see https://tdn.totvs.com/display/tec/TDialog
// **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
USER FUNCTION zExe486()
    LOCAL oDlgAux, nJanAltu, nJanLarg, lDimPixels, lCentraliz, bBlocoIni, cJanTitulo

    oDlgAux := Nil
    nJanAltu := 200
    nJanLarg := 400
    lDimPixels := .T.
    lCentraliz := .T.
    bBlocoIni := Nil
    cJanTitulo := "Tela usando TDialog"
    // Cria a dialog
    oDlgAux := TDialog():New(0, 0, nJanAltu, nJanLarg, cJanTitulo, Nil, Nil, Nil, Nil, Nil, Nil, Nil, Nil, lDimPixels)
    // Ativa e exibe a janela
    oDlgAux:Activate(Nil, Nil, Nil, lCentraliz, Nil, Nil, bBlocoIni)
    RETURN
