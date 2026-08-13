// caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2023/09/29/buscando-o-tempo-total-entre-dois-periodos-com-attothora-e-difperiodo-maratona-advpl-e-tl-052/
// Bibliotecas
#Include "TOTVS.ch"
// {Protheus.doc} User Function zExe052
// Exemplo de função que retorna o tempo total entre duas datas e horários
// @type Function
// @author Atilio
// @since 05/12/2022
// Função AtTotHora
// Parâmetros
// + Data inicial
// + Hora inicial
// + Data final
// + Hora final
// + Máscara que irá formatar o retorno (sendo opcional com o conteúdo default "999D 99:99")
// Retorno
// + Retorna o tempo total encontrado
// Função DifPeriodo
// Parâmetros
// + Data inicial
// + Hora inicial
// + Data final
// + Hora final
// Retorno
// + Retorna o tempo total encontrado
// **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
USER FUNCTION zExe052()
    LOCAL aArea, dDataIni, cHoraIni, dDataFim, cHoraFim, cResult1, cResult2

    aArea := FWGetArea()
    dDataIni := sToD("20221201")
    cHoraIni := "06:30:00"
    dDataFim := sToD("20221205")
    cHoraFim := "14:15:00"
    cResult1 := ""
    cResult2 := ""
    // Busca o total com AtTotHora (que retorna o número de dias com horas)
    cResult1 := AtTotHora(dDataIni, cHoraIni, dDataFim, cHoraFim)
    FWAlertInfo("Resultado da função é: " + cResult1, "Teste AtTotHora")
    // Busca o total com DifPeriodo (que retorna o número total de horas entre duas datas)
    cResult2 := DifPeriodo(dDataIni, cHoraIni, dDataFim, cHoraFim)
    FWAlertInfo("Resultado da função é: " + cResult2, "Teste DifPeriodo")
    FWRestArea(aArea)
    RETURN
