// caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2023/11/30/buscando-o-numero-do-dia-no-formato-dd-com-a-day2str-maratona-advpl-e-tl-114/
// Bibliotecas
#Include "TOTVS.ch"
// {Protheus.doc} User Function zExe114
// Retorna o dia atual conforme a data informada no formato "DD"
// @type Function
// @author Atilio
// @since 13/12/2022
// Função Day2Str
// Parâmetros
// + Conteúdo que será analisado podendo ser: Data (ex: 05/12/2022); Numérico (ex: 5); Caractere (ex: "5")
// Retorno
// + Retorna uma string com o dia no formato "DD"
// **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
USER FUNCTION zExe114()
    LOCAL aArea, dDataRef, cDiaHoje

    aArea := FWGetArea()
    dDataRef := sToD("20221203")
    cDiaHoje := ""
    // Busca o dia atual conforme a data
    cDiaHoje := Day2Str(dDataRef)
    // Exibe a diferença
    FWAlertInfo("Hoje é " + cDiaHoje, "Teste Day2Str")
    FWRestArea(aArea)
    RETURN
