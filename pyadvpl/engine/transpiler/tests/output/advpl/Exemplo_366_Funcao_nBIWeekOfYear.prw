// caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2024/04/20/buscando-a-semana-do-ano-com-nbiweekofyear-maratona-advpl-e-tl-366/
// Bibliotecas
#Include "TOTVS.ch"
// {Protheus.doc} User Function zExe366
// Busca o número da semana no ano
// @type Function
// @author Atilio
// @since 27/03/2023
// Função nBIWeekOfYear
// Parâmetros
// Recebe a data a ser verificada
// Retorno
// Retorna o número da semana do ano
// **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
USER FUNCTION zExe366()
    LOCAL aArea, dDataHoje, nSemana

    aArea := FWGetArea()
    dDataHoje := Date()
    nSemana := Nil
    // Busca a semana do ano
    nSemana := nBIWeekOfYear(dDataHoje)
    // Exibe em tela
    FWAlertInfo("Na data '" + dToC(dDataHoje) + "', estamos na semana '" + cValToChar(nSemana) + "'", "Teste nBIWeekOfYear")
    FWRestArea(aArea)
    RETURN
