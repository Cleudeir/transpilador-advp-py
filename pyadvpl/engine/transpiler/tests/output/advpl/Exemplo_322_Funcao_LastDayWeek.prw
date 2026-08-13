// caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2024/03/29/buscando-o-ultimo-dia-da-semana-com-a-lastdayweek-maratona-advpl-e-tl-322/
// Bibliotecas
#Include "TOTVS.ch"
// {Protheus.doc} User Function zExe322
// Busca o último dia da semana conforme data passada
// @type Function
// @author Atilio
// @since 11/03/2023
// @see https://tdn.totvs.com/display/public/framework/LastDayWeek
// Função LastDayWeek
// Parâmetros
// + dDate        , Data      , Data de Referência
// Retorno
// + dLastDay     , Data      , Último dia da semana (sexta feira)
// **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
USER FUNCTION zExe322()
    LOCAL aArea, dData, dUltDia

    aArea := FWGetArea()
    dData := sToD("20230418")
    dUltDia := Nil
    // Busca o último dia da semana
    dUltDia := LastDayWeek(dData)
    // Mostra o resultado
    FWAlertInfo("Na data '" + dToC(dData) + "' o último dia da semana (sexta feira) é '" + dToC(dUltDia) + "'", "Teste LastDayWeek")
    FWRestArea(aArea)
    RETURN
