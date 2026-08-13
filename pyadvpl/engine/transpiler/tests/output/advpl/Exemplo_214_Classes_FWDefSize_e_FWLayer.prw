// caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2024/02/04/criando-camadas-dentro-de-uma-dialog-com-fwdefsize-e-fwlayer-maratona-advpl-e-tl-214/
// Bibliotecas
#Include "TOTVS.ch"
// {Protheus.doc} User Function zExe214
// Exemplo de função que cria uma tela com dimensionamentos responsivos
// @type Function
// @author Atilio
// @since 20/02/2023
// @see https://tdn.totvs.com/display/public/framework/FWDefSize e https://tdn.totvs.com/display/public/framework/FWLayer
// **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
USER FUNCTION zExe214()
    LOCAL aArea

    aArea := FWGetArea()
    If FWAlertYesNo("Você deseja ver o exemplo com FWLayer (sim) ou com FWDefSize (não)?", "Continua?")
        fExemplo1()
    Else
        fExemplo2()
    EndIf
    FWRestArea(aArea)
    RETURN Static

FUNCTION fExemplo1()
    LOCAL nLargBtn, nLinhaObj, nLargPanel, oDlgExemp, oFwLayer, oPanTitulo, oPanGrid, oPanCheck, oPanTotal, cMascara, oSayModulo, cSayModulo, oSayTitulo, cSayTitulo, oSaySubTit, cSaySubTit, aSize, nJanLarg, nJanAltu, cFontUti, oFontMod, oFontSub, oFontSubN, oFontBtn, oFontSay, aCampos, cAliasTmp, aColunas, oMarkBrowse, oSayChkDes, oSayChkPer, oSayChkVlr, oCheck01, lCheck01, oGetPerc01, nGetPerc01, oGetTot01, nGetTot01, oCheck02, lCheck02, oGetPerc02, nGetPerc02, oGetTot02, nGetTot02, oCheck03, lCheck03, oGetPerc03, nGetPerc03, oGetTot03, nGetTot03, oCheck04, lCheck04, oGetPerc04, nGetPerc04, oGetTot04, nGetTot04, oCheck05, lCheck05, oGetPerc05, nGetPerc05, oGetTot05, nGetTot05, oSayTot, cSayTot, oGetTot, nGetTot, oSayApu, cSayApu, oGetApu, nGetApu, oSayPro, cSayPro, oGetPro, nGetPro, oBtnProc, oBtnPrev, oTempTable, oPanHeader, oPanSair, oBtnSair, nTotEspCol, nTotCol01, nTotCol02, nTotCol03

    nLargBtn := 50
    nLinhaObj := 0
    nLargPanel := 0
    // Objetos e componentes gerais
    oDlgExemp := Nil
    oFwLayer := Nil
    oPanTitulo := Nil
    oPanGrid := Nil
    oPanCheck := Nil
    oPanTotal := Nil
    cMascara := "@E 999,999,999,999,999.99"
    // Cabeçalho
    oSayModulo := Nil
    cSayModulo := "TST"
    oSayTitulo := Nil
    cSayTitulo := "'Exemplo de Tela com"
    oSaySubTit := Nil
    cSaySubTit := "Objetos gráficos usando FWLayer"
    // Tamanho da janela
    aSize := MsAdvSize(.F.)
    nJanLarg := aSize[5]
    nJanAltu := aSize[6]
    // Fontes
    cFontUti := "Tahoma"
    oFontMod := TFont():New(cFontUti, Nil, - 38)
    oFontSub := TFont():New(cFontUti, Nil, - 20)
    oFontSubN := TFont():New(cFontUti, Nil, - 20, Nil, .T.)
    oFontBtn := TFont():New(cFontUti, Nil, - 14)
    oFontSay := TFont():New(cFontUti, Nil, - 12)
    // Grid
    aCampos := {  }
    cAliasTmp := "TST_" + RetCodUsr()
    aColunas := {  }
    oMarkBrowse := Nil
    // Componentes da segunda coluna
    oSayChkDes := Nil
    oSayChkPer := Nil
    oSayChkVlr := Nil
    oCheck01 := Nil
    lCheck01 := .F.
    oGetPerc01 := Nil
    nGetPerc01 := 0
    oGetTot01 := Nil
    nGetTot01 := 0
    oCheck02 := Nil
    lCheck02 := .F.
    oGetPerc02 := Nil
    nGetPerc02 := 0
    oGetTot02 := Nil
    nGetTot02 := 0
    oCheck03 := Nil
    lCheck03 := .F.
    oGetPerc03 := Nil
    nGetPerc03 := 0
    oGetTot03 := Nil
    nGetTot03 := 0
    oCheck04 := Nil
    lCheck04 := .F.
    oGetPerc04 := Nil
    nGetPerc04 := 0
    oGetTot04 := Nil
    nGetTot04 := 0
    oCheck05 := Nil
    lCheck05 := .F.
    oGetPerc05 := Nil
    nGetPerc05 := 0
    oGetTot05 := Nil
    nGetTot05 := 0
    // Componentes da terceira coluna
    oSayTot := Nil
    cSayTot := "Total marcado:"
    oGetTot := Nil
    nGetTot := 0
    oSayApu := Nil
    cSayApu := "% Apurado:"
    oGetApu := Nil
    nGetApu := 0
    oSayPro := Nil
    cSayPro := "Total que será processado:"
    oGetPro := Nil
    nGetPro := 0
    oBtnProc := Nil
    oBtnPrev := Nil
    // Adiciona as colunas que serão criadas na temporária
    aAdd(aCampos, { "OK", "C", 2, 0 })
    aAdd(aCampos, { "CONTA", "C", 10, 0 })
    aAdd(aCampos, { "VALOR", "N", 18, 2 })
    // Cria a tabela temporária
    oTempTable := FWTemporaryTable():New(cAliasTmp)
    oTempTable:SetFields(aCampos)
    oTempTable:Create()
    // Busca as colunas do browse
    aColunas := fCriaCols()
    // Popula a tabela temporária
    Processa(Nil, "Processando...")
    // Cria a janela
    DEFINE
    MSDIALOG
    oDlgExemp
    TITLE
    "Exemplo de Tela com Objetos gráficos usando FWLayer"
    FROM_
    0
    // ,
    0
    TO
    nJanAltu
    // ,
    nJanLarg
    PIXEL
    // Criando a camada
    oFwLayer := FwLayer():New()
    oFwLayer:init(oDlgExemp, .F.)
    // Adicionando 3 linhas, a de título, a do corpo e a inferior
    oFWLayer:addLine("TITULO", 10, .F.)
    oFWLayer:addLine("CORPO", 88, .F.)
    oFWLayer:addLine("RODAPE", 2, .F.)
    // Adicionando as colunas das linhas
    oFWLayer:addCollumn("HEADERTEXT", 50, .T., "TITULO")
    oFWLayer:addCollumn("BLANKBTN", 40, .T., "TITULO")
    oFWLayer:addCollumn("BTNSAIR", 10, .T., "TITULO")
    oFWLayer:addCollumn("BLANKANTES", 1, .T., "CORPO")
    oFWLayer:addCollumn("COLGRID", 39, .T., "CORPO")
    oFWLayer:addCollumn("COLCHECK", 40, .T., "CORPO")
    oFWLayer:addCollumn("COLTOTAL", 19, .T., "CORPO")
    oFWLayer:addCollumn("BLANKDEPOIS", 1, .T., "CORPO")
    // Criando os paineis
    oPanHeader := oFWLayer:GetColPanel("HEADERTEXT", "TITULO")
    oPanSair := oFWLayer:GetColPanel("BTNSAIR", "TITULO")
    oPanGrid := oFWLayer:GetColPanel("COLGRID", "CORPO")
    oPanCheck := oFWLayer:GetColPanel("COLCHECK", "CORPO")
    oPanTotal := oFWLayer:GetColPanel("COLTOTAL", "CORPO")
    // Títulos e SubTítulos
    oSayModulo := TSay():New(4, 3, Nil, oPanHeader, "", oFontMod, Nil, Nil, Nil, .T., RGB(149, 179, 215), Nil, 200, 30, Nil, Nil, Nil, Nil, Nil, .F., Nil)
    oSayTitulo := TSay():New(4, 45, Nil, oPanHeader, "", oFontSub, Nil, Nil, Nil, .T., RGB(31, 73, 125), Nil, 200, 30, Nil, Nil, Nil, Nil, Nil, .F., Nil)
    oSaySubTit := TSay():New(14, 45, Nil, oPanHeader, "", oFontSubN, Nil, Nil, Nil, .T., RGB(31, 73, 125), Nil, 300, 30, Nil, Nil, Nil, Nil, Nil, .F., Nil)
    // Criando os botões
    oBtnSair := TButton():New(6, 1, "Fechar", oPanSair, Nil, nLargBtn, 18, Nil, oFontBtn, Nil, .T., Nil, Nil, Nil, Nil, Nil)
    // Cria a grid
    oMarkBrowse := FWMarkBrowse():New()
    oMarkBrowse:SetAlias(cAliasTmp)
    oMarkBrowse:DisableFilter()
    oMarkBrowse:DisableConfig()
    oMarkBrowse:DisableReport()
    oMarkBrowse:DisableSeek()
    oMarkBrowse:DisableSaveConfig()
    oMarkBrowse:SetFontBrowse(oFontSay)
    oMarkBrowse:SetFieldMark("OK")
    oMarkBrowse:SetTemporary(.T.)
    oMarkBrowse:SetColumns(aColunas)
    oMarkBrowse:SetOwner(oPanGrid)
    oMarkBrowse:Activate()
    // Cria os componentes da segunda coluna
    // RAW: @ 001 , 001 SCROLLBOX oScroll VERTICAL HORIZONTAL SIZE oPanCheck : nHeight / 2 , oPanCheck : nWidth / 2 OF oPanCheck
    nLinhaObj := 1
    nLargPanel := oPanCheck:nWidth() / 2
    nTotEspCol := nLargPanel / 3
    nTotCol01 := 3 + nTotEspCol * 0
    nTotCol02 := 3 + nTotEspCol * 1
    nTotCol03 := 3 + nTotEspCol * 2
    oSayChkDes := TSay():New(nLinhaObj, 1 + nTotCol01, Nil, oScroll, "", oFontSay, Nil, Nil, Nil, .T., RGB(31, 73, 125), Nil, nTotEspCol, 10, Nil, Nil, Nil, Nil, Nil, .F., Nil)
    oSayChkPer := TSay():New(nLinhaObj, 1 + nTotCol02, Nil, oScroll, "", oFontSay, Nil, Nil, Nil, .T., RGB(31, 73, 125), Nil, nTotEspCol, 10, Nil, Nil, Nil, Nil, Nil, .F., Nil)
    oSayChkVlr := TSay():New(nLinhaObj, 1 + nTotCol03, Nil, oScroll, "", oFontSay, Nil, Nil, Nil, .T., RGB(31, 73, 125), Nil, nTotEspCol, 10, Nil, Nil, Nil, Nil, Nil, .F., Nil)
    nLinhaObj += 25
    oCheck01 := TCheckBox():New(nLinhaObj, 3 + nTotCol01, "Check 01", Nil, oScroll, nTotEspCol - 3, 10, Nil, Nil, oFontSay, Nil, Nil, Nil, Nil, .T.)
    oGetPerc01 := TGet():New(nLinhaObj, 3 + nTotCol02, Nil, oScroll, nTotEspCol - 9, 10, cMascara, Nil, Nil, Nil, oFontSay, Nil, Nil, .T.)
    oGetTot01 := TGet():New(nLinhaObj, 3 + nTotCol03, Nil, oScroll, nTotEspCol - 9, 10, cMascara, Nil, Nil, Nil, oFontSay, Nil, Nil, .T.)
    oGetTot01->lActive := .F.
    nLinhaObj += 15
    oCheck02 := TCheckBox():New(nLinhaObj, 3 + nTotCol01, "Check 02", Nil, oScroll, nTotEspCol - 3, 10, Nil, Nil, oFontSay, Nil, Nil, Nil, Nil, .T.)
    oGetPerc02 := TGet():New(nLinhaObj, 3 + nTotCol02, Nil, oScroll, nTotEspCol - 9, 10, cMascara, Nil, Nil, Nil, oFontSay, Nil, Nil, .T.)
    oGetTot02 := TGet():New(nLinhaObj, 3 + nTotCol03, Nil, oScroll, nTotEspCol - 9, 10, cMascara, Nil, Nil, Nil, oFontSay, Nil, Nil, .T.)
    oGetTot02->lActive := .F.
    nLinhaObj += 15
    oCheck03 := TCheckBox():New(nLinhaObj, 3 + nTotCol01, "Check 03", Nil, oScroll, nTotEspCol - 3, 10, Nil, Nil, oFontSay, Nil, Nil, Nil, Nil, .T.)
    oGetPerc03 := TGet():New(nLinhaObj, 3 + nTotCol02, Nil, oScroll, nTotEspCol - 9, 10, cMascara, Nil, Nil, Nil, oFontSay, Nil, Nil, .T.)
    oGetTot03 := TGet():New(nLinhaObj, 3 + nTotCol03, Nil, oScroll, nTotEspCol - 9, 10, cMascara, Nil, Nil, Nil, oFontSay, Nil, Nil, .T.)
    oGetTot03->lActive := .F.
    nLinhaObj += 15
    oCheck04 := TCheckBox():New(nLinhaObj, 3 + nTotCol01, "Check 04", Nil, oScroll, nTotEspCol - 3, 10, Nil, Nil, oFontSay, Nil, Nil, Nil, Nil, .T.)
    oGetPerc04 := TGet():New(nLinhaObj, 3 + nTotCol02, Nil, oScroll, nTotEspCol - 9, 10, cMascara, Nil, Nil, Nil, oFontSay, Nil, Nil, .T.)
    oGetTot04 := TGet():New(nLinhaObj, 3 + nTotCol03, Nil, oScroll, nTotEspCol - 9, 10, cMascara, Nil, Nil, Nil, oFontSay, Nil, Nil, .T.)
    oGetTot04->lActive := .F.
    nLinhaObj += 15
    oCheck05 := TCheckBox():New(nLinhaObj, 3 + nTotCol01, "Check 05", Nil, oScroll, nTotEspCol - 3, 10, Nil, Nil, oFontSay, Nil, Nil, Nil, Nil, .T.)
    oGetPerc05 := TGet():New(nLinhaObj, 3 + nTotCol02, Nil, oScroll, nTotEspCol - 9, 10, cMascara, Nil, Nil, Nil, oFontSay, Nil, Nil, .T.)
    oGetTot05 := TGet():New(nLinhaObj, 3 + nTotCol03, Nil, oScroll, nTotEspCol - 9, 10, cMascara, Nil, Nil, Nil, oFontSay, Nil, Nil, .T.)
    oGetTot05->lActive := .F.
    // Cria os componentes da terceira coluna
    nLargPanel := oPanTotal:nWidth() / 2
    nLinhaObj := 30
    oSayTot := TSay():New(nLinhaObj, 3, Nil, oPanTotal, "", oFontSay, Nil, Nil, Nil, .T., RGB(31, 73, 125), Nil, 200, 10, Nil, Nil, Nil, Nil, Nil, .F., Nil)
    nLinhaObj += 10
    oGetTot := TGet():New(nLinhaObj, 13, Nil, oPanTotal, nLargPanel - 25, 15, cMascara, Nil, Nil, Nil, oFontSay, Nil, Nil, .T.)
    oGetTot->lReadOnly := .T.
    nLinhaObj += 25
    oSayApu := TSay():New(nLinhaObj, 3, Nil, oPanTotal, "", oFontSay, Nil, Nil, Nil, .T., RGB(31, 73, 125), Nil, 200, 10, Nil, Nil, Nil, Nil, Nil, .F., Nil)
    nLinhaObj += 10
    oGetApu := TGet():New(nLinhaObj, 13, Nil, oPanTotal, nLargPanel - 25, 15, cMascara, Nil, Nil, Nil, oFontSay, Nil, Nil, .T.)
    oGetApu->lReadOnly := .T.
    nLinhaObj += 25
    oSayPro := TSay():New(nLinhaObj, 3, Nil, oPanTotal, "", oFontSay, Nil, Nil, Nil, .T., RGB(31, 73, 125), Nil, 200, 10, Nil, Nil, Nil, Nil, Nil, .F., Nil)
    nLinhaObj += 10
    oGetPro := TGet():New(nLinhaObj, 13, Nil, oPanTotal, nLargPanel - 25, 15, cMascara, Nil, Nil, Nil, oFontSay, Nil, Nil, .T.)
    oGetApu->lReadOnly := .T.
    nLinhaObj += 25
    nLinhaObj += 20
    oBtnProc := TButton():New(nLinhaObj, 3, "Processar informações", oPanTotal, Nil, nLargPanel - 3, 18, Nil, oFontBtn, Nil, .T., Nil, Nil, Nil, Nil, Nil)
    nLinhaObj += 25
    oBtnPrev := TButton():New(nLinhaObj, 3, "Previsão dos dados", oPanTotal, Nil, nLargPanel - 3, 18, Nil, oFontBtn, Nil, .T., Nil, Nil, Nil, Nil, Nil)
    Activate
    MsDialog
    oDlgExemp
    Centered
    oTempTable:Delete()
    RETURN Static

FUNCTION fCriaCols()
    LOCAL nAtual, aColunas, aEstrut, oColumn

    nAtual := 0
    aColunas := {  }
    aEstrut := {  }
    oColumn := Nil
    // Adicionando campos que serão mostrados na tela
    // [1] - Campo da Temporaria
    // [2] - Titulo
    // [3] - Tipo
    // [4] - Tamanho
    // [5] - Decimais
    // [6] - Máscara
    aAdd(aEstrut, { "CONTA", "Conta", "C", 10, 0, "" })
    aAdd(aEstrut, { "VALOR", "Valor", "N", 18, 2, cMascara })
    // Percorrendo todos os campos da estrutura
    RETURN aColunas

STATIC FUNCTION fPopula()
    LOCAL nAtual

    nAtual := 0
    RETURN Static

FUNCTION fExemplo2()
    LOCAL nLargBtn, nLinhaObj, nLargPanel, oDlgExemp, oSize, oPanTitulo, oPanGrid, oPanCheck, oPanTotal, cMascara, oSayModulo, cSayModulo, oSayTitulo, cSayTitulo, oSaySubTit, cSaySubTit, aSize, nJanLarg, nJanAltu, cFontUti, oFontMod, oFontSub, oFontSubN, oFontBtn, oFontSay, aCampos, cAliasTmp, aColunas, oMarkBrowse, oSayChkDes, oSayChkPer, oSayChkVlr, oCheck01, lCheck01, oGetPerc01, nGetPerc01, oGetTot01, nGetTot01, oCheck02, lCheck02, oGetPerc02, nGetPerc02, oGetTot02, nGetTot02, oCheck03, lCheck03, oGetPerc03, nGetPerc03, oGetTot03, nGetTot03, oCheck04, lCheck04, oGetPerc04, nGetPerc04, oGetTot04, nGetTot04, oCheck05, lCheck05, oGetPerc05, nGetPerc05, oGetTot05, nGetTot05, oSayTot, cSayTot, oGetTot, nGetTot, oSayApu, cSayApu, oGetApu, nGetApu, oSayPro, cSayPro, oGetPro, nGetPro, oBtnProc, oBtnPrev, oTempTable, aTitulo, aCorpo, aRodape, oPanHeader, oPanSair, oBtnSair, nTotEspCol, nTotCol01, nTotCol02, nTotCol03

    nLargBtn := 50
    nLinhaObj := 0
    nLargPanel := 0
    // Objetos e componentes gerais
    oDlgExemp := Nil
    oSize := Nil
    oPanTitulo := Nil
    oPanGrid := Nil
    oPanCheck := Nil
    oPanTotal := Nil
    cMascara := "@E 999,999,999,999,999.99"
    // Cabeçalho
    oSayModulo := Nil
    cSayModulo := "TST"
    oSayTitulo := Nil
    cSayTitulo := "'Exemplo de Tela com"
    oSaySubTit := Nil
    cSaySubTit := "Objetos gráficos usando FWDefSize"
    // Tamanho da janela
    aSize := MsAdvSize(.F.)
    nJanLarg := aSize[5]
    nJanAltu := aSize[6]
    // Fontes
    cFontUti := "Tahoma"
    oFontMod := TFont():New(cFontUti, Nil, - 38)
    oFontSub := TFont():New(cFontUti, Nil, - 20)
    oFontSubN := TFont():New(cFontUti, Nil, - 20, Nil, .T.)
    oFontBtn := TFont():New(cFontUti, Nil, - 14)
    oFontSay := TFont():New(cFontUti, Nil, - 12)
    // Grid
    aCampos := {  }
    cAliasTmp := "TST_" + RetCodUsr()
    aColunas := {  }
    oMarkBrowse := Nil
    // Componentes da segunda coluna
    oSayChkDes := Nil
    oSayChkPer := Nil
    oSayChkVlr := Nil
    oCheck01 := Nil
    lCheck01 := .F.
    oGetPerc01 := Nil
    nGetPerc01 := 0
    oGetTot01 := Nil
    nGetTot01 := 0
    oCheck02 := Nil
    lCheck02 := .F.
    oGetPerc02 := Nil
    nGetPerc02 := 0
    oGetTot02 := Nil
    nGetTot02 := 0
    oCheck03 := Nil
    lCheck03 := .F.
    oGetPerc03 := Nil
    nGetPerc03 := 0
    oGetTot03 := Nil
    nGetTot03 := 0
    oCheck04 := Nil
    lCheck04 := .F.
    oGetPerc04 := Nil
    nGetPerc04 := 0
    oGetTot04 := Nil
    nGetTot04 := 0
    oCheck05 := Nil
    lCheck05 := .F.
    oGetPerc05 := Nil
    nGetPerc05 := 0
    oGetTot05 := Nil
    nGetTot05 := 0
    // Componentes da terceira coluna
    oSayTot := Nil
    cSayTot := "Total marcado:"
    oGetTot := Nil
    nGetTot := 0
    oSayApu := Nil
    cSayApu := "% Apurado:"
    oGetApu := Nil
    nGetApu := 0
    oSayPro := Nil
    cSayPro := "Total que será processado:"
    oGetPro := Nil
    nGetPro := 0
    oBtnProc := Nil
    oBtnPrev := Nil
    // Adiciona as colunas que serão criadas na temporária
    aAdd(aCampos, { "OK", "C", 2, 0 })
    aAdd(aCampos, { "CONTA", "C", 10, 0 })
    aAdd(aCampos, { "VALOR", "N", 18, 2 })
    // Cria a tabela temporária
    oTempTable := FWTemporaryTable():New(cAliasTmp)
    oTempTable:SetFields(aCampos)
    oTempTable:Create()
    // Busca as colunas do browse
    aColunas := fCriaCols()
    // Popula a tabela temporária
    Processa(Nil, "Processando...")
    // Cria a janela
    DEFINE
    MSDIALOG
    oDlgExemp
    TITLE
    "Exemplo de Tela com Objetos gráficos usando FWDefSize"
    FROM_
    0
    // ,
    0
    TO
    nJanAltu
    // ,
    nJanLarg
    PIXEL
    // Criando a camada
    oSize := FwDefSize():New(.F., Nil, Nil, oDlgExemp)
    // Sem EnchoiceBar
    // Adicionando 3 linhas, a de título, a do corpo e a inferior
    oSize:AddObject("TITULO", 100, 10, .T., .T.)
    oSize:AddObject("CORPO", 100, 88, .T., .T.)
    oSize:AddObject("RODAPE", 100, 2, .T., .T.)
    // Define a margem entre os objetos
    oSize->aMargins := { 3, 3, 3, 3 }
    // Efetua os cálculos do dimensionamento
    oSize:Process()
    // Pegando o dimensionamento das linhas
    aTitulo := { oSize:GetDimension("TITULO", "LININI"), oSize:GetDimension("TITULO", "COLINI"), oSize:GetDimension("TITULO", "XSIZE"), oSize:GetDimension("TITULO", "YSIZE") }
    aCorpo := { oSize:GetDimension("CORPO", "LININI"), oSize:GetDimension("CORPO", "COLINI"), oSize:GetDimension("CORPO", "XSIZE"), oSize:GetDimension("CORPO", "YSIZE") }
    aRodape := { oSize:GetDimension("RODAPE", "LININI"), oSize:GetDimension("RODAPE", "COLINI"), oSize:GetDimension("RODAPE", "LINEND"), oSize:GetDimension("RODAPE", "COLEND") }
    // Ajuste no dimensionamento (linha inicial e linha final)
    aCorpo[1] := aCorpo[1] - 50
    aCorpo[4] := aCorpo[4] + 140
    // Criando os paineis
    oPanHeader := tPanel():New(aTitulo[1], aTitulo[2], "", oDlgExemp, Nil, Nil, Nil, RGB(0, 0, 0), RGB(254, 254, 254), aTitulo[3] - 200, aTitulo[4])
    oPanSair := tPanel():New(aTitulo[1], aTitulo[3] - 200, "", oDlgExemp, Nil, Nil, Nil, RGB(0, 0, 0), RGB(254, 254, 254), aTitulo[3], aTitulo[4])
    oPanGrid := tPanel():New(aCorpo[1], aCorpo[2] + aCorpo[3] / 3 * 0, "", oDlgExemp, Nil, Nil, Nil, RGB(0, 0, 0), RGB(254, 254, 254), aCorpo[3] / 3, aCorpo[4])
    oPanCheck := tPanel():New(aCorpo[1], aCorpo[2] + aCorpo[3] / 3 * 1, "", oDlgExemp, Nil, Nil, Nil, RGB(0, 0, 0), RGB(254, 254, 254), aCorpo[3] / 3, aCorpo[4])
    oPanTotal := tPanel():New(aCorpo[1], aCorpo[2] + aCorpo[3] / 3 * 2, "", oDlgExemp, Nil, Nil, Nil, RGB(0, 0, 0), RGB(254, 254, 254), aCorpo[3] / 3, aCorpo[4])
    // Títulos e SubTítulos
    oSayModulo := TSay():New(4, 3, Nil, oPanHeader, "", oFontMod, Nil, Nil, Nil, .T., RGB(149, 179, 215), Nil, 200, 30, Nil, Nil, Nil, Nil, Nil, .F., Nil)
    oSayTitulo := TSay():New(4, 45, Nil, oPanHeader, "", oFontSub, Nil, Nil, Nil, .T., RGB(31, 73, 125), Nil, 200, 30, Nil, Nil, Nil, Nil, Nil, .F., Nil)
    oSaySubTit := TSay():New(14, 45, Nil, oPanHeader, "", oFontSubN, Nil, Nil, Nil, .T., RGB(31, 73, 125), Nil, 300, 30, Nil, Nil, Nil, Nil, Nil, .F., Nil)
    // Criando os botões
    oBtnSair := TButton():New(6, 1, "Fechar", oPanSair, Nil, nLargBtn, 18, Nil, oFontBtn, Nil, .T., Nil, Nil, Nil, Nil, Nil)
    // Cria a grid
    oMarkBrowse := FWMarkBrowse():New()
    oMarkBrowse:SetAlias(cAliasTmp)
    oMarkBrowse:DisableFilter()
    oMarkBrowse:DisableConfig()
    oMarkBrowse:DisableReport()
    oMarkBrowse:DisableSeek()
    oMarkBrowse:DisableSaveConfig()
    oMarkBrowse:SetFontBrowse(oFontSay)
    oMarkBrowse:SetFieldMark("OK")
    oMarkBrowse:SetTemporary(.T.)
    oMarkBrowse:SetColumns(aColunas)
    oMarkBrowse:SetOwner(oPanGrid)
    oMarkBrowse:Activate()
    // Cria os componentes da segunda coluna
    // RAW: @ 001 , 001 SCROLLBOX oScroll VERTICAL HORIZONTAL SIZE oPanCheck : nHeight / 2 , oPanCheck : nWidth / 2 OF oPanCheck
    nLinhaObj := 1
    nLargPanel := oPanCheck:nWidth() / 2
    nTotEspCol := nLargPanel / 3
    nTotCol01 := 3 + nTotEspCol * 0
    nTotCol02 := 3 + nTotEspCol * 1
    nTotCol03 := 3 + nTotEspCol * 2
    oSayChkDes := TSay():New(nLinhaObj, 1 + nTotCol01, Nil, oScroll, "", oFontSay, Nil, Nil, Nil, .T., RGB(31, 73, 125), Nil, nTotEspCol, 10, Nil, Nil, Nil, Nil, Nil, .F., Nil)
    oSayChkPer := TSay():New(nLinhaObj, 1 + nTotCol02, Nil, oScroll, "", oFontSay, Nil, Nil, Nil, .T., RGB(31, 73, 125), Nil, nTotEspCol, 10, Nil, Nil, Nil, Nil, Nil, .F., Nil)
    oSayChkVlr := TSay():New(nLinhaObj, 1 + nTotCol03, Nil, oScroll, "", oFontSay, Nil, Nil, Nil, .T., RGB(31, 73, 125), Nil, nTotEspCol, 10, Nil, Nil, Nil, Nil, Nil, .F., Nil)
    nLinhaObj += 25
    oCheck01 := TCheckBox():New(nLinhaObj, 3 + nTotCol01, "Check 01", Nil, oScroll, nTotEspCol - 3, 10, Nil, Nil, oFontSay, Nil, Nil, Nil, Nil, .T.)
    oGetPerc01 := TGet():New(nLinhaObj, 3 + nTotCol02, Nil, oScroll, nTotEspCol - 9, 10, cMascara, Nil, Nil, Nil, oFontSay, Nil, Nil, .T.)
    oGetTot01 := TGet():New(nLinhaObj, 3 + nTotCol03, Nil, oScroll, nTotEspCol - 9, 10, cMascara, Nil, Nil, Nil, oFontSay, Nil, Nil, .T.)
    oGetTot01->lActive := .F.
    nLinhaObj += 15
    oCheck02 := TCheckBox():New(nLinhaObj, 3 + nTotCol01, "Check 02", Nil, oScroll, nTotEspCol - 3, 10, Nil, Nil, oFontSay, Nil, Nil, Nil, Nil, .T.)
    oGetPerc02 := TGet():New(nLinhaObj, 3 + nTotCol02, Nil, oScroll, nTotEspCol - 9, 10, cMascara, Nil, Nil, Nil, oFontSay, Nil, Nil, .T.)
    oGetTot02 := TGet():New(nLinhaObj, 3 + nTotCol03, Nil, oScroll, nTotEspCol - 9, 10, cMascara, Nil, Nil, Nil, oFontSay, Nil, Nil, .T.)
    oGetTot02->lActive := .F.
    nLinhaObj += 15
    oCheck03 := TCheckBox():New(nLinhaObj, 3 + nTotCol01, "Check 03", Nil, oScroll, nTotEspCol - 3, 10, Nil, Nil, oFontSay, Nil, Nil, Nil, Nil, .T.)
    oGetPerc03 := TGet():New(nLinhaObj, 3 + nTotCol02, Nil, oScroll, nTotEspCol - 9, 10, cMascara, Nil, Nil, Nil, oFontSay, Nil, Nil, .T.)
    oGetTot03 := TGet():New(nLinhaObj, 3 + nTotCol03, Nil, oScroll, nTotEspCol - 9, 10, cMascara, Nil, Nil, Nil, oFontSay, Nil, Nil, .T.)
    oGetTot03->lActive := .F.
    nLinhaObj += 15
    oCheck04 := TCheckBox():New(nLinhaObj, 3 + nTotCol01, "Check 04", Nil, oScroll, nTotEspCol - 3, 10, Nil, Nil, oFontSay, Nil, Nil, Nil, Nil, .T.)
    oGetPerc04 := TGet():New(nLinhaObj, 3 + nTotCol02, Nil, oScroll, nTotEspCol - 9, 10, cMascara, Nil, Nil, Nil, oFontSay, Nil, Nil, .T.)
    oGetTot04 := TGet():New(nLinhaObj, 3 + nTotCol03, Nil, oScroll, nTotEspCol - 9, 10, cMascara, Nil, Nil, Nil, oFontSay, Nil, Nil, .T.)
    oGetTot04->lActive := .F.
    nLinhaObj += 15
    oCheck05 := TCheckBox():New(nLinhaObj, 3 + nTotCol01, "Check 05", Nil, oScroll, nTotEspCol - 3, 10, Nil, Nil, oFontSay, Nil, Nil, Nil, Nil, .T.)
    oGetPerc05 := TGet():New(nLinhaObj, 3 + nTotCol02, Nil, oScroll, nTotEspCol - 9, 10, cMascara, Nil, Nil, Nil, oFontSay, Nil, Nil, .T.)
    oGetTot05 := TGet():New(nLinhaObj, 3 + nTotCol03, Nil, oScroll, nTotEspCol - 9, 10, cMascara, Nil, Nil, Nil, oFontSay, Nil, Nil, .T.)
    oGetTot05->lActive := .F.
    // Cria os componentes da terceira coluna
    nLargPanel := oPanTotal:nWidth() / 2
    nLinhaObj := 30
    oSayTot := TSay():New(nLinhaObj, 3, Nil, oPanTotal, "", oFontSay, Nil, Nil, Nil, .T., RGB(31, 73, 125), Nil, 200, 10, Nil, Nil, Nil, Nil, Nil, .F., Nil)
    nLinhaObj += 10
    oGetTot := TGet():New(nLinhaObj, 13, Nil, oPanTotal, nLargPanel - 25, 15, cMascara, Nil, Nil, Nil, oFontSay, Nil, Nil, .T.)
    oGetTot->lReadOnly := .T.
    nLinhaObj += 25
    oSayApu := TSay():New(nLinhaObj, 3, Nil, oPanTotal, "", oFontSay, Nil, Nil, Nil, .T., RGB(31, 73, 125), Nil, 200, 10, Nil, Nil, Nil, Nil, Nil, .F., Nil)
    nLinhaObj += 10
    oGetApu := TGet():New(nLinhaObj, 13, Nil, oPanTotal, nLargPanel - 25, 15, cMascara, Nil, Nil, Nil, oFontSay, Nil, Nil, .T.)
    oGetApu->lReadOnly := .T.
    nLinhaObj += 25
    oSayPro := TSay():New(nLinhaObj, 3, Nil, oPanTotal, "", oFontSay, Nil, Nil, Nil, .T., RGB(31, 73, 125), Nil, 200, 10, Nil, Nil, Nil, Nil, Nil, .F., Nil)
    nLinhaObj += 10
    oGetPro := TGet():New(nLinhaObj, 13, Nil, oPanTotal, nLargPanel - 25, 15, cMascara, Nil, Nil, Nil, oFontSay, Nil, Nil, .T.)
    oGetApu->lReadOnly := .T.
    nLinhaObj += 25
    nLinhaObj += 20
    oBtnProc := TButton():New(nLinhaObj, 3, "Processar informações", oPanTotal, Nil, nLargPanel - 3, 18, Nil, oFontBtn, Nil, .T., Nil, Nil, Nil, Nil, Nil)
    nLinhaObj += 25
    oBtnPrev := TButton():New(nLinhaObj, 3, "Previsão dos dados", oPanTotal, Nil, nLargPanel - 3, 18, Nil, oFontBtn, Nil, .T., Nil, Nil, Nil, Nil, Nil)
    Activate
    MsDialog
    oDlgExemp
    Centered
    oTempTable:Delete()
    RETURN
