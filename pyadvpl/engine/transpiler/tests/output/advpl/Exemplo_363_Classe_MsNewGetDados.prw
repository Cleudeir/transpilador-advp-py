// caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2024/04/18/lendo-e-gravando-em-antigos-campos-memo-com-a-msmm-maratona-advpl-e-tl-362/
// Bibliotecas
#Include "TOTVS.ch"
#Include "TopConn.ch"
// Legendas
oBmpVerde := LoadBitmap(GetResources(), "BR_VERDE")
oBmpVermelho := LoadBitmap(GetResources(), "BR_VERMELHO")
oBmpPreto := LoadBitmap(GetResources(), "BR_PRETO")
// {Protheus.doc} User Function zExe363
// Cria uma grid usando a classe antiga
// @type Function
// @author Atilio
// @since 27/03/2023
// @see https://tdn.totvs.com/display/public/framework/MsNewGetDados
// Essa classe foi depreciada, este aqui é só um exemplo, caso precisem algum dia dar manutenção
// em códigos antigos. Para novos códigos, tentem utilizar a FWBrowse.
// **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
USER FUNCTION zExe363()
    LOCAL aArea, oDlgPvt, oMsGetSBM, aHeadSBM, aColsSBM, oBtnSalv, oBtnFech, oBtnLege, nJanLarg, nJanAltu, cFontUti, oFontAno, oFontSub, oFontSubN, oFontBtn

    aArea := GetArea()
    // Objetos da Janela
    oDlgPvt := Nil
    oMsGetSBM := Nil
    aHeadSBM := {  }
    aColsSBM := {  }
    oBtnSalv := Nil
    oBtnFech := Nil
    oBtnLege := Nil
    // Tamanho da Janela
    nJanLarg := 700
    nJanAltu := 500
    // Fontes
    cFontUti := "Tahoma"
    oFontAno := TFont():New(cFontUti, Nil, - 38)
    oFontSub := TFont():New(cFontUti, Nil, - 20)
    oFontSubN := TFont():New(cFontUti, Nil, - 20, Nil, .T.)
    oFontBtn := TFont():New(cFontUti, Nil, - 14)
    // Criando o cabeçalho da Grid
    // Título               Campo        Máscara                        Tamanho                   Decimal                   Valid               Usado  Tipo F3     Combo
    aAdd(aHeadSBM, { "", "XX_COR", "@BMP", 2, 0, ".F.", "   ", "C", "", "V", "", "", "", "V" })
    aAdd(aHeadSBM, { "Código", "BM_GRUPO", "", TamSX3("BM_GRUPO")[1], 0, ".T.", ".T.", "C", "", "" })
    aAdd(aHeadSBM, { "Descrição", "BM_DESC", "", TamSX3("BM_DESC")[1], 0, "NaoVazio()", ".T.", "C", "", "" })
    aAdd(aHeadSBM, { "Status Grupo", "BM_STATUS", "", TamSX3("BM_STATUS")[1], 0, "PERTENCE('1234')", ".T.", "C", "", "1=Novo;2=Remanufaturado;3=Reciclado;4=Usado" })
    aAdd(aHeadSBM, { "Procedencia", "BM_PROORI", "", TamSX3("BM_PROORI")[1], 0, "Pertence('01')", ".T.", "C", "", "1=Original;0=Nao Original" })
    aAdd(aHeadSBM, { "Total de Produtos", "XX_TOTAL", "@E 999,999,999,999,999,999", 18, 0, ".T.", ".T.", "N", "", "" })
    aAdd(aHeadSBM, { "SBM Recno", "XX_RECNO", "@E 999,999,999,999,999,999", 18, 0, ".T.", ".T.", "N", "", "" })
    Processa(Nil, "Processando")
    // Criação da tela com os dados que serão informados
    DEFINE
    MSDIALOG
    oDlgPvt
    TITLE
    "Grupos de Produto"
    FROM_
    0
    // ,
    0
    TO
    nJanAltu
    // ,
    nJanLarg
    COLORS
    0
    // ,
    16777215
    PIXEL
    // Labels gerais
    // RAW: @ 004 , 003 SAY "TST" SIZE 200 , 030 FONT oFontAno OF oDlgPvt COLORS RGB ( 149 , 179 , 215 ) PIXEL
    // RAW: @ 004 , 050 SAY "Listagem de" SIZE 200 , 030 FONT oFontSub OF oDlgPvt COLORS RGB ( 031 , 073 , 125 ) PIXEL
    // RAW: @ 014 , 050 SAY "Grupos de Produtos" SIZE 200 , 030 FONT oFontSubN OF oDlgPvt COLORS RGB ( 031 , 073 , 125 ) PIXEL
    // Botões
    // RAW: @ 006 , ( nJanLarg / 2 - 001 ) - ( 0052 * 01 ) BUTTON oBtnFech PROMPT "Fechar" SIZE 050 , 018 OF oDlgPvt ACTION ( oDlgPvt : End ( ) ) FONT oFontBtn PIXEL
    // RAW: @ 006 , ( nJanLarg / 2 - 001 ) - ( 0052 * 02 ) BUTTON oBtnLege PROMPT "Legenda" SIZE 050 , 018 OF oDlgPvt ACTION ( fLegenda ( ) ) FONT oFontBtn PIXEL
    // RAW: @ 006 , ( nJanLarg / 2 - 001 ) - ( 0052 * 03 ) BUTTON oBtnSalv PROMPT "Salvar" SIZE 050 , 018 OF oDlgPvt ACTION ( fSalvar ( ) ) FONT oFontBtn PIXEL
    // Grid dos grupos
    oMsGetSBM := MsNewGetDados():New(29, 3, nJanAltu / 2 - 3, nJanLarg / 2 - 3, GD_INSERT + GD_UPDATE + GD_DELETE, "AllwaysTrue()", Nil, "", Nil, Nil, 9999, Nil, Nil, Nil, oDlgPvt, aHeadSBM, aColsSBM)
    // aCols     - Dados da Grid
    ACTIVATE
    MSDIALOG
    oDlgPvt
    CENTERED
    RestArea(aArea)
    RETURN Static

FUNCTION fCarAcols()
    LOCAL aArea, cQry, nAtual, nTotal, oBmpAux

    aArea := GetArea()
    cQry := ""
    nAtual := 0
    nTotal := 0
    oBmpAux := Nil
    // Seleciona dados do documento de entrada
    cQry := " SELECT " + CRLF
    cQry += "     BM_GRUPO, " + CRLF
    cQry += "     BM_DESC, " + CRLF
    cQry += "     BM_STATUS, " + CRLF
    cQry += "     BM_PROORI, " + CRLF
    cQry += "     ( " + CRLF
    cQry += "         SELECT " + CRLF
    cQry += "             COUNT(*) " + CRLF
    cQry += "         FROM " + CRLF
    cQry += "             " + RetSQLName("SB1") + " SB1 " + CRLF
    cQry += "         WHERE " + CRLF
    cQry += "             B1_FILIAL = '" + FWxFilial("SB1") + "' " + CRLF
    cQry += "             AND B1_GRUPO = BM_GRUPO " + CRLF
    cQry += "             AND B1_MSBLQL != '1' " + CRLF
    cQry += "             AND SB1.D_E_L_E_T_ = ' ' " + CRLF
    cQry += "     ) AS TOT_PROD, " + CRLF
    cQry += "     SBM.R_E_C_N_O_ AS SBMREC " + CRLF
    cQry += " FROM " + CRLF
    cQry += "     " + RetSQLName("SBM") + " SBM " + CRLF
    cQry += " WHERE " + CRLF
    cQry += "     BM_FILIAL = '" + FWxFilial("SBM") + "' " + CRLF
    cQry += "     AND SBM.D_E_L_E_T_ = ' ' " + CRLF
    cQry += " ORDER BY " + CRLF
    cQry += "     BM_GRUPO " + CRLF
    TCQuery
    cQry
    New
    Alias
    "QRY_SBM"
    // Setando o tamanho da régua
    Count
    To
    nTotal
    ProcRegua(nTotal)
    // Enquanto houver dados
    QRY_SBM:DbGoTop()
    While .NOT. QRY_SBM->( DbEof() )
        // Atualizar régua de processamento
        nAtual += 1
        IncProc("Adicionando " + Alltrim(QRY_SBM->BM_GRUPO) + " (" + cValToChar(nAtual) + " de " + cValToChar(nTotal) + ")...")
        // Definindo a legenda padrão como preto
        oBmpAux := oBmpPreto
        // Se for Original será verde
        If QRY_SBM->BM_PROORI = "1"
            oBmpAux := oBmpVerde
            // Senão, se for Não Original, será vermelho
        ElseIf QRY_SBM->BM_PROORI = "0"
            oBmpAux := oBmpVermelho
        EndIf
        // Adiciona o item no aCols
        aAdd(aColsSBM, { oBmpAux, QRY_SBM->BM_GRUPO, QRY_SBM->BM_DESC, QRY_SBM->BM_STATUS, QRY_SBM->BM_PROORI, QRY_SBM->TOT_PROD, QRY_SBM->SBMREC, .F. })
        QRY_SBM:DbSkip()
    EndDo
    QRY_SBM:DbCloseArea()
    RestArea(aArea)
    RETURN Static

FUNCTION fLegenda()
    LOCAL aLegenda

    aLegenda := {  }
    aAdd(aLegenda, { "BR_PRETO", "Sem Classificação" })
    aAdd(aLegenda, { "BR_VERDE", "Original" })
    aAdd(aLegenda, { "BR_VERMELHO", "Não Original" })
    BrwLegenda("Grupo de Produtos", "Legenda", aLegenda)
    RETURN Static

FUNCTION fSalvar()
    LOCAL aColsAux, nPosCod, nPosDes, nPosSta, nPosPro, nPosTot, nPosRec, nPosDel, nLinha

    aColsAux := oMsGetSBM:aCols()
    nPosCod := aScan(aHeadSBM, Nil)
    nPosDes := aScan(aHeadSBM, Nil)
    nPosSta := aScan(aHeadSBM, Nil)
    nPosPro := aScan(aHeadSBM, Nil)
    nPosTot := aScan(aHeadSBM, Nil)
    nPosRec := aScan(aHeadSBM, Nil)
    nPosDel := Len(aHeadSBM) + 1
    nLinha := 0
    DbSelectArea("SBM")
    // Percorrendo todas as linhas
    MsgInfo("Manipulações finalizadas!", "Atenção")
    oDlgPvt:End()
    RETURN
