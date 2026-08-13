# Esse exemplo faz parte da série do YouTube, Maratona de Exemplos, do canal Terminal de Informação, 
#     caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2024/07/03/criando-uma-janela-atraves-da-twindow-maratona-advpl-e-tl-515/
# Bibliotecas
# PREPROCESSOR: #Include "TOTVS.ch"
# {Protheus.doc} User Function zExe515
# Cria uma janela nativa com comportamento do sistema operacional (como minimizar)
# @type  Function
# @author Atilio
# @since 05/04/2023
# @see https://tdn.totvs.com/display/tec/TWindow
# @obs 
#     
#     **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
def u_zExe515():
    lContinua = True
    cEmprAux = '99'
    cFilAux = ''
    cUsrAux = ''
    cPswAux = ''
    lProgInic = False
    # Se a SX2 não tiver aberta, quer dizer que não veio pelo Protheus, logo é quiosque
    if Select('SX2') == 0:
        # Montando uma seção, apenas para poder pegar os parâmetros da SX61
        RPCSetEnv(cEmprAux, '', '', '', '')
        # Verificando se o login deu certo
        if u_zLogin(ref_(cUsrAux), ref_(cPswAux)):
            RPCSetEnv(cEmprAux, cFilAux, cUsrAux, cPswAux, 'SIGAEST')
            lContinua = True
            lProgInic = True
        else:
            lContinua = False


    if lContinua:
        fMontaTela()

    return Static

def fMontaTela():
    nLinObj = 0
    nLargBtn = 85
    nAltuBtn = 15
    # Blocos de código chamados pelos botões
    bConfirm = lambda : RptStatus(lambda : FWAlertInfo('Em Construção', 'Atenção'), 'Processando Registros...', 'Aguarde...')
    bCancela = lambda : fCancelar()
    # Fontes
    cFontPad = 'Tahoma'
    oFontBtn = TFont().New(cFontPad, None, -14)
    oFontBtnN = TFont().New(cFontPad, None, -14, None, True)
    oFontMod = TFont().New(cFontPad, None, -38)
    oFontMaior = TFont().New(cFontPad, None, -68)
    oFontSub = TFont().New(cFontPad, None, -20)
    # Objetos da Janela
    lCentered = None
    oBtConfirm = None
    oBtCancela = None
    oSayTitulo = None
    cSayTitulo = 'Tela de Testes'
    oSayEtiqus = None
    cSayEtiqus = '000'
    oDlgCentral = None
    # Tamanho da janela
    aTamanho = None
    nJanLarg = None
    nJanAltu = None
    nPosTop = None
    nPosLeft = None
    # Etiqueta
    cEspacProd = Space(TamSX3('B1_COD')[1])
    oGetProdut = None
    cGetProdut = cEspacProd
    oGetBlank = None
    cGetBlank = ''
    # Grid
    oGridPro = None
    aHeaderPro = []
    aColsPro = []
    # Se vier do programa inicial, a dimensão será diferente
    if lProgInic:
        aTamanho = GetScreenRes()
        nJanLarg = aTamanho[1]
        nJanAltu = aTamanho[2] - 80
        lCentered = False
        nPosTop = 0
        nPosLeft = -10
    else:
        aTamanho = MsAdvSize()
        nJanLarg = aTamanho[5]
        nJanAltu = aTamanho[6]
        lCentered = True
        nPosTop = 0
        nPosLeft = 0

    # Cria o cabeçalho da grid
    # Titulo                    Campo         Picture                        Tamanho                       Dec                     Valid           Usado  Tipo F3
    aAdd(aHeaderPro, ['Produto', 'XX_PROD', '', 15, 0, '.F.', '.F.', 'C', '', ''])
    aAdd(aHeaderPro, ['Descrição', 'XX_DESC', '', 30, 0, '.F.', '.F.', 'C', '', ''])
    aAdd(aHeaderPro, ['SB1 RecNo', 'XX_RECNUM', '@E 999,999,999,999,999,999', 18, 0, '.F.', '.F.', 'N', '', ''])
    aAdd(aHeaderPro, [' ', 'XX_BLANK', '', 1, 0, '.F.', '.F.', 'C', '', ''])
    # Cria a janela
    if lProgInic:
        oDlgCentral = TWindow().New(nPosTop, nPosLeft, nJanAltu, nJanLarg, cSayTitulo, None, None, None, None, None, None, None, CLR_BLACK, RGB(250, 250, 250), None, None, None, None, None, None, True)
    else:
        oDlgCentral = TDialog().New(nPosTop, nPosLeft, nJanAltu, nJanLarg, cSayTitulo, None, None, None, None, CLR_BLACK, RGB(250, 250, 250), None, None, True)

    # Títulos e SubTítulos
    oSayTitulo = TSay().New(4, 3, lambda : cSayTitulo, oDlgCentral, '', oFontMod, None, None, None, True, RGB(149, 179, 215), None, 200, 30, None, None, None, None, None, False, None)
    oSayEtiqus = TSay().New(-3, nJanLarg / 2 - 120, lambda : cSayEtiqus, oDlgCentral, '', oFontMaior, None, None, None, True, RGB(255, 0, 0), None, 100, 50, None, None, None, None, None, False, None)
    # Get da Etiqueta
    nLinObj = 36
    oGetProdut = TGet().New(nLinObj, 3, lambda u: ((cGetProdut := u) if Pcount() > 0 else cGetProdut), oDlgCentral, nJanLarg / 2 - 3, 20, '@!', lambda : fVldCodig(), None, None, oFontMod, None, None, True, None, None, None, None, None, None, False, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None)
    oGetProdut.cPlaceHold = '< Código do Produto >'
    oGetBlank = TGet().New(-100, -100, lambda u: ((cGetBlank := u) if PCount() > 0 else cGetBlank), oDlgCentral, 10, 10, None, None, None, None, oFontBtn, None, None, True)
    oGetBlank.bGotFocus = lambda : oGetProdut.SetFocus()
    # Botões
    nLinObj = 59
    oBtConfirm = TButton().New(nLinObj + nAltuBtn * 0, nJanLarg / 2 - nLargBtn * 1, 'Confirmar', oDlgCentral, bConfirm, nLargBtn, nAltuBtn, None, oFontBtnN, None, True, None, None, None, None, None)
    oBtCancela = TButton().New(nLinObj + nAltuBtn * 1, nJanLarg / 2 - nLargBtn * 1, 'Cancelar', oDlgCentral, bCancela, nLargBtn, nAltuBtn, None, oFontBtn, None, True, None, None, None, None, None)
    # Abaixo cria a grid
    oGridPro = MsNewGetDados().New(nLinObj, 3, nJanAltu / 2 - 3, nJanLarg / 2 - 3 - nLargBtn, None, 'AllwaysTrue()', None, '', [], None, 99999999, None, None, None, oDlgCentral, aHeaderPro, aColsPro)
    # aCols
    oGridPro.oBrowse().SetCSS(u_zCSSGrid())
    oGridPro.lActive = False
    # Ativa e exibe a janela
    if lProgInic:
        oDlgCentral.Activate('MAXIMIZED')
    else:
        oDlgCentral.Activate(None, None, None, lCentered, lambda : True, None)

    return Static

def fVldCodig():
    lRet = True
    aColsAux = oGridPro.aCols()
    lAdiciona = True
    nPosProd = aScan(aHeaderPro, lambda x: Alltrim(x[2]) == 'XX_PROD')
    nLinha = 0
    # Somente se tiver código de etiqueta
    if not Empty(cGetProdut):
        # Validar se a etiqueta não foi inserida na grid ainda
        # Se deu tudo certo
        if lAdiciona:
            DbSelectArea('SB1')
            SB1.DbSetOrder(1)
            # Se conseguir posicionar no produto
            if SB1.MsSeek(FWxFilial('SB1') + cGetProdut):
                # Se tiver apenas 1 linha e a coluna do produto estivar vazia
                if Len(aColsAux) == 1 and Empty(aColsAux[1][nPosProd]):
                    aColsAux = []

                # Adiciona uma linha na grid
                aAdd(aColsAux, [SB1.B1_COD, SubStr(SB1.B1_DESC, 1, 30), SB1.RecNo(), '', False])
                oGridPro.SetArray(aColsAux)
                oGridPro.Refresh()
                # Atualiza produtos lidos
                cSayEtiqus = Soma1(cSayEtiqus)
                oSayEtiqus.Refresh()
            else:
                FWAlertError("O produto '" + cGetProdut + "' não encontrado!", 'Falha')


        # Zera o Get, para ser inserida uma nova etiqueta
        cGetProdut = cEspacProd

    return lRet

def s_fCancelar():
    aColsAux = oGridPro.aCols()
    # Somente se a pergunta for confirmada
    if FWAlertYesNo('Deseja cancelar?', 'Continua?'):
        aColsAux = []
        oGridPro.SetArray(aColsAux)
        oGridPro.Refresh()
        cSayEtiqus = '000'
        oSayEtiqus.Refresh()

    return
