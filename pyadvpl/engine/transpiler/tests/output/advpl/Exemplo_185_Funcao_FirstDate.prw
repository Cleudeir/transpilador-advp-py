// caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2024/01/20/invertendo-uma-string-com-a-funcao-finvstring-maratona-advpl-e-tl-184/
// Bibliotecas
#Include "TOTVS.ch"
// {Protheus.doc} User Function zExe185
// Busca o primeiro dia do mês conforme a data passada
// @type Function
// @author Atilio
// @since 21/12/2022
// Função FirstDate
// Parâmetros
// Data de Referência
// Retorno
// Retorna o primeiro dia do mês
// **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
USER FUNCTION zExe185()
    LOCAL aArea, dData, dPriDia

    aArea := FWGetArea()
    dData := sToD("20221215")
    dPriDia := Nil
    // Busca o primeiro dia
    dPriDia := FirstDate(dData)
    // Mostra o resultado
    FWAlertInfo("Na data '" + dToC(dData) + "' o primeiro dia do mês é '" + dToC(dPriDia) + "'", "Teste FirstDate")
    FWRestArea(aArea)
    RETURN
