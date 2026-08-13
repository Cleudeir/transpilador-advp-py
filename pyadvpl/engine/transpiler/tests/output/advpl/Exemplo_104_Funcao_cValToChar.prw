// caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2023/11/20/convertendo-variaveis-para-caractere-com-a-funcao-cvaltochar-maratona-advpl-e-tl-104/
// Bibliotecas
#Include "TOTVS.ch"
// {Protheus.doc} User Function zExe104
// Converte valores para o tipo caractere
// @type Function
// @author Atilio
// @since 12/12/2022
// @see https://tdn.totvs.com/display/tec/cValToChar
// Função cValToChar
// Parâmetros
// + xParametro    , Indefinido   , Valor a ser convertido (data, lógico, numérico)
// Retorno
// + cRet          , Caractere    , Retorna a string conforme o valor informado
// **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
USER FUNCTION zExe104()
    LOCAL aArea, dData, nValor, lLogico, cMensagem

    aArea := FWGetArea()
    dData := Date()
    nValor := 13.8
    lLogico := .T.
    cMensagem := ""
    // Monta a mensagem de teste
    cMensagem += "Data: " + cValToChar(dData) + CRLF
    cMensagem += "Numérico: " + cValToChar(nValor) + CRLF
    cMensagem += "Lógico: " + cValToChar(lLogico)
    // Exibe a mensagem
    FWAlertInfo(cMensagem, "Teste de cValToChar")
    FWRestArea(aArea)
    RETURN
