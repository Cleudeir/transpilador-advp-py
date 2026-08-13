# Esse exemplo faz parte da série do YouTube, Maratona de Exemplos, do canal Terminal de Informação, 
#     caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2023/10/05/deixando-uma-string-com-o-tamanho-do-campo-com-a-funcao-avkey-maratona-advpl-e-tl-058/
# Bibliotecas
# PREPROCESSOR: #Include "TOTVS.ch"
# {Protheus.doc} User Function zExe058
# Exemplo de função que formata um conteúdo conforme o campo do dicionário
# @type Function
# @author Atilio
# @since 05/12/2022
# @obs 
#     Função AvKey
#     Parâmetros
#         + Conteúdo que será formatado podendo ser numérico ou data ou caractere
#         + Nome do campo do dicionário (SX3)
#         + Define se irá truncar o conteúdo do xInformacao caso o seja menor que o tamanho do campo
#         + Se é para considerar um array como struct do campo (similar ao DbStruct mas somente do campo)
#     Retorno
#         + Conteúdo formatado conforme campo do dicionário de dados (SX3)
# 
#     **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
def u_zExe058():
    aArea = FWGetArea()
    cDescri = 'Banana'
    cCodigo = 'F0002'
    # Abre a tabela de produtos e usa o índice da descrição
    DbSelectArea('SB1')
    SB1.DbSetOrder(3)
    # B1_FILIAL + B1_DESC + B1_COD
    # Tenta posicionar logo como veio os dados
    if SB1.MsSeek(FWxFilial('SB1') + cDescri + cCodigo):
        FWAlertSuccess('Encontrou a busca', 'Teste 1')
    else:
        FWAlertError('Não Encontrou', 'Teste 1')

    # Agora formata o conteúdo com o AvKey
    cDescri = AvKey(cDescri, 'B1_DESC')
    cCodigo = AvKey(cCodigo, 'B1_COD')
    if SB1.MsSeek(FWxFilial('SB1') + cDescri + cCodigo):
        FWAlertSuccess('Encontrou a busca', 'Teste 2')
    else:
        FWAlertError('Não Encontrou', 'Teste 2')

    FWRestArea(aArea)
    return
