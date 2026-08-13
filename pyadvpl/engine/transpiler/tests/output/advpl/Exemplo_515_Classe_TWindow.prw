// caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2024/07/03/criando-uma-janela-atraves-da-twindow-maratona-advpl-e-tl-515/
// Bibliotecas
#Include "TOTVS.ch"
// {Protheus.doc} User Function zExe515
// Cria uma janela nativa com comportamento do sistema operacional (como minimizar)
// @type  Function
// @author Atilio
// @since 05/04/2023
// @see https://tdn.totvs.com/display/tec/TWindow
// **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
USER FUNCTION zExe515()
    LOCAL lContinua, cEmprAux, cFilAux, cUsrAux, cPswAux, lProgInic

    lContinua := .T.
    cEmprAux := "99"
    cFilAux := ""
    cUsrAux := ""
    cPswAux := ""
    lProgInic := .F.
    // Se a SX2 não tiver aberta, quer dizer que não veio pelo Protheus, logo é quiosque
    If Select("SX2") = 0
        // Montando uma seção, apenas para poder pegar os parâmetros da SX61
        RPCSetEnv(cEmprAux, "", "", "", "")
        // Verificando se o login deu certo
        If u_zLogin(@ cUsrAux, @ cPswAux)
            RPCSetEnv(cEmprAux, cFilAux, cUsrAux, cPswAux, "SIGAEST")
            lContinua := .T.
            lProgInic := .T.
        Else
            lContinua := .F.
        EndIf
    EndIf
    If lContinua
        fMontaTela()
    EndIf
    RETURN Static

FUNCTION fMontaTela()
    LOCAL nLinObj, nLargBtn, nAltuBtn, bConfirm, bCancela, cFontPad, oFontBtn, oFontBtnN, oFontMod, oFontMaior, oFontSub, lCentered, oBtConfirm, oBtCancela, oSayTitulo, cSayTitulo, oSayEtiqus, cSayEtiqus, oDlgCentral, aTamanho, nJanLarg, nJanAltu, nPosTop, nPosLeft, cEspacProd, oGetProdut, cGetProdut, oGetBlank, cGetBlank, oGridPro, aHeaderPro, aColsPro

    nLinObj := 0
    nLargBtn := 85
    nAltuBtn := 15
    // Blocos de código chamados pelos botões
    bConfirm := Nil
    bCancela := Nil
    // Fontes
    cFontPad := "Tahoma"
    oFontBtn := TFont():New(cFontPad, Nil, - 14)
    oFontBtnN := TFont():New(cFontPad, Nil, - 14, Nil, .T.)
    oFontMod := TFont():New(cFontPad, Nil, - 38)
    oFontMaior := TFont():New(cFontPad, Nil, - 68)
    oFontSub := TFont():New(cFontPad, Nil, - 20)
    // Objetos da Janela
    lCentered := Nil
    oBtConfirm := Nil
    oBtCancela := Nil
    oSayTitulo := Nil
    cSayTitulo := "Tela de Testes"
    oSayEtiqus := Nil
    cSayEtiqus := "000"
    oDlgCentral := Nil
    // Tamanho da janela
    aTamanho := Nil
    nJanLarg := Nil
    nJanAltu := Nil
    nPosTop := Nil
    nPosLeft := Nil
    // Etiqueta
    cEspacProd := Space(TamSX3("B1_COD")[1])
    oGetProdut := Nil
    cGetProdut := cEspacProd
    oGetBlank := Nil
    cGetBlank := ""
    // Grid
    oGridPro := Nil
    aHeaderPro := {  }
    aColsPro := {  }
    // Se vier do programa inicial, a dimensão será diferente
    If lProgInic
        aTamanho := GetScreenRes()
        nJanLarg := aTamanho[1]
        nJanAltu := aTamanho[2] - 80
        lCentered := .F.
        nPosTop := 0
        nPosLeft := - 10
    Else
        aTamanho := MsAdvSize()
        nJanLarg := aTamanho[5]
        nJanAltu := aTamanho[6]
        lCentered := .T.
        nPosTop := 0
        nPosLeft := 0
    EndIf
    // Cria o cabeçalho da grid
    // Titulo                    Campo         Picture                        Tamanho                       Dec                     Valid           Usado  Tipo F3
    aAdd(aHeaderPro, { "Produto", "XX_PROD", "", 15, 0, ".F.", ".F.", "C", "", "" })
    aAdd(aHeaderPro, { "Descrição", "XX_DESC", "", 30, 0, ".F.", ".F.", "C", "", "" })
    aAdd(aHeaderPro, { "SB1 RecNo", "XX_RECNUM", "@E 999,999,999,999,999,999", 18, 0, ".F.", ".F.", "N", "", "" })
    aAdd(aHeaderPro, { " ", "XX_BLANK", "", 1, 0, ".F.", ".F.", "C", "", "" })
    // Cria a janela
    If lProgInic
        oDlgCentral := TWindow():New(nPosTop, nPosLeft, nJanAltu, nJanLarg, cSayTitulo, Nil, Nil, Nil, Nil, Nil, Nil, Nil, CLR_BLACK, RGB(250, 250, 250), Nil, Nil, Nil, Nil, Nil, Nil, .T.)
    Else
        oDlgCentral := TDialog():New(nPosTop, nPosLeft, nJanAltu, nJanLarg, cSayTitulo, Nil, Nil, Nil, Nil, CLR_BLACK, RGB(250, 250, 250), Nil, Nil, .T.)
    EndIf
    // Títulos e SubTítulos
    oSayTitulo := TSay():New(4, 3, Nil, oDlgCentral, "", oFontMod, Nil, Nil, Nil, .T., RGB(149, 179, 215), Nil, 200, 30, Nil, Nil, Nil, Nil, Nil, .F., Nil)
    oSayEtiqus := TSay():New(- 3, nJanLarg / 2 - 120, Nil, oDlgCentral, "", oFontMaior, Nil, Nil, Nil, .T., RGB(255, 0, 0), Nil, 100, 50, Nil, Nil, Nil, Nil, Nil, .F., Nil)
    // Get da Etiqueta
    nLinObj := 36
    oGetProdut := TGet():New(nLinObj, 3, Nil, oDlgCentral, nJanLarg / 2 - 3, 20, "@!", Nil, Nil, Nil, oFontMod, Nil, Nil, .T., Nil, Nil, Nil, Nil, Nil, Nil, .F., Nil, Nil, Nil, Nil, Nil, Nil, Nil, Nil, Nil, Nil, Nil, Nil, Nil, Nil, Nil)
    oGetProdut->cPlaceHold := "< Código do Produto >"
    oGetBlank := TGet():New(- 100, - 100, Nil, oDlgCentral, 10, 10, Nil, Nil, Nil, Nil, oFontBtn, Nil, Nil, .T.)
    oGetBlank->bGotFocus := Nil
    // Botões
    nLinObj := 59
    oBtConfirm := TButton():New(nLinObj + nAltuBtn * 0, nJanLarg / 2 - nLargBtn * 1, "Confirmar", oDlgCentral, bConfirm, nLargBtn, nAltuBtn, Nil, oFontBtnN, Nil, .T., Nil, Nil, Nil, Nil, Nil)
    oBtCancela := TButton():New(nLinObj + nAltuBtn * 1, nJanLarg / 2 - nLargBtn * 1, "Cancelar", oDlgCentral, bCancela, nLargBtn, nAltuBtn, Nil, oFontBtn, Nil, .T., Nil, Nil, Nil, Nil, Nil)
    // Abaixo cria a grid
    oGridPro := MsNewGetDados():New(nLinObj, 3, nJanAltu / 2 - 3, nJanLarg / 2 - 3 - nLargBtn, Nil, "AllwaysTrue()", Nil, "", {  }, Nil, 99999999, Nil, Nil, Nil, oDlgCentral, aHeaderPro, aColsPro)
    // aCols
    oGridPro:oBrowse():SetCSS(u_zCSSGrid())
    oGridPro->lActive := .F.
    // Ativa e exibe a janela
    If lProgInic
        oDlgCentral:Activate("MAXIMIZED")
    Else
        oDlgCentral:Activate(Nil, Nil, Nil, lCentered, Nil, Nil)
    EndIf
    RETURN Static

FUNCTION fVldCodig()
    LOCAL lRet, aColsAux, lAdiciona, nPosProd, nLinha, cSayEtiqus, cGetProdut

    lRet := .T.
    aColsAux := oGridPro:aCols()
    lAdiciona := .T.
    nPosProd := aScan(aHeaderPro, Nil)
    nLinha := 0
    // Somente se tiver código de etiqueta
    If .NOT. Empty(cGetProdut)
        // Validar se a etiqueta não foi inserida na grid ainda
        // Se deu tudo certo
        If lAdiciona
            DbSelectArea("SB1")
            SB1:DbSetOrder(1)
            // Se conseguir posicionar no produto
            If SB1:MsSeek(FWxFilial("SB1") + cGetProdut)
                // Se tiver apenas 1 linha e a coluna do produto estivar vazia
                If Len(aColsAux) = 1 .AND. Empty(aColsAux[1][nPosProd])
                    aColsAux := {  }
                EndIf
                // Adiciona uma linha na grid
                aAdd(aColsAux, { SB1->B1_COD, SubStr(SB1->B1_DESC, 1, 30), SB1:RecNo(), "", .F. })
                oGridPro:SetArray(aColsAux)
                oGridPro:Refresh()
                // Atualiza produtos lidos
                cSayEtiqus := Soma1(cSayEtiqus)
                oSayEtiqus:Refresh()
            Else
                FWAlertError("O produto '" + cGetProdut + "' não encontrado!", "Falha")
            EndIf
        EndIf
        // Zera o Get, para ser inserida uma nova etiqueta
        cGetProdut := cEspacProd
    EndIf
    RETURN lRet

STATIC FUNCTION fCancelar()
    LOCAL aColsAux, cSayEtiqus

    aColsAux := oGridPro:aCols()
    // Somente se a pergunta for confirmada
    If FWAlertYesNo("Deseja cancelar?", "Continua?")
        aColsAux := {  }
        oGridPro:SetArray(aColsAux)
        oGridPro:Refresh()
        cSayEtiqus := "000"
        oSayEtiqus:Refresh()
    EndIf
    RETURN
