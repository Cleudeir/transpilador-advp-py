// caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2024/03/28/encerrando-conexoes-com-a-killuser-maratona-advpl-e-tl-320/
// Bibliotecas
#Include "TOTVS.ch"
// {Protheus.doc} User Function zExe321
// Busca o último dia do mês conforme a data passada
// @type Function
// @author Atilio
// @since 11/03/2023
// Função LastDate
// Parâmetros
// + Data de Referência
// Retorno
// Retorna o último dia do mês
// **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
USER FUNCTION zExe321()
    LOCAL aArea, dData, dUltDia

    aArea := FWGetArea()
    dData := sToD("20221215")
    dUltDia := Nil
    // Busca o último dia
    dUltDia := LastDate(dData)
    // Mostra o resultado
    FWAlertInfo("Na data '" + dToC(dData) + "' o último dia do mês é '" + dToC(dUltDia) + "'", "Teste LastDate")
    FWRestArea(aArea)
    RETURN
