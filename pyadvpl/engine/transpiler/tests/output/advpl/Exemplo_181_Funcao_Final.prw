// caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2024/01/18/encerrando-uma-thread-com-a-funcao-final-maratona-advpl-e-tl-181/
// Bibliotecas
#Include "TOTVS.ch"
// {Protheus.doc} User Function zExe181
// Finaliza a thread em execução
// @type Function
// @author Atilio
// @since 21/12/2022
// Função Final
// Parâmetros
// + Mensagem a ser exibida ao usuário
// Retorno
// Não tem retorno
// **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
USER FUNCTION zExe181()
    LOCAL aArea

    aArea := FWGetArea()
    // Finaliza o protheus fechando o sistema ou a aba
    Final("Essa thread foi encerrada")
    FWRestArea(aArea)
    RETURN
