// caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2024/02/01/criando-um-calendario-em-tela-atraves-da-fwcalendar-maratona-advpl-e-tl-209/
// Bibliotecas
#Include "TOTVS.ch"
// Posições do array dos agendamentos do calendário
#Define ID         1 // Id do Celula
#Define OBJETO     2 // Objeto de Tela
#Define DATADIA    3 // Data Completa da Celula
#Define DIA        4 // Dia Ref. Data da Celula
#Define MES        5 // Mes Ref. Data da Celula
#Define ANO        6 // Ano Ref. Data da Celula
#Define NSEMANO    7 // Semana do Ano Ref. Data da Celula
#Define NSEMMES    8 // Semana do Mes Ref. Data da Celula
#Define ATIVO      9 // É celula referente a um dia ativo
#Define FOOTER    10 // É celula referente ao rodape
#Define HEADER    11 // É celula referente ao Header
#Define SEMANA    12 // É celula referente a semana
#Define BGDefault 13 // Cor de BackGround da Celula
// {Protheus.doc} User Function zExe209
// Tela de agendamentos do Telemarketing
// @type  Function
// @author Atilio
// @since 20/02/2023
// @version 1.0
// @see https://tdn.totvs.com/display/public/framework/FWCalendar
// **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
USER FUNCTION zExe209()
    LOCAL aArea, aSize

    aArea := GetArea()
    aSize := MsAdvSize(.F.)
    fMontaTela()
    RestArea(aArea)
    RETURN Static

FUNCTION fMontaTela()
    LOCAL nCorFundo, nLargBtn, dDtIni, cMes, cAno, oDlgTmk, oFwLayer, oPanTitulo, oPanCalend, oPanPreMon, oPanNexMon, oPanSair, oMesAtual, cMesAno, cTitHtml, oSayModulo, cSayModulo, oSayTitulo, cSayTitulo, oSaySubTit, cSaySubTit, nJanLarg, nJanAltu, cFontUti, oFontMod, oFontSub, oFontSubN, oFontBtn, oFontSay, aInfoDia, nSelecao, cTextoSel, nPosCell, oPanHeader, oBtnEnd, oCalend

    nCorFundo := 16777215
    nLargBtn := 50
    // Data
    dDtIni := Date()
    cMes := StrZero(Month(dDtIni), 2)
    cAno := StrZero(Year(dDtIni), 4)
    // Objetos e componentes
    oDlgTmk := Nil
    oFwLayer := Nil
    oPanTitulo := Nil
    oPanCalend := Nil
    oPanPreMon := Nil
    oPanNexMon := Nil
    oPanSair := Nil
    oMesAtual := Nil
    cMesAno := Nil
    cTitHtml := Nil
    // Cabeçalho
    oSayModulo := Nil
    cSayModulo := "FAT"
    oSayTitulo := Nil
    cSayTitulo := "Calendário de Agendamentos"
    oSaySubTit := Nil
    cSaySubTit := "Clique com o botão direito para registrar agendamentos"
    // Tamanho da janela
    nJanLarg := aSize[5]
    nJanAltu := aSize[6]
    // Fontes
    cFontUti := "Tahoma"
    oFontMod := TFont():New(cFontUti, Nil, - 38)
    oFontSub := TFont():New(cFontUti, Nil, - 20)
    oFontSubN := TFont():New(cFontUti, Nil, - 20, Nil, .T.)
    oFontBtn := TFont():New(cFontUti, Nil, - 14)
    oFontSay := TFont():New(cFontUti, Nil, - 12)
    // Variáveis usadas para atualização das informações
    aInfoDia := Nil
    nSelecao := Nil
    cTextoSel := Nil
    nPosCell := Nil
    // Cria a janela
    DEFINE
    MSDIALOG
    oDlgTmk
    TITLE
    "Agendamentos Telemarketing"
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
    oFwLayer:init(oDlgTmk, .F.)
    // Adicionando 3 linhas, a de título, a superior e a do calendário
    oFWLayer:addLine("TIT", 10, .F.)
    oFWLayer:addLine("SUP", 5, .F.)
    oFWLayer:addLine("CAL", 85, .F.)
    // Adicionando as colunas das linhas
    oFWLayer:addCollumn("HEADERTEXT", 50, .T., "TIT")
    oFWLayer:addCollumn("BLANKBTN", 40, .T., "TIT")
    oFWLayer:addCollumn("BTNSAIR", 10, .T., "TIT")
    oFWLayer:addCollumn("BLANKSUP1", 15, .T., "SUP")
    oFWLayer:addCollumn("BTNPREVMONTH", 20, .T., "SUP")
    oFWLayer:addCollumn("TITLE", 30, .T., "SUP")
    oFWLayer:addCollumn("BTNNEXTMONTH", 20, .T., "SUP")
    oFWLayer:addCollumn("COLCAL", 100, .T., "CAL")
    // Criando os paineis
    oPanTitulo := oFWLayer:GetColPanel("TITLE", "SUP")
    oPanCalend := oFWLayer:GetColPanel("COLCAL", "CAL")
    oPanPreMon := oFWLayer:GetColPanel("BTNPREVMONTH", "SUP")
    oPanNexMon := oFWLayer:GetColPanel("BTNNEXTMONTH", "SUP")
    oPanSair := oFWLayer:GetColPanel("BTNSAIR", "TIT")
    oPanHeader := oFWLayer:GetColPanel("HEADERTEXT", "TIT")
    // Títulos e SubTítulos
    oSayModulo := TSay():New(4, 3, Nil, oPanHeader, "", oFontMod, Nil, Nil, Nil, .T., RGB(149, 179, 215), Nil, 200, 30, Nil, Nil, Nil, Nil, Nil, .F., Nil)
    oSayTitulo := TSay():New(4, 45, Nil, oPanHeader, "", oFontSub, Nil, Nil, Nil, .T., RGB(31, 73, 125), Nil, 200, 30, Nil, Nil, Nil, Nil, Nil, .F., Nil)
    oSaySubTit := TSay():New(14, 45, Nil, oPanHeader, "", oFontSubN, Nil, Nil, Nil, .T., RGB(31, 73, 125), Nil, 300, 30, Nil, Nil, Nil, Nil, Nil, .F., Nil)
    // Criando os botões
    oBtnEnd := TButton():New(6, 1, "Fechar", oPanSair, Nil, nLargBtn, 18, Nil, oFontBtn, Nil, .T., Nil, Nil, Nil, Nil, Nil)
    // Cria o calendário
    oCalend := FWCalendar():New(VAL(cMes), VAL(cAno))
    oCalend->aNomeCol := { "Domingo", "Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Semana" }
    // 'Domingo'    # 'Segunda' # 'Terça' # 'Quarta' # 'Quinta'    # 'Sexta' # 'Sábado' # 'Semana'
    oCalend->lWeekColumn := .F.
    oCalend->lFooterLine := .F.
    oCalend->bLClicked := Nil
    oCalend->bLDblClick := Nil
    oCalend->bRClicked := Nil
    fCalendFont()
    oCalend:Activate(oPanCalend)
    // Criando o Say com o mês Atual
    oMesAtual := TSay():New(0, 0, Nil, oPanTitulo, Nil, Nil, Nil, Nil, Nil, .T., 20, 20, Nil, Nil, Nil, Nil, Nil, Nil, Nil, .T.)
    oMesAtual->Align := CONTROL_ALIGN_ALLCLIENT
    oMesAtual->nClrPane := nCorFundo
    fMesAno(Val(cMes), Val(cAno))
    // Criando o botão do Mês Anterior
    // RAW: @ 0 , 0 BTNBMP oPrevMonth Resource "PMSSETAESQ" Size 80 , 90 Of oPanPreMon Pixel
    oPrevMontht->cToolTip := "Mes Anterior"
    // "Mes Anterior"
    oPrevMonth->bAction := Nil
    // "Montando calendário..."
    oPrevMonth->Align := CONTROL_ALIGN_RIGHT
    // Criando o botão do Próximo Mês
    // RAW: @ 0 , 0 BTNBMP oNextMonth Resource "PMSSETADIR" Size 90 , 90 Of oPanNexMon Pixel
    oNextMonth->cToolTip := "Proximo Mes"
    // "Proximo Mes"
    oNextMonth->bAction := Nil
    // "Montando calendário..."
    oNextMonth->Align := CONTROL_ALIGN_LEFT
    Activate
    MsDialog
    oDlgTmk
    Centered
    RETURN Static

FUNCTION fMudaMes(oPan, oCalend, nOp)
    LOCAL nMonth, nYear, nOp

    nMonth := oCalend:nMes()
    nYear := oCalend:nAno()
    Default
    nOp := 1
    // Se for a seta ->, incrementa um mês
    If nOp = 1
        If nMonth = 12
            nMonth := 1
            nYear += 1
        Else
            nMonth := Nil
        EndIf
        // Se for a seta <-, diminui um mês
    ElseIf nOp = 2
        If nMonth = 1
            nMonth := 12
            nYear -= 1
        Else
            nMonth := Nil
        EndIf
    EndIf
    // Define o calendário e seta o título
    oCalend:SetCalendar(oPan, cValToChar(nMonth), cValToChar(nYear))
    fMesAno(nMonth, nYear)
    RETURN Static

FUNCTION fMesAno(nMonth, nYear)
    LOCAL cMesAno, cTitHtml

    cMesAno := Capital(MesExtenso(nMonth)) + " / " + cValToChar(nYear)
    cTitHtml := fTitHTML(cMesAno)
    oMesAtual:SetText(cTitHtml)
    // Chama a busca de informações para definir as informações no calendário
    fBuscaInfo()
    RETURN
    // Função que transforma o título no formato html

STATIC FUNCTION fTitHTML(cMesAno)
    LOCAL cRet

    cRet := ""
    cRet += "<p align="center">"
    cRet += "<font face="" + cFontUti + "" color="#000000" style="font-size:14px"><strong>" + cMesAno + "</strong></font>"
    cRet += "</p>"
    RETURN cRet
    // Função que define o primeiro calendário com a fonte Tahom

STATIC FUNCTION fCalendFont()
    oCalend:aFontDay()[1] := cFontUti
    oCalend:aFontDayHead()[1] := cFontUti
    oCalend:aFontDayText()[1] := cFontUti
    oCalend:aFontFooter()[1] := cFontUti
    oCalend:aFontFsFer()[1] := cFontUti
    oCalend:aFontHeader()[1] := cFontUti
    oCalend:aFontOff()[1] := cFontUti
    oCalend:aFontToday()[1] := cFontUti
    oCalend:aFontWeek()[1] := cFontUti
    oCalend->cHtmlDay := StrTran(oCalend:cHtmlDay(), "MS Sans Serif", cFontUti)
    oCalend->cHtmlDayOff := StrTran(oCalend:cHtmlDayOff(), "MS Sans Serif", cFontUti)
    oCalend->cHtmlFooter := StrTran(oCalend:cHtmlFooter(), "MS Sans Serif", cFontUti)
    oCalend->cHtmlHeader := StrTran(oCalend:cHtmlHeader(), "MS Sans Serif", cFontUti)
    oCalend->cHtmlToday := StrTran(oCalend:cHtmlToday(), "MS Sans Serif", cFontUti)
    oCalend->cHtmlWeek := StrTran(oCalend:cHtmlWeek(), "MS Sans Serif", cFontUti)
    oCalend->cHtmlWeekend := StrTran(oCalend:cHtmlWeekend(), "MS Sans Serif", cFontUti)
    RETURN Static

FUNCTION fBuscaInfo()
    LOCAL nCell, nDia

    nCell := Nil
    nDia := Nil
    RETURN Static

FUNCTION fCliqueDir(aInfo, oObj, nRow, nCol)
    LOCAL cClassName, oMenu, oMenuItem, aOpcoes, nOpcao, dData, aInfoDia, nSelecao, cTextoSel, nPosCell

    cClassName := Upper(Alltrim(oObj:ClassName()))
    oMenu := Nil
    oMenuItem := {  }
    aOpcoes := {  }
    nOpcao := 0
    dData := aInfo[DATADIA]
    aInfoDia := aInfo
    nSelecao := aInfo[OBJETO]:nSelectedIndex()
    cTextoSel := ""
    nPosCell := aScan(oCalend:aCell(), Nil)
    // Somente se estiver dentro do ListBox
    If cClassName = "TLISTBOX"
        aAdd(aOpcoes, { "Novo Agendamento", Nil })
        // Se houver linhas, terá outras opções
        If nSelecao <> 0
            aAdd(aOpcoes, { "Visualizar Agendamento", Nil })
            aAdd(aOpcoes, { "Alterar Agendamento", Nil })
            aAdd(aOpcoes, { "Excluir Agendamento", Nil })
            cTextoSel := aInfo[OBJETO]:oListBoxContent():aItems()[nSelecao]
        EndIf
    EndIf
    // Criando o menu e os itens
    MENU
    oMenu
    POPUP
    ENDMENU
    oMenu:Activate(nRow, nCol, oObj)
    RETURN Static

FUNCTION fPopOpcao(nOpcao, dData)
    LOCAL aPergs, cTexto, cEditCli, cCliente, cLoja, cObserv, nOpcao, dData, cNomeCli, aItens

    aPergs := {  }
    cTexto := ""
    cEditCli := ".F."
    cCliente := Space(TamSX3("A1_COD")[1])
    cLoja := Space(TamSX3("A1_LOJA")[1])
    cObserv := ""
    Default
    nOpcao := 3
    Default
    dData := Date()
    // Define o texto
    If nOpcao = 3
        cEditCli := ".T."
        cTexto := "Inclusão de Agendamento"
    Else
        cEditCli := ".F."
        If nOpcao = 2
            cTexto := "Visualização de Agendamento"
        ElseIf nOpcao = 4
            cTexto := "Alteração de Agendamento"
        ElseIf nOpcao = 5
            cTexto := "Exclusão de Agendamento"
        EndIf
        cCliente := SubStr(cTextoSel, 1, 6)
        cLoja := "01"
        cTexto += " (" + SubStr(cTextoSel, 10, Len(cTextoSel)) + ")"
    EndIf
    // Adiciona os parâmetros
    aAdd(aPergs, { 9, cTexto, 200, 40, .T. })
    aAdd(aPergs, { 1, "Data", dData, "", ".T.", "", ".F.", 80, .T. })
    aAdd(aPergs, { 1, "Cliente", cCliente, "", ".T.", "SA1", cEditCli, 80, .T. })
    aAdd(aPergs, { 1, "Loja", cLoja, "", ".T.", "", cEditCli, 80, .T. })
    aAdd(aPergs, { 11, "Histórico", cObserv, ".T.", ".T.", .T. })
    // Se a pergunta for confirmada
    If ParamBox(aPergs, "Informe os parâmetros", Nil, Nil, Nil, Nil, Nil, Nil, Nil, Nil, .F., .F.)
        cCliente := MV_PAR03
        cLoja := MV_PAR04
        cObserv := MV_PAR05
        cNomeCli := Posicione("SA1", 1, FWxFilial("SA1") + cCliente + cLoja, "A1_NOME")
        // Se for inclusão, adiciona no calendário
        If nOpcao = 3
            aItens := aClone(aInfoDia[OBJETO]:oListBoxContent():aItems())
            aAdd(aItens, cCliente + " - " + SubStr(cNomeCli, 1, 15))
            oCalend:SetInfo(oCalend:aCell()[nPosCell][ID], aClone(aItens))
            // Se for exclusãoRetira o elemento do array e depois define no calendário
        ElseIf nOpcao = 5
            aItens := aClone(aInfoDia[OBJETO]:oListBoxContent():aItems())
            aDel(aItens, nSelecao)
            aSize(aItens, Len(aItens) - 1)
            oCalend:SetInfo(oCalend:aCell()[nPosCell][ID], aClone(aItens))
        EndIf
    EndIf
    RETURN
