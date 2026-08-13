# Esse exemplo faz parte da série do YouTube, Maratona de Exemplos, do canal Terminal de Informação, 
#     caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2024/07/02/criando-um-temporizador-atraves-da-ttimer-maratona-advpl-e-tl-513/
# Bibliotecas
# PREPROCESSOR: #Include "TOTVS.ch"
# {Protheus.doc} User Function zExe513
# Cria um temporizador que é executado a cada x milissegundos
# @type  Function
# @author Atilio
# @since 05/04/2023
# @see https://tdn.totvs.com/display/tec/TTimer
# @obs 
#     
#     **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
def u_zExe513():
    aArea = FWGetArea()
    nTempo = 30000
    # 30.000 milissegundos e igual a 30 segundos
    lUpdate = False
    dDataAtu = Date()
    # Objetos da Janela
    oDlgPvt = None
    oBtnAtu = None
    oBtnFech = None
    oTimer = None
    nTamBtn = 48
    cGetTot = ''
    oGetTot = None
    cGetObs = ''
    oGetObs = None
    # Tamanho da Janela
    aTamanho = MsAdvSize()
    nJanLarg = 600
    # aTamanho[5]
    nJanAltu = 150
    # aTamanho[6]
    # Fontes
    cFontUti = 'Tahoma'
    oFontAno = TFont().New(cFontUti, None, -38)
    oFontSub = TFont().New(cFontUti, None, -20)
    oFontSubN = TFont().New(cFontUti, None, -20, None, True)
    oFontBtn = TFont().New(cFontUti, None, -14)
    # Criacao da tela com os dados que serao informados dos titulos
    DEFINE
    MSDIALOG
    oDlgPvt
    TITLE
    'Teste de TTimer'
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
    # RAW: @ 004 , 003 SAY "TI" SIZE 200 , 030 FONT oFontAno OF oDlgPvt COLORS RGB ( 149 , 179 , 215 ) PIXEL
    # RAW: @ 004 , 030 SAY "Função de Exemplo" SIZE 200 , 030 FONT oFontSub OF oDlgPvt COLORS RGB ( 031 , 073 , 125 ) PIXEL
    # RAW: @ 014 , 030 SAY "para testar TTimer" SIZE 200 , 030 FONT oFontSubN OF oDlgPvt COLORS RGB ( 031 , 073 , 125 ) PIXEL
    # Botoes
    # RAW: @ 006 , ( nJanLarg / 2 - 3 ) - ( ( nTamBtn ) * 01 ) - 0 BUTTON oBtnFech PROMPT "Fechar" SIZE nTamBtn , 018 OF oDlgPvt ACTION ( oDlgPvt : End ( ) ) FONT oFontBtn PIXEL
    # RAW: @ 006 , ( nJanLarg / 2 - 3 ) - ( ( nTamBtn ) * 02 ) - 1 BUTTON oBtnAtu PROMPT "Atualizar" SIZE nTamBtn , 018 OF oDlgPvt ACTION ( fAtualiza ( ) ) FONT oFontBtn PIXEL
    # Get com Total de Produtos
    # RAW: @ 030 , 003 MSGET oGetTot VAR cGetTot SIZE ( nJanLarg / 2 ) - 3 , 015 OF oDlgPvt COLORS 0 , 16777215 FONT oFontBtn PIXEL
    oGetTot.lReadOnly = True
    # Get com observacoes
    ref_(nJanAltu / 2) - 21
    # ,
    3
    MSGET
    oGetObs
    VAR
    cGetObs
    SIZE(nJanLarg / 2) - 3
    # ,
    15
    OF
    oDlgPvt
    COLORS
    0
    # ,
    16777215
    FONT
    oFontBtn
    PIXEL
    oGetObs.lReadOnly = True
    oGetObs.setCSS('QLineEdit{color:#ff0000; background-color:#ffffff;}')
    # Chamando a primeira vez para atualizar o get
    fAtualiza()
    # Temporizador para atualizar a tela sozinho
    oTimer = TTimer().New(nTempo, lambda : fAtualiza(), oDlgPvt)
    oTimer.Activate()
    ACTIVATE
    MSDIALOG
    oDlgPvt
    CENTERED
    FWRestArea(aArea)
    return Static

def fAtualiza():
    Processa(lambda : fAtuTela(), 'Processando...')
    return Static

def fAtuTela():
    cQuery = ''
    nTotal = 0
    # Se nao estiver sendo atualizada, comeca a atualizar a tela
    if not lUpdate:
        lUpdate = True
        # Monta a query, executa e pega o resultado
        cQuery = ' SELECT  ' + CRLF
        cQuery += '     COUNT(B1_COD) AS TOTAL  ' + CRLF
        cQuery += ' FROM  ' + CRLF
        cQuery += '     ' + RetSQLName('SB1') + ' SB1 ' + CRLF
        cQuery += ' WHERE  ' + CRLF
        cQuery += "     B1_FILIAL = '" + FWxFilial('SB1') + "'  " + CRLF
        cQuery += "     AND SB1.D_E_L_E_T_ = '' " + CRLF
        PLSQuery(cQuery, 'QRY_SB1')
        nTotal = QRY_SB1.TOTAL
        QRY_SB1.DbCloseArea()
        # Atualiza o totalizador dos produtos
        cGetTot = cValToChar(nTotal) + ' produtos encontrados!'
        oGetTot.Refresh()
        # Atualiza o Get de Observacao
        cGetObs = 'Rotina atualiza a cada ' + cValToChar(nTempo / 60000) + ' minutos. ult. atualizacao - ' + dToC(Date()) + ' as ' + Time()
        oGetObs.Refresh()
        lUpdate = False

    return
