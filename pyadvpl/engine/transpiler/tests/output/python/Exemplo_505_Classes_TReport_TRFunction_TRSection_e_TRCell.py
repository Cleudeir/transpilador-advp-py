# Esse exemplo faz parte da série do YouTube, Maratona de Exemplos, do canal Terminal de Informação, 
#     caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2024/06/28/quebrando-um-endereco-em-partes-atraves-da-trataend-maratona-advpl-e-tl-504/
# Bibliotecas
# PREPROCESSOR: #Include "TOTVS.ch"
# {Protheus.doc} User Function zExe505
# Classes para montagem de um relatório com listagem de informações
# @type Function
# @author Atilio
# @since 04/04/2023
# @see https://tdn.totvs.com/display/public/framework/TReport e https://tdn.totvs.com/display/public/framework/TRSection e https://tdn.totvs.com/display/public/framework/TRFunction e https://tdn.totvs.com/display/public/framework/TRCell
# @obs 
# 
#     **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
def u_zExe505():
    aArea = FWGetArea()
    oReport = None
    aPergs = []
    cProdDe = Space(TamSX3('B1_COD')[1])
    cProdAte = StrTran(cProdDe, ' ', 'Z')
    cTipoDe = Space(TamSX3('B1_TIPO')[1])
    cTipoAte = StrTran(cTipoDe, ' ', 'Z')
    nOrden = 1
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
    # Se a pergunta for confirma, cria as definicoes do relatorio
    if ParamBox(aPergs, 'Informe os parâmetros', None, None, None, None, None, None, None, None, False, False):
        MV_PAR05 = Val(cValToChar(MV_PAR05))
        oReport = fReportDef()
        oReport.PrintDialog()

    FWRestArea(aArea)
    return Static

def fReportDef():
    oReport = None
    oSection = None
    # Criacao do componente de impressao
    oReport = TReport().New('zRel02', 'Relatório de Produto', None, lambda oReport: fRepPrint(oReport))
    oReport.SetTotalInLine(False)
    oReport.lParamPage = False
    oReport.oPage().SetPaperSize(9)
    # Orientacao do Relatorio
    oReport.SetPortrait()
    # Definicoes da fonte utilizada
    oReport.SetLineHeight(50)
    oReport.nFontBody = 12
    # Criando a secao de dados
    oSection = TRSection().New(oReport, 'Dados', ['QRY_REP'])
    oSection.SetTotalInLine(False)
    # Colunas do relatorio
    TRCell().New(oSection, 'B1_COD', 'QRY_REP', 'Codigo', None, 15, None, None, 'LEFT', None, 'LEFT', None, None, None, None, None, True)
    TRCell().New(oSection, 'B1_DESC', 'QRY_REP', 'Descricao', None, 30, None, None, 'LEFT', None, 'LEFT', None, None, None, None, None, False)
    TRCell().New(oSection, 'B1_TIPO', 'QRY_REP', 'Tipo', None, 2, None, None, 'LEFT', None, 'LEFT', None, None, None, None, None, False)
    TRCell().New(oSection, 'TIPODESCR', 'QRY_REP', 'Tp. Descr.', None, 55, None, None, 'LEFT', None, 'LEFT', None, None, None, None, None, False)
    TRCell().New(oSection, 'B1_UM', 'QRY_REP', 'Unid. Med.', None, 2, None, None, 'LEFT', None, 'LEFT', None, None, None, None, None, False)
    TRCell().New(oSection, 'UMDESCR', 'QRY_REP', 'UM. Descr.', None, 40, None, None, 'LEFT', None, 'LEFT', None, None, None, None, None, False)
    # Quebras do relatorio
    oBreak = TRBreak().New(oSection, oSection.Cell('B1_TIPO'), lambda : 'Total da Quebra', False)
    # Totalizadores
    TRFunction().New(oSection.Cell('B1_COD'), None, 'COUNT', None, None, '@E 999,999,999', None, False)
    return oReport

def s_fRepPrint(oReport):
    aArea = FWGetArea()
    cQryReport = ''
    oSectDad = None
    nAtual = 0
    nTotal = 0
    # Pegando as secoes do relatorio
    oSectDad = oReport.Section(1)
    # Montando consulta de dados
    cQryReport += 'SELECT ' + CRLF
    cQryReport += '    B1_COD, ' + CRLF
    cQryReport += '    B1_DESC, ' + CRLF
    cQryReport += '    B1_TIPO, ' + CRLF
    cQryReport += "    ISNULL(X5_DESCRI, '') AS TIPODESCR, " + CRLF
    cQryReport += '    B1_UM, ' + CRLF
    cQryReport += "    ISNULL(AH_DESCPO, '') AS UMDESCR " + CRLF
    cQryReport += 'FROM ' + CRLF
    cQryReport += '    ' + RetSQLName('SB1') + ' SB1 ' + CRLF
    cQryReport += '    LEFT JOIN ' + RetSQLName('SX5') + ' SX5 ON ( ' + CRLF
    cQryReport += "       X5_FILIAL = '" + FWxFilial('SX5') + "' " + CRLF
    cQryReport += "       AND X5_TABELA = '02' " + CRLF
    cQryReport += '       AND X5_CHAVE = B1_TIPO ' + CRLF
    cQryReport += "       AND SX5.D_E_L_E_T_ = ' ' " + CRLF
    cQryReport += '    ) ' + CRLF
    cQryReport += '    LEFT JOIN ' + RetSQLName('SAH') + ' SAH ON ( ' + CRLF
    cQryReport += "       AH_FILIAL = '" + FWxFilial('SAH') + "' " + CRLF
    cQryReport += '       AND AH_UNIMED = B1_UM ' + CRLF
    cQryReport += "       AND SAH.D_E_L_E_T_ = ' ' " + CRLF
    cQryReport += '    ) ' + CRLF
    cQryReport += 'WHERE ' + CRLF
    cQryReport += "    B1_FILIAL = '" + FWxFilial('SB1') + "' " + CRLF
    cQryReport += "    AND B1_COD >= '" + MV_PAR01 + "' " + CRLF
    cQryReport += "    AND B1_COD <= '" + MV_PAR02 + "' " + CRLF
    cQryReport += "    AND B1_TIPO >= '" + MV_PAR03 + "' " + CRLF
    cQryReport += "    AND B1_TIPO <= '" + MV_PAR04 + "' " + CRLF
    cQryReport += "    AND B1_MSBLQL != '1' " + CRLF
    cQryReport += "    AND SB1.D_E_L_E_T_ = ' ' " + CRLF
    cQryReport += 'ORDER BY ' + CRLF
    cQryReport += '    B1_TIPO, ' + CRLF
    if MV_PAR05 == 1:
        cQryReport += '    B1_COD ' + CRLF
    elif MV_PAR05 == 2:
        cQryReport += '    B1_DESC ' + CRLF
    elif MV_PAR05 == 3:
        cQryReport += '    B1_UM ' + CRLF

    # Executando consulta e setando o total da regua
    PlsQuery(cQryReport, 'QRY_REP')
    DbSelectArea('QRY_REP')
    Count
    to
    nTotal
    oReport.SetMeter(nTotal)
    # Enquanto houver dados
    oSectDad.Init()
    QRY_REP.DbGoTop()
    while not QRY_REP.Eof():
        # Incrementando a regua
        nAtual += 1
        oReport.SetMsgPrint('Imprimindo registro ' + cValToChar(nAtual) + ' de ' + cValToChar(nTotal) + '...')
        oReport.IncMeter()
        # Imprimindo a linha atual
        oSectDad.PrintLine()
        QRY_REP.DbSkip()

    oSectDad.Finish()
    QRY_REP.DbCloseArea()
    FWRestArea(aArea)
    return
