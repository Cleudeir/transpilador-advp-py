// caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2024/03/15/buscando-a-quantidade-de-dias-em-um-ano-com-a-getyeardaysnumber-maratona-advpl-e-tl-294/
// Bibliotecas
#Include "TOTVS.ch"
// {Protheus.doc} User Function zExe294
// Retorna a quantidade de dias em um ano normal ou bissexto
// @type  Function
// @author Atilio
// @since 21/02/2023
// Função GetYearDaysNumber
// Parâmetros
// Recebe o ano em caractere
// Retorno
// Retorna o número de dias
// **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
USER FUNCTION zExe294()
    LOCAL aArea, nAnoAtual, nAnoNormal, nAnoBissex, cMensagem

    aArea := FWGetArea()
    nAnoAtual := 0
    nAnoNormal := 0
    nAnoBissex := 0
    cMensagem := ""
    // Busca os dias do ano atual, de um ano normal e de um ano bissexsto
    nAnoAtual := GetYearDaysNumber(cValToChar(Year(Date()))) + 1
    nAnoNormal := GetYearDaysNumber("2021") + 1
    nAnoBissex := GetYearDaysNumber("2024") + 1
    // Monta a mensagem e exibe
    cMensagem += "Ano Atual: " + cValToChar(nAnoAtual) + CRLF
    cMensagem += "Ano Normal: " + cValToChar(nAnoNormal) + CRLF
    cMensagem += "Ano Bissexto: " + cValToChar(nAnoBissex) + CRLF
    FWAlertInfo(cMensagem, "Teste GetYearDaysNumber")
    FWRestArea(aArea)
    RETURN
