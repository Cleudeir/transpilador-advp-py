# Esse exemplo faz parte da série do YouTube, Maratona de Exemplos, do canal Terminal de Informação, 
#     caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2024/02/01/criando-dois-browses-com-relacionamento-atraves-da-fwbrwrelation-maratona-advpl-e-tl-208/
# Bibliotecas
# PREPROCESSOR: #Include "Totvs.ch"
# PREPROCESSOR: #Include "FWMVCDef.ch"
lEmExecucao = False
# {Protheus.doc} User Function zExe208
# Exemplo de tela com 2 browses de cadastro usando FWBrwRelation
# @type  Function
# @author Atilio
# @since 20/02/2023
# @obs 
#     
#     **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
def u_zExe208():
    aArea = GetArea()
    cFunBkp = FunName()
    aCoors = FWGetDialogSize(oMainWnd)
    cIdGrupo = None
    cIdProdut = None
    oPanelUp = None
    oTela = None
    oPanelDown = None
    oRelaction = None
    # Tratativa para impedir que seja aberta a mesma janela por cima da original do browse
    if not lEmExecucao:
        SetFunName('MATA035')
        DbSelectArea('SBM')
        DbSelectArea('SB1')
        # Cria a janela principal
        Define
        MsDialog
        oDlgPrinc
        Title
        'Grupos x Produtos'
        From_
        aCoors[1]
        # ,
        aCoors[2]
        To
        aCoors[3]
        # ,
        aCoors[4]
        OF
        oMainWnd
        Pixel
        # Divide a tela em dois containers, um de 30% e outro de 68%
        oTela = FWFormContainer().New(oDlgPrinc)
        cIdGrupo = oTela.CreateHorizontalBox(30)
        cIdProdut = oTela.CreateHorizontalBox(68)
        oTela.Activate(oDlgPrinc, False)
        # Cria os painéis
        oPanelUp = oTela.GetPanel(cIdGrupo)
        oPanelDown = oTela.GetPanel(cIdProdut)
        # Cria o browse superior trazendo dados da SBM
        oBrowseUp = FWmBrowse().New()
        oBrowseUp.SetOwner(oPanelUp)
        oBrowseUp.SetDescription('Grupos')
        oBrowseUp.SetAlias('SBM')
        oBrowseUp.DisableDetails()
        oBrowseUp.SetProfileID('1')
        oBrowseUp.ExecuteFilter(True)
        oBrowseUp.SetMainProc('MATA010')
        oBrowseUp.ForceQuitButton()
        oBrowseUp.SetMenuDef('MATA035')
        oBrowseUp.SetCacheView(False)
        oBrowseUp.SetOnlyFields(['BM_GRUPO', 'BM_DESC'])
        oBrowseUp.Activate()
        # Cria o browse inferior, que irá trazer todos os produtos
        aRotina = FWLoadMenuDef('MATA010')
        oBrowseDwn = FWMBrowse().New()
        oBrowseDwn.SetOwner(oPanelDown)
        oBrowseDwn.SetDescription('Produtos')
        oBrowseDwn.SetMenuDef('MATA010')
        oBrowseDwn.DisableDetails()
        oBrowseDwn.SetAlias('SB1')
        oBrowseDwn.SetProfileID('2')
        oBrowseDwn.SetMainProc('MATA035')
        oBrowseDwn.SetCacheView(False)
        oBrowseDwn.SetOnlyFields(['B1_COD', 'B1_DESC'])
        # Faz o relacionamento entre os dois browses
        oRelaction = FWBrwRelation().New()
        oRelaction.AddRelation(oBrowseUp, oBrowseDwn, [['B1_GRUPO', 'BM_GRUPO']])
        oRelaction.Activate()
        oBrowseDwn.Activate()
        # Atualiza os browses e cria a janela na tela
        oBrowseUp.Refresh()
        oBrowseDwn.Refresh()
        lEmExecucao = True
        Activate
        MsDialog
        oDlgPrinc
        Center
        lEmExecucao = False
        SetFunName(cFunBkp)

    RestArea(aArea)
    return Static

def MenuDef():
    aRotina = FWLoadMenuDef('MATA035')
    return aRotina
