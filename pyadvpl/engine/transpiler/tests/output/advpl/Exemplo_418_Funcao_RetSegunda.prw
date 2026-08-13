// caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2024/05/16/buscando-a-ultima-segunda-feira-atraves-da-retsegunda-maratona-advpl-e-tl-418/
// Bibliotecas
#Include "TOTVS.ch"
// {Protheus.doc} User Function zExe418
// Busaca a última segunda feira
// @type Function
// @author Atilio
// @since 22/02/2023
// Função RetSegunda
// Parâmetros
// Recebe uma data de referência
// Retorno
// Se recebeu um domingo no parâmetro avança pra próxima segunda do contrário se for outros dias (terça; quarta; etc) vem retroagindo até a última segunda
// **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
USER FUNCTION zExe418()
    LOCAL aArea, dDataRef, dUltSegun

    aArea := FWGetArea()
    dDataRef := sToD("20230329")
    dUltSegun := Nil
    // Busca a última segunda feira, conforme data passada
    dUltSegun := RetSegunda(dDataRef)
    // Exibe uma mensagem
    FWAlertInfo("Para a data '" + dToC(dDataRef) + "', a última segunda é '" + dToC(dUltSegun) + "'", "Teste RetSegunda")
    FWRestArea(aArea)
    RETURN
