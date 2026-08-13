// caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2024/02/26/buscando-a-filial-usada-em-uma-tabela-com-fwxfilial-e-xfilial-maratona-advpl-e-tl-259/
// Bibliotecas
#Include "TOTVS.ch"
// {Protheus.doc} User Function zExe258
// Classe para criar uma uma navegação de Wizard (com opção de avançar ou retroceder)
// @type  Function
// @author Atilio
// @since 21/02/2023
// @see https://tdn.totvs.com/display/public/framework/FWWizardControl
// **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
USER FUNCTION zExe258()
    LOCAL aArea, nCorFundo, nJanAltura, nJanLargur, cJanTitulo, lCentraliz, lDimPixels, nObjLinha, nObjColun, nObjLargu, nObjAltur, cFontNome, oFontPadrao, oDialogPvt, bBlocoIni, oSayInsira, cSayInsira, oGetTexto, cGetTexto, oQrCode, oSayFim, cSayFim, oPanelGer, oWizard, oNewPag

    aArea := FWGetArea()
    nCorFundo := RGB(238, 238, 238)
    nJanAltura := 400
    nJanLargur := 600
    cJanTitulo := "Exemplo FWWizardControl"
    lCentraliz := .T.
    lDimPixels := .T.
    nObjLinha := 0
    nObjColun := 0
    nObjLargu := 0
    nObjAltur := 0
    cFontNome := "Tahoma"
    oFontPadrao := TFont():New(cFontNome, Nil, - 12)
    oDialogPvt := Nil
    bBlocoIni := Nil
    // Aqui voce pode acionar funcoes customizadas que irao ser acionadas ao abrir a dialog
    // objeto1
    oSayInsira := Nil
    cSayInsira := "Insira o Texto:"
    // objeto2
    oGetTexto := Nil
    cGetTexto := "https://terminaldeinformacao.com" + Space(200)
    // objeto3
    oQrCode := Nil
    // objeto4
    oSayFim := Nil
    cSayFim := "Wizard concluído!"
    // Objetos do Wizard
    oPanelGer := Nil
    oWizard := Nil
    // Cria a dialog
    oDialogPvt := TDialog():New(0, 0, nJanAltura, nJanLargur, cJanTitulo, Nil, Nil, Nil, Nil, Nil, nCorFundo, Nil, Nil, lDimPixels)
    // Cria um painel geral
    oPanelGer := TPanel():New(1, 1, "", oDialogPvt, Nil, Nil, Nil, RGB(0, 0, 0), RGB(254, 254, 254), nJanLargur / 2 - 1, nJanAltura / 2 - 3)
    // Instancia o Wizard
    oWizard := FWWizardControl():New(oPanelGer)
    oWizard:ActiveUISteps()
    // Página 1 do Wizard (terá um campo para o usuário digitar)
    oNewPag := oWizard:AddStep("1")
    oNewPag:SetStepDescription("Definição para usar o QRCode")
    oNewPag:SetConstruction(Nil)
    oNewPag:SetNextAction(Nil)
    oNewPag:SetCancelAction(Nil)
    // Página 2 do Wizard
    oNewPag := oWizard:AddStep("2", Nil)
    oNewPag:SetStepDescription("QRCode Gerado")
    oNewPag:SetNextAction(Nil)
    oNewPag:SetPrevAction(Nil)
    oNewPag:SetCancelAction(Nil)
    // Página 3 do Wizard
    oNewPag := oWizard:AddStep("3", Nil)
    oNewPag:SetStepDescription("Teste concluído")
    oNewPag:SetNextAction(Nil)
    oNewPag:SetPrevAction(Nil)
    oNewPag:SetCancelAction(Nil)
    // Ativa o Wizard para visualização
    oWizard:Activate()
    // Ativa e exibe a janela
    oDialogPvt:Activate(Nil, Nil, Nil, lCentraliz, Nil, Nil, bBlocoIni)
    FWRestArea(aArea)
    RETURN Static

FUNCTION fEncerra()
    oDialogPvt:End()
    RETURN .T.

STATIC FUNCTION fValidPag1()
    LOCAL lRet

    lRet := .T.
    // Se não houver texto para montar o QRCode, não permite prosseguir
    If Empty(cGetTexto)
        FWAlertError("Preencha algo no campo antes de prosseguir!", "Atenção")
        lRet := .F.
    Else
        // Se o QRCode já tiver sido criado, atualiza ele
        If ValType(oQrCode) = "O"
            oQrCode:SetCodeBar(cGetTexto)
            oQrCode:Refresh()
        EndIf
    EndIf
    RETURN lRet

STATIC FUNCTION fCriaPag1(oPanel)
    LOCAL nObjLinha, nObjColun, nObjLargu, nObjAltur, oSayInsira, oGetTexto

    // objeto1 - usando a classe TSay
    nObjLinha := 4
    nObjColun := 4
    nObjLargu := 70
    nObjAltur := 6
    oSayInsira := TSay():New(nObjLinha, nObjColun, Nil, oPanel, Nil, oFontPadrao, Nil, Nil, Nil, lDimPixels, Nil, Nil, nObjLargu, nObjAltur, Nil, Nil, Nil, Nil, Nil)
    // objeto2 - usando a classe TGet
    nObjLinha := 3
    nObjColun := 64
    nObjLargu := 110
    nObjAltur := 10
    oGetTexto := TGet():New(nObjLinha, nObjColun, Nil, oPanel, nObjLargu, nObjAltur, Nil, Nil, Nil, Nil, oFontPadrao, Nil, Nil, lDimPixels)
    RETURN Static

FUNCTION fCriaPag2(oPanel)
    LOCAL nObjLinha, nObjColun, nObjLargu, nObjAltur, oQrCode

    // objeto3 - usando a classe FWQRCode
    nObjLinha := 4
    nObjColun := 110
    nObjLargu := 160
    nObjAltur := 160
    oQrCode := FwQrCode():New({ nObjLinha, nObjColun, nObjLargu, nObjAltur }, oPanel, cGetTexto)
    RETURN Static

FUNCTION fCriaPag3(oPanel)
    LOCAL nObjLinha, nObjColun, nObjLargu, nObjAltur, oSayFim

    // objeto4 - usando a classe TSay
    nObjLinha := 4
    nObjColun := 4
    nObjLargu := 200
    nObjAltur := 6
    oSayFim := TSay():New(nObjLinha, nObjColun, Nil, oPanel, Nil, oFontPadrao, Nil, Nil, Nil, lDimPixels, Nil, Nil, nObjLargu, nObjAltur, Nil, Nil, Nil, Nil, Nil)
    RETURN
