// caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2024/06/26/abrindo-uma-tela-de-processamento-com-tnewprocess-maratona-advpl-e-tl-501/
// Bibliotecas
#Include "TOTVS.ch"
#Include "TopConn.ch"
// {Protheus.doc} User Function zExe501
// Monta uma tela de processamento com previsão de tempo e parametrizações na esquerda
// @type Function
// @author Atilio
// @since 27/03/2023
// @see https://tdn.totvs.com/display/public/framework/tNewProcess
// **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
USER FUNCTION zExe501()
    LOCAL aArea, bBlocoExec

    aArea := FWGetArea()
    bBlocoExec := Nil
    // Cria a tela de processamento
    TNewProcess():New("zExe501", "Teste de TNewProcess", bBlocoExec, "Descrição teste", Nil, Nil, Nil, Nil, Nil, .T.)
    FWRestArea(aArea)
    RETURN Static

FUNCTION fExemplo(oSelf)
    LOCAL aArea, nAtual, nTotal, cQryAux, nAtu2, nTot2, cMensagem

    aArea := FWGetArea()
    nAtual := 0
    nTotal := 0
    cQryAux := ""
    nAtu2 := 0
    nTot2 := 90
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
    oSelf:SetRegua1(nTotal)
    // Percorre todos os registros da query
    QRY_AUX:DbGoTop()
    oSelf:SaveLog("Iniciando")
    While .NOT. QRY_AUX->( DbEof() )
        // Incrementa a mensagem na regua
        nAtual += 1
        cMensagem := "Analisando registro " + cValToChar(nAtual) + " de " + cValToChar(nTotal) + "..."
        oSelf:IncRegua1(cMensagem)
        oSelf:SaveLog(cMensagem)
        // Incrementando a regua 2
        oSelf:SetRegua2(nTot2)
        QRY_AUX:DbSkip()
    EndDo
    QRY_AUX:DbCloseArea()
    FWRestArea(aArea)
    RETURN
