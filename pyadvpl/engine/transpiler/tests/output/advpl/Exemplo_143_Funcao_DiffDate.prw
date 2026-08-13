// caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2023/12/29/verificando-se-uma-data-e-maior-que-a-outra-com-a-diffdate-maratona-advpl-e-tl-143/
// Bibliotecas
#Include "TOTVS.ch"
// {Protheus.doc} User Function zExe143
// Verifica se as datas são válidas a inicial menor que a final
// @type Function
// @author Atilio
// @since 16/12/2022
// Função DiffDate
// Parâmetros
// + Data inicial a ser comparada
// + Data final a ser comparada
// Retorno
// + .T. se a data final for maior que a inicial ou .F. se a data final for menor que a inicial
// **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
USER FUNCTION zExe143()
    LOCAL aArea, dDataIni, dDataFim

    aArea := FWGetArea()
    dDataIni := Nil
    dDataFim := Nil
    // Monta as datas e faz a comparação
    dDataIni := sToD("20220705")
    dDataFim := sToD("20220715")
    If DiffDate(dDataIni, dDataFim)
        FWAlertSuccess("A data final é maior que a inicial", "Teste 1 DiffDate")
    Else
        FWAlertError("A data final é menor que a inicial", "Teste 1 DiffDate")
    EndIf
    // Monta as datas e faz a comparação
    dDataIni := sToD("20220131")
    dDataFim := sToD("20220110")
    If DiffDate(dDataIni, dDataFim)
        FWAlertSuccess("A data final é maior que a inicial", "Teste 2 DiffDate")
    Else
        FWAlertError("A data final é menor que a inicial", "Teste 2 DiffDate")
    EndIf
    FWRestArea(aArea)
    RETURN
