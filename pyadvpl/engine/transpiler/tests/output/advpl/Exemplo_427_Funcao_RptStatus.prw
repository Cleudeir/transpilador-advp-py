// caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2024/05/20/preparando-o-ambiente-com-a-rpcsetenv-maratona-advpl-e-tl-426/
// Bibliotecas
#Include "TOTVS.ch"
#Include "TopConn.ch"
// {Protheus.doc} User Function zExe427
// Abre uma régua simples de processamento
// @type Function
// @author Atilio
// @since 29/03/2023
// Função RptStatus
// Parâmetros
// Bloco de código que será executado
// Título da janela
// Mensagem que ficará em exibição
// Retorno
// Função não tem retorno
// **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
USER FUNCTION zExe427()
    LOCAL aArea

    aArea := FWGetArea()
    RptStatus(Nil, "Aguarde...", "Executando rotina...")
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
    SetRegua(nTotal)
    // Percorre todos os registros da query
    QRY_AUX:DbGoTop()
    While .NOT. QRY_AUX->( DbEof() )
        // Incrementa a mensagem na regua
        nAtual += 1
        IncRegua()
        Sleep(100)
        QRY_AUX:DbSkip()
    EndDo
    QRY_AUX:DbCloseArea()
    FWRestArea(aArea)
    RETURN
