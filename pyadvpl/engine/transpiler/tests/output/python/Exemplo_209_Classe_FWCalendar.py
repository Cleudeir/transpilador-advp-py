# Esse exemplo faz parte da série do YouTube, Maratona de Exemplos, do canal Terminal de Informação, 
#     caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2024/02/01/criando-um-calendario-em-tela-atraves-da-fwcalendar-maratona-advpl-e-tl-209/
# Bibliotecas
# PREPROCESSOR: #Include "TOTVS.ch"
# Posições do array dos agendamentos do calendário
# PREPROCESSOR: #Define ID         1 // Id do Celula
# PREPROCESSOR: #Define OBJETO     2 // Objeto de Tela
# PREPROCESSOR: #Define DATADIA    3 // Data Completa da Celula
# PREPROCESSOR: #Define DIA        4 // Dia Ref. Data da Celula
# PREPROCESSOR: #Define MES        5 // Mes Ref. Data da Celula
# PREPROCESSOR: #Define ANO        6 // Ano Ref. Data da Celula
# PREPROCESSOR: #Define NSEMANO    7 // Semana do Ano Ref. Data da Celula
# PREPROCESSOR: #Define NSEMMES    8 // Semana do Mes Ref. Data da Celula
# PREPROCESSOR: #Define ATIVO      9 // É celula referente a um dia ativo
# PREPROCESSOR: #Define FOOTER    10 // É celula referente ao rodape
# PREPROCESSOR: #Define HEADER    11 // É celula referente ao Header
# PREPROCESSOR: #Define SEMANA    12 // É celula referente a semana
# PREPROCESSOR: #Define BGDefault 13 // Cor de BackGround da Celula
# {Protheus.doc} User Function zExe209
# Tela de agendamentos do Telemarketing
# @type  Function
# @author Atilio
# @since 20/02/2023
# @version 1.0
# @see https://tdn.totvs.com/display/public/framework/FWCalendar
# @obs 
#     
#     **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
def u_zExe209():
    aArea = GetArea()
    aSize = MsAdvSize(False)
    fMontaTela()
    RestArea(aArea)
    return Static

def fMontaTela():
    nCorFundo = 16777215
    nLargBtn = 50
    # Data
    dDtIni = Date()
    cMes = StrZero(Month(dDtIni), 2)
    cAno = StrZero(Year(dDtIni), 4)
    # Objetos e componentes
    oDlgTmk = None
    oFwLayer = None
    oPanTitulo = None
    oPanCalend = None
    oPanPreMon = None
    oPanNexMon = None
    oPanSair = None
    oMesAtual = None
    cMesAno = None
    cTitHtml = None
    # Cabeçalho
    oSayModulo = None
    cSayModulo = 'FAT'
    oSayTitulo = None
    cSayTitulo = 'Calendário de Agendamentos'
    oSaySubTit = None
    cSaySubTit = 'Clique com o botão direito para registrar agendamentos'
    # Tamanho da janela
    nJanLarg = aSize[5]
    nJanAltu = aSize[6]
    # Fontes
    cFontUti = 'Tahoma'
    oFontMod = TFont().New(cFontUti, None, -38)
    oFontSub = TFont().New(cFontUti, None, -20)
    oFontSubN = TFont().New(cFontUti, None, -20, None, True)
    oFontBtn = TFont().New(cFontUti, None, -14)
    oFontSay = TFont().New(cFontUti, None, -12)
    # Variáveis usadas para atualização das informações
    aInfoDia = None
    nSelecao = None
    cTextoSel = None
    nPosCell = None
    # Cria a janela
    DEFINE
    MSDIALOG
    oDlgTmk
    TITLE
    'Agendamentos Telemarketing'
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
    oFwLayer.init(oDlgTmk, False)
    # Adicionando 3 linhas, a de título, a superior e a do calendário
    oFWLayer.addLine('TIT', 10, False)
    oFWLayer.addLine('SUP', 5, False)
    oFWLayer.addLine('CAL', 85, False)
    # Adicionando as colunas das linhas
    oFWLayer.addCollumn('HEADERTEXT', 50, True, 'TIT')
    oFWLayer.addCollumn('BLANKBTN', 40, True, 'TIT')
    oFWLayer.addCollumn('BTNSAIR', 10, True, 'TIT')
    oFWLayer.addCollumn('BLANKSUP1', 15, True, 'SUP')
    oFWLayer.addCollumn('BTNPREVMONTH', 20, True, 'SUP')
    oFWLayer.addCollumn('TITLE', 30, True, 'SUP')
    oFWLayer.addCollumn('BTNNEXTMONTH', 20, True, 'SUP')
    oFWLayer.addCollumn('COLCAL', 100, True, 'CAL')
    # Criando os paineis
    oPanTitulo = oFWLayer.GetColPanel('TITLE', 'SUP')
    oPanCalend = oFWLayer.GetColPanel('COLCAL', 'CAL')
    oPanPreMon = oFWLayer.GetColPanel('BTNPREVMONTH', 'SUP')
    oPanNexMon = oFWLayer.GetColPanel('BTNNEXTMONTH', 'SUP')
    oPanSair = oFWLayer.GetColPanel('BTNSAIR', 'TIT')
    oPanHeader = oFWLayer.GetColPanel('HEADERTEXT', 'TIT')
    # Títulos e SubTítulos
    oSayModulo = TSay().New(4, 3, lambda : cSayModulo, oPanHeader, '', oFontMod, None, None, None, True, RGB(149, 179, 215), None, 200, 30, None, None, None, None, None, False, None)
    oSayTitulo = TSay().New(4, 45, lambda : cSayTitulo, oPanHeader, '', oFontSub, None, None, None, True, RGB(31, 73, 125), None, 200, 30, None, None, None, None, None, False, None)
    oSaySubTit = TSay().New(14, 45, lambda : cSaySubTit, oPanHeader, '', oFontSubN, None, None, None, True, RGB(31, 73, 125), None, 300, 30, None, None, None, None, None, False, None)
    # Criando os botões
    oBtnEnd = TButton().New(6, 1, 'Fechar', oPanSair, lambda : oDlgTmk.End(), nLargBtn, 18, None, oFontBtn, None, True, None, None, None, None, None)
    # Cria o calendário
    oCalend = FWCalendar().New(VAL(cMes), VAL(cAno))
    oCalend.aNomeCol = ['Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Semana']
    # 'Domingo'    # 'Segunda' # 'Terça' # 'Quarta' # 'Quinta'    # 'Sexta' # 'Sábado' # 'Semana'
    oCalend.lWeekColumn = False
    oCalend.lFooterLine = False
    oCalend.bLClicked = lambda : None
    oCalend.bLDblClick = lambda : None
    oCalend.bRClicked = lambda aInfo, oObj, nRow, nCol: fCliqueDir(aInfo, oObj, nRow, nCol)
    fCalendFont()
    oCalend.Activate(oPanCalend)
    # Criando o Say com o mês Atual
    oMesAtual = TSay().New(0, 0, lambda : None, oPanTitulo, None, None, None, None, None, True, 20, 20, None, None, None, None, None, None, None, True)
    oMesAtual.Align = CONTROL_ALIGN_ALLCLIENT
    oMesAtual.nClrPane = nCorFundo
    fMesAno(Val(cMes), Val(cAno))
    # Criando o botão do Mês Anterior
    # RAW: @ 0 , 0 BTNBMP oPrevMonth Resource "PMSSETAESQ" Size 80 , 90 Of oPanPreMon Pixel
    oPrevMontht.cToolTip = 'Mes Anterior'
    # "Mes Anterior"
    oPrevMonth.bAction = lambda : FwMsgRun(None, lambda : fMudaMes(oPanCalend, oCalend, 2), None, 'Montando calendário...')
    # "Montando calendário..."
    oPrevMonth.Align = CONTROL_ALIGN_RIGHT
    # Criando o botão do Próximo Mês
    # RAW: @ 0 , 0 BTNBMP oNextMonth Resource "PMSSETADIR" Size 90 , 90 Of oPanNexMon Pixel
    oNextMonth.cToolTip = 'Proximo Mes'
    # "Proximo Mes"
    oNextMonth.bAction = lambda : FwMsgRun(None, lambda : fMudaMes(oPanCalend, oCalend, 1), None, 'Montando calendário...')
    # "Montando calendário..."
    oNextMonth.Align = CONTROL_ALIGN_LEFT
    Activate
    MsDialog
    oDlgTmk
    Centered
    return Static

def fMudaMes(oPan, oCalend, nOp):
    nMonth = oCalend.nMes()
    nYear = oCalend.nAno()
    Default
    nOp = 1
    # Se for a seta ->, incrementa um mês
    if nOp == 1:
        if nMonth == 12:
            nMonth = 1
            nYear += 1
        else:
            nMonth = (nMonth := nMonth + 1)

        # Se for a seta <-, diminui um mês
    elif nOp == 2:
        if nMonth == 1:
            nMonth = 12
            nYear -= 1
        else:
            nMonth = (nMonth := nMonth - 1)


    # Define o calendário e seta o título
    oCalend.SetCalendar(oPan, cValToChar(nMonth), cValToChar(nYear))
    fMesAno(nMonth, nYear)
    return Static

def fMesAno(nMonth, nYear):
    cMesAno = Capital(MesExtenso(nMonth)) + ' / ' + cValToChar(nYear)
    cTitHtml = fTitHTML(cMesAno)
    oMesAtual.SetText(cTitHtml)
    # Chama a busca de informações para definir as informações no calendário
    fBuscaInfo()
    return None
    # Função que transforma o título no formato html

def s_fTitHTML(cMesAno):
    cRet = ''
    cRet += '<p align="center">'
    cRet += '<font face="' + cFontUti + '" color="#000000" style="font-size:14px"><strong>' + cMesAno + '</strong></font>'
    cRet += '</p>'
    return cRet
    # Função que define o primeiro calendário com a fonte Tahom

def s_fCalendFont():
    oCalend.aFontDay()[1] = cFontUti
    oCalend.aFontDayHead()[1] = cFontUti
    oCalend.aFontDayText()[1] = cFontUti
    oCalend.aFontFooter()[1] = cFontUti
    oCalend.aFontFsFer()[1] = cFontUti
    oCalend.aFontHeader()[1] = cFontUti
    oCalend.aFontOff()[1] = cFontUti
    oCalend.aFontToday()[1] = cFontUti
    oCalend.aFontWeek()[1] = cFontUti
    oCalend.cHtmlDay = StrTran(oCalend.cHtmlDay(), 'MS Sans Serif', cFontUti)
    oCalend.cHtmlDayOff = StrTran(oCalend.cHtmlDayOff(), 'MS Sans Serif', cFontUti)
    oCalend.cHtmlFooter = StrTran(oCalend.cHtmlFooter(), 'MS Sans Serif', cFontUti)
    oCalend.cHtmlHeader = StrTran(oCalend.cHtmlHeader(), 'MS Sans Serif', cFontUti)
    oCalend.cHtmlToday = StrTran(oCalend.cHtmlToday(), 'MS Sans Serif', cFontUti)
    oCalend.cHtmlWeek = StrTran(oCalend.cHtmlWeek(), 'MS Sans Serif', cFontUti)
    oCalend.cHtmlWeekend = StrTran(oCalend.cHtmlWeekend(), 'MS Sans Serif', cFontUti)
    return Static

def fBuscaInfo():
    nCell = None
    nDia = None
    return Static

def fCliqueDir(aInfo, oObj, nRow, nCol):
    cClassName = Upper(Alltrim(oObj.ClassName()))
    oMenu = None
    oMenuItem = []
    aOpcoes = []
    nOpcao = 0
    dData = aInfo[DATADIA]
    aInfoDia = aInfo
    nSelecao = aInfo[OBJETO].nSelectedIndex()
    cTextoSel = ''
    nPosCell = aScan(oCalend.aCell(), lambda x: AllTrim(Upper(x[1])) == aInfo[1])
    # Somente se estiver dentro do ListBox
    if cClassName == 'TLISTBOX':
        aAdd(aOpcoes, ['Novo Agendamento', lambda : fPopOpcao(3, dData)])
        # Se houver linhas, terá outras opções
        if nSelecao != 0:
            aAdd(aOpcoes, ['Visualizar Agendamento', lambda : fPopOpcao(2, dData)])
            aAdd(aOpcoes, ['Alterar Agendamento', lambda : fPopOpcao(4, dData)])
            aAdd(aOpcoes, ['Excluir Agendamento', lambda : fPopOpcao(5, dData)])
            cTextoSel = aInfo[OBJETO].oListBoxContent().aItems()[nSelecao]


    # Criando o menu e os itens
    MENU
    oMenu
    POPUP
    ENDMENU
    oMenu.Activate(nRow, nCol, oObj)
    return Static

def fPopOpcao(nOpcao, dData):
    aPergs = []
    cTexto = ''
    cEditCli = '.F.'
    cCliente = Space(TamSX3('A1_COD')[1])
    cLoja = Space(TamSX3('A1_LOJA')[1])
    cObserv = ''
    Default
    nOpcao = 3
    Default
    dData = Date()
    # Define o texto
    if nOpcao == 3:
        cEditCli = '.T.'
        cTexto = 'Inclusão de Agendamento'
    else:
        cEditCli = '.F.'
        if nOpcao == 2:
            cTexto = 'Visualização de Agendamento'
        elif nOpcao == 4:
            cTexto = 'Alteração de Agendamento'
        elif nOpcao == 5:
            cTexto = 'Exclusão de Agendamento'

        cCliente = SubStr(cTextoSel, 1, 6)
        cLoja = '01'
        cTexto += ' (' + SubStr(cTextoSel, 10, Len(cTextoSel)) + ')'

    # Adiciona os parâmetros
    aAdd(aPergs, [9, cTexto, 200, 40, True])
    aAdd(aPergs, [1, 'Data', dData, '', '.T.', '', '.F.', 80, True])
    aAdd(aPergs, [1, 'Cliente', cCliente, '', '.T.', 'SA1', cEditCli, 80, True])
    aAdd(aPergs, [1, 'Loja', cLoja, '', '.T.', '', cEditCli, 80, True])
    aAdd(aPergs, [11, 'Histórico', cObserv, '.T.', '.T.', True])
    # Se a pergunta for confirmada
    if ParamBox(aPergs, 'Informe os parâmetros', None, None, None, None, None, None, None, None, False, False):
        cCliente = MV_PAR03
        cLoja = MV_PAR04
        cObserv = MV_PAR05
        cNomeCli = Posicione('SA1', 1, FWxFilial('SA1') + cCliente + cLoja, 'A1_NOME')
        # Se for inclusão, adiciona no calendário
        if nOpcao == 3:
            aItens = aClone(aInfoDia[OBJETO].oListBoxContent().aItems())
            aAdd(aItens, cCliente + ' - ' + SubStr(cNomeCli, 1, 15))
            oCalend.SetInfo(oCalend.aCell()[nPosCell][ID], aClone(aItens))
            # Se for exclusãoRetira o elemento do array e depois define no calendário
        elif nOpcao == 5:
            aItens = aClone(aInfoDia[OBJETO].oListBoxContent().aItems())
            aDel(aItens, nSelecao)
            aSize(aItens, Len(aItens) - 1)
            oCalend.SetInfo(oCalend.aCell()[nPosCell][ID], aClone(aItens))


    return
