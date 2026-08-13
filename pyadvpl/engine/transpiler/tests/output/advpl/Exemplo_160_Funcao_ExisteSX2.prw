// caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2024/01/08/validando-se-a-funcao-existe-no-rpo-com-existfunc-e-findfunction-maratona-advpl-e-tl-161/
// Bibliotecas
#Include "TOTVS.ch"
// {Protheus.doc} User Function zExe160
// Verifica se uma tabela existe no dicionário
// @type Function
// @author Atilio
// @since 18/12/2022
// Função ExisteSX2
// Parâmetros
// + Nome da tabela a ser validada
// Retorno
// + .T. Se a tabela existir ou .F. se ela não existir
// **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
USER FUNCTION zExe160()
    LOCAL aArea

    aArea := FWGetArea()
    // Teste 1 com uma tabela padrão
    If ExisteSX2("SA1")
        FWAlertSuccess("Tabela SA1 encontrada", "Teste 1 ExisteSX2")
    Else
        FWAlertError("Tabela SA1 não encontrada", "Teste 1 ExisteSX2")
    EndIf
    // Teste 2 com uma tabela customizada
    If ExisteSX2("ZY0")
        FWAlertSuccess("Tabela ZY0 encontrada", "Teste 2 ExisteSX2")
    Else
        FWAlertError("Tabela ZY0 não encontrada", "Teste 2 ExisteSX2")
    EndIf
    FWRestArea(aArea)
    RETURN
