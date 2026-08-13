// caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2023/12/20/criando-uma-arvore-de-navegacao-com-a-classe-dbtree-maratona-advpl-e-tl-134/
// Bibliotecas
#Include "TOTVS.ch"
// {Protheus.doc} User Function zExe134
// Cria uma navegação de níveis em árvore
// @type Function
// @author Atilio
// @since 15/12/2022
// @see https://tdn.totvs.com/display/public/framework/DBTree
// **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
USER FUNCTION zExe134()
    LOCAL cBmp1, cBmp2, aArea, aAreaSBM, aAreaSB1, nJanAltu, nJanLarg, oBtnFec, nAtu, nAtuGrp, nAtuPrd, nCorFundo, lDimPixels, cFontNome, oFontPadrao, aDados, cCadastro, oDlgTree, oDBTree, oSayGCod, oGetGCod, cGetGCod, oSayGDes, oGetGDes, cGetGDes, oSayPCod, oGetPCod, cGetPCod, oSayPDes, oGetPDes, cGetPDes, oSayPTip, oGetPTip, cGetPTip, oSayCarg, oGetCarg, cGetCarg

    cBmp1 := "PMSEDT3"
    cBmp2 := "PMSDOC"
    aArea := GetArea()
    aAreaSBM := SBM:GetArea()
    aAreaSB1 := SB1:GetArea()
    nJanAltu := 500
    nJanLarg := 700
    oBtnFec := Nil
    nAtu := 1
    nAtuGrp := 1
    nAtuPrd := 1
    nCorFundo := RGB(240, 240, 240)
    lDimPixels := .T.
    cFontNome := "Tahoma"
    oFontPadrao := TFont():New(cFontNome, Nil, - 12)
    aDados := {  }
    cCadastro := "Grupo de Produtos"
    oDlgTree := Nil
    oDBTree := Nil
    oSayGCod := Nil
    oGetGCod := Nil
    cGetGCod := Space(TamSX3("BM_GRUPO")[1])
    oSayGDes := Nil
    oGetGDes := Nil
    cGetGDes := Space(TamSX3("BM_DESC")[1])
    oSayPCod := Nil
    oGetPCod := Nil
    cGetPCod := Space(TamSX3("B1_COD")[1])
    oSayPDes := Nil
    oGetPDes := Nil
    cGetPDes := Space(TamSX3("B1_DESC")[1])
    oSayPTip := Nil
    oGetPTip := Nil
    cGetPTip := Space(TamSX3("B1_TIPO")[1])
    oSayCarg := Nil
    oGetCarg := Nil
    cGetCarg := Space(10)
    // Abrindo o grupo de produtos
    DbSelectArea("SBM")
    SBM:DbSetOrder(1)
    // BM_FILIAL+BM_GRUPO
    SBM:DbGoTop()
    // Abrindo os produtos
    DbSelectArea("SB1")
    SB1:DbSetOrder(4)
    // B1_FILIAL+B1_GRUPO+B1_COD
    SB1:DbGoTop()
    // Criando a janela
    oDlgTree := TDialog():New(0, 0, nJanAltu, nJanLarg, cCadastro, Nil, Nil, Nil, Nil, Nil, nCorFundo, Nil, Nil, lDimPixels)
    // Criando o DbTree
    oDBTree := DBTree():New(3, 3, nJanAltu / 2 - 100, nJanLarg / 2 - 3, oDlgTree, Nil, Nil, .T.)
    // Adiciona raíz
    oDBTree:AddTree("Grupo de Produtos" + Space(30), .T., cBmp1, cBmp1, Nil, Nil, cValToChar(nAtu) + ".0.0")
    aAdd(aDados, { cValToChar(nAtu) + ".0.0", "", "" })
    // Código do Produto
    cGetCarg := cValToChar(nAtu) + ".0.0"
    // Enquanto houver grupo de produtos
    While .NOT. SBM->( DbEof() )
        // Adiciona raíz
        oDBTree:AddTree(SBM->BM_GRUPO + " - " + SBM->BM_DESC, .T., cBmp1, cBmp1, Nil, Nil, cValToChar(nAtu) + "." + cValToChar(nAtuGrp) + ".0")
        nAtuPrd := 1
        aAdd(aDados, { cValToChar(nAtu) + "." + cValToChar(nAtuGrp) + ".0", SBM->BM_GRUPO, "" })
        // Código do Produto
        // Tenta posicionar no produto
        If SB1:DbSeek(FWxFilial("SB1") + SBM->BM_GRUPO)
            While .NOT. SB1->( DbEof() ) .AND. FWxFilial("SB1") + SBM->BM_GRUPO = SB1->B1_FILIAL + SB1->B1_GRUPO
                oDBTree:AddTreeItem(Alltrim(SB1->B1_COD) + " - " + SB1->B1_DESC, cBmp2, Nil, cValToChar(nAtu) + "." + cValToChar(nAtuGrp) + "." + cValToChar(nAtuPrd))
                aAdd(aDados, { cValToChar(nAtu) + "." + cValToChar(nAtuGrp) + "." + cValToChar(nAtuPrd), SBM->BM_GRUPO, SB1->B1_COD })
                // Código do Produto
                nAtuPrd += 1
                SB1:DbSkip()
            EndDo
        EndIf
        // Finaliza raíz
        oDBTree:EndTree()
        nAtuGrp += 1
        SBM:DbSkip()
    EndDo
    // Finaliza raíz
    oDBTree:EndTree()
    // Montando os says e gets - Grupo de Produto
    oSayGCod := TSay():New(nJanAltu / 2 - 80, 10, Nil, oDlgTree, Nil, oFontPadrao, Nil, Nil, Nil, lDimPixels, Nil, Nil, 30, 8, Nil, Nil, Nil, Nil, Nil)
    oGetGCod := TGet():New(nJanAltu / 2 - 83, 60, Nil, oDlgTree, 50, 12, Nil, Nil, Nil, Nil, oFontPadrao, Nil, Nil, lDimPixels)
    oSayGDes := TSay():New(nJanAltu / 2 - 80, 170, Nil, oDlgTree, Nil, oFontPadrao, Nil, Nil, Nil, lDimPixels, Nil, Nil, 30, 8, Nil, Nil, Nil, Nil, Nil)
    oGetGDes := TGet():New(nJanAltu / 2 - 83, 220, Nil, oDlgTree, 100, 12, Nil, Nil, Nil, Nil, oFontPadrao, Nil, Nil, lDimPixels)
    // Montando os says e gets - Produto
    oSayPCod := TSay():New(nJanAltu / 2 - 60, 10, Nil, oDlgTree, Nil, oFontPadrao, Nil, Nil, Nil, lDimPixels, Nil, Nil, 30, 8, Nil, Nil, Nil, Nil, Nil)
    oGetPCod := TGet():New(nJanAltu / 2 - 63, 60, Nil, oDlgTree, 50, 12, Nil, Nil, Nil, Nil, oFontPadrao, Nil, Nil, lDimPixels)
    oSayPDes := TSay():New(nJanAltu / 2 - 60, 170, Nil, oDlgTree, Nil, oFontPadrao, Nil, Nil, Nil, lDimPixels, Nil, Nil, 30, 8, Nil, Nil, Nil, Nil, Nil)
    oGetPDes := TGet():New(nJanAltu / 2 - 63, 220, Nil, oDlgTree, 100, 12, Nil, Nil, Nil, Nil, oFontPadrao, Nil, Nil, lDimPixels)
    oSayPTip := TSay():New(nJanAltu / 2 - 40, 10, Nil, oDlgTree, Nil, oFontPadrao, Nil, Nil, Nil, lDimPixels, Nil, Nil, 30, 8, Nil, Nil, Nil, Nil, Nil)
    oGetPTip := TGet():New(nJanAltu / 2 - 43, 60, Nil, oDlgTree, 30, 12, Nil, Nil, Nil, Nil, oFontPadrao, Nil, Nil, lDimPixels)
    // Cargo
    oSayCarg := TSay():New(nJanAltu / 2 - 20, 10, Nil, oDlgTree, Nil, oFontPadrao, Nil, Nil, Nil, lDimPixels, Nil, Nil, 30, 8, Nil, Nil, Nil, Nil, Nil)
    oGetCarg := TGet():New(nJanAltu / 2 - 23, 60, Nil, oDlgTree, 100, 12, Nil, Nil, Nil, Nil, oFontPadrao, Nil, Nil, lDimPixels)
    // Criando um botão para fechar a janela
    oBtnFec := TButton():New(nJanAltu / 2 - 20, nJanLarg / 2 - 61 * 1, "Fechar", oDlgTree, Nil, 58, 17, Nil, oFontPadrao, Nil, lDimPixels)
    // Deixa todos os gets como ReadOnly
    oGetGCod->lReadOnly := .T.
    oGetGDes->lReadOnly := .T.
    oGetPCod->lReadOnly := .T.
    oGetPDes->lReadOnly := .T.
    oGetPTip->lReadOnly := .T.
    oGetCarg->lReadOnly := .T.
    oDlgTree:Activate(Nil, Nil, Nil, .T.)
    RestArea(aAreaSB1)
    RestArea(aAreaSBM)
    RestArea(aArea)
    RETURN Static

FUNCTION fProc(cCargo)
    LOCAL nEncon, cGetGCod, cGetGDes, cGetPCod, cGetPDes, cGetPTip, cGetCarg

    nEncon := aScan(aDados, Nil)
    // Se conseguiu encontrar algo
    If nEncon > 0
        // Se tiver grupo de produto
        If .NOT. Empty(aDados[nEncon][2])
            SBM:DbSetOrder(1)
            // BM_FILIAL+BM_GRUPO
            SBM:DbSeek(FWxFilial("SBM") + aDados[nEncon][2])
            cGetGCod := SBM->BM_GRUPO
            cGetGDes := SBM->BM_DESC
            // Senão
        Else
            cGetGCod := ""
            cGetGDes := ""
        EndIf
        // Se tiver produto
        If .NOT. Empty(aDados[nEncon][3])
            SB1:DbSetOrder(1)
            // B1_FILIAL+B1_COD
            SB1:DbSeek(FWxFilial("SB1") + aDados[nEncon][3])
            cGetPCod := SB1->B1_COD
            cGetPDes := SB1->B1_DESC
            cGetPTip := SB1->B1_TIPO
            // Senão
        Else
            cGetPCod := ""
            cGetPDes := ""
            cGetPTip := ""
        EndIf
        // Senão
    Else
        cGetGCod := ""
        cGetGDes := ""
        cGetPCod := ""
        cGetPDes := ""
        cGetPTip := ""
    EndIf
    // Definindo o cargo
    cGetCarg := cCargo
    // Atualizando gets
    oGetGCod:Refresh()
    oGetGDes:Refresh()
    oGetPCod:Refresh()
    oGetPDes:Refresh()
    oGetPTip:Refresh()
    oGetCarg:Refresh()
    RETURN
