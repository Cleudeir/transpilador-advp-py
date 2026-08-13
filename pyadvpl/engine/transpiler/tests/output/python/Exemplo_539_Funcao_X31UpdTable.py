# Esse exemplo faz parte da série do YouTube, Maratona de Exemplos, do canal Terminal de Informação, 
#     caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2024/07/15/buscando-a-chave-unica-da-tabela-com-x2unique2index-e-getsx2unico-maratona-advpl-e-tl-538/
# Bibliotecas
# PREPROCESSOR: #Include "TOTVS.ch"
# {Protheus.doc} User Function zExe539
# Atualiza uma tabela no SQL conforme as alterações nos dicionários (SX2, SX3 e SIX)
# @type Function
# @author Atilio
# @since 07/04/2023
# @obs 
# 
#     Função X31UpdTable
#     Parâmetros
#         Recebe o alias a ser atualizado
#     Retorno
#         Função não tem retorno
# 
# 
# 
#     A partir da LIB 20221010_P12, é exibido uma mensagem de que essa função será descontinuada em breve
#     Saiba mais em: https://tdn.totvs.com/pages/releaseview.action?pageId=698632582
# 
# 
#     **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
def u_zExe539():
    aArea = FWGetArea()
    cTabAlias = ''
    # Abre um input pro usuário digitar a tabela
    cTabAlias = FWInputBox('Insira o alias da tabela')
    cTabAlias = Alltrim(cTabAlias)
    # Caso a variável foi preenchida, seja tamanho 3 e exista no dicionário, ai prossegue
    if not Empty(cTabAlias) and Len(cTabAlias) == 3 and ExisteSX2(cTabAlias):
        # Limpa as mensagens que haja em memória do X31
        __SetX31Mode(False)
        # Tenta executar a atualização da tabela (criação e alteração de índices e campos)
        X31UpdTable(cTabAlias)
        # Se houve algum erro, mostra mensagem
        if __GetX31Error():
            ShowLog("Houve um erro na atualização da tabela '" + cTabAlias + "':" + CRLF + CRLF + __GetX31Trace())
        else:
            FWAlertSuccess("Sucesso na atualização da tabela '" + cTabAlias + "'", 'Sucesso')


    FWRestArea(aArea)
    return
