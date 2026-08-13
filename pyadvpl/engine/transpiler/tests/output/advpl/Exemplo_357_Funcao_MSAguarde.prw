// caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2024/04/15/validando-se-o-dicionario-esta-no-banco-com-mpdicindb-maratona-advpl-e-tl-356/
// Bibliotecas
#Include "TOTVS.ch"
#Include "TopConn.ch"
// {Protheus.doc} User Function zExe357
// Exibe uma tela de carregamento de rotinas
// @type Function
// @author Atilio
// @since 26/03/2023
// Função MSAguarde
// Parâmetros
// Bloco de código com a execução que será processada
// Título da janela
// Mensagem exibida no processamento
// Define se poderá ser abortado a rotina (.T.) ou não (.F.)
// Retorno
// Função não tem retorno
// **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
USER FUNCTION zExe357()
    LOCAL aArea

    aArea := FWGetArea()
    // Aciona a rotina para processar os registros
    MsAguarde(Nil, "Aguarde...", "Processando Registros...")
    FWRestArea(aArea)
    RETURN Static

FUNCTION fExemplo()
    LOCAL aArea, nAtual, nTotal, cQryAux

    aArea := GetArea()
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
    // Percorre todos os registros da query
    QRY_AUX:DbGoTop()
    While .NOT. QRY_AUX->( DbEof() )
        // Incrementa a mensagem na regua
        nAtual += 1
        MsProcTxt("Analisando registro " + cValToChar(nAtual) + " de " + cValToChar(nTotal) + "...")
        Sleep(100)
        QRY_AUX:DbSkip()
    EndDo
    QRY_AUX:DbCloseArea()
    RestArea(aArea)
    RETURN
