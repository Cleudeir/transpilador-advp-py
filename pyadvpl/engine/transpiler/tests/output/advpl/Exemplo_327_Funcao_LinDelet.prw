// caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2024/03/31/validando-se-uma-linha-esta-apagada-numa-grid-com-a-lindelet-maratona-advpl-e-tl-327/
// Bibliotecas
#Include "TOTVS.ch"
// {Protheus.doc} User Function zExe327
// Função que verifica se a linha esta apagada
// @type  Function
// @author Atilio
// @since 12/03/2023
// Função LinDelet
// Parâmetros
// Recebe um array com a linha atual
// Retorno
// Retorna .T. se a linha esta apagada ou .F. se não
// **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
USER FUNCTION zExe327()
    LOCAL aArea, nLinha, cApagadas

    aArea := FWGetArea()
    nLinha := 1
    cApagadas := ""
    // Se a pergunta for confirmada
    If FWAlertYesNo("Deseja validar todas as linhas?", "Continua")
        // Percorre as linhas digitadas na grid
        // Se a variavel estiver vazia, apenas mostra mensagem, senão mostra quais foram as linhas
        If Empty(cApagadas)
            FWAlertSuccess("Não há linha(s) apagada(s)", "Sucesso")
        Else
            FWAlertError(cApagadas, "Linhas Excluidas")
        EndIf
    EndIf
    FWRestArea(aArea)
    RETURN

USER FUNCTION A410CONS()
    LOCAL aArea, aBotoes

    aArea := FWGetArea()
    aBotoes := {  }
    aAdd(aBotoes, { "DBG07", Nil, "* Ver Linhas Apagadas", "* Apagadas" })
    FWRestArea(aArea)
    RETURN aBotoes
