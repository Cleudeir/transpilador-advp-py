// caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2024/02/15/criando-relatorios-atraves-da-fwmsprinter-maratona-advpl-e-tl-236/
// Bibliotecas
#Include "Totvs.ch"
#Include "TopConn.ch"
#Include "RPTDef.ch"
#Include "FWPrintSetup.ch"
// Alinhamentos
#Define PAD_LEFT    0
#Define PAD_RIGHT   1
#Define PAD_CENTER  2
// Cor(es)
nCorCinza := RGB(110, 110, 110)
nCorLinha := RGB(148, 255, 180)
// {Protheus.doc} User Function zExe236
// Exemplo de um relatório com FWMSPrinter
// @author Atilio
// @since 20/02/2023
// @version 1.0
// @type function
// @obs Codigo gerado automaticamente pelo Autumn Code Maker
// @see https://tdn.totvs.com/display/public/framework/FWMsPrinter e http://autumncodemaker.com
USER FUNCTION zExe236()
    LOCAL aArea, aPergs, xPar0, xPar1

    aArea := FWGetArea()
    aPergs := {  }
    xPar0 := Space(15)
    xPar1 := Space(15)
    // Adicionando os parametros do ParamBox
    aAdd(aPergs, { 1, "Produto De", xPar0, "", ".T.", "SB1", ".T.", 80, .F. })
    aAdd(aPergs, { 1, "Produto Até", xPar1, "", ".T.", "SB1", ".T.", 80, .T. })
    // Se a pergunta for confirma, cria o relatorio
    If ParamBox(aPergs, "Informe os parametros")
        Processa(Nil)
    EndIf
    FWRestArea(aArea)
    RETURN Static

FUNCTION fImprime()
    LOCAL aArea, nTotAux, nAtuAux, cQryAux, cArquivo, oPrintPvt, oBrushLin, cHoraEx, nPagAtu, cLogoEmp, nLinAtu, nLinFin, nColIni, nColFin, nColMeio, nColDad1, nColDad2, nColDad3, nColDad4, nColDad5, cNomeFont, oFontDet, oFontDetN, oFontRod, oFontMin, oFontTit

    aArea := GetArea()
    nTotAux := 0
    nAtuAux := 0
    cQryAux := ""
    cArquivo := "zExe236" + RetCodUsr() + "_" + dToS(Date()) + "_" + StrTran(Time(), ":", "-") + ".pdf"
    oPrintPvt := Nil
    oBrushLin := TBrush():New(Nil, nCorLinha)
    cHoraEx := Time()
    nPagAtu := 1
    cLogoEmp := fLogoEmp()
    // Linhas e colunas
    nLinAtu := 0
    nLinFin := 800
    nColIni := 10
    nColFin := 580
    nColMeio := nColFin - nColIni / 2
    // Colunas dos relatorio
    nColDad1 := nColIni
    nColDad2 := nColIni + 50
    nColDad3 := nColIni + 150
    nColDad4 := nColIni + 200
    nColDad5 := nColIni + 300
    // Declarando as fontes
    cNomeFont := "Arial"
    oFontDet := TFont():New(cNomeFont, 9, - 11, .T., .F., 5, .T., 5, .T., .F.)
    oFontDetN := TFont():New(cNomeFont, 9, - 13, .T., .T., 5, .T., 5, .T., .F.)
    oFontRod := TFont():New(cNomeFont, 9, - 8, .T., .F., 5, .T., 5, .T., .F.)
    oFontMin := TFont():New(cNomeFont, 9, - 7, .T., .F., 5, .T., 5, .T., .F.)
    oFontTit := TFont():New(cNomeFont, 9, - 15, .T., .T., 5, .T., 5, .T., .F.)
    // Monta a consulta de dados
    cQryAux += "SELECT " + CRLF
    cQryAux += " B1_COD, " + CRLF
    cQryAux += " B1_DESC, " + CRLF
    cQryAux += " B1_GRUPO, " + CRLF
    cQryAux += " BM_DESC " + CRLF
    cQryAux += "FROM " + CRLF
    cQryAux += " SB1990 SB1 " + CRLF
    cQryAux += " INNER JOIN SBM990 SBM ON ( " + CRLF
    cQryAux += " BM_FILIAL = '01' " + CRLF
    cQryAux += " AND BM_GRUPO = B1_GRUPO " + CRLF
    cQryAux += " AND SBM.D_E_L_E_T_ = ' ' " + CRLF
    cQryAux += " ) " + CRLF
    cQryAux += "WHERE " + CRLF
    cQryAux += " B1_FILIAL = '' " + CRLF
    cQryAux += " AND B1_COD >= '" + MV_PAR01 + "' " + CRLF
    cQryAux += " AND B1_COD <= '" + MV_PAR02 + "' " + CRLF
    cQryAux += " AND B1_MSBLQL != '1' " + CRLF
    cQryAux += " AND SB1.D_E_L_E_T_ = ' '" + CRLF
    PLSQuery(cQryAux, "QRY_AUX")
    // Define o tamanho da régua
    DbSelectArea("QRY_AUX")
    QRY_AUX:DbGoTop()
    Count
    to
    nTotAux
    ProcRegua(nTotAux)
    QRY_AUX:DbGoTop()
    // Somente se tiver dados
    If .NOT. QRY_AUX->( DbEof() )
        // Criando o objeto de impressao
        oPrintPvt := FWMSPrinter():New(cArquivo, IMP_PDF, .F., Nil, .T., Nil, @ oPrintPvt, Nil, Nil, Nil, Nil, .T.)
        oPrintPvt->cPathPDF := GetTempPath()
        oPrintPvt:SetResolution(72)
        oPrintPvt:SetPortrait()
        oPrintPvt:SetPaperSize(DMPAPER_A4)
        oPrintPvt:SetMargin(0, 0, 0, 0)
        // Imprime os dados
        fImpCab()
        While .NOT. QRY_AUX->( DbEof() )
            nAtuAux += 1
            IncProc("Imprimindo registro " + cValToChar(nAtuAux) + " de " + cValToChar(nTotAux) + "...")
            // Se atingiu o limite, quebra de pagina
            fQuebra()
            // Faz o zebrado ao fundo
            If nAtuAux + 2 = 0
                oPrintPvt:FillRect({ nLinAtu - 2, nColIni, nLinAtu + 12, nColFin }, oBrushLin)
            EndIf
            // Imprime a linha atual
            oPrintPvt:SayAlign(nLinAtu, nColDad1, Alltrim(QRY_AUX->B1_COD), oFontDet, 50, 10, Nil, PAD_LEFT, Nil, Nil)
            oPrintPvt:SayAlign(nLinAtu, nColDad2, Alltrim(QRY_AUX->B1_DESC), oFontDetN, 100, 10, Nil, PAD_LEFT, Nil, Nil)
            oPrintPvt:SayAlign(nLinAtu, nColDad3, Alltrim(QRY_AUX->B1_GRUPO), oFontDet, 50, 10, Nil, PAD_LEFT, Nil, Nil)
            oPrintPvt:SayAlign(nLinAtu, nColDad4, Alltrim(QRY_AUX->BM_DESC), oFontDet, 100, 10, Nil, PAD_LEFT, Nil, Nil)
            nLinAtu += 15
            oPrintPvt:Line(nLinAtu - 3, nColIni, nLinAtu - 3, nColFin, nCorCinza)
            // Se atingiu o limite, quebra de pagina
            fQuebra()
            QRY_AUX:DbSkip()
        EndDo
        fImpRod()
        oPrintPvt:Preview()
    Else
        MsgStop("Não foi encontrado informações com os parâmetros informados!", "Atenção")
    EndIf
    QRY_AUX:DbCloseArea()
    RestArea(aArea)
    RETURN Static

FUNCTION fLogoEmp()
    LOCAL cGrpCompany, cCodEmpGrp, cUnitGrp, cFilGrp, cLogo, cCamFim, cStart, cDescLogo

    cGrpCompany := AllTrim(FWGrpCompany())
    cCodEmpGrp := AllTrim(FWCodEmp())
    cUnitGrp := AllTrim(FWUnitBusiness())
    cFilGrp := AllTrim(FWFilial())
    cLogo := ""
    cCamFim := GetTempPath()
    cStart := GetSrvProfString("Startpath", "")
    // Se tiver filiais por grupo de empresas
    If .NOT. Empty(cUnitGrp)
        cDescLogo := cGrpCompany + cCodEmpGrp + cUnitGrp + cFilGrp
        // Senão, será apenas, empresa + filial
    Else
        cDescLogo := cEmpAnt + cFilAnt
    EndIf
    // Pega a imagem
    cLogo := cStart + "DANFE" + cDescLogo + ".BMP"
    // Se o arquivo não existir, pega apenas o da empresa, desconsiderando a filial
    If .NOT. File(cLogo)
        cLogo := cStart + "DANFE" + cEmpAnt + ".BMP"
    EndIf
    // Copia para a temporária do s.o.
    CpyS2T(cLogo, cCamFim)
    cLogo := cCamFim + StrTran(cLogo, cStart, "")
    // Se o arquivo não existir na temporária, espera meio segundo para terminar a cópia
    If .NOT. File(cLogo)
        Sleep(500)
    EndIf
    RETURN cLogo
    // {Protheus.doc} fImpCab
    // Função que imprime o cabeçalho do relatório
    // @author Atilio
    // @since 20/02/2023
    // @version 1.0
    // @type function
    // @obs Codigo gerado automaticamente pelo Autumn Code Maker
    // @see http://autumncodemaker.com

STATIC FUNCTION fImpCab()
    LOCAL cTexto, nLinCab, nLinAtu

    cTexto := ""
    nLinCab := 15
    // Iniciando Pagina
    oPrintPvt:StartPage()
    // Imprime o logo
    If File(cLogoEmp)
        oPrintPvt:SayBitmap(5, nColIni, cLogoEmp, 30, 30)
    EndIf
    // Cabecalho
    cTexto := "Produtos e Grupos"
    oPrintPvt:SayAlign(nLinCab, nColMeio - 200, cTexto, oFontTit, 400, 20, Nil, PAD_CENTER, Nil, Nil)
    // Linha Separatoria
    nLinCab += 20
    oPrintPvt:Line(nLinCab, nColIni, nLinCab, nColFin)
    // Atualizando a linha inicial do relatorio
    nLinAtu := nLinCab + 5
    If nPagAtu = 1
        // Imprimindo os parâmetros
        oPrintPvt:SayAlign(nLinAtu, nColIni, "Produto De", oFontDetN, 200, 10, Nil, PAD_LEFT, Nil, Nil)
        oPrintPvt:SayAlign(nLinAtu, nColIni + 200, MV_PAR01, oFontDet, 200, 10, Nil, PAD_LEFT, Nil, Nil)
        nLinAtu += 15
        oPrintPvt:SayAlign(nLinAtu, nColIni, "Produto Até", oFontDetN, 200, 10, Nil, PAD_LEFT, Nil, Nil)
        oPrintPvt:SayAlign(nLinAtu, nColIni + 200, MV_PAR02, oFontDet, 200, 10, Nil, PAD_LEFT, Nil, Nil)
        nLinAtu += 15
        oPrintPvt:Line(nLinAtu - 3, nColIni, nLinAtu - 3, nColFin, nCorCinza)
        nLinAtu += 5
    EndIf
    oPrintPvt:SayAlign(nLinAtu, nColDad1, "Produto", oFontMin, 50, 10, Nil, PAD_LEFT, Nil, Nil)
    oPrintPvt:SayAlign(nLinAtu, nColDad2, "Descrição", oFontMin, 100, 10, Nil, PAD_LEFT, Nil, Nil)
    oPrintPvt:SayAlign(nLinAtu, nColDad3, "Grupo", oFontMin, 50, 10, Nil, PAD_LEFT, Nil, Nil)
    oPrintPvt:SayAlign(nLinAtu, nColDad4, "Grp. Descrição", oFontMin, 100, 10, Nil, PAD_LEFT, Nil, Nil)
    nLinAtu += 15
    RETURN Static

FUNCTION fImpRod()
    LOCAL nLinRod, cTexto, nPagAtu

    nLinRod := nLinFin
    cTexto := ""
    // Linha Separatoria
    oPrintPvt:Line(nLinRod, nColIni, nLinRod, nColFin)
    nLinRod += 3
    // Dados da Esquerda
    cTexto := dToC(dDataBase) + "     " + cHoraEx + "     " + FunName() + " (zExe236)     " + UsrRetName(RetCodUsr())
    oPrintPvt:SayAlign(nLinRod, nColIni, cTexto, oFontRod, 500, 10, Nil, PAD_LEFT, Nil, Nil)
    // Direita
    cTexto := "Pagina " + cValToChar(nPagAtu)
    oPrintPvt:SayAlign(nLinRod, nColFin - 40, cTexto, oFontRod, 40, 10, Nil, PAD_RIGHT, Nil, Nil)
    // Finalizando a pagina e somando mais um
    oPrintPvt:EndPage()
    nPagAtu += 1
    RETURN Static

FUNCTION fQuebra()
    If nLinAtu >= nLinFin - 10
        fImpRod()
        fImpCab()
    EndIf
    RETURN
