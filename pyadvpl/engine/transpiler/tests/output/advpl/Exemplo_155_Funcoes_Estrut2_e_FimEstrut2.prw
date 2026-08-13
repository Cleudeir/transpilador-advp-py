// caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2024/01/05/tratando-caracteres-especiais-com-a-funcao-escape-maratona-advpl-e-tl-154/
// Bibliotecas
#Include "TOTVS.ch"
// {Protheus.doc} User Function zExe155
// Monta a estrutura de um produto em uma tabela temporária
// @type Function
// @author Atilio
// @since 18/12/2022
// @see https://tdn.totvs.com/pages/releaseview.action?pageId=287060852 e https://tdn.totvs.com/pages/releaseview.action?pageId=287060899
// Função Estrut2
// Parâmetros
// + cProduto     , Caractere   , Código do produto (passar com os espaços a direita)
// + nQuantidade  , Numérico    , Quantidade base para ser calculada na estrutura
// + cAliasEstru  , Caractere   , Nome do alias da estrutura
// + oTempTable   , Objeto      , Objeto que será criado como temporária
// + lAsShow      , Lógico      , Monta a estrutura exatamente igual é na visualização em tela
// + lPreEstru    , Lógico      , Se for .T. olha a pré estrutura na SGG senão se for .F. olha na estrutura na SG1
// + lVldData     , Lógico      , Faz a consistência se os componentes estão dentro ou fora das datas de vigência (data ini e fim)
// Retorno
// Não tem Retorno
// Função FimEstrut2
// Parâmetros
// + cAliasEstru    , Caractere       , Nome do alias usado
// + oTempTable     , Objeto          , Objeto da Tabela temporária criada na Estrut2
// Retorno
// Não tem Retorno
// **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
USER FUNCTION zExe155()
    LOCAL aArea, cMensagem, cCodProd, nQuant, oTempTable, cAliasTmp, nEstru

    aArea := FWGetArea()
    cMensagem := ""
    cCodProd := "E0001"
    // Produto raíz da estrutura
    nQuant := 5
    // Quantidade a produzir
    // Variáveis Private para utilização da função Estrut2
    oTempTable := Nil
    cAliasTmp := "ESTRUT"
    nEstru := 0
    // Cria a estrutura temporária
    cCodProd := AvKey(cCodProd, "B1_COD")
    Estrut2(cCodProd, nQuant, cAliasTmp, @ oTempTable)
    // Se houver dados
    cAliasTmp:DbGoTop()
    If .NOT. cAliasTmp->( DbEof() )
        // Enquanto houver dados, monta mensagem do produto, componente e quantidade
        While .NOT. cAliasTmp->( DbEof() )
            cMensagem += "Produto: " + cAliasTmp->CODIGO + ", Componente: " + cAliasTmp->COMP + ", Quantidade: " + cValToChar(cAliasTmp->QUANT) + CRLF(cAliasTmp):DbSkip()
        EndDo
        FWAlertInfo(cMensagem, "Estrutura através de Estrut2")
    Else
        FWAlertError("Estrutura não encontrada!", "Falha Estrut2")
    EndIf
    // Finaliza a função de estrutura
    FimEstrut2(cAliasTmp, @ oTempTable)
    FWRestArea(aArea)
    RETURN
