# Esse exemplo faz parte da série do YouTube, Maratona de Exemplos, do canal Terminal de Informação, 
#     caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2023/12/20/criando-uma-arvore-de-navegacao-com-a-classe-dbtree-maratona-advpl-e-tl-134/
# Bibliotecas
# PREPROCESSOR: #Include "TOTVS.ch"
# {Protheus.doc} User Function zExe134
# Cria uma navegação de níveis em árvore
# @type Function
# @author Atilio
# @since 15/12/2022
# @see https://tdn.totvs.com/display/public/framework/DBTree
# @obs 
# 
#     **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
def u_zExe134():
    cBmp1 = 'PMSEDT3'
    cBmp2 = 'PMSDOC'
    aArea = GetArea()
    aAreaSBM = SBM.GetArea()
    aAreaSB1 = SB1.GetArea()
    nJanAltu = 500
    nJanLarg = 700
    oBtnFec = None
    nAtu = 1
    nAtuGrp = 1
    nAtuPrd = 1
    nCorFundo = RGB(240, 240, 240)
    lDimPixels = True
    cFontNome = 'Tahoma'
    oFontPadrao = TFont().New(cFontNome, None, -12)
    aDados = []
    cCadastro = 'Grupo de Produtos'
    oDlgTree = None
    oDBTree = None
    oSayGCod = None
    oGetGCod = None
    cGetGCod = Space(TamSX3('BM_GRUPO')[1])
    oSayGDes = None
    oGetGDes = None
    cGetGDes = Space(TamSX3('BM_DESC')[1])
    oSayPCod = None
    oGetPCod = None
    cGetPCod = Space(TamSX3('B1_COD')[1])
    oSayPDes = None
    oGetPDes = None
    cGetPDes = Space(TamSX3('B1_DESC')[1])
    oSayPTip = None
    oGetPTip = None
    cGetPTip = Space(TamSX3('B1_TIPO')[1])
    oSayCarg = None
    oGetCarg = None
    cGetCarg = Space(10)
    # Abrindo o grupo de produtos
    DbSelectArea('SBM')
    SBM.DbSetOrder(1)
    # BM_FILIAL+BM_GRUPO
    SBM.DbGoTop()
    # Abrindo os produtos
    DbSelectArea('SB1')
    SB1.DbSetOrder(4)
    # B1_FILIAL+B1_GRUPO+B1_COD
    SB1.DbGoTop()
    # Criando a janela
    oDlgTree = TDialog().New(0, 0, nJanAltu, nJanLarg, cCadastro, None, None, None, None, None, nCorFundo, None, None, lDimPixels)
    # Criando o DbTree
    oDBTree = DBTree().New(3, 3, nJanAltu / 2 - 100, nJanLarg / 2 - 3, oDlgTree, lambda : fProc(oDBTree.GetCargo()), None, True)
    # Adiciona raíz
    oDBTree.AddTree('Grupo de Produtos' + Space(30), True, cBmp1, cBmp1, None, None, cValToChar(nAtu) + '.0.0')
    aAdd(aDados, [cValToChar(nAtu) + '.0.0', '', ''])
    # Código do Produto
    cGetCarg = cValToChar(nAtu) + '.0.0'
    # Enquanto houver grupo de produtos
    while not SBM.EoF():
        # Adiciona raíz
        oDBTree.AddTree(SBM.BM_GRUPO + ' - ' + SBM.BM_DESC, True, cBmp1, cBmp1, None, None, cValToChar(nAtu) + '.' + cValToChar(nAtuGrp) + '.0')
        nAtuPrd = 1
        aAdd(aDados, [cValToChar(nAtu) + '.' + cValToChar(nAtuGrp) + '.0', SBM.BM_GRUPO, ''])
        # Código do Produto
        # Tenta posicionar no produto
        if SB1.DbSeek(FWxFilial('SB1') + SBM.BM_GRUPO):
            while not SB1.EoF() and FWxFilial('SB1') + SBM.BM_GRUPO == SB1.B1_FILIAL + SB1.B1_GRUPO:
                oDBTree.AddTreeItem(Alltrim(SB1.B1_COD) + ' - ' + SB1.B1_DESC, cBmp2, None, cValToChar(nAtu) + '.' + cValToChar(nAtuGrp) + '.' + cValToChar(nAtuPrd))
                aAdd(aDados, [cValToChar(nAtu) + '.' + cValToChar(nAtuGrp) + '.' + cValToChar(nAtuPrd), SBM.BM_GRUPO, SB1.B1_COD])
                # Código do Produto
                nAtuPrd += 1
                SB1.DbSkip()


        # Finaliza raíz
        oDBTree.EndTree()
        nAtuGrp += 1
        SBM.DbSkip()

    # Finaliza raíz
    oDBTree.EndTree()
    # Montando os says e gets - Grupo de Produto
    oSayGCod = TSay().New(nJanAltu / 2 - 80, 10, lambda : 'Grupo:', oDlgTree, None, oFontPadrao, None, None, None, lDimPixels, None, None, 30, 8, None, None, None, None, None)
    oGetGCod = TGet().New(nJanAltu / 2 - 83, 60, lambda u: ((cGetGCod := u) if PCount() > 0 else cGetGCod), oDlgTree, 50, 12, None, None, None, None, oFontPadrao, None, None, lDimPixels)
    oSayGDes = TSay().New(nJanAltu / 2 - 80, 170, lambda : 'Descrição:', oDlgTree, None, oFontPadrao, None, None, None, lDimPixels, None, None, 30, 8, None, None, None, None, None)
    oGetGDes = TGet().New(nJanAltu / 2 - 83, 220, lambda u: ((cGetGDes := u) if PCount() > 0 else cGetGDes), oDlgTree, 100, 12, None, None, None, None, oFontPadrao, None, None, lDimPixels)
    # Montando os says e gets - Produto
    oSayPCod = TSay().New(nJanAltu / 2 - 60, 10, lambda : 'Produto:', oDlgTree, None, oFontPadrao, None, None, None, lDimPixels, None, None, 30, 8, None, None, None, None, None)
    oGetPCod = TGet().New(nJanAltu / 2 - 63, 60, lambda u: ((cGetPCod := u) if PCount() > 0 else cGetPCod), oDlgTree, 50, 12, None, None, None, None, oFontPadrao, None, None, lDimPixels)
    oSayPDes = TSay().New(nJanAltu / 2 - 60, 170, lambda : 'Prod.Desc:', oDlgTree, None, oFontPadrao, None, None, None, lDimPixels, None, None, 30, 8, None, None, None, None, None)
    oGetPDes = TGet().New(nJanAltu / 2 - 63, 220, lambda u: ((cGetPDes := u) if PCount() > 0 else cGetPDes), oDlgTree, 100, 12, None, None, None, None, oFontPadrao, None, None, lDimPixels)
    oSayPTip = TSay().New(nJanAltu / 2 - 40, 10, lambda : 'Prod.Tipo:', oDlgTree, None, oFontPadrao, None, None, None, lDimPixels, None, None, 30, 8, None, None, None, None, None)
    oGetPTip = TGet().New(nJanAltu / 2 - 43, 60, lambda u: ((cGetPTip := u) if PCount() > 0 else cGetPTip), oDlgTree, 30, 12, None, None, None, None, oFontPadrao, None, None, lDimPixels)
    # Cargo
    oSayCarg = TSay().New(nJanAltu / 2 - 20, 10, lambda : 'Cargo:', oDlgTree, None, oFontPadrao, None, None, None, lDimPixels, None, None, 30, 8, None, None, None, None, None)
    oGetCarg = TGet().New(nJanAltu / 2 - 23, 60, lambda u: ((cGetCarg := u) if PCount() > 0 else cGetCarg), oDlgTree, 100, 12, None, None, None, None, oFontPadrao, None, None, lDimPixels)
    # Criando um botão para fechar a janela
    oBtnFec = TButton().New(nJanAltu / 2 - 20, nJanLarg / 2 - 61 * 1, 'Fechar', oDlgTree, lambda : oDlgTree.End(), 58, 17, None, oFontPadrao, None, lDimPixels)
    # Deixa todos os gets como ReadOnly
    oGetGCod.lReadOnly = True
    oGetGDes.lReadOnly = True
    oGetPCod.lReadOnly = True
    oGetPDes.lReadOnly = True
    oGetPTip.lReadOnly = True
    oGetCarg.lReadOnly = True
    oDlgTree.Activate(None, None, None, True)
    RestArea(aAreaSB1)
    RestArea(aAreaSBM)
    RestArea(aArea)
    return Static

def fProc(cCargo):
    nEncon = aScan(aDados, lambda x: AllTrim(x[1]) == cCargo)
    # Se conseguiu encontrar algo
    if nEncon > 0:
        # Se tiver grupo de produto
        if not Empty(aDados[nEncon][2]):
            SBM.DbSetOrder(1)
            # BM_FILIAL+BM_GRUPO
            SBM.DbSeek(FWxFilial('SBM') + aDados[nEncon][2])
            cGetGCod = SBM.BM_GRUPO
            cGetGDes = SBM.BM_DESC
            # Senão
        else:
            cGetGCod = ''
            cGetGDes = ''

        # Se tiver produto
        if not Empty(aDados[nEncon][3]):
            SB1.DbSetOrder(1)
            # B1_FILIAL+B1_COD
            SB1.DbSeek(FWxFilial('SB1') + aDados[nEncon][3])
            cGetPCod = SB1.B1_COD
            cGetPDes = SB1.B1_DESC
            cGetPTip = SB1.B1_TIPO
            # Senão
        else:
            cGetPCod = ''
            cGetPDes = ''
            cGetPTip = ''

        # Senão
    else:
        cGetGCod = ''
        cGetGDes = ''
        cGetPCod = ''
        cGetPDes = ''
        cGetPTip = ''

    # Definindo o cargo
    cGetCarg = cCargo
    # Atualizando gets
    oGetGCod.Refresh()
    oGetGDes.Refresh()
    oGetPCod.Refresh()
    oGetPDes.Refresh()
    oGetPTip.Refresh()
    oGetCarg.Refresh()
    return
