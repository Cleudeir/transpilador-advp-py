// caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2024/04/13/buscando-o-mes-de-uma-data-no-formato-mm-com-a-month2str-maratona-advpl-e-tl-352/
// Bibliotecas
#Include "Totvs.ch"
// {Protheus.doc} User Function zExe352
// Retorna o mês conforme data informada no formato "MM"
// @type Function
// @author Atilio
// @since 26/03/2023
// Função Month
// Parâmetros
// Data a ser verificada
// Retorno
// Número do mês no formato "MM"
// **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
USER FUNCTION zExe352()
    LOCAL aArea, dDtHoje, cMes

    aArea := FWGetArea()
    dDtHoje := Date()
    cMes := Nil
    // Pega o mês da data de hoje
    cMes := Month2Str(dDtHoje)
    FWAlertInfo("O mês é " + cMes, "Teste - Month2Str")
    FWRestArea(aArea)
    RETURN
