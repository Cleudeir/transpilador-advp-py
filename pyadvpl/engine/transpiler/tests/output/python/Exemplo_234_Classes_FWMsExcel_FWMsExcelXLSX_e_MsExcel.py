# Esse exemplo faz parte da série do YouTube, Maratona de Exemplos, do canal Terminal de Informação, 
#     caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2024/02/14/abrindo-telas-de-processamento-com-fwmsgrun-e-msgrun-maratona-advpl-e-tl-235/
# Bibliotecas
# PREPROCESSOR: #Include "Totvs.ch"
# PREPROCESSOR: #Include "FWMVCDef.ch"
# {Protheus.doc} User Function zExe234
# Gera um arquivo do Excel e abre
# @type Function
# @author Atilio
# @since 20/02/2023
# @see https://tdn.totvs.com/display/public/framework/FWMsExcel e https://tdn.totvs.com/display/public/framework/FWMsExcelXlsx
# @obs 
# 
#     **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
def u_zExe234():
    aArea = FWGetArea()
    aPergs = []
    cProdDe = Space(TamSX3('B1_COD')[1])
    cProdAte = StrTran(cProdDe, ' ', 'Z')
    cTipoDe = Space(TamSX3('B1_TIPO')[1])
    cTipoAte = StrTran(cTipoDe, ' ', 'Z')
    nOrden = 1
    nTipoRel = 1
    # Adicionando os parametros do ParamBox
    aAdd(aPergs, [1, 'Produto De', cProdDe, '', '.T.', 'SB1', '.T.', 80, False])
    # MV_PAR01
    aAdd(aPergs, [1, 'Produto Até', cProdAte, '', '.T.', 'SB1', '.T.', 80, True])
    # MV_PAR02
    aAdd(aPergs, [1, 'Tipo De', cTipoDe, '', '.T.', '02', '.T.', 40, False])
    # MV_PAR03
    aAdd(aPergs, [1, 'Tipo Até', cTipoAte, '', '.T.', '02', '.T.', 40, True])
    # MV_PAR04
    aAdd(aPergs, [2, 'Ordenar por', nOrden, ['1=Código do Produto', '2=Descrição do Produto', '3=Unidade de Medida'], 100, '.T.', True])
    # MV_PAR05
    aAdd(aPergs, [2, 'Tipo Relat.', nTipoRel, ['1=Excel XML', '2=Excel XLSX'], 80, '.T.', True])
    # MV_PAR06
    # Se a pergunta for confirma, cria as definicoes do relatorio
    if ParamBox(aPergs, 'Informe os parâmetros', None, None, None, None, None, None, None, None, False, False):
        MV_PAR05 = Val(cValToChar(MV_PAR05))
        MV_PAR06 = Val(cValToChar(MV_PAR06))
        Processa(lambda : fGeraExcel())

    FWRestArea(aArea)
    return Static

def fGeraExcel():
    cQryDad = ''
    oFWMsExcel = None
    oExcel = None
    cArquivo = GetTempPath() + 'zRel21.xml'
    cWorkSheet = 'Produtos'
    cTitulo = 'Listagem de Produtos'
    nAtual = 0
    nTotal = 0
    # Montando consulta de dados
    cQryDad = 'SELECT ' + CRLF
    cQryDad += '    B1_COD, ' + CRLF
    cQryDad += '    B1_DESC, ' + CRLF
    cQryDad += '    B1_TIPO, ' + CRLF
    cQryDad += "    ISNULL(X5_DESCRI, '') AS TIPODESCR, " + CRLF
    cQryDad += '    B1_UM, ' + CRLF
    cQryDad += "    ISNULL(AH_DESCPO, '') AS UMDESCR, " + CRLF
    cQryDad += '    B1_PESO ' + CRLF
    cQryDad += 'FROM ' + CRLF
    cQryDad += '    ' + RetSQLName('SB1') + ' SB1 ' + CRLF
    cQryDad += '    LEFT JOIN ' + RetSQLName('SX5') + ' SX5 ON ( ' + CRLF
    cQryDad += "       X5_FILIAL = '" + FWxFilial('SX5') + "' " + CRLF
    cQryDad += "       AND X5_TABELA = '02' " + CRLF
    cQryDad += '       AND X5_CHAVE = B1_TIPO ' + CRLF
    cQryDad += "       AND SX5.D_E_L_E_T_ = ' ' " + CRLF
    cQryDad += '    ) ' + CRLF
    cQryDad += '    LEFT JOIN ' + RetSQLName('SAH') + ' SAH ON ( ' + CRLF
    cQryDad += "       AH_FILIAL = '" + FWxFilial('SAH') + "' " + CRLF
    cQryDad += '       AND AH_UNIMED = B1_UM ' + CRLF
    cQryDad += "       AND SAH.D_E_L_E_T_ = ' ' " + CRLF
    cQryDad += '    ) ' + CRLF
    cQryDad += 'WHERE ' + CRLF
    cQryDad += "    B1_FILIAL = '" + FWxFilial('SB1') + "' " + CRLF
    cQryDad += "    AND B1_COD >= '" + MV_PAR01 + "' " + CRLF
    cQryDad += "    AND B1_COD <= '" + MV_PAR02 + "' " + CRLF
    cQryDad += "    AND B1_TIPO >= '" + MV_PAR03 + "' " + CRLF
    cQryDad += "    AND B1_TIPO <= '" + MV_PAR04 + "' " + CRLF
    cQryDad += "    AND B1_MSBLQL != '1' " + CRLF
    cQryDad += "    AND SB1.D_E_L_E_T_ = ' ' " + CRLF
    cQryDad += 'ORDER BY ' + CRLF
    cQryDad += '    B1_TIPO, ' + CRLF
    if MV_PAR05 == 1:
        cQryDad += '    B1_COD ' + CRLF
    elif MV_PAR05 == 2:
        cQryDad += '    B1_DESC ' + CRLF
    elif MV_PAR05 == 3:
        cQryDad += '    B1_UM ' + CRLF

    # Executando consulta e setando o total da regua
    PlsQuery(cQryDad, 'QRY_DAD')
    DbSelectArea('QRY_DAD')
    # Cria a planilha do excel
    if MV_PAR06 == 1:
        oFWMsExcel = FWMSExcel().New()
    elif MV_PAR06 == 2:
        oFWMsExcel = FWMSExcelXLSX().New()

    # Criando a aba da planilha
    oFWMsExcel.AddworkSheet(cWorkSheet)
    # Criando a Tabela e as colunas
    oFWMsExcel.AddTable(cWorkSheet, cTitulo)
    oFWMsExcel.AddColumn(cWorkSheet, cTitulo, 'Produto', 1, 1, False)
    oFWMsExcel.AddColumn(cWorkSheet, cTitulo, 'Descrição', 1, 1, False)
    oFWMsExcel.AddColumn(cWorkSheet, cTitulo, 'Tipo', 1, 1, False)
    oFWMsExcel.AddColumn(cWorkSheet, cTitulo, 'Tp. Descrição', 1, 1, False)
    oFWMsExcel.AddColumn(cWorkSheet, cTitulo, 'UM', 1, 1, False)
    oFWMsExcel.AddColumn(cWorkSheet, cTitulo, 'UM Descrição', 1, 1, False)
    oFWMsExcel.AddColumn(cWorkSheet, cTitulo, 'Peso', 3, 2, False)
    # Definindo o tamanho da regua
    Count
    To
    nTotal
    ProcRegua(nTotal)
    QRY_DAD.DbGoTop()
    # Percorrendo os dados da query
    while not QRY_DAD.EoF():
        # Incrementando a regua
        nAtual += 1
        IncProc('Adicionando registro ' + cValToChar(nAtual) + ' de ' + cValToChar(nTotal) + '...')
        # Adicionando uma nova linha
        oFWMsExcel.AddRow(cWorkSheet, cTitulo, [QRY_DAD.B1_COD, QRY_DAD.B1_DESC, QRY_DAD.B1_TIPO, QRY_DAD.TIPODESCR, QRY_DAD.B1_UM, QRY_DAD.UMDESCR, QRY_DAD.B1_PESO])
        QRY_DAD.DbSkip()

    QRY_DAD.DbCloseArea()
    # Ativando o arquivo e gerando o xml
    oFWMsExcel.Activate()
    oFWMsExcel.GetXMLFile(cArquivo)
    # Abrindo o excel e abrindo o arquivo xml
    oExcel = MsExcel().New()
    oExcel.WorkBooks().Open(cArquivo)
    oExcel.SetVisible(True)
    oExcel.Destroy()
    return
