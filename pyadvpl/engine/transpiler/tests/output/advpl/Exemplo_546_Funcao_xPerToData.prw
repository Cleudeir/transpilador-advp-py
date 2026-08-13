// caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2024/07/19/buscando-uma-data-conforme-um-periodo-no-formato-mmyyyy-com-xpertodata-maratona-advpl-e-tl-546/
// Bibliotecas
#Include "TOTVS.ch"
// {Protheus.doc} User Function zExe546
// Retorna uma data conforme o período informado no formato "MMYYYY"
// @type Function
// @author Atilio
// @since 07/04/2023
// Função xPerToData
// Parâmetros
// Recebe o período no formato string sendo "MMYYYY"
// Retorno
// Retorna o primeiro dia do período encontrado
// **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
USER FUNCTION zExe546()
    LOCAL aArea, cPeriodo, dData

    aArea := FWGetArea()
    cPeriodo := ""
    dData := dToS("")
    // Define o período e converte pra data
    cPeriodo := "052023"
    dData := xPerToData(cPeriodo)
    // Mostra o resultado
    FWAlertInfo("O resultado é " + dToC(dData), "Teste xPerToData")
    FWRestArea(aArea)
    RETURN
