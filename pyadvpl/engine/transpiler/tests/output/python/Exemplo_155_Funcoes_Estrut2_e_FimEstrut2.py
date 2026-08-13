# Esse exemplo faz parte da série do YouTube, Maratona de Exemplos, do canal Terminal de Informação, 
#     caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2024/01/05/tratando-caracteres-especiais-com-a-funcao-escape-maratona-advpl-e-tl-154/
# Bibliotecas
# PREPROCESSOR: #Include "TOTVS.ch"
# {Protheus.doc} User Function zExe155
# Monta a estrutura de um produto em uma tabela temporária
# @type Function
# @author Atilio
# @since 18/12/2022
# @see https://tdn.totvs.com/pages/releaseview.action?pageId=287060852 e https://tdn.totvs.com/pages/releaseview.action?pageId=287060899
# @obs 
#     Função Estrut2
#     Parâmetros
#         + cProduto     , Caractere   , Código do produto (passar com os espaços a direita)
#         + nQuantidade  , Numérico    , Quantidade base para ser calculada na estrutura
#         + cAliasEstru  , Caractere   , Nome do alias da estrutura
#         + oTempTable   , Objeto      , Objeto que será criado como temporária
#         + lAsShow      , Lógico      , Monta a estrutura exatamente igual é na visualização em tela
#         + lPreEstru    , Lógico      , Se for .T. olha a pré estrutura na SGG senão se for .F. olha na estrutura na SG1
#         + lVldData     , Lógico      , Faz a consistência se os componentes estão dentro ou fora das datas de vigência (data ini e fim)
#     Retorno
#         Não tem Retorno
# 
#     Função FimEstrut2
#     Parâmetros
#         + cAliasEstru    , Caractere       , Nome do alias usado
#         + oTempTable     , Objeto          , Objeto da Tabela temporária criada na Estrut2
#     Retorno
#         Não tem Retorno
# 
#     **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
def u_zExe155():
    aArea = FWGetArea()
    cMensagem = ''
    cCodProd = 'E0001'
    # Produto raíz da estrutura
    nQuant = 5
    # Quantidade a produzir
    # Variáveis Private para utilização da função Estrut2
    oTempTable = None
    cAliasTmp = 'ESTRUT'
    nEstru = 0
    # Cria a estrutura temporária
    cCodProd = AvKey(cCodProd, 'B1_COD')
    Estrut2(cCodProd, nQuant, cAliasTmp, ref_(oTempTable))
    # Se houver dados
    cAliasTmp.DbGoTop()
    if not cAliasTmp.EoF():
        # Enquanto houver dados, monta mensagem do produto, componente e quantidade
        while not cAliasTmp.EoF():
            cMensagem += 'Produto: ' + cAliasTmp.CODIGO + ', Componente: ' + cAliasTmp.COMP + ', Quantidade: ' + cValToChar(cAliasTmp.QUANT) + CRLF(cAliasTmp).DbSkip()

        FWAlertInfo(cMensagem, 'Estrutura através de Estrut2')
    else:
        FWAlertError('Estrutura não encontrada!', 'Falha Estrut2')

    # Finaliza a função de estrutura
    FimEstrut2(cAliasTmp, ref_(oTempTable))
    FWRestArea(aArea)
    return
