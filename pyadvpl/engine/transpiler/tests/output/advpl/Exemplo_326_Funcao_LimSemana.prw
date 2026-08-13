// caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2024/03/31/buscando-os-limites-de-uma-semana-com-a-limsemana-maratona-advpl-e-tl-326/
// Bibliotecas
#Include "TOTVS.ch"
// {Protheus.doc} User Function zExe326
// Busca os limites da semana (data inicial e final)
// @type Function
// @author Atilio
// @since 12/03/2023
// Função LimSemana
// Parâmetros
// Data de Referência
// Retorno
// Array com o primeiro e último dia da semana
// **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
USER FUNCTION zExe326()
    LOCAL aArea, dData, aDias, dPriDia, dUltDia

    aArea := FWGetArea()
    dData := sToD("20230315")
    aDias := {  }
    dPriDia := Nil
    dUltDia := Nil
    // Busca os limites da semana
    aDias := LimSemana(dData)
    dPriDia := aDias[1]
    dUltDia := aDias[2]
    // Mostra o resultado
    FWAlertInfo("Na data '" + dToC(dData) + "' o primeiro dia é '" + dToC(dPriDia) + "' e o último dia é '" + dToC(dUltDia) + "'", "Teste LimSemana")
    FWRestArea(aArea)
    RETURN
