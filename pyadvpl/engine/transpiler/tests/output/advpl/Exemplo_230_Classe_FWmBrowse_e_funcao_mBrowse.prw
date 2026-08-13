// caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2024/02/12/criando-uma-tela-de-navegacao-de-registros-com-fwmbrowse-e-mbrowse-maratona-advpl-e-tl-230/
// Bibliotecas
#Include "TOTVS.ch"
// {Protheus.doc} User Function zExe230
// Exemplo de criação de browses de cadastro
// @type Function
// @author Atilio
// @since 20/02/2023
// @see https://tdn.totvs.com/display/public/framework/FWMBrowse e https://tdn.totvs.com/pages/releaseview.action?pageId=24346981
// **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
USER FUNCTION zExe230()
    LOCAL aArea

    aArea := FWGetArea()
    If FWAlertYesNo("Você deseja ver o exemplo com FWMBrowse (sim) ou com mBrowse (não)?", "Continua?")
        fExemplo1()
    Else
        fExemplo2()
    EndIf
    FWRestArea(aArea)
    RETURN Static

FUNCTION fExemplo1()
    LOCAL aArea, oBrowse, aRotina, cCadastro

    aArea := FWGetArea()
    oBrowse := Nil
    aRotina := {  }
    cCadastro := "Grupo de Produtos"
    // Definicao do menu
    aRotina := MenuDef()
    // Instanciando o browse
    oBrowse := FWMBrowse():New()
    oBrowse:SetAlias("SBM")
    oBrowse:SetDescription(cCadastro)
    oBrowse:DisableDetails()
    // Adicionando as Legendas
    oBrowse:AddLegend("SBM->BM_PROORI == '1'", "BLACK", "Pro. Ori. igual a 1")
    oBrowse:AddLegend("SBM->BM_PROORI == '0'", "RED", "Pro. Ori. igual a 0")
    oBrowse:AddLegend("EMPTY(SBM->BM_PROORI)", "WHITE", "Pro. Ori. vazio")
    // Ativa a Browse
    oBrowse:Activate()
    FWRestArea(aArea)
    RETURN
    // {Protheus.doc} MenuDef
    // Menu de opcoes na funcao zExe230
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
    aAdd(aRotina, { "Pesquisar", "AXPESQUI", 0, 1 })
    aAdd(aRotina, { "Visualizar", "AXVISUAL", 0, 2 })
    aAdd(aRotina, { "Incluir", "AXINCLUI", 0, 3 })
    aAdd(aRotina, { "Alterar", "AXALTERA", 0, 4 })
    aAdd(aRotina, { "Excluir", "AXDELETA", 0, 5 })
    RETURN aRotina

STATIC FUNCTION fExemplo2()
    LOCAL aArea, aCores, aRotina, cCadastro

    aArea := FWGetArea()
    aCores := {  }
    aRotina := MenuDef()
    cCadastro := "Grupo de Produtos"
    aAdd(aCores, { "SBM->BM_PROORI == '1'", "BR_PRETO" })
    aAdd(aCores, { "SBM->BM_PROORI == '0'", "BR_VERMELHO" })
    aAdd(aCores, { "EMPTY(SBM->BM_PROORI)", "BR_BRANCO" })
    // Faz a abertura da tela
    mBrowse(1, 1, Nil, Nil, "SBM", Nil, Nil, Nil, Nil, Nil, aCores)
    FWRestArea(aArea)
    RETURN
