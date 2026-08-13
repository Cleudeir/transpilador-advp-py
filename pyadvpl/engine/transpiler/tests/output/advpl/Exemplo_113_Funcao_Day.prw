// caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2023/11/29/buscando-o-numero-do-dia-de-uma-data-com-a-funcao-day-maratona-advpl-e-tl-113/
// Bibliotecas
#Include "TOTVS.ch"
// {Protheus.doc} User Function zExe113
// Retorna o dia atual conforme a data informada
// @type Function
// @author Atilio
// @since 13/12/2022
// @see https://tdn.totvs.com/display/tec/Day
// Função Day
// Parâmetros
// + dData         , Data         , Data que será analisada
// Retorno
// + nDia          , Numérico     , Retorna o número do dia de 1 a 31 conforme a data passada
// **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
USER FUNCTION zExe113()
    LOCAL aArea, dDataRef, nDiaHoje

    aArea := FWGetArea()
    dDataRef := sToD("20221203")
    nDiaHoje := 0
    // Busca o dia atual conforme a data
    nDiaHoje := Day(dDataRef)
    // Exibe a diferença
    FWAlertInfo("Hoje é " + cValToChar(nDiaHoje), "Teste Day")
    FWRestArea(aArea)
    RETURN
