# Esse exemplo faz parte da série do YouTube, Maratona de Exemplos, do canal Terminal de Informação, 
#     caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2024/06/11/exibindo-imagens-atraves-da-tbitmap-maratona-advpl-e-tl-470/
# Bibliotecas
# PREPROCESSOR: #Include "Totvs.ch"
# PREPROCESSOR: #Include "TopConn.ch"
# PREPROCESSOR: #Include "RPTDef.ch"
# PREPROCESSOR: #Include "FWPrintSetup.ch"
# Alinhamentos
# PREPROCESSOR: #Define PAD_LEFT    0
# PREPROCESSOR: #Define PAD_RIGHT   1
# PREPROCESSOR: #Define PAD_CENTER  2
# Cor(es)
nCorCinza = RGB(110, 110, 110)
nCorLinha = RGB(148, 255, 180)
# {Protheus.doc} User Function zExe471
# Classe para criar um pincel (geralmente para usar em relatórios)
# @type Function
# @author Atilio
# @since 03/04/2023
# @see https://tdn.totvs.com/display/tec/TBrush
# @obs 
# 
#     **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
def u_zExe471():
    aArea = FWGetArea()
    aPergs = []
    xPar0 = Space(15)
    xPar1 = Space(15)
    # Adicionando os parametros do ParamBox
    aAdd(aPergs, [1, 'Produto De', xPar0, '', '.T.', 'SB1', '.T.', 80, False])
    aAdd(aPergs, [1, 'Produto Até', xPar1, '', '.T.', 'SB1', '.T.', 80, True])
    # Se a pergunta for confirma, cria o relatorio
    if ParamBox(aPergs, 'Informe os parametros'):
        Processa(lambda : fImprime())

    FWRestArea(aArea)
    return Static

def fImprime():
    aArea = GetArea()
    nTotAux = 0
    nAtuAux = 0
    cQryAux = ''
    cArquivo = 'zExe236' + RetCodUsr() + '_' + dToS(Date()) + '_' + StrTran(Time(), ':', '-') + '.pdf'
    oPrintPvt = None
    oBrushLin = TBrush().New(None, nCorLinha)
    cHoraEx = Time()
    nPagAtu = 1
    cLogoEmp = fLogoEmp()
    # Linhas e colunas
    nLinAtu = 0
    nLinFin = 800
    nColIni = 10
    nColFin = 580
    nColMeio = nColFin - nColIni / 2
    # Colunas dos relatorio
    nColDad1 = nColIni
    nColDad2 = nColIni + 50
    nColDad3 = nColIni + 150
    nColDad4 = nColIni + 200
    nColDad5 = nColIni + 300
    # Declarando as fontes
    cNomeFont = 'Arial'
    oFontDet = TFont().New(cNomeFont, 9, -11, True, False, 5, True, 5, True, False)
    oFontDetN = TFont().New(cNomeFont, 9, -13, True, True, 5, True, 5, True, False)
    oFontRod = TFont().New(cNomeFont, 9, -8, True, False, 5, True, 5, True, False)
    oFontMin = TFont().New(cNomeFont, 9, -7, True, False, 5, True, 5, True, False)
    oFontTit = TFont().New(cNomeFont, 9, -15, True, True, 5, True, 5, True, False)
    # Monta a consulta de dados
    cQryAux += 'SELECT ' + CRLF
    cQryAux += ' B1_COD, ' + CRLF
    cQryAux += ' B1_DESC, ' + CRLF
    cQryAux += ' B1_GRUPO, ' + CRLF
    cQryAux += ' BM_DESC ' + CRLF
    cQryAux += 'FROM ' + CRLF
    cQryAux += ' SB1990 SB1 ' + CRLF
    cQryAux += ' INNER JOIN SBM990 SBM ON ( ' + CRLF
    cQryAux += " BM_FILIAL = '01' " + CRLF
    cQryAux += ' AND BM_GRUPO = B1_GRUPO ' + CRLF
    cQryAux += " AND SBM.D_E_L_E_T_ = ' ' " + CRLF
    cQryAux += ' ) ' + CRLF
    cQryAux += 'WHERE ' + CRLF
    cQryAux += " B1_FILIAL = '' " + CRLF
    cQryAux += " AND B1_COD >= '" + MV_PAR01 + "' " + CRLF
    cQryAux += " AND B1_COD <= '" + MV_PAR02 + "' " + CRLF
    cQryAux += " AND B1_MSBLQL != '1' " + CRLF
    cQryAux += " AND SB1.D_E_L_E_T_ = ' '" + CRLF
    PLSQuery(cQryAux, 'QRY_AUX')
    # Define o tamanho da régua
    DbSelectArea('QRY_AUX')
    QRY_AUX.DbGoTop()
    Count
    to
    nTotAux
    ProcRegua(nTotAux)
    QRY_AUX.DbGoTop()
    # Somente se tiver dados
    if not QRY_AUX.EoF():
        # Criando o objeto de impressao
        oPrintPvt = FWMSPrinter().New(cArquivo, IMP_PDF, False, None, True, None, ref_(oPrintPvt), None, None, None, None, True)
        oPrintPvt.cPathPDF = GetTempPath()
        oPrintPvt.SetResolution(72)
        oPrintPvt.SetPortrait()
        oPrintPvt.SetPaperSize(DMPAPER_A4)
        oPrintPvt.SetMargin(0, 0, 0, 0)
        # Imprime os dados
        fImpCab()
        while not QRY_AUX.EoF():
            nAtuAux += 1
            IncProc('Imprimindo registro ' + cValToChar(nAtuAux) + ' de ' + cValToChar(nTotAux) + '...')
            # Se atingiu o limite, quebra de pagina
            fQuebra()
            # Faz o zebrado ao fundo
            if nAtuAux % 2 == 0:
                oPrintPvt.FillRect([nLinAtu - 2, nColIni, nLinAtu + 12, nColFin], oBrushLin)

            # Imprime a linha atual
            oPrintPvt.SayAlign(nLinAtu, nColDad1, Alltrim(QRY_AUX.B1_COD), oFontDet, 50, 10, None, PAD_LEFT, None, None)
            oPrintPvt.SayAlign(nLinAtu, nColDad2, Alltrim(QRY_AUX.B1_DESC), oFontDetN, 100, 10, None, PAD_LEFT, None, None)
            oPrintPvt.SayAlign(nLinAtu, nColDad3, Alltrim(QRY_AUX.B1_GRUPO), oFontDet, 50, 10, None, PAD_LEFT, None, None)
            oPrintPvt.SayAlign(nLinAtu, nColDad4, Alltrim(QRY_AUX.BM_DESC), oFontDet, 100, 10, None, PAD_LEFT, None, None)
            nLinAtu += 15
            oPrintPvt.Line(nLinAtu - 3, nColIni, nLinAtu - 3, nColFin, nCorCinza)
            # Se atingiu o limite, quebra de pagina
            fQuebra()
            QRY_AUX.DbSkip()

        fImpRod()
        oPrintPvt.Preview()
    else:
        MsgStop('Não foi encontrado informações com os parâmetros informados!', 'Atenção')

    QRY_AUX.DbCloseArea()
    RestArea(aArea)
    return Static

def fLogoEmp():
    cGrpCompany = AllTrim(FWGrpCompany())
    cCodEmpGrp = AllTrim(FWCodEmp())
    cUnitGrp = AllTrim(FWUnitBusiness())
    cFilGrp = AllTrim(FWFilial())
    cLogo = ''
    cCamFim = GetTempPath()
    cStart = GetSrvProfString('Startpath', '')
    # Se tiver filiais por grupo de empresas
    if not Empty(cUnitGrp):
        cDescLogo = cGrpCompany + cCodEmpGrp + cUnitGrp + cFilGrp
        # Senão, será apenas, empresa + filial
    else:
        cDescLogo = cEmpAnt + cFilAnt

    # Pega a imagem
    cLogo = cStart + 'DANFE' + cDescLogo + '.BMP'
    # Se o arquivo não existir, pega apenas o da empresa, desconsiderando a filial
    if not File(cLogo):
        cLogo = cStart + 'DANFE' + cEmpAnt + '.BMP'

    # Copia para a temporária do s.o.
    CpyS2T(cLogo, cCamFim)
    cLogo = cCamFim + StrTran(cLogo, cStart, '')
    # Se o arquivo não existir na temporária, espera meio segundo para terminar a cópia
    if not File(cLogo):
        Sleep(500)

    return cLogo
    # {Protheus.doc} fImpCab
    # Função que imprime o cabeçalho do relatório
    # @author Atilio
    # @since 20/02/2023
    # @version 1.0
    # @type function
    # @obs Codigo gerado automaticamente pelo Autumn Code Maker
    # @see http://autumncodemaker.com

def s_fImpCab():
    cTexto = ''
    nLinCab = 15
    # Iniciando Pagina
    oPrintPvt.StartPage()
    # Imprime o logo
    if File(cLogoEmp):
        oPrintPvt.SayBitmap(5, nColIni, cLogoEmp, 30, 30)

    # Cabecalho
    cTexto = 'Produtos e Grupos'
    oPrintPvt.SayAlign(nLinCab, nColMeio - 200, cTexto, oFontTit, 400, 20, None, PAD_CENTER, None, None)
    # Linha Separatoria
    nLinCab += 20
    oPrintPvt.Line(nLinCab, nColIni, nLinCab, nColFin)
    # Atualizando a linha inicial do relatorio
    nLinAtu = nLinCab + 5
    if nPagAtu == 1:
        # Imprimindo os parâmetros
        oPrintPvt.SayAlign(nLinAtu, nColIni, 'Produto De', oFontDetN, 200, 10, None, PAD_LEFT, None, None)
        oPrintPvt.SayAlign(nLinAtu, nColIni + 200, MV_PAR01, oFontDet, 200, 10, None, PAD_LEFT, None, None)
        nLinAtu += 15
        oPrintPvt.SayAlign(nLinAtu, nColIni, 'Produto Até', oFontDetN, 200, 10, None, PAD_LEFT, None, None)
        oPrintPvt.SayAlign(nLinAtu, nColIni + 200, MV_PAR02, oFontDet, 200, 10, None, PAD_LEFT, None, None)
        nLinAtu += 15
        oPrintPvt.Line(nLinAtu - 3, nColIni, nLinAtu - 3, nColFin, nCorCinza)
        nLinAtu += 5

    oPrintPvt.SayAlign(nLinAtu, nColDad1, 'Produto', oFontMin, 50, 10, None, PAD_LEFT, None, None)
    oPrintPvt.SayAlign(nLinAtu, nColDad2, 'Descrição', oFontMin, 100, 10, None, PAD_LEFT, None, None)
    oPrintPvt.SayAlign(nLinAtu, nColDad3, 'Grupo', oFontMin, 50, 10, None, PAD_LEFT, None, None)
    oPrintPvt.SayAlign(nLinAtu, nColDad4, 'Grp. Descrição', oFontMin, 100, 10, None, PAD_LEFT, None, None)
    nLinAtu += 15
    return Static

def fImpRod():
    nLinRod = nLinFin
    cTexto = ''
    # Linha Separatoria
    oPrintPvt.Line(nLinRod, nColIni, nLinRod, nColFin)
    nLinRod += 3
    # Dados da Esquerda
    cTexto = dToC(dDataBase) + '     ' + cHoraEx + '     ' + FunName() + ' (zExe236)     ' + UsrRetName(RetCodUsr())
    oPrintPvt.SayAlign(nLinRod, nColIni, cTexto, oFontRod, 500, 10, None, PAD_LEFT, None, None)
    # Direita
    cTexto = 'Pagina ' + cValToChar(nPagAtu)
    oPrintPvt.SayAlign(nLinRod, nColFin - 40, cTexto, oFontRod, 40, 10, None, PAD_RIGHT, None, None)
    # Finalizando a pagina e somando mais um
    oPrintPvt.EndPage()
    nPagAtu += 1
    return Static

def fQuebra():
    if nLinAtu >= nLinFin - 10:
        fImpRod()
        fImpCab()

    return
