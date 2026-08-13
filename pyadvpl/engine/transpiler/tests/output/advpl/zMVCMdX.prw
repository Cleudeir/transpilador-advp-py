// ===
// Esse é um exemplo disponibilizado no Terminal de Informação
// Confira o artigo sobre esse assunto, no seguinte link: https://terminaldeinformacao.com/2015/08/26/exemplos-de-rotinas-mvc-em-advpl/
// Caso queira ver outros conteúdos envolvendo AdvPL e TL++, veja em: https://terminaldeinformacao.com/advpl/
// ===
// Bibliotecas
#Include 'Protheus.ch'
#Include 'FWMVCDef.ch'
// Variáveis Estáticas
cTitulo := "Grp.Produtos (Mod.X)"
// {Protheus.doc} zMVCMdX
// Função para cadastro de Grupo de Produtos (SBM), Produtos (SB1) e Saldos dos Produtos (SB2), exemplo de Modelo X em MVC
// @author Atilio
// @since 17/08/2015
// @version 1.0
// @return Nil, Função não tem retorno
// @example
// u_zMVCMdX()
// @obs Não se pode executar função MVC dentro do fórmulas
USER FUNCTION zMVCMdX()
    LOCAL aArea, oBrowse

    aArea := GetArea()
    oBrowse := Nil
    // Instânciando FWMBrowse - Somente com dicionário de dados
    oBrowse := FWMBrowse():New()
    // Setando a tabela de cadastro de Autor/Interprete
    oBrowse:SetAlias("SBM")
    // Setando a descrição da rotina
    oBrowse:SetDescription(cTitulo)
    // Legendas
    oBrowse:AddLegend("SBM->BM_PROORI == '1'", "GREEN", "Original")
    oBrowse:AddLegend("SBM->BM_PROORI == '0'", "RED", "Não Original")
    // Ativa a Browse
    oBrowse:Activate()
    RestArea(aArea)
    RETURN
    // ---------------------------------------------------------------------*
    // | Func:  MenuDef                                                      |
    // | Autor: Daniel Atilio                                                |
    // | Data:  17/08/2015                                                   |
    // | Desc:  Criação do menu MVC                                          |
    // | Obs.:  /                                                            |
    // *---------------------------------------------------------------------

STATIC FUNCTION MenuDef()
    LOCAL aRot

    aRot := {  }
    // Adicionando opções
    ADD
    OPTION
    aRot
    TITLE
    "Visualizar"
    ACTION
    "VIEWDEF.zMVCMdX"
    OPERATION
    MODEL_OPERATION_VIEW
    ACCESS
    0
    // OPERATION 1
    ADD
    OPTION
    aRot
    TITLE
    "Legenda"
    ACTION
    "u_zMVC01Leg"
    OPERATION
    6
    ACCESS
    0
    // OPERATION X
    // ADD OPTION aRot TITLE 'Incluir'    ACTION 'VIEWDEF.zMVCMdX' OPERATION MODEL_OPERATION_INSERT ACCESS 0 //OPERATION 3
    // ADD OPTION aRot TITLE 'Alterar'    ACTION 'VIEWDEF.zMVCMdX' OPERATION MODEL_OPERATION_UPDATE ACCESS 0 //OPERATION 4
    // ADD OPTION aRot TITLE 'Excluir'    ACTION 'VIEWDEF.zMVCMdX' OPERATION MODEL_OPERATION_DELETE ACCESS 0 //OPERATION 5
    RETURN aRot
    // ---------------------------------------------------------------------*
    // | Func:  ModelDef                                                     |
    // | Autor: Daniel Atilio                                                |
    // | Data:  17/08/2015                                                   |
    // | Desc:  Criação do modelo de dados MVC                               |
    // | Obs.:  /                                                            |
    // *---------------------------------------------------------------------

STATIC FUNCTION ModelDef()
    LOCAL oModel, oStPai, oStFilho, oStNeto, aSB1Rel, aSB2Rel

    oModel := Nil
    oStPai := FWFormStruct(1, "SBM")
    oStFilho := FWFormStruct(1, "SB1")
    oStNeto := FWFormStruct(1, "SB2")
    aSB1Rel := {  }
    aSB2Rel := {  }
    // Criando o modelo e os relacionamentos
    oModel := MPFormModel():New("zMVCMdXM")
    oModel:AddFields("SBMMASTER", Nil, oStPai)
    oModel:AddGrid("SB1DETAIL", "SBMMASTER", oStFilho, Nil, Nil, Nil, Nil)
    // cOwner é para quem pertence
    oModel:AddGrid("SB2DETAIL", "SB1DETAIL", oStNeto, Nil, Nil, Nil, Nil)
    // cOwner é para quem pertence
    // Fazendo o relacionamento entre o Pai e Filho
    aAdd(aSB1Rel, { "B1_FILIAL", "BM_FILIAL" })
    aAdd(aSB1Rel, { "B1_GRUPO", "BM_GRUPO" })
    // Fazendo o relacionamento entre o Filho e Neto
    aAdd(aSB2Rel, { "B2_FILIAL", "B1_FILIAL" })
    aAdd(aSB2Rel, { "B2_COD", "B1_COD" })
    oModel:SetRelation("SB1DETAIL", aSB1Rel, SB1:IndexKey(1))
    // IndexKey -> quero a ordenação e depois filtrado
    oModel:GetModel("SB1DETAIL"):SetUniqueLine({ "B1_FILIAL", "B1_COD" })
    // Não repetir informações ou combinações {"CAMPO1","CAMPO2","CAMPOX"}
    oModel:SetPrimaryKey({  })
    oModel:SetRelation("SB2DETAIL", aSB2Rel, SB2:IndexKey(1))
    // IndexKey -> quero a ordenação e depois filtrado
    oModel:GetModel("SB2DETAIL"):SetUniqueLine({ "B2_COD", "B2_LOCAL", "B2_QATU" })
    // Não repetir informações ou combinações {"CAMPO1","CAMPO2","CAMPOX"}
    oModel:SetPrimaryKey({  })
    // Setando as descrições
    oModel:SetDescription("Grupo de Produtos - Mod. X")
    oModel:GetModel("SBMMASTER"):SetDescription("Modelo Grupo")
    oModel:GetModel("SB1DETAIL"):SetDescription("Modelo Produtos")
    oModel:GetModel("SB2DETAIL"):SetDescription("Modelo Saldos")
    // Adicionando totalizadores
    oModel:AddCalc("TOT_SALDO", "SB1DETAIL", "SB2DETAIL", "B2_QATU", "XX_TOTAL", "SUM", Nil, Nil, "Saldo Total:")
    RETURN oModel
    // ---------------------------------------------------------------------*
    // | Func:  ViewDef                                                      |
    // | Autor: Daniel Atilio                                                |
    // | Data:  17/08/2015                                                   |
    // | Desc:  Criação da visão MVC                                         |
    // | Obs.:  /                                                            |
    // *---------------------------------------------------------------------

STATIC FUNCTION ViewDef()
    LOCAL oView, oModel, oStPai, oStFilho, oStNeto, oStTot, aStruSBM, aStruSB1, aStruSB2, cConsSBM, cConsSB1, cConsSB2, nAtual

    oView := Nil
    oModel := FWLoadModel("zMVCMdX")
    oStPai := FWFormStruct(2, "SBM")
    oStFilho := FWFormStruct(2, "SB1")
    oStNeto := FWFormStruct(2, "SB2")
    oStTot := FWCalcStruct(oModel:GetModel("TOT_SALDO"))
    // Estruturas das tabelas e campos a serem considerados
    aStruSBM := SBM:DbStruct()
    aStruSB1 := SB1:DbStruct()
    aStruSB2 := SB2:DbStruct()
    cConsSBM := "BM_GRUPO;BM_DESC;BM_PROORI"
    cConsSB1 := "B1_COD;B1_DESC;B1_TIPO;B1_UM;B1_LOCPAD"
    cConsSB2 := "B2_LOCAL;B2_QATU"
    nAtual := 0
    // Criando a View
    oView := FWFormView():New()
    oView:SetModel(oModel)
    // Adicionando os campos do cabeçalho e o grid dos filhos
    oView:AddField("VIEW_SBM", oStPai, "SBMMASTER")
    oView:AddGrid("VIEW_SB1", oStFilho, "SB1DETAIL")
    oView:AddGrid("VIEW_SB2", oStNeto, "SB2DETAIL")
    oView:AddField("VIEW_TOT", oStTot, "TOT_SALDO")
    // Setando o dimensionamento de tamanho
    oView:CreateHorizontalBox("CABEC", 20)
    oView:CreateHorizontalBox("GRID", 40)
    oView:CreateHorizontalBox("GRID2", 27)
    oView:CreateHorizontalBox("TOTAL", 13)
    // Amarrando a view com as box
    oView:SetOwnerView("VIEW_SBM", "CABEC")
    oView:SetOwnerView("VIEW_SB1", "GRID")
    oView:SetOwnerView("VIEW_SB2", "GRID2")
    oView:SetOwnerView("VIEW_TOT", "TOTAL")
    // Habilitando título
    oView:EnableTitleView("VIEW_SBM", "Grupo")
    oView:EnableTitleView("VIEW_SB1", "Produtos")
    oView:EnableTitleView("VIEW_SB2", "Saldos")
    // Percorrendo a estrutura da SBM
    // Percorrendo a estrutura da SB1
    // Percorrendo a estrutura da SB2
    RETURN oView
