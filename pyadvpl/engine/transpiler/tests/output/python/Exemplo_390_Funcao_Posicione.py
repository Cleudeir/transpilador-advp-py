# Esse exemplo faz parte da série do YouTube, Maratona de Exemplos, do canal Terminal de Informação, 
#     caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2024/05/02/buscando-a-informacao-de-uma-tabela-com-a-posicione-maratona-advpl-e-tl-390/
# Bibliotecas
# PREPROCESSOR: #Include "TOTVS.ch"
# PREPROCESSOR: #Include "TopConn.ch"
# {Protheus.doc} User Function zExe390
# Busca o conteúdo de um campo de uma tabela
# @type Function
# @author Atilio
# @since 28/03/2023
# @see https://tdn.totvs.com/display/public/framework/Posicione+-+Posiciona+tabela+em+registro
# @obs 
# 
#     Função Posicione
#     Parâmetros
#         + cAlias     , Caractere      , Alias da Tabela
#         + nOrdem     , Numérico       , Índice da Tabela usado na busca
#         + cSeek      , Caractere      , Expressão da busca conforme o índice
#         + cField     , Caractere      , Campo a ser buscado
#         + cNickName  , Caractere      , Apelido do índice caso queira usar no lugar do nOrdem
#     Retorno
#         + cReturn    , Caractere      , Conteúdo do campo buscado
# 
#     **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
def u_zExe390():
    aArea = FWGetArea()
    aPergs = []
    cCliente = Space(TamSX3('A1_COD')[1])
    cLoja = Space(TamSX3('A1_LOJA')[1])
    # Adiciona os parâmetros que serão mostrados no ParamBox
    aAdd(aPergs, [1, 'Cliente', cCliente, '', "ExistCPO('SA1')", 'SA1', '.T.', 80, True])
    aAdd(aPergs, [1, 'Loja', cLoja, '', '.T.', '', '.T.', 80, True])
    # Se a pergunta for confirmada, busca o nome do cliente
    if ParamBox(aPergs, 'Informe os parâmetros', None, None, None, None, None, None, None, None, False, False):
        cNomeCli = Posicione('SA1', 1, FWxFilial('SA1') + MV_PAR01 + MV_PAR02, 'A1_NOME')
        FWAlertInfo('O nome do cliente é ' + cNomeCli, 'Teste Posicione')

    FWRestArea(aArea)
    return
