// caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2024/02/21/buscando-informacoes-das-perguntas-com-a-fwsx1util-maratona-advpl-e-tl-249/
// Bibliotecas
#Include "Totvs.ch"
#Include "FWMVCDef.ch"
// Variveis Estaticas
cTitulo := "Grupo de Produtos"
cAliasMVC := "SBM"
// {Protheus.doc} User Function zExe248
// Grupo de Produtos (teste de FWStruTrigger)
// @author Atilio
// @since 20/02/2023
// @version 1.0
// @type function
// @obs Codigo gerado automaticamente pelo Autumn Code Maker
// @see https://tdn.totvs.com/display/public/framework/FwStruTrigger e http://autumncodemaker.com
// Função FWStruTrigger
// Parâmetros
// + cDom           , Caractere       , Campo Origem
// + cCDom          , Caractere       , Campo Destino
// + cRegra         , Caractere       , Regra de Preenchimento
// + lSeek          , Lógico          , Irá Posicionar?
// + cAlias         , Caractere       , Alias de Posicionamento
// + nOrdem         , Numérico        , Índice de Posicionamento
// + cChave         , Caractere       , Chave de Posicionamento
// + cCondic        , Caractere       , Condição para execução do gatilho
// + cSequen        , Caractere       , Sequência do gatilho
// Retorno
// + aRetorno       , Array           , Array com os dados que serão necessários para a Struct
// **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
USER FUNCTION zExe248()
    LOCAL aArea, oBrowse, aRotina

    aArea := FWGetArea()
    oBrowse := Nil
    aRotina := {  }
    // Definicao do menu
    aRotina := MenuDef()
    // Instanciando o browse
    oBrowse := FWMBrowse():New()
    oBrowse:SetAlias(cAliasMVC)
    oBrowse:SetDescription(cTitulo)
    oBrowse:DisableDetails()
    // Ativa a Browse
    oBrowse:Activate()
    FWRestArea(aArea)
    RETURN
    // {Protheus.doc} MenuDef
    // Menu de opcoes na funcao zExe248
    // @author Atilio
    // @since 20/02/2023
    // @version 1.0
    // @type function
    // @obs Codigo gerado automaticamente pelo Autumn Code Maker
    // @see http://autumncodemaker.com

STATIC FUNCTION MenuDef()
    LOCAL aRotina

    aRotina := {  }
    // Adicionando opcoes do menu
    ADD
    OPTION
    aRotina
    TITLE
    "Visualizar"
    ACTION
    "VIEWDEF.Exemplo_248_Funcao_FWStruTriggger"
    OPERATION
    1
    ACCESS
    0
    ADD
    OPTION
    aRotina
    TITLE
    "Incluir"
    ACTION
    "VIEWDEF.Exemplo_248_Funcao_FWStruTriggger"
    OPERATION
    3
    ACCESS
    0
    ADD
    OPTION
    aRotina
    TITLE
    "Alterar"
    ACTION
    "VIEWDEF.Exemplo_248_Funcao_FWStruTriggger"
    OPERATION
    4
    ACCESS
    0
    ADD
    OPTION
    aRotina
    TITLE
    "Excluir"
    ACTION
    "VIEWDEF.Exemplo_248_Funcao_FWStruTriggger"
    OPERATION
    5
    ACCESS
    0
    RETURN aRotina
    // {Protheus.doc} ModelDef
    // Modelo de dados na funcao zExe248
    // @author Atilio
    // @since 20/02/2023
    // @version 1.0
    // @type function
    // @obs Codigo gerado automaticamente pelo Autumn Code Maker
    // @see http://autumncodemaker.com

STATIC FUNCTION ModelDef()
    LOCAL oStruct, oModel, bPre, bPos, bCommit, bCancel, aGatilhos, nAtual

    oStruct := FWFormStruct(1, cAliasMVC)
    oModel := Nil
    bPre := Nil
    bPos := Nil
    bCommit := Nil
    bCancel := Nil
    aGatilhos := {  }
    nAtual := Nil
    // Adicionando um gatilho, do codigo para data
    aAdd(aGatilhos, FWStruTriggger("BM_GRUPO", "BM_DESC", "'Grupo ' + Replicate('x', 10)", .F., "", 0, "", Nil, "01"))
    aAdd(aGatilhos, FWStruTriggger("BM_DESC", "BM_PROORI", "'1'", .F., "", 0, "", Nil, "01"))
    // Percorrendo os gatilhos e adicionando na Struct
    // Cria o modelo de dados para cadastro
    oModel := MPFormModel():New("zExe248M", bPre, bPos, bCommit, bCancel)
    oModel:AddFields("SBMMASTER", Nil, oStruct)
    oModel:SetDescription("Modelo de dados - " + cTitulo)
    oModel:GetModel("SBMMASTER"):SetDescription("Dados de - " + cTitulo)
    oModel:SetPrimaryKey({  })
    RETURN oModel
    // {Protheus.doc} ViewDef
    // Visualizacao de dados na funcao zExe248
    // @author Atilio
    // @since 20/02/2023
    // @version 1.0
    // @type function
    // @obs Codigo gerado automaticamente pelo Autumn Code Maker
    // @see http://autumncodemaker.com

STATIC FUNCTION ViewDef()
    LOCAL oModel, oStruct, oView

    oModel := ModelDef()
    oStruct := FWFormStruct(2, cAliasMVC)
    oView := Nil
    // Cria a visualizacao do cadastro
    oView := FWFormView():New()
    oView:SetModel(oModel)
    oView:AddField("VIEW_SBM", oStruct, "SBMMASTER")
    oView:CreateHorizontalBox("TELA", 100)
    oView:SetOwnerView("VIEW_SBM", "TELA")
    RETURN oView
