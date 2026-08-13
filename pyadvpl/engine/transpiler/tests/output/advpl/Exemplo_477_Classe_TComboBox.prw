// caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2024/06/14/criando-um-combo-atraves-da-tcombobox-maratona-advpl-e-tl-477/
// Bibliotecas
#Include "TOTVS.ch"
// {Protheus.doc} User Function zExe477
// Classe para criar combobox em uma Dialog
// @type Function
// @author Atilio
// @since 03/04/2023
// @see https://tdn.totvs.com/display/tec/TComboBox
// **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
USER FUNCTION zExe477()
    LOCAL aArea, nCorFundo, nJanAltura, nJanLargur, cJanTitulo, lDimPixels, lCentraliz, nObjLinha, nObjColun, nObjLargu, nObjAltur, cFontNome, oFontPadrao, oDialogPvt, bBlocoIni, oSayObj0, cSayObj0, oCmbObj1, cCmbObj1, aCmbObj1, oSayObj2, cSayObj2, oCmbObj3, cCmbObj3, aCmbObj3, oBtnObj4, cBtnObj4, bBtnObj4

    aArea := FWGetArea()
    nCorFundo := RGB(238, 238, 238)
    nJanAltura := 190
    nJanLargur := 245
    cJanTitulo := "Exemplo Combo"
    lDimPixels := .T.
    lCentraliz := .T.
    nObjLinha := 0
    nObjColun := 0
    nObjLargu := 0
    nObjAltur := 0
    cFontNome := "Tahoma"
    oFontPadrao := TFont():New(cFontNome, Nil, - 12)
    oDialogPvt := Nil
    bBlocoIni := Nil
    // Aqui voce pode acionar funcoes customizadas que irao ser acionadas ao abrir a dialog
    // objeto0
    oSayObj0 := Nil
    cSayObj0 := "Região:"
    // objeto1
    oCmbObj1 := Nil
    cCmbObj1 := "XX"
    aCmbObj1 := { "XX=Nenhuma Região", "NT=Norte", "ND=Nordeste", "CO=Centro Oeste", "SD=Sudeste", "SU=Sul" }
    // objeto2
    oSayObj2 := Nil
    cSayObj2 := "Estado:"
    // objeto3
    oCmbObj3 := Nil
    cCmbObj3 := ""
    aCmbObj3 := {  }
    // objeto4
    oBtnObj4 := Nil
    cBtnObj4 := "Confirmar"
    bBtnObj4 := Nil
    // Cria a dialog
    oDialogPvt := TDialog():New(0, 0, nJanAltura, nJanLargur, cJanTitulo, Nil, Nil, Nil, Nil, Nil, nCorFundo, Nil, Nil, lDimPixels)
    // objeto0 - usando a classe TSay
    nObjLinha := 8
    nObjColun := 7
    nObjLargu := 28
    nObjAltur := 6
    oSayObj0 := TSay():New(nObjLinha, nObjColun, Nil, oDialogPvt, Nil, oFontPadrao, Nil, Nil, Nil, lDimPixels, Nil, Nil, nObjLargu, nObjAltur, Nil, Nil, Nil, Nil, Nil)
    // objeto1 - usando a classe TComboBox
    nObjLinha := 17
    nObjColun := 18
    nObjLargu := 100
    nObjAltur := 12
    oCmbObj1 := TComboBox():New(nObjLinha, nObjColun, Nil, aCmbObj1, nObjLargu, nObjAltur, oDialogPvt, Nil, Nil, Nil, Nil, Nil, lDimPixels, oFontPadrao)
    // objeto2 - usando a classe TSay
    nObjLinha := 35
    nObjColun := 7
    nObjLargu := 28
    nObjAltur := 6
    oSayObj2 := TSay():New(nObjLinha, nObjColun, Nil, oDialogPvt, Nil, oFontPadrao, Nil, Nil, Nil, lDimPixels, Nil, Nil, nObjLargu, nObjAltur, Nil, Nil, Nil, Nil, Nil)
    // objeto3 - usando a classe TComboBox
    nObjLinha := 44
    nObjColun := 18
    nObjLargu := 100
    nObjAltur := 12
    oCmbObj3 := TComboBox():New(nObjLinha, nObjColun, Nil, aCmbObj3, nObjLargu, nObjAltur, oDialogPvt, Nil, Nil, Nil, Nil, Nil, lDimPixels, oFontPadrao)
    // objeto4 - usando a classe TButton
    nObjLinha := 72
    nObjColun := 70
    nObjLargu := 50
    nObjAltur := 15
    oBtnObj4 := TButton():New(nObjLinha, nObjColun, cBtnObj4, oDialogPvt, bBtnObj4, nObjLargu, nObjAltur, Nil, oFontPadrao, Nil, lDimPixels)
    // Ativa e exibe a janela
    oDialogPvt:Activate(Nil, Nil, Nil, lCentraliz, Nil, Nil, bBlocoIni)
    FWRestArea(aArea)
    RETURN Static

FUNCTION fAtuCmb()
    LOCAL aEstados

    aEstados := {  }
    // Se for a região Norte
    If cCmbObj1 = "NT"
        aAdd(aEstados, "RR=Roraima")
        aAdd(aEstados, "AP=Amapá")
        aAdd(aEstados, "AM=Amazonas")
        aAdd(aEstados, "PA=Pará")
        aAdd(aEstados, "AC=Acre")
        aAdd(aEstados, "RO=Rondônia")
        aAdd(aEstados, "TO=Tocantins")
        // Senão se for a região Nordeste
    ElseIf cCmbObj1 = "ND"
        aAdd(aEstados, "MA=Maranhão")
        aAdd(aEstados, "PI=Piauí")
        aAdd(aEstados, "CE=Ceará")
        aAdd(aEstados, "RN=Rio Grande do Norte")
        aAdd(aEstados, "PB=Paraíba")
        aAdd(aEstados, "PE=Pernambuco")
        aAdd(aEstados, "AL=Alagoas")
        aAdd(aEstados, "SE=Sergipe")
        aAdd(aEstados, "BA=Bahia")
        // Senão se for a região Centro Oeste
    ElseIf cCmbObj1 = "CO"
        aAdd(aEstados, "MT=Mato Grosso")
        aAdd(aEstados, "DF=Distrito Federal")
        aAdd(aEstados, "GO=Goiás")
        aAdd(aEstados, "MS=Mato Grosso do Sul")
        // Senão se for a região Sudeste
    ElseIf cCmbObj1 = "SD"
        aAdd(aEstados, "MG=Minas Gerais")
        aAdd(aEstados, "ES=Espírito Santo")
        aAdd(aEstados, "RJ=Rio de Janeiro")
        aAdd(aEstados, "SP=São Paulo")
        // Senão se for a região Sul
    ElseIf cCmbObj1 = "SU"
        aAdd(aEstados, "PR=Paraná")
        aAdd(aEstados, "SC=Santa Catarina")
        aAdd(aEstados, "RS=Rio Grande do Sul")
        // Nenhuma região
    Else
        aAdd(aEstados, "")
    EndIf
    // Define no segundo combo o array com os estados
    oCmbObj3:SetItems(aEstados)
    oCmbObj3:Refresh()
    RETURN
