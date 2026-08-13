# Esse exemplo faz parte da série do YouTube, Maratona de Exemplos, do canal Terminal de Informação, 
#     caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2024/02/04/criando-camadas-dentro-de-uma-dialog-com-fwdefsize-e-fwlayer-maratona-advpl-e-tl-214/
# Bibliotecas
# PREPROCESSOR: #Include "TOTVS.ch"
# {Protheus.doc} User Function zExe214
# Exemplo de função que cria uma tela com dimensionamentos responsivos
# @type Function
# @author Atilio
# @since 20/02/2023
# @see https://tdn.totvs.com/display/public/framework/FWDefSize e https://tdn.totvs.com/display/public/framework/FWLayer
# @obs 
# 
#     **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
def u_zExe214():
    aArea = FWGetArea()
    if FWAlertYesNo('Você deseja ver o exemplo com FWLayer (sim) ou com FWDefSize (não)?', 'Continua?'):
        fExemplo1()
    else:
        fExemplo2()

    FWRestArea(aArea)
    return Static

def fExemplo1():
    nLargBtn = 50
    nLinhaObj = 0
    nLargPanel = 0
    # Objetos e componentes gerais
    oDlgExemp = None
    oFwLayer = None
    oPanTitulo = None
    oPanGrid = None
    oPanCheck = None
    oPanTotal = None
    cMascara = '@E 999,999,999,999,999.99'
    # Cabeçalho
    oSayModulo = None
    cSayModulo = 'TST'
    oSayTitulo = None
    cSayTitulo = "'Exemplo de Tela com"
    oSaySubTit = None
    cSaySubTit = 'Objetos gráficos usando FWLayer'
    # Tamanho da janela
    aSize = MsAdvSize(False)
    nJanLarg = aSize[5]
    nJanAltu = aSize[6]
    # Fontes
    cFontUti = 'Tahoma'
    oFontMod = TFont().New(cFontUti, None, -38)
    oFontSub = TFont().New(cFontUti, None, -20)
    oFontSubN = TFont().New(cFontUti, None, -20, None, True)
    oFontBtn = TFont().New(cFontUti, None, -14)
    oFontSay = TFont().New(cFontUti, None, -12)
    # Grid
    aCampos = []
    cAliasTmp = 'TST_' + RetCodUsr()
    aColunas = []
    oMarkBrowse = None
    # Componentes da segunda coluna
    oSayChkDes = None
    oSayChkPer = None
    oSayChkVlr = None
    oCheck01 = None
    lCheck01 = False
    oGetPerc01 = None
    nGetPerc01 = 0
    oGetTot01 = None
    nGetTot01 = 0
    oCheck02 = None
    lCheck02 = False
    oGetPerc02 = None
    nGetPerc02 = 0
    oGetTot02 = None
    nGetTot02 = 0
    oCheck03 = None
    lCheck03 = False
    oGetPerc03 = None
    nGetPerc03 = 0
    oGetTot03 = None
    nGetTot03 = 0
    oCheck04 = None
    lCheck04 = False
    oGetPerc04 = None
    nGetPerc04 = 0
    oGetTot04 = None
    nGetTot04 = 0
    oCheck05 = None
    lCheck05 = False
    oGetPerc05 = None
    nGetPerc05 = 0
    oGetTot05 = None
    nGetTot05 = 0
    # Componentes da terceira coluna
    oSayTot = None
    cSayTot = 'Total marcado:'
    oGetTot = None
    nGetTot = 0
    oSayApu = None
    cSayApu = '% Apurado:'
    oGetApu = None
    nGetApu = 0
    oSayPro = None
    cSayPro = 'Total que será processado:'
    oGetPro = None
    nGetPro = 0
    oBtnProc = None
    oBtnPrev = None
    # Adiciona as colunas que serão criadas na temporária
    aAdd(aCampos, ['OK', 'C', 2, 0])
    aAdd(aCampos, ['CONTA', 'C', 10, 0])
    aAdd(aCampos, ['VALOR', 'N', 18, 2])
    # Cria a tabela temporária
    oTempTable = FWTemporaryTable().New(cAliasTmp)
    oTempTable.SetFields(aCampos)
    oTempTable.Create()
    # Busca as colunas do browse
    aColunas = fCriaCols()
    # Popula a tabela temporária
    Processa(lambda : fPopula(), 'Processando...')
    # Cria a janela
    DEFINE
    MSDIALOG
    oDlgExemp
    TITLE
    'Exemplo de Tela com Objetos gráficos usando FWLayer'
    FROM_
    0
    # ,
    0
    TO
    nJanAltu
    # ,
    nJanLarg
    PIXEL
    # Criando a camada
    oFwLayer = FwLayer().New()
    oFwLayer.init(oDlgExemp, False)
    # Adicionando 3 linhas, a de título, a do corpo e a inferior
    oFWLayer.addLine('TITULO', 10, False)
    oFWLayer.addLine('CORPO', 88, False)
    oFWLayer.addLine('RODAPE', 2, False)
    # Adicionando as colunas das linhas
    oFWLayer.addCollumn('HEADERTEXT', 50, True, 'TITULO')
    oFWLayer.addCollumn('BLANKBTN', 40, True, 'TITULO')
    oFWLayer.addCollumn('BTNSAIR', 10, True, 'TITULO')
    oFWLayer.addCollumn('BLANKANTES', 1, True, 'CORPO')
    oFWLayer.addCollumn('COLGRID', 39, True, 'CORPO')
    oFWLayer.addCollumn('COLCHECK', 40, True, 'CORPO')
    oFWLayer.addCollumn('COLTOTAL', 19, True, 'CORPO')
    oFWLayer.addCollumn('BLANKDEPOIS', 1, True, 'CORPO')
    # Criando os paineis
    oPanHeader = oFWLayer.GetColPanel('HEADERTEXT', 'TITULO')
    oPanSair = oFWLayer.GetColPanel('BTNSAIR', 'TITULO')
    oPanGrid = oFWLayer.GetColPanel('COLGRID', 'CORPO')
    oPanCheck = oFWLayer.GetColPanel('COLCHECK', 'CORPO')
    oPanTotal = oFWLayer.GetColPanel('COLTOTAL', 'CORPO')
    # Títulos e SubTítulos
    oSayModulo = TSay().New(4, 3, lambda : cSayModulo, oPanHeader, '', oFontMod, None, None, None, True, RGB(149, 179, 215), None, 200, 30, None, None, None, None, None, False, None)
    oSayTitulo = TSay().New(4, 45, lambda : cSayTitulo, oPanHeader, '', oFontSub, None, None, None, True, RGB(31, 73, 125), None, 200, 30, None, None, None, None, None, False, None)
    oSaySubTit = TSay().New(14, 45, lambda : cSaySubTit, oPanHeader, '', oFontSubN, None, None, None, True, RGB(31, 73, 125), None, 300, 30, None, None, None, None, None, False, None)
    # Criando os botões
    oBtnSair = TButton().New(6, 1, 'Fechar', oPanSair, lambda : oDlgExemp.End(), nLargBtn, 18, None, oFontBtn, None, True, None, None, None, None, None)
    # Cria a grid
    oMarkBrowse = FWMarkBrowse().New()
    oMarkBrowse.SetAlias(cAliasTmp)
    oMarkBrowse.DisableFilter()
    oMarkBrowse.DisableConfig()
    oMarkBrowse.DisableReport()
    oMarkBrowse.DisableSeek()
    oMarkBrowse.DisableSaveConfig()
    oMarkBrowse.SetFontBrowse(oFontSay)
    oMarkBrowse.SetFieldMark('OK')
    oMarkBrowse.SetTemporary(True)
    oMarkBrowse.SetColumns(aColunas)
    oMarkBrowse.SetOwner(oPanGrid)
    oMarkBrowse.Activate()
    # Cria os componentes da segunda coluna
    # RAW: @ 001 , 001 SCROLLBOX oScroll VERTICAL HORIZONTAL SIZE oPanCheck : nHeight / 2 , oPanCheck : nWidth / 2 OF oPanCheck
    nLinhaObj = 1
    nLargPanel = oPanCheck.nWidth() / 2
    nTotEspCol = nLargPanel / 3
    nTotCol01 = 3 + nTotEspCol * 0
    nTotCol02 = 3 + nTotEspCol * 1
    nTotCol03 = 3 + nTotEspCol * 2
    oSayChkDes = TSay().New(nLinhaObj, 1 + nTotCol01, lambda : 'Descrição', oScroll, '', oFontSay, None, None, None, True, RGB(31, 73, 125), None, nTotEspCol, 10, None, None, None, None, None, False, None)
    oSayChkPer = TSay().New(nLinhaObj, 1 + nTotCol02, lambda : '%', oScroll, '', oFontSay, None, None, None, True, RGB(31, 73, 125), None, nTotEspCol, 10, None, None, None, None, None, False, None)
    oSayChkVlr = TSay().New(nLinhaObj, 1 + nTotCol03, lambda : 'Valor', oScroll, '', oFontSay, None, None, None, True, RGB(31, 73, 125), None, nTotEspCol, 10, None, None, None, None, None, False, None)
    nLinhaObj += 25
    oCheck01 = TCheckBox().New(nLinhaObj, 3 + nTotCol01, 'Check 01', lambda u: ((lCheck01 := u) if PCount() > 0 else lCheck01), oScroll, nTotEspCol - 3, 10, None, None, oFontSay, None, None, None, None, True)
    oGetPerc01 = TGet().New(nLinhaObj, 3 + nTotCol02, lambda u: ((nGetPerc01 := u) if PCount() > 0 else nGetPerc01), oScroll, nTotEspCol - 9, 10, cMascara, None, None, None, oFontSay, None, None, True)
    oGetTot01 = TGet().New(nLinhaObj, 3 + nTotCol03, lambda u: ((nGetTot01 := u) if PCount() > 0 else nGetTot01), oScroll, nTotEspCol - 9, 10, cMascara, None, None, None, oFontSay, None, None, True)
    oGetTot01.lActive = False
    nLinhaObj += 15
    oCheck02 = TCheckBox().New(nLinhaObj, 3 + nTotCol01, 'Check 02', lambda u: ((lCheck02 := u) if PCount() > 0 else lCheck02), oScroll, nTotEspCol - 3, 10, None, None, oFontSay, None, None, None, None, True)
    oGetPerc02 = TGet().New(nLinhaObj, 3 + nTotCol02, lambda u: ((nGetPerc02 := u) if PCount() > 0 else nGetPerc02), oScroll, nTotEspCol - 9, 10, cMascara, None, None, None, oFontSay, None, None, True)
    oGetTot02 = TGet().New(nLinhaObj, 3 + nTotCol03, lambda u: ((nGetTot02 := u) if PCount() > 0 else nGetTot02), oScroll, nTotEspCol - 9, 10, cMascara, None, None, None, oFontSay, None, None, True)
    oGetTot02.lActive = False
    nLinhaObj += 15
    oCheck03 = TCheckBox().New(nLinhaObj, 3 + nTotCol01, 'Check 03', lambda u: ((lCheck03 := u) if PCount() > 0 else lCheck03), oScroll, nTotEspCol - 3, 10, None, None, oFontSay, None, None, None, None, True)
    oGetPerc03 = TGet().New(nLinhaObj, 3 + nTotCol02, lambda u: ((nGetPerc03 := u) if PCount() > 0 else nGetPerc03), oScroll, nTotEspCol - 9, 10, cMascara, None, None, None, oFontSay, None, None, True)
    oGetTot03 = TGet().New(nLinhaObj, 3 + nTotCol03, lambda u: ((nGetTot03 := u) if PCount() > 0 else nGetTot03), oScroll, nTotEspCol - 9, 10, cMascara, None, None, None, oFontSay, None, None, True)
    oGetTot03.lActive = False
    nLinhaObj += 15
    oCheck04 = TCheckBox().New(nLinhaObj, 3 + nTotCol01, 'Check 04', lambda u: ((lCheck04 := u) if PCount() > 0 else lCheck04), oScroll, nTotEspCol - 3, 10, None, None, oFontSay, None, None, None, None, True)
    oGetPerc04 = TGet().New(nLinhaObj, 3 + nTotCol02, lambda u: ((nGetPerc04 := u) if PCount() > 0 else nGetPerc04), oScroll, nTotEspCol - 9, 10, cMascara, None, None, None, oFontSay, None, None, True)
    oGetTot04 = TGet().New(nLinhaObj, 3 + nTotCol03, lambda u: ((nGetTot04 := u) if PCount() > 0 else nGetTot04), oScroll, nTotEspCol - 9, 10, cMascara, None, None, None, oFontSay, None, None, True)
    oGetTot04.lActive = False
    nLinhaObj += 15
    oCheck05 = TCheckBox().New(nLinhaObj, 3 + nTotCol01, 'Check 05', lambda u: ((lCheck05 := u) if PCount() > 0 else lCheck05), oScroll, nTotEspCol - 3, 10, None, None, oFontSay, None, None, None, None, True)
    oGetPerc05 = TGet().New(nLinhaObj, 3 + nTotCol02, lambda u: ((nGetPerc05 := u) if PCount() > 0 else nGetPerc05), oScroll, nTotEspCol - 9, 10, cMascara, None, None, None, oFontSay, None, None, True)
    oGetTot05 = TGet().New(nLinhaObj, 3 + nTotCol03, lambda u: ((nGetTot05 := u) if PCount() > 0 else nGetTot05), oScroll, nTotEspCol - 9, 10, cMascara, None, None, None, oFontSay, None, None, True)
    oGetTot05.lActive = False
    # Cria os componentes da terceira coluna
    nLargPanel = oPanTotal.nWidth() / 2
    nLinhaObj = 30
    oSayTot = TSay().New(nLinhaObj, 3, lambda : cSayTot, oPanTotal, '', oFontSay, None, None, None, True, RGB(31, 73, 125), None, 200, 10, None, None, None, None, None, False, None)
    nLinhaObj += 10
    oGetTot = TGet().New(nLinhaObj, 13, lambda u: ((nGetTot := u) if PCount() > 0 else nGetTot), oPanTotal, nLargPanel - 25, 15, cMascara, None, None, None, oFontSay, None, None, True)
    oGetTot.lReadOnly = True
    nLinhaObj += 25
    oSayApu = TSay().New(nLinhaObj, 3, lambda : cSayApu, oPanTotal, '', oFontSay, None, None, None, True, RGB(31, 73, 125), None, 200, 10, None, None, None, None, None, False, None)
    nLinhaObj += 10
    oGetApu = TGet().New(nLinhaObj, 13, lambda u: ((nGetApu := u) if PCount() > 0 else nGetApu), oPanTotal, nLargPanel - 25, 15, cMascara, None, None, None, oFontSay, None, None, True)
    oGetApu.lReadOnly = True
    nLinhaObj += 25
    oSayPro = TSay().New(nLinhaObj, 3, lambda : cSayPro, oPanTotal, '', oFontSay, None, None, None, True, RGB(31, 73, 125), None, 200, 10, None, None, None, None, None, False, None)
    nLinhaObj += 10
    oGetPro = TGet().New(nLinhaObj, 13, lambda u: ((nGetPro := u) if PCount() > 0 else nGetPro), oPanTotal, nLargPanel - 25, 15, cMascara, None, None, None, oFontSay, None, None, True)
    oGetApu.lReadOnly = True
    nLinhaObj += 25
    nLinhaObj += 20
    oBtnProc = TButton().New(nLinhaObj, 3, 'Processar informações', oPanTotal, lambda : Alert('botão 1'), nLargPanel - 3, 18, None, oFontBtn, None, True, None, None, None, None, None)
    nLinhaObj += 25
    oBtnPrev = TButton().New(nLinhaObj, 3, 'Previsão dos dados', oPanTotal, lambda : Alert('botão 2'), nLargPanel - 3, 18, None, oFontBtn, None, True, None, None, None, None, None)
    Activate
    MsDialog
    oDlgExemp
    Centered
    oTempTable.Delete()
    return Static

def fCriaCols():
    nAtual = 0
    aColunas = []
    aEstrut = []
    oColumn = None
    # Adicionando campos que serão mostrados na tela
    # [1] - Campo da Temporaria
    # [2] - Titulo
    # [3] - Tipo
    # [4] - Tamanho
    # [5] - Decimais
    # [6] - Máscara
    aAdd(aEstrut, ['CONTA', 'Conta', 'C', 10, 0, ''])
    aAdd(aEstrut, ['VALOR', 'Valor', 'N', 18, 2, cMascara])
    # Percorrendo todos os campos da estrutura
    return aColunas

def s_fPopula():
    nAtual = 0
    return Static

def fExemplo2():
    nLargBtn = 50
    nLinhaObj = 0
    nLargPanel = 0
    # Objetos e componentes gerais
    oDlgExemp = None
    oSize = None
    oPanTitulo = None
    oPanGrid = None
    oPanCheck = None
    oPanTotal = None
    cMascara = '@E 999,999,999,999,999.99'
    # Cabeçalho
    oSayModulo = None
    cSayModulo = 'TST'
    oSayTitulo = None
    cSayTitulo = "'Exemplo de Tela com"
    oSaySubTit = None
    cSaySubTit = 'Objetos gráficos usando FWDefSize'
    # Tamanho da janela
    aSize = MsAdvSize(False)
    nJanLarg = aSize[5]
    nJanAltu = aSize[6]
    # Fontes
    cFontUti = 'Tahoma'
    oFontMod = TFont().New(cFontUti, None, -38)
    oFontSub = TFont().New(cFontUti, None, -20)
    oFontSubN = TFont().New(cFontUti, None, -20, None, True)
    oFontBtn = TFont().New(cFontUti, None, -14)
    oFontSay = TFont().New(cFontUti, None, -12)
    # Grid
    aCampos = []
    cAliasTmp = 'TST_' + RetCodUsr()
    aColunas = []
    oMarkBrowse = None
    # Componentes da segunda coluna
    oSayChkDes = None
    oSayChkPer = None
    oSayChkVlr = None
    oCheck01 = None
    lCheck01 = False
    oGetPerc01 = None
    nGetPerc01 = 0
    oGetTot01 = None
    nGetTot01 = 0
    oCheck02 = None
    lCheck02 = False
    oGetPerc02 = None
    nGetPerc02 = 0
    oGetTot02 = None
    nGetTot02 = 0
    oCheck03 = None
    lCheck03 = False
    oGetPerc03 = None
    nGetPerc03 = 0
    oGetTot03 = None
    nGetTot03 = 0
    oCheck04 = None
    lCheck04 = False
    oGetPerc04 = None
    nGetPerc04 = 0
    oGetTot04 = None
    nGetTot04 = 0
    oCheck05 = None
    lCheck05 = False
    oGetPerc05 = None
    nGetPerc05 = 0
    oGetTot05 = None
    nGetTot05 = 0
    # Componentes da terceira coluna
    oSayTot = None
    cSayTot = 'Total marcado:'
    oGetTot = None
    nGetTot = 0
    oSayApu = None
    cSayApu = '% Apurado:'
    oGetApu = None
    nGetApu = 0
    oSayPro = None
    cSayPro = 'Total que será processado:'
    oGetPro = None
    nGetPro = 0
    oBtnProc = None
    oBtnPrev = None
    # Adiciona as colunas que serão criadas na temporária
    aAdd(aCampos, ['OK', 'C', 2, 0])
    aAdd(aCampos, ['CONTA', 'C', 10, 0])
    aAdd(aCampos, ['VALOR', 'N', 18, 2])
    # Cria a tabela temporária
    oTempTable = FWTemporaryTable().New(cAliasTmp)
    oTempTable.SetFields(aCampos)
    oTempTable.Create()
    # Busca as colunas do browse
    aColunas = fCriaCols()
    # Popula a tabela temporária
    Processa(lambda : fPopula(), 'Processando...')
    # Cria a janela
    DEFINE
    MSDIALOG
    oDlgExemp
    TITLE
    'Exemplo de Tela com Objetos gráficos usando FWDefSize'
    FROM_
    0
    # ,
    0
    TO
    nJanAltu
    # ,
    nJanLarg
    PIXEL
    # Criando a camada
    oSize = FwDefSize().New(False, None, None, oDlgExemp)
    # Sem EnchoiceBar
    # Adicionando 3 linhas, a de título, a do corpo e a inferior
    oSize.AddObject('TITULO', 100, 10, True, True)
    oSize.AddObject('CORPO', 100, 88, True, True)
    oSize.AddObject('RODAPE', 100, 2, True, True)
    # Define a margem entre os objetos
    oSize.aMargins = [3, 3, 3, 3]
    # Efetua os cálculos do dimensionamento
    oSize.Process()
    # Pegando o dimensionamento das linhas
    aTitulo = [oSize.GetDimension('TITULO', 'LININI'), oSize.GetDimension('TITULO', 'COLINI'), oSize.GetDimension('TITULO', 'XSIZE'), oSize.GetDimension('TITULO', 'YSIZE')]
    aCorpo = [oSize.GetDimension('CORPO', 'LININI'), oSize.GetDimension('CORPO', 'COLINI'), oSize.GetDimension('CORPO', 'XSIZE'), oSize.GetDimension('CORPO', 'YSIZE')]
    aRodape = [oSize.GetDimension('RODAPE', 'LININI'), oSize.GetDimension('RODAPE', 'COLINI'), oSize.GetDimension('RODAPE', 'LINEND'), oSize.GetDimension('RODAPE', 'COLEND')]
    # Ajuste no dimensionamento (linha inicial e linha final)
    aCorpo[1] = aCorpo[1] - 50
    aCorpo[4] = aCorpo[4] + 140
    # Criando os paineis
    oPanHeader = tPanel().New(aTitulo[1], aTitulo[2], '', oDlgExemp, None, None, None, RGB(0, 0, 0), RGB(254, 254, 254), aTitulo[3] - 200, aTitulo[4])
    oPanSair = tPanel().New(aTitulo[1], aTitulo[3] - 200, '', oDlgExemp, None, None, None, RGB(0, 0, 0), RGB(254, 254, 254), aTitulo[3], aTitulo[4])
    oPanGrid = tPanel().New(aCorpo[1], aCorpo[2] + aCorpo[3] / 3 * 0, '', oDlgExemp, None, None, None, RGB(0, 0, 0), RGB(254, 254, 254), aCorpo[3] / 3, aCorpo[4])
    oPanCheck = tPanel().New(aCorpo[1], aCorpo[2] + aCorpo[3] / 3 * 1, '', oDlgExemp, None, None, None, RGB(0, 0, 0), RGB(254, 254, 254), aCorpo[3] / 3, aCorpo[4])
    oPanTotal = tPanel().New(aCorpo[1], aCorpo[2] + aCorpo[3] / 3 * 2, '', oDlgExemp, None, None, None, RGB(0, 0, 0), RGB(254, 254, 254), aCorpo[3] / 3, aCorpo[4])
    # Títulos e SubTítulos
    oSayModulo = TSay().New(4, 3, lambda : cSayModulo, oPanHeader, '', oFontMod, None, None, None, True, RGB(149, 179, 215), None, 200, 30, None, None, None, None, None, False, None)
    oSayTitulo = TSay().New(4, 45, lambda : cSayTitulo, oPanHeader, '', oFontSub, None, None, None, True, RGB(31, 73, 125), None, 200, 30, None, None, None, None, None, False, None)
    oSaySubTit = TSay().New(14, 45, lambda : cSaySubTit, oPanHeader, '', oFontSubN, None, None, None, True, RGB(31, 73, 125), None, 300, 30, None, None, None, None, None, False, None)
    # Criando os botões
    oBtnSair = TButton().New(6, 1, 'Fechar', oPanSair, lambda : oDlgExemp.End(), nLargBtn, 18, None, oFontBtn, None, True, None, None, None, None, None)
    # Cria a grid
    oMarkBrowse = FWMarkBrowse().New()
    oMarkBrowse.SetAlias(cAliasTmp)
    oMarkBrowse.DisableFilter()
    oMarkBrowse.DisableConfig()
    oMarkBrowse.DisableReport()
    oMarkBrowse.DisableSeek()
    oMarkBrowse.DisableSaveConfig()
    oMarkBrowse.SetFontBrowse(oFontSay)
    oMarkBrowse.SetFieldMark('OK')
    oMarkBrowse.SetTemporary(True)
    oMarkBrowse.SetColumns(aColunas)
    oMarkBrowse.SetOwner(oPanGrid)
    oMarkBrowse.Activate()
    # Cria os componentes da segunda coluna
    # RAW: @ 001 , 001 SCROLLBOX oScroll VERTICAL HORIZONTAL SIZE oPanCheck : nHeight / 2 , oPanCheck : nWidth / 2 OF oPanCheck
    nLinhaObj = 1
    nLargPanel = oPanCheck.nWidth() / 2
    nTotEspCol = nLargPanel / 3
    nTotCol01 = 3 + nTotEspCol * 0
    nTotCol02 = 3 + nTotEspCol * 1
    nTotCol03 = 3 + nTotEspCol * 2
    oSayChkDes = TSay().New(nLinhaObj, 1 + nTotCol01, lambda : 'Descrição', oScroll, '', oFontSay, None, None, None, True, RGB(31, 73, 125), None, nTotEspCol, 10, None, None, None, None, None, False, None)
    oSayChkPer = TSay().New(nLinhaObj, 1 + nTotCol02, lambda : '%', oScroll, '', oFontSay, None, None, None, True, RGB(31, 73, 125), None, nTotEspCol, 10, None, None, None, None, None, False, None)
    oSayChkVlr = TSay().New(nLinhaObj, 1 + nTotCol03, lambda : 'Valor', oScroll, '', oFontSay, None, None, None, True, RGB(31, 73, 125), None, nTotEspCol, 10, None, None, None, None, None, False, None)
    nLinhaObj += 25
    oCheck01 = TCheckBox().New(nLinhaObj, 3 + nTotCol01, 'Check 01', lambda u: ((lCheck01 := u) if PCount() > 0 else lCheck01), oScroll, nTotEspCol - 3, 10, None, None, oFontSay, None, None, None, None, True)
    oGetPerc01 = TGet().New(nLinhaObj, 3 + nTotCol02, lambda u: ((nGetPerc01 := u) if PCount() > 0 else nGetPerc01), oScroll, nTotEspCol - 9, 10, cMascara, None, None, None, oFontSay, None, None, True)
    oGetTot01 = TGet().New(nLinhaObj, 3 + nTotCol03, lambda u: ((nGetTot01 := u) if PCount() > 0 else nGetTot01), oScroll, nTotEspCol - 9, 10, cMascara, None, None, None, oFontSay, None, None, True)
    oGetTot01.lActive = False
    nLinhaObj += 15
    oCheck02 = TCheckBox().New(nLinhaObj, 3 + nTotCol01, 'Check 02', lambda u: ((lCheck02 := u) if PCount() > 0 else lCheck02), oScroll, nTotEspCol - 3, 10, None, None, oFontSay, None, None, None, None, True)
    oGetPerc02 = TGet().New(nLinhaObj, 3 + nTotCol02, lambda u: ((nGetPerc02 := u) if PCount() > 0 else nGetPerc02), oScroll, nTotEspCol - 9, 10, cMascara, None, None, None, oFontSay, None, None, True)
    oGetTot02 = TGet().New(nLinhaObj, 3 + nTotCol03, lambda u: ((nGetTot02 := u) if PCount() > 0 else nGetTot02), oScroll, nTotEspCol - 9, 10, cMascara, None, None, None, oFontSay, None, None, True)
    oGetTot02.lActive = False
    nLinhaObj += 15
    oCheck03 = TCheckBox().New(nLinhaObj, 3 + nTotCol01, 'Check 03', lambda u: ((lCheck03 := u) if PCount() > 0 else lCheck03), oScroll, nTotEspCol - 3, 10, None, None, oFontSay, None, None, None, None, True)
    oGetPerc03 = TGet().New(nLinhaObj, 3 + nTotCol02, lambda u: ((nGetPerc03 := u) if PCount() > 0 else nGetPerc03), oScroll, nTotEspCol - 9, 10, cMascara, None, None, None, oFontSay, None, None, True)
    oGetTot03 = TGet().New(nLinhaObj, 3 + nTotCol03, lambda u: ((nGetTot03 := u) if PCount() > 0 else nGetTot03), oScroll, nTotEspCol - 9, 10, cMascara, None, None, None, oFontSay, None, None, True)
    oGetTot03.lActive = False
    nLinhaObj += 15
    oCheck04 = TCheckBox().New(nLinhaObj, 3 + nTotCol01, 'Check 04', lambda u: ((lCheck04 := u) if PCount() > 0 else lCheck04), oScroll, nTotEspCol - 3, 10, None, None, oFontSay, None, None, None, None, True)
    oGetPerc04 = TGet().New(nLinhaObj, 3 + nTotCol02, lambda u: ((nGetPerc04 := u) if PCount() > 0 else nGetPerc04), oScroll, nTotEspCol - 9, 10, cMascara, None, None, None, oFontSay, None, None, True)
    oGetTot04 = TGet().New(nLinhaObj, 3 + nTotCol03, lambda u: ((nGetTot04 := u) if PCount() > 0 else nGetTot04), oScroll, nTotEspCol - 9, 10, cMascara, None, None, None, oFontSay, None, None, True)
    oGetTot04.lActive = False
    nLinhaObj += 15
    oCheck05 = TCheckBox().New(nLinhaObj, 3 + nTotCol01, 'Check 05', lambda u: ((lCheck05 := u) if PCount() > 0 else lCheck05), oScroll, nTotEspCol - 3, 10, None, None, oFontSay, None, None, None, None, True)
    oGetPerc05 = TGet().New(nLinhaObj, 3 + nTotCol02, lambda u: ((nGetPerc05 := u) if PCount() > 0 else nGetPerc05), oScroll, nTotEspCol - 9, 10, cMascara, None, None, None, oFontSay, None, None, True)
    oGetTot05 = TGet().New(nLinhaObj, 3 + nTotCol03, lambda u: ((nGetTot05 := u) if PCount() > 0 else nGetTot05), oScroll, nTotEspCol - 9, 10, cMascara, None, None, None, oFontSay, None, None, True)
    oGetTot05.lActive = False
    # Cria os componentes da terceira coluna
    nLargPanel = oPanTotal.nWidth() / 2
    nLinhaObj = 30
    oSayTot = TSay().New(nLinhaObj, 3, lambda : cSayTot, oPanTotal, '', oFontSay, None, None, None, True, RGB(31, 73, 125), None, 200, 10, None, None, None, None, None, False, None)
    nLinhaObj += 10
    oGetTot = TGet().New(nLinhaObj, 13, lambda u: ((nGetTot := u) if PCount() > 0 else nGetTot), oPanTotal, nLargPanel - 25, 15, cMascara, None, None, None, oFontSay, None, None, True)
    oGetTot.lReadOnly = True
    nLinhaObj += 25
    oSayApu = TSay().New(nLinhaObj, 3, lambda : cSayApu, oPanTotal, '', oFontSay, None, None, None, True, RGB(31, 73, 125), None, 200, 10, None, None, None, None, None, False, None)
    nLinhaObj += 10
    oGetApu = TGet().New(nLinhaObj, 13, lambda u: ((nGetApu := u) if PCount() > 0 else nGetApu), oPanTotal, nLargPanel - 25, 15, cMascara, None, None, None, oFontSay, None, None, True)
    oGetApu.lReadOnly = True
    nLinhaObj += 25
    oSayPro = TSay().New(nLinhaObj, 3, lambda : cSayPro, oPanTotal, '', oFontSay, None, None, None, True, RGB(31, 73, 125), None, 200, 10, None, None, None, None, None, False, None)
    nLinhaObj += 10
    oGetPro = TGet().New(nLinhaObj, 13, lambda u: ((nGetPro := u) if PCount() > 0 else nGetPro), oPanTotal, nLargPanel - 25, 15, cMascara, None, None, None, oFontSay, None, None, True)
    oGetApu.lReadOnly = True
    nLinhaObj += 25
    nLinhaObj += 20
    oBtnProc = TButton().New(nLinhaObj, 3, 'Processar informações', oPanTotal, lambda : Alert('botão 1'), nLargPanel - 3, 18, None, oFontBtn, None, True, None, None, None, None, None)
    nLinhaObj += 25
    oBtnPrev = TButton().New(nLinhaObj, 3, 'Previsão dos dados', oPanTotal, lambda : Alert('botão 2'), nLargPanel - 3, 18, None, oFontBtn, None, True, None, None, None, None, None)
    Activate
    MsDialog
    oDlgExemp
    Centered
    oTempTable.Delete()
    return
