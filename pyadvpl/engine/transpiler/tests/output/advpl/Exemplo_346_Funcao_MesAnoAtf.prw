// caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2024/04/10/buscando-o-periodo-no-formato-mmdd-com-a-mesdia-maratona-advpl-e-tl-347/
// Bibliotecas
#Include "Totvs.ch"
// {Protheus.doc} User Function zExe346
// Retorna o ano e o mês no formato "YYYYMM"
// @type Function
// @author Atilio
// @since 25/03/2023
// Função MesAnoAtf
// Parâmetros
// Recebe a Data a ser verificada
// Retorno
// Retorna o Ano e o Mês em uma string no formato "YYYYMM"
// **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
USER FUNCTION zExe346()
    LOCAL aArea, dDtHoje, cAnoMes

    aArea := FWGetArea()
    dDtHoje := Date()
    cAnoMes := Nil
    // Pega o Ano e o Mês conforme a data passada e exibe uma mensagem
    cAnoMes := MesAnoAtf(dDtHoje)
    FWAlertInfo("O resultado é " + cAnoMes, "Teste - MesAnoAtf")
    FWRestArea(aArea)
    RETURN
