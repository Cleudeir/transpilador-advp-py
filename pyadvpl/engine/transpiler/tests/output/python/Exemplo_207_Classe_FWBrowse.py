# Esse exemplo faz parte da série do YouTube, Maratona de Exemplos, do canal Terminal de Informação, 
#     caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2024/01/31/criando-um-browse-com-a-classe-fwbrowse-maratona-advpl-e-tl-207/
# Bibliotecas
# PREPROCESSOR: #Include "TOTVS.ch"
# {Protheus.doc} User Function zExe207
# Exemplo de tela com navegação em um browse / grid
# @type Function
# @author Atilio
# @since 12/02/2023
# @see https://tdn.totvs.com/display/public/framework/FwBrowse
# @obs 
# 
#     **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
def u_zExe207():
    aArea = GetArea()
    # Fontes
    cFontUti = 'Tahoma'
    oFontAno = TFont().New(cFontUti, None, -38)
    oFontSub = TFont().New(cFontUti, None, -20)
    oFontSubN = TFont().New(cFontUti, None, -20, None, True)
    oFontBtn = TFont().New(cFontUti, None, -14)
    # Janela e componentes
    oDlgGrp = None
    oPanGrid = None
    oGetGrid = None
    aColunas = []
    cAliasTab = 'TMPSBM'
    # Tamanho da janela
    aTamanho = MsAdvSize()
    nJanLarg = aTamanho[5]
    nJanAltu = aTamanho[6]
    # Cria a temporária
    oTempTable = FWTemporaryTable().New(cAliasTab)
    # Adiciona no array das colunas as que serão incluidas (Nome do Campo, Tipo do Campo, Tamanho, Decimais)
    aFields = []
    aAdd(aFields, ['XXCODIGO', 'C', 6, 0])
    aAdd(aFields, ['XXDESCRI', 'C', 30, 0])
    aAdd(aFields, ['XXQUANTI', 'N', 9, 2])
    aAdd(aFields, ['XXEMISSA', 'D', 8, 0])
    aAdd(aFields, ['XXOBSERV', 'C', 100, 0])
    # Define as colunas usadas, adiciona indice e cria a temporaria no banco
    oTempTable.SetFields(aFields)
    oTempTable.AddIndex('1', ['XXCODIGO'])
    oTempTable.Create()
    # Monta o cabecalho
    fMontaHead()
    # Montando os dados, eles devem ser montados antes de ser criado o FWBrowse
    FWMsgRun(None, lambda oSay: fMontDados(oSay), 'Processando', 'Buscando grupos')
    # Criando a janela
    DEFINE
    MSDIALOG
    oDlgGrp
    TITLE
    'Dados'
    FROM_
    0
    # ,
    0
    TO
    nJanAltu
    # ,
    nJanLarg
    COLORS
    0
    # ,
    16777215
    PIXEL
    # Labels gerais
    # RAW: @ 004 , 003 SAY "FAT" SIZE 200 , 030 FONT oFontAno OF oDlgGrp COLORS RGB ( 149 , 179 , 215 ) PIXEL
    # RAW: @ 004 , 050 SAY "Listagem Genérica de" SIZE 200 , 030 FONT oFontSub OF oDlgGrp COLORS RGB ( 031 , 073 , 125 ) PIXEL
    # RAW: @ 014 , 050 SAY "Dados Temporários" SIZE 200 , 030 FONT oFontSubN OF oDlgGrp COLORS RGB ( 031 , 073 , 125 ) PIXEL
    # Botões
    # RAW: @ 006 , ( nJanLarg / 2 - 001 ) - ( 0052 * 01 ) BUTTON oBtnFech PROMPT "Fechar" SIZE 050 , 018 OF oDlgGrp ACTION ( oDlgGrp : End ( ) ) FONT oFontBtn PIXEL
    # Dados
    # RAW: @ 024 , 003 GROUP oGrpDad TO ( nJanAltu / 2 - 003 ) , ( nJanLarg / 2 - 003 ) PROMPT "Browse" OF oDlgGrp COLOR 0 , 16777215 PIXEL
    oGrpDad.oFont = oFontBtn
    oPanGrid = tPanel().New(33, 6, '', oDlgGrp, None, None, None, RGB(0, 0, 0), RGB(254, 254, 254), nJanLarg / 2 - 13, nJanAltu / 2 - 45)
    oGetGrid = FWBrowse().New()
    oGetGrid.DisableFilter()
    oGetGrid.DisableConfig()
    oGetGrid.DisableReport()
    oGetGrid.DisableSeek()
    oGetGrid.DisableSaveConfig()
    oGetGrid.SetFontBrowse(oFontBtn)
    oGetGrid.SetAlias(cAliasTab)
    oGetGrid.SetDataTable()
    oGetGrid.SetEditCell(True, lambda : True)
    oGetGrid.lHeaderClick = False
    oGetGrid.AddLegend(cAliasTab + '->XXQUANTI == 0', 'YELLOW', 'Quantidade zerada')
    oGetGrid.AddLegend(cAliasTab + '->XXQUANTI <  0', 'RED', 'Quantidade menor que zero')
    oGetGrid.AddLegend(cAliasTab + '->XXQUANTI >  0', 'GREEN', 'Quantidade maior que zero')
    oGetGrid.SetColumns(aColunas)
    oGetGrid.SetOwner(oPanGrid)
    oGetGrid.Activate()
    ACTIVATE
    MsDialog
    oDlgGrp
    CENTERED
    # Deleta a temporaria
    oTempTable.Delete()
    RestArea(aArea)
    return Static

def fMontaHead():
    nAtual = None
    aHeadAux = []
    # Adicionando colunas
    # [1] - Campo da Temporaria
    # [2] - Titulo
    # [3] - Tipo
    # [4] - Tamanho
    # [5] - Decimais
    # [6] - Máscara
    # [7] - Editável? .T. = sim, .F. = não
    aAdd(aHeadAux, ['XXCODIGO', 'Código', 'C', 6, 0, '', False])
    aAdd(aHeadAux, ['XXDESCRI', 'Descricao', 'C', 30, 0, '', False])
    aAdd(aHeadAux, ['XXQUANTI', 'Quantidade', 'N', 9, 2, '@E 999,999.99', True])
    aAdd(aHeadAux, ['XXEMISSA', 'Emissão', 'D', 8, 0, '', True])
    aAdd(aHeadAux, ['XXOBSERV', 'Observação', 'C', 100, 0, '', True])
    # Percorrendo e criando as colunas
    return Static

def fMontDados(oSay):
    aArea = GetArea()
    nAtual = 0
    nTotal = 50
    dDtRef = Date()
    cCodAtu = '000000'
    cDescri = ''
    nQuanti = 0
    dEmissa = sToD('')
    # Faz um laço de repetição
    RestArea(aArea)
    return
