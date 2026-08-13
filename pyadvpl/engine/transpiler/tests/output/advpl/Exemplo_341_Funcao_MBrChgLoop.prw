// caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2024/04/07/pegando-o-valor-maximo-e-minimo-entre-dois-valores-com-max-e-min-maratona-advpl-e-tl-340/
// Bibliotecas
#Include "Totvs.ch"
// {Protheus.doc} User Function zExe341
// Ativa recurso para que cada inclusão acione a tela novamente (similar ao recurso que existe em MVC)
// @type Function
// @author Atilio
// @since 22/03/2023
// Função MBrChgLoop
// Parâmetros
// .T. se quiser ativar recurso em Loop e .F. se não quiser
// Retorno
// Função não tem retorno
// **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
USER FUNCTION zExe341()
    LOCAL aArea, aCores, aRotina, cCadastro

    aArea := FWGetArea()
    aCores := {  }
    aRotina := MenuDef()
    cCadastro := "Grupo de Produtos"
    aAdd(aCores, { "SBM->BM_PROORI == '1'", "BR_PRETO" })
    aAdd(aCores, { "SBM->BM_PROORI == '0'", "BR_VERMELHO" })
    aAdd(aCores, { "EMPTY(SBM->BM_PROORI)", "BR_BRANCO" })
    // Ativa o recurso para funcionar em Loop
    MBrChgLoop(.T.)
    // Faz a abertura da tela
    mBrowse(1, 1, Nil, Nil, "SBM", Nil, Nil, Nil, Nil, Nil, aCores)
    FWRestArea(aArea)
    RETURN Static

FUNCTION MenuDef()
    LOCAL aRotina

    aRotina := {  }
    // Adicionando opcoes do menu
    aAdd(aRotina, { "Pesquisar", "AXPESQUI", 0, 1 })
    aAdd(aRotina, { "Visualizar", "AXVISUAL", 0, 2 })
    aAdd(aRotina, { "Incluir", "AXINCLUI", 0, 3 })
    aAdd(aRotina, { "Alterar", "AXALTERA", 0, 4 })
    aAdd(aRotina, { "Excluir", "AXDELETA", 0, 5 })
    RETURN aRotina
