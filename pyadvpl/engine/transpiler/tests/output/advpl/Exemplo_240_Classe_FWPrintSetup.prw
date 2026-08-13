// caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2024/02/17/configurando-a-impressao-atraves-da-fwprintsetup-maratona-advpl-e-tl-240/
// Bibliotecas
#Include "TOTVS.ch"
#Include "FWPrintSetup.ch"
// Constantes
#Define PAD_LEFT			0					//Alinhamento Esquerda
#Define PAD_RIGHT			1					//Alinhamento Direita
#Define PAD_CENTER			2					//Alinhamento Centralizado
#Define IMP_SPOOL           2
oSetupRel := Nil
// {Protheus.doc} User Function zExe240
// Imprime a etiqueta via fwmsprinter
// @type  Function
// @author Atilio
// @since 20/02/2023
// @see https://tdn.totvs.com/display/public/framework/FWPrintSetup
// **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
USER FUNCTION zExe240()
    LOCAL aArea, aPergs, cCodProd

    aArea := FWGetArea()
    aPergs := {  }
    cCodProd := Space(TamSX3("B1_COD")[1])
    // Adiciona os parâmetros que serão exibidos
    aAdd(aPergs, { 1, "Produto", cCodProd, "", ".T.", "SB1", ".T.", 60, .T. })
    // Se a pergunta for confirmada
    If ParamBox(aPergs, "Informe os parâmetros", Nil, Nil, Nil, Nil, Nil, Nil, Nil, Nil, .F., .F.)
        cCodProd := Alltrim(MV_PAR01)
        fImprEtq()
    EndIf
    FWRestArea(aArea)
    RETURN Static

FUNCTION fImprEtq()
    LOCAL oPrint, oBrush, nAltura, nLargura, nLinAux, lNegrito, lSublinhado, lItalico, cNomeFont, oFontDadN, oFontRoda

    oPrint := Nil
    oBrush := TBrush():New(Nil, RGB(0, 0, 0))
    nAltura := 1200
    nLargura := 1200
    nLinAux := 0
    lNegrito := .T.
    lSublinhado := .T.
    lItalico := .T.
    cNomeFont := "Arial"
    oFontDadN := TFont():New(cNomeFont, Nil, - 15, Nil, lNegrito, Nil, Nil, Nil, Nil, .NOT. lSublinhado, .NOT. lItalico)
    oFontRoda := TFont():New(cNomeFont, Nil, - 13, Nil, lNegrito, Nil, Nil, Nil, Nil, .NOT. lSublinhado, .NOT. lItalico)
    DbSelectArea("SB1")
    SB1:DbSetOrder(1)
    // Filial + Produto
    If SB1:MsSeek(FWxFilial("SB1") + cCodProd)
        // Criando a impressão
        oPrint := FwMsPrinter():New("ETQPRODU", Nil, .T., GetTempPath(), .T.)
        // Se ainda não tiver configuração de Setup
        While ValType(oSetupRel) = "U"
            fConfImpr()
        EndDo
        // Se for direto para impressora
        If oSetupRel:GetProperty(PD_PRINTTYPE) = IMP_SPOOL
            oPrint->nDevice := IMP_SPOOL
            oPrint->cPrinter := oSetupRel:aOptions()[PD_VALUETYPE]
        EndIf
        oPrint:StartPage()
        // Imprimindo o cabeçalho (imagem e mensagem)
        oPrint:SayBitmap(75, 10, "\x_imagens\logo.png", 105, 105)
        oPrint:Say(130, nLargura - 490, "Terminal de Informação", oFontDadN, Nil, Nil, Nil, PAD_CENTER)
        oPrint:Line(250, 0, 250, nAltura)
        nLinAux := 290
        oPrint:Say(nLinAux, 30, "Etiqueta de Produto", oFontDadN, Nil, Nil, Nil, PAD_LEFT)
        nLinAux += 80
        // Descrição
        oPrint:Say(nLinAux, 30, "Descrição:", oFontDadN, Nil, Nil, Nil, PAD_LEFT)
        oPrint:Say(nLinAux, 340, Alltrim(SB1->B1_DESC), oFontDadN, Nil, Nil, Nil, PAD_LEFT)
        nLinAux += 80
        // Data e Validade
        oPrint:Say(nLinAux, 30, "Tipo:", oFontDadN, Nil, Nil, Nil, PAD_LEFT)
        oPrint:Say(nLinAux, 340, SB1->B1_TIPO, oFontDadN, Nil, Nil, Nil, PAD_LEFT)
        oPrint:Say(nLinAux, 580, "U.M.:", oFontDadN, Nil, Nil, Nil, PAD_LEFT)
        oPrint:Say(nLinAux, 850, SB1->B1_UM, oFontDadN, Nil, Nil, Nil, PAD_LEFT)
        nLinAux += 80
        // Código de Barras
        oPrint:FwMsBar("CODE128", 12, 1, Alltrim(cCodProd), oPrint, .F., Nil, Nil, Nil, Nil, Nil, Nil, Nil, .F., Nil, Nil)
        nLinAux += 240
        // Dados finais
        oPrint:FillRect({ nLinAux - 20, 0, nAltura - 250, nLargura - 20 }, oBrush)
        oPrint:Say(nLinAux + 30, 30, "PRODUTO", oFontDadN, Nil, RGB(255, 255, 255), Nil, PAD_LEFT)
        oPrint:Say(nLinAux + 140, 30, cCodProd, oFontRoda, Nil, RGB(255, 255, 255), Nil, PAD_LEFT)
        oPrint:Say(nLinAux + 20, nLargura - 720, "Se tiver dúvidas", oFontRoda, Nil, RGB(255, 255, 255), Nil, PAD_CENTER)
        oPrint:Say(nLinAux + 60, nLargura - 720, "entre em contato conosco", oFontRoda, Nil, RGB(255, 255, 255), Nil, PAD_CENTER)
        oPrint:Say(nLinAux + 100, nLargura - 720, "através do e-Mail", oFontRoda, Nil, RGB(255, 255, 255), Nil, PAD_CENTER)
        oPrint:Say(nLinAux + 140, nLargura - 720, "contato@atiliosistemas.com", oFontRoda, Nil, RGB(255, 255, 255), Nil, PAD_CENTER)
        // Mandando para o spool de impressão
        oPrint:Print()
    Else
        FWAlertError("Produto não encontrado", "Falha")
    EndIf
    RETURN Static

FUNCTION fConfImpr()
    LOCAL aDevice, oSetup, cSession, cDevice, nPrintType, nOrientation, nLocal, nFlags, oSetupRel

    aDevice := { "DISCO", "SPOOL", "EMAIL", "EXCEL", "HTML", "PDF" }
    oSetup := Nil
    cSession := GetPrinterSession()
    cDevice := If_(Empty(fwGetProfString(cSession, "PRINTTYPE", "SPOOL", .T.)), "PDF", fwGetProfString(cSession, "PRINTTYPE", "SPOOL", .T.))
    nPrintType := aScan(aDevice, Nil)
    nOrientation := 1
    // If(fwGetProfString(cSession, "ORIENTATION", "PORTRAIT", .T.) == "PORTRAIT", 1, 2)
    nLocal := 2
    // If(fwGetProfString(cSession, "LOCAL", "SERVER", .T.) == "SERVER", 1, 2)
    nFlags := PD_ISTOTVSPRINTER + PD_DISABLEPAPERSIZE + PD_DISABLEPREVIEW + PD_DISABLEMARGIN
    // Cria o setup do relatório
    oSetup := FWPrintSetup():New(nFlags, "ETIQUETA")
    oSetup:SetPropert(PD_DESTINATION, nLocal)
    oSetup:SetPropert(PD_ORIENTATION, nOrientation)
    oSetup:SetPropert(PD_PRINTTYPE, nPrintType)
    oSetupRel := Nil
    // Se a tela for confirmada, atualiza o setup default do relatório
    If oSetup:Activate() = PD_OK
        If oSetup:GetProperty(PD_PRINTTYPE) = IMP_SPOOL .AND. oSetup:GetProperty(PD_DESTINATION) = 2
            oSetupRel := oSetup
        Else
            FWAlertInfo("Escolha o tipo SPOOL e LOCAL para impressão!")
        EndIf
    EndIf
    RETURN
