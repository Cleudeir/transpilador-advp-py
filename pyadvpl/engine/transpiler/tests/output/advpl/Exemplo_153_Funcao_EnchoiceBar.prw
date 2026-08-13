// caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2024/01/04/validando-se-uma-expressao-esta-vazia-com-a-funcao-empty-maratona-advpl-e-tl-152/
// Bibliotecas
#Include "TOTVS.ch"
// {Protheus.doc} User Function zExe153
// Cria uma barra na tela com botões como Confirmar, Cancelar e Outras Ações
// @type Function
// @author Atilio
// @since 18/12/2022
// Função EnchoiceBar
// Parâmetros
// + Nome da Dialog que a EnchoiceBar será vinculada
// + Ação ao clicar no botão Confirmar
// + Ação ao clicar no botão Cancelar
// + Se for .T. mostra uma mensagem de deseja realmente excluir
// + Botões do Outras Ações
// + Número do Recno que será posicionado da tabela
// + Tabela de onde esta sendo feito as operações
// + Ativa a função Mashups no Outras Ações
// Retorno
// Função não tem retorno
// **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
USER FUNCTION zExe153()
    LOCAL aArea, nJanAltu, nJanLarg, lDimPixels, lCentraliz, bBlocoOk, bBlocoCan, aOutrasAc, bBlocoIni, cJanTitulo, oDlgAux, lOk

    aArea := FWGetArea()
    nJanAltu := 200
    nJanLarg := 600
    lDimPixels := .T.
    lCentraliz := .T.
    bBlocoOk := Nil
    bBlocoCan := Nil
    aOutrasAc := { { "BMP", Nil, "Botão 1" }, { "BMP", Nil, "Botão 2" } }
    bBlocoIni := Nil
    cJanTitulo := "Tela usando TDialog com EnchoiceBar"
    oDlgAux := Nil
    lOk := .F.
    // Cria a dialog
    oDlgAux := TDialog():New(0, 0, nJanAltu, nJanLarg, cJanTitulo, Nil, Nil, Nil, Nil, Nil, Nil, Nil, Nil, lDimPixels)
    // Ativa e exibe a janela
    oDlgAux:Activate(Nil, Nil, Nil, lCentraliz, Nil, Nil, bBlocoIni)
    // Se o retorno for positivo, foi clicado no botão Confirmar ao invés do Cancelar
    If lOk
        FWAlertSuccess("Foi clicado no botão Confirmar!", "OK")
    EndIf
    FWRestArea(aArea)
    RETURN
