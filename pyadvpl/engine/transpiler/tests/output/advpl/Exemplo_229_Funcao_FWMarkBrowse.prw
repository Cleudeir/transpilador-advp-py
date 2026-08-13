// caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2024/02/11/exibindo-mensagens-no-console-log-com-a-fwlogmsg-maratona-advpl-e-tl-228/
// Bibliotecas
#Include "Totvs.ch"
#Include "FWMVCDef.ch"
// {Protheus.doc} User Function zExe229
// Exemplo de tela com marcação de dados
// @author Atilio
// @since 20/02/2023
// @version 1.0
// @type function
// @obs Codigo gerado automaticamente pelo Autumn Code Maker
// @see http://autumncodemaker.com e https://tdn.totvs.com/display/public/framework/FWMarkBrowse
USER FUNCTION zExe229()
    LOCAL aArea, aPergs, xPar0, xPar1

    aArea := FWGetArea()
    aPergs := {  }
    xPar0 := Space(15)
    xPar1 := Space(15)
    // Adicionando os parametros do ParamBox
    aAdd(aPergs, { 1, "Produto De", xPar0, "", ".T.", "SB1", ".T.", 80, .F. })
    aAdd(aPergs, { 1, "Produto Até", xPar1, "", ".T.", "SB1", ".T.", 80, .T. })
    // Se a pergunta for confirma, chama a tela
    If ParamBox(aPergs, "Informe os parametros")
        fMontaTela()
    EndIf
    FWRestArea(aArea)
    RETURN Static

FUNCTION fMontaTela()
    LOCAL aArea, aCampos, oTempTable, aColunas, cFontPad, oFontGrid, oDlgMark, oPanGrid, oMarkBrowse, cAliasTmp, aRotina, aTamanho, nJanLarg, nJanAltu

    aArea := GetArea()
    aCampos := {  }
    oTempTable := Nil
    aColunas := {  }
    cFontPad := "Tahoma"
    oFontGrid := TFont():New(cFontPad, Nil, - 14)
    // Janela e componentes
    oDlgMark := Nil
    oPanGrid := Nil
    oMarkBrowse := Nil
    cAliasTmp := GetNextAlias()
    aRotina := MenuDef()
    // Tamanho da janela
    aTamanho := MsAdvSize()
    nJanLarg := aTamanho[5]
    nJanAltu := aTamanho[6]
    // Adiciona as colunas que serão criadas na temporária
    aAdd(aCampos, { "OK", "C", 2, 0 })
    // Flag para marcação
    aAdd(aCampos, { "B1_COD", "C", 15, 0 })
    // Produto
    aAdd(aCampos, { "B1_TIPO", "C", 2, 0 })
    // Tipo
    aAdd(aCampos, { "B1_UM", "C", 2, 0 })
    // Unid. Med.
    aAdd(aCampos, { "B1_DESC", "C", 50, 0 })
    // Descrição
    // Cria a tabela temporária
    oTempTable := FWTemporaryTable():New(cAliasTmp)
    oTempTable:SetFields(aCampos)
    oTempTable:Create()
    // Popula a tabela temporária
    Processa(Nil, "Processando...")
    // Adiciona as colunas que serão exibidas no FWMarkBrowse
    aColunas := fCriaCols()
    // Criando a janela
    DEFINE
    MSDIALOG
    oDlgMark
    TITLE
    "Tela para Marcação de dados - Autumn Code Maker"
    FROM_
    0
    // ,
    0
    TO
    nJanAltu
    // ,
    nJanLarg
    COLORS
    0
    // ,
    16777215
    PIXEL
    // Dados
    oPanGrid := tPanel():New(1, 1, "", oDlgMark, Nil, Nil, Nil, RGB(0, 0, 0), RGB(254, 254, 254), nJanLarg / 2 - 1, nJanAltu / 2 - 1)
    oMarkBrowse := FWMarkBrowse():New()
    oMarkBrowse:SetAlias(cAliasTmp)
    oMarkBrowse:SetDescription("Produtos")
    oMarkBrowse:DisableFilter()
    oMarkBrowse:DisableConfig()
    oMarkBrowse:DisableSeek()
    oMarkBrowse:DisableSaveConfig()
    oMarkBrowse:SetFontBrowse(oFontGrid)
    oMarkBrowse:SetFieldMark("OK")
    oMarkBrowse:SetTemporary(.T.)
    oMarkBrowse:SetColumns(aColunas)
    // oMarkBrowse:AllMark()
    oMarkBrowse:SetOwner(oPanGrid)
    oMarkBrowse:Activate()
    ACTIVATE
    MsDialog
    oDlgMark
    CENTERED
    // Deleta a temporária e desativa a tela de marcação
    oTempTable:Delete()
    oMarkBrowse:DeActivate()
    RestArea(aArea)
    RETURN Static

FUNCTION MenuDef()
    LOCAL aRotina

    aRotina := {  }
    // Criação das opções
    ADD
    OPTION
    aRotina
    TITLE
    "Continuar"
    ACTION
    "u_zExe229O"
    OPERATION
    2
    ACCESS
    0
    RETURN aRotina
    // {Protheus.doc} fPopula
    // Executa a query SQL e popula essa informação na tabela temporária usada no browse
    // @author Atilio
    // @since 20/02/2023
    // @version 1.0
    // @type function
    // @obs Codigo gerado automaticamente pelo Autumn Code Maker
    // @see http://autumncodemaker.com

STATIC FUNCTION fPopula()
    LOCAL cQryDados, nTotal, nAtual

    cQryDados := ""
    nTotal := 0
    nAtual := 0
    // Monta a consulta
    cQryDados += "SELECT B1_COD, B1_TIPO, B1_UM, B1_DESC " + CRLF
    cQryDados += "FROM SB1990 SB1 " + CRLF
    cQryDados += "WHERE B1_FILIAL = '' AND B1_COD >= '" + MV_PAR01 + "' AND B1_COD <= '" + MV_PAR02 + "' AND SB1.D_E_L_E_T_ = ' ' " + CRLF
    cQryDados += "ORDER BY B1_COD" + CRLF
    PLSQuery(cQryDados, "QRYDADTMP")
    // Definindo o tamanho da régua
    DbSelectArea("QRYDADTMP")
    Count
    to
    nTotal
    ProcRegua(nTotal)
    QRYDADTMP:DbGoTop()
    // Enquanto houver registros, adiciona na temporária
    While .NOT. QRYDADTMP->( DbEof() )
        nAtual += 1
        IncProc("Analisando registro " + cValToChar(nAtual) + " de " + cValToChar(nTotal) + "...")
        RecLock(cAliasTmp, .T.)
        cAliasTmp->OK := Space(2)
        cAliasTmp->B1_COD := setattr(QRYDADTMP:B1_COD(cAliasTmp), "B1_TIPO", setattr(QRYDADTMP:B1_TIPO(cAliasTmp), "B1_UM", setattr(QRYDADTMP:B1_UM(cAliasTmp), "B1_DESC", QRYDADTMP:B1_DESC(cAliasTmp):MsUnlock()) .OR. QRYDADTMP:B1_DESC(cAliasTmp):MsUnlock()) .OR. setattr(QRYDADTMP:B1_UM(cAliasTmp), "B1_DESC", QRYDADTMP:B1_DESC(cAliasTmp):MsUnlock()) .OR. QRYDADTMP:B1_DESC(cAliasTmp):MsUnlock()) .OR. setattr(QRYDADTMP:B1_TIPO(cAliasTmp), "B1_UM", setattr(QRYDADTMP:B1_UM(cAliasTmp), "B1_DESC", QRYDADTMP:B1_DESC(cAliasTmp):MsUnlock()) .OR. QRYDADTMP:B1_DESC(cAliasTmp):MsUnlock()) .OR. setattr(QRYDADTMP:B1_UM(cAliasTmp), "B1_DESC", QRYDADTMP:B1_DESC(cAliasTmp):MsUnlock()) .OR. QRYDADTMP:B1_DESC(cAliasTmp):MsUnlock()
        QRYDADTMP:DbSkip()
    EndDo
    QRYDADTMP:DbCloseArea()
    cAliasTmp:DbGoTop()
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
    aAdd(aEstrut, { "B1_COD", "Produto", "C", 15, 0, "" })
    aAdd(aEstrut, { "B1_TIPO", "Tipo", "C", 2, 0, "" })
    aAdd(aEstrut, { "B1_UM", "Unid. Med.", "C", 2, 0, "" })
    aAdd(aEstrut, { "B1_DESC", "Descrição", "C", 50, 0, "" })
    // Percorrendo todos os campos da estrutura
    RETURN aColunas
    // {Protheus.doc} User Function zExe229O
    // Função acionada pelo botão continuar da rotina
    // @author Atilio
    // @since 20/02/2023
    // @version 1.0
    // @type function
    // @obs Codigo gerado automaticamente pelo Autumn Code Maker
    // @see http://autumncodemaker.com

USER FUNCTION zExe229O()
    Processa(Nil, "Processando...")
    RETURN Static

FUNCTION fProcessa()
    LOCAL aArea, cMarca, nAtual, nTotal, nTotMarc

    aArea := FWGetArea()
    cMarca := oMarkBrowse:Mark()
    nAtual := 0
    nTotal := 0
    nTotMarc := 0
    // Define o tamanho da régua
    DbSelectArea(cAliasTmp)
    cAliasTmp:DbGoTop()
    Count
    To
    nTotal
    ProcRegua(nTotal)
    // Percorrendo os registros
    cAliasTmp:DbGoTop()
    While .NOT. cAliasTmp->( DbEof() )
        nAtual += 1
        IncProc("Analisando registro " + cValToChar(nAtual) + " de " + cValToChar(nTotal) + "...")
        // Caso esteja marcado
        If oMarkBrowse:IsMark(cMarca)
            nTotMarc += 1
            // //Aqui dentro você pode fazer o seu processamento
            // Alert((cAliasTmp)->B1_COD)
        EndIf
        cAliasTmp:DbSkip()
    EndDo
    // Mostra a mensagem de término e caso queria fechar a dialog, basta usar o método End()
    FWAlertInfo("Dos [" + cValToChar(nTotal) + "] registros, foram processados [" + cValToChar(nTotMarc) + "] registros", "Atenção")
    // oDlgMark:End()
    FWRestArea(aArea)
    RETURN
