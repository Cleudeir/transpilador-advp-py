# Esse exemplo faz parte da série do YouTube, Maratona de Exemplos, do canal Terminal de Informação, 
#     caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2023/10/06/excluindo-os-dados-de-uma-tabela-com-a-funcao-avzap-maratona-advpl-e-tl-059/
# Bibliotecas
# PREPROCESSOR: #Include "TOTVS.ch"
# {Protheus.doc} User Function zExe059
# Exemplo de função que executa o ZAP (limpeza) em uma tabela do Protheus apagando todos os dados
# @type Function
# @author Atilio
# @since 05/12/2022
# @obs 
#     Função AvZap
#     Parâmetros
#         + Alias da Tabela que terá os dados apagados
#     Retorno
#         + .T. em caso de sucesso ou .F. em caso de falha
# 
#     **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
def u_zExe059():
    aArea = FWGetArea()
    cTable = 'ZD4990'
    cTabAlias = 'ZD4'
    # Tenta executar o zap na tabela
    USE(cTable)
    ALIAS(cTabAlias)
    EXCLUSIVE
    NEW
    VIA
    'TOPCONN'
    if cTabAlias.AvZap():
        FWAlertSuccess('Limpeza executada com sucesso!', 'Teste AvZap')
    else:
        FWAlertError('Não foi possível excluir os dados da tabela, ela pode estar em uso!', 'Teste AvZap')

    FWRestArea(aArea)
    return
