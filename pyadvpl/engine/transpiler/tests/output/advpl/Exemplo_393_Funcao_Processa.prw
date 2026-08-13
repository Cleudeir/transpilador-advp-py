// caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2024/05/03/criando-uma-regua-de-processamento-com-a-processa-maratona-advpl-e-tl-393/
// Bibliotecas
#Include "TOTVS.ch"
#Include "TopConn.ch"
// {Protheus.doc} User Function zExe393
// Cria uma régua de processamento
// @type Function
// @author Atilio
// @since 28/03/2023
// Função Processa
// Parâmetros
// Bloco de Código a ser executado
// Título da janela
// Mensagem inicial da janela
// Se será possível abortar o processo (.T.) ou não (.F.)
// Retorno
// Função não tem retorno
// **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
USER FUNCTION zExe393()
    LOCAL aArea

    aArea := FWGetArea()
    Processa(Nil, "Filtrando...")
    FWRestArea(aArea)
    RETURN Static

FUNCTION fExemplo()
    LOCAL aArea, nAtual, nTotal, cQryAux

    aArea := FWGetArea()
    nAtual := 0
    nTotal := 0
    cQryAux := ""
    // Executa a consulta
    cQryAux := " SELECT " + CRLF
    cQryAux += "     BM_GRUPO, " + CRLF
    cQryAux += "     BM_DESC " + CRLF
    cQryAux += " FROM " + CRLF
    cQryAux += "     " + RetSQLName("SBM") + " SBM " + CRLF
    cQryAux += " WHERE " + CRLF
    cQryAux += "     BM_FILIAL = '" + FWxFilial("SBM") + "' " + CRLF
    cQryAux += "     AND SBM.D_E_L_E_T_ = ' ' " + CRLF
    TCQuery
    cQryAux
    New
    Alias
    "QRY_AUX"
    // Conta quantos registros existem, e seta no tamanho da regua
    Count
    To
    nTotal
    ProcRegua(nTotal)
    // Percorre todos os registros da query
    QRY_AUX:DbGoTop()
    While .NOT. QRY_AUX->( DbEof() )
        // Incrementa a mensagem na regua
        nAtual += 1
        IncProc("Analisando registro " + cValToChar(nAtual) + " de " + cValToChar(nTotal) + "...")
        Sleep(100)
        QRY_AUX:DbSkip()
    EndDo
    QRY_AUX:DbCloseArea()
    FWRestArea(aArea)
    RETURN
