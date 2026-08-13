// caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2023/10/06/excluindo-os-dados-de-uma-tabela-com-a-funcao-avzap-maratona-advpl-e-tl-059/
// Bibliotecas
#Include "TOTVS.ch"
// {Protheus.doc} User Function zExe059
// Exemplo de função que executa o ZAP (limpeza) em uma tabela do Protheus apagando todos os dados
// @type Function
// @author Atilio
// @since 05/12/2022
// Função AvZap
// Parâmetros
// + Alias da Tabela que terá os dados apagados
// Retorno
// + .T. em caso de sucesso ou .F. em caso de falha
// **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
USER FUNCTION zExe059()
    LOCAL aArea, cTable, cTabAlias

    aArea := FWGetArea()
    cTable := "ZD4990"
    cTabAlias := "ZD4"
    // Tenta executar o zap na tabela
    USE(cTable)
    ALIAS(cTabAlias)
    EXCLUSIVE
    NEW
    VIA
    "TOPCONN"
    If cTabAlias:AvZap()
        FWAlertSuccess("Limpeza executada com sucesso!", "Teste AvZap")
    Else
        FWAlertError("Não foi possível excluir os dados da tabela, ela pode estar em uso!", "Teste AvZap")
    EndIf
    FWRestArea(aArea)
    RETURN
