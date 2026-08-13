# Esse exemplo faz parte da série do YouTube, Maratona de Exemplos, do canal Terminal de Informação, 
#     caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2024/02/14/gerando-e-abrindo-o-excel-com-fwmsexcel-fwmsexcelxlsx-e-msexcel-maratona-advpl-e-tl-234/
# Bibliotecas
# PREPROCESSOR: #Include "TOTVS.ch"
# {Protheus.doc} User Function zExe235
# Exemplo de barras de processamento
# @type Function
# @author Atilio
# @since 20/02/2023
# @see https://tdn.totvs.com/display/public/framework/FWMsgRun e https://tdn.totvs.com/display/tec/MsgRun
# @obs 
#     Função FWMsgRun
#     Parâmetros
#         + oComponent    , Objeto            , Componente que será sobreposto com o painel
#         + bAction       , Bloco de Código   , Bloco que será executado
#         + cHeader       , Caractere         , Título da janela
#         + cText         , Caractere         , Texto que será apresentado
#     Retorno
#         Não tem retorno
# 
#     Função MsgRun
#     Parâmetros
#         + cText         , Caractere         , Texto que será apresentado
#         + cHeader       , Caractere         , Título da janela
#         + bBlock        , Bloco de Código   , Bloco que será executado
#     Retorno
#         Não tem retorno
# 
#     **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
def u_zExe235():
    aArea = FWGetArea()
    nTotal = 0
    aDados = Array(1000000)
    # Mostra qualquer mensagem
    MsgRun('Lendo informações...', 'Teste', lambda : aEval(aDados, lambda x: (nTotal := nTotal + 1)))
    # Mostra a barra que fica carregando
    FWMsgRun(None, lambda oSay: fCorre(oSay), 'Processando', 'Buscando informações')
    FWRestArea(aArea)
    return Static

def fCorre(oSay):
    nAtual = 0
    # Percorre o array e define o texto
    return
