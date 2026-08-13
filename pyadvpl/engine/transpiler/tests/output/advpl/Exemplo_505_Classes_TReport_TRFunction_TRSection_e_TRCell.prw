// caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2024/06/28/quebrando-um-endereco-em-partes-atraves-da-trataend-maratona-advpl-e-tl-504/
// Bibliotecas
#Include "TOTVS.ch"
// {Protheus.doc} User Function zExe505
// Classes para montagem de um relatório com listagem de informações
// @type Function
// @author Atilio
// @since 04/04/2023
// @see https://tdn.totvs.com/display/public/framework/TReport e https://tdn.totvs.com/display/public/framework/TRSection e https://tdn.totvs.com/display/public/framework/TRFunction e https://tdn.totvs.com/display/public/framework/TRCell
// **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
USER FUNCTION zExe505()
    LOCAL aArea, oReport, aPergs, cProdDe, cProdAte, cTipoDe, cTipoAte, nOrden, MV_PAR05

    aArea := FWGetArea()
    oReport := Nil
    aPergs := {  }
    cProdDe := Space(TamSX3("B1_COD")[1])
    cProdAte := StrTran(cProdDe, " ", "Z")
    cTipoDe := Space(TamSX3("B1_TIPO")[1])
    cTipoAte := StrTran(cTipoDe, " ", "Z")
    nOrden := 1
    // Adicionando os parametros do ParamBox
    aAdd(aPergs, { 1, "Produto De", cProdDe, "", ".T.", "SB1", ".T.", 80, .F. })
    // MV_PAR01
    aAdd(aPergs, { 1, "Produto Até", cProdAte, "", ".T.", "SB1", ".T.", 80, .T. })
    // MV_PAR02
    aAdd(aPergs, { 1, "Tipo De", cTipoDe, "", ".T.", "02", ".T.", 40, .F. })
    // MV_PAR03
    aAdd(aPergs, { 1, "Tipo Até", cTipoAte, "", ".T.", "02", ".T.", 40, .T. })
    // MV_PAR04
    aAdd(aPergs, { 2, "Ordenar por", nOrden, { "1=Código do Produto", "2=Descrição do Produto", "3=Unidade de Medida" }, 100, ".T.", .T. })
    // MV_PAR05
    // Se a pergunta for confirma, cria as definicoes do relatorio
    If ParamBox(aPergs, "Informe os parâmetros", Nil, Nil, Nil, Nil, Nil, Nil, Nil, Nil, .F., .F.)
        MV_PAR05 := Val(cValToChar(MV_PAR05))
        oReport := fReportDef()
        oReport:PrintDialog()
    EndIf
    FWRestArea(aArea)
    RETURN Static

FUNCTION fReportDef()
    LOCAL oReport, oSection, oBreak

    oReport := Nil
    oSection := Nil
    // Criacao do componente de impressao
    oReport := TReport():New("zRel02", "Relatório de Produto", Nil, Nil)
    oReport:SetTotalInLine(.F.)
    oReport->lParamPage := .F.
    oReport:oPage():SetPaperSize(9)
    // Orientacao do Relatorio
    oReport:SetPortrait()
    // Definicoes da fonte utilizada
    oReport:SetLineHeight(50)
    oReport->nFontBody := 12
    // Criando a secao de dados
    oSection := TRSection():New(oReport, "Dados", { "QRY_REP" })
    oSection:SetTotalInLine(.F.)
    // Colunas do relatorio
    TRCell():New(oSection, "B1_COD", "QRY_REP", "Codigo", Nil, 15, Nil, Nil, "LEFT", Nil, "LEFT", Nil, Nil, Nil, Nil, Nil, .T.)
    TRCell():New(oSection, "B1_DESC", "QRY_REP", "Descricao", Nil, 30, Nil, Nil, "LEFT", Nil, "LEFT", Nil, Nil, Nil, Nil, Nil, .F.)
    TRCell():New(oSection, "B1_TIPO", "QRY_REP", "Tipo", Nil, 2, Nil, Nil, "LEFT", Nil, "LEFT", Nil, Nil, Nil, Nil, Nil, .F.)
    TRCell():New(oSection, "TIPODESCR", "QRY_REP", "Tp. Descr.", Nil, 55, Nil, Nil, "LEFT", Nil, "LEFT", Nil, Nil, Nil, Nil, Nil, .F.)
    TRCell():New(oSection, "B1_UM", "QRY_REP", "Unid. Med.", Nil, 2, Nil, Nil, "LEFT", Nil, "LEFT", Nil, Nil, Nil, Nil, Nil, .F.)
    TRCell():New(oSection, "UMDESCR", "QRY_REP", "UM. Descr.", Nil, 40, Nil, Nil, "LEFT", Nil, "LEFT", Nil, Nil, Nil, Nil, Nil, .F.)
    // Quebras do relatorio
    oBreak := TRBreak():New(oSection, oSection:Cell("B1_TIPO"), Nil, .F.)
    // Totalizadores
    TRFunction():New(oSection:Cell("B1_COD"), Nil, "COUNT", Nil, Nil, "@E 999,999,999", Nil, .F.)
    RETURN oReport

STATIC FUNCTION fRepPrint(oReport)
    LOCAL aArea, cQryReport, oSectDad, nAtual, nTotal

    aArea := FWGetArea()
    cQryReport := ""
    oSectDad := Nil
    nAtual := 0
    nTotal := 0
    // Pegando as secoes do relatorio
    oSectDad := oReport:Section(1)
    // Montando consulta de dados
    cQryReport += "SELECT " + CRLF
    cQryReport += "    B1_COD, " + CRLF
    cQryReport += "    B1_DESC, " + CRLF
    cQryReport += "    B1_TIPO, " + CRLF
    cQryReport += "    ISNULL(X5_DESCRI, '') AS TIPODESCR, " + CRLF
    cQryReport += "    B1_UM, " + CRLF
    cQryReport += "    ISNULL(AH_DESCPO, '') AS UMDESCR " + CRLF
    cQryReport += "FROM " + CRLF
    cQryReport += "    " + RetSQLName("SB1") + " SB1 " + CRLF
    cQryReport += "    LEFT JOIN " + RetSQLName("SX5") + " SX5 ON ( " + CRLF
    cQryReport += "       X5_FILIAL = '" + FWxFilial("SX5") + "' " + CRLF
    cQryReport += "       AND X5_TABELA = '02' " + CRLF
    cQryReport += "       AND X5_CHAVE = B1_TIPO " + CRLF
    cQryReport += "       AND SX5.D_E_L_E_T_ = ' ' " + CRLF
    cQryReport += "    ) " + CRLF
    cQryReport += "    LEFT JOIN " + RetSQLName("SAH") + " SAH ON ( " + CRLF
    cQryReport += "       AH_FILIAL = '" + FWxFilial("SAH") + "' " + CRLF
    cQryReport += "       AND AH_UNIMED = B1_UM " + CRLF
    cQryReport += "       AND SAH.D_E_L_E_T_ = ' ' " + CRLF
    cQryReport += "    ) " + CRLF
    cQryReport += "WHERE " + CRLF
    cQryReport += "    B1_FILIAL = '" + FWxFilial("SB1") + "' " + CRLF
    cQryReport += "    AND B1_COD >= '" + MV_PAR01 + "' " + CRLF
    cQryReport += "    AND B1_COD <= '" + MV_PAR02 + "' " + CRLF
    cQryReport += "    AND B1_TIPO >= '" + MV_PAR03 + "' " + CRLF
    cQryReport += "    AND B1_TIPO <= '" + MV_PAR04 + "' " + CRLF
    cQryReport += "    AND B1_MSBLQL != '1' " + CRLF
    cQryReport += "    AND SB1.D_E_L_E_T_ = ' ' " + CRLF
    cQryReport += "ORDER BY " + CRLF
    cQryReport += "    B1_TIPO, " + CRLF
    If MV_PAR05 = 1
        cQryReport += "    B1_COD " + CRLF
    ElseIf MV_PAR05 = 2
        cQryReport += "    B1_DESC " + CRLF
    ElseIf MV_PAR05 = 3
        cQryReport += "    B1_UM " + CRLF
    EndIf
    // Executando consulta e setando o total da regua
    PlsQuery(cQryReport, "QRY_REP")
    DbSelectArea("QRY_REP")
    Count
    to
    nTotal
    oReport:SetMeter(nTotal)
    // Enquanto houver dados
    oSectDad:Init()
    QRY_REP:DbGoTop()
    While .NOT. QRY_REP->( DbEof() )
        // Incrementando a regua
        nAtual += 1
        oReport:SetMsgPrint("Imprimindo registro " + cValToChar(nAtual) + " de " + cValToChar(nTotal) + "...")
        oReport:IncMeter()
        // Imprimindo a linha atual
        oSectDad:PrintLine()
        QRY_REP:DbSkip()
    EndDo
    oSectDad:Finish()
    QRY_REP:DbCloseArea()
    FWRestArea(aArea)
    RETURN
