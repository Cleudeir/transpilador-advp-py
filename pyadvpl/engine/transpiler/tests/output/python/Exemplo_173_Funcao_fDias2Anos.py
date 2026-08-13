# Esse exemplo faz parte da série do YouTube, Maratona de Exemplos, do canal Terminal de Informação, 
#     caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2024/01/14/calculando-numero-de-anos-e-meses-com-a-funcao-fdias2anos-maratona-advpl-e-tl-173/
# Bibliotecas
# PREPROCESSOR: #Include "TOTVS.ch"
# {Protheus.doc} User Function zExe173
# Calcula um número de anos, meses e dias conforme a quantidade de dias passadas em um parâmetro
# @type Function
# @author Atilio
# @since 20/12/2022
# @obs 
#     Função fDias2Anos
#     Parâmetros
#         + Tempo total em dias
#         + Número de anos que será calculado
#         + Número de meses que será calculado
#         + Número de dias que será calculado
#     Retorno
#         Função não tem retorno
# 
#     **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
def u_zExe173():
    aArea = FWGetArea()
    nDiasTot = 1054
    nAnos = 0
    nMeses = 0
    nDias = 0
    cMensagem = ''
    # Calcula o total de anos, meses e dias
    fDias2Anos(nDiasTot, ref_(nAnos), ref_(nMeses), ref_(nDias))
    # Monta uma mensagem de teste e exibe
    cMensagem = 'Em um total de ' + cValToChar(nDiasTot) + ' dia(s), o resultado é: ' + CRLF + CRLF
    cMensagem += cValToChar(nAnos) + ' anos, ' + cValToChar(nMeses) + ' meses e ' + cValToChar(nDias) + ' dias'
    FWAlertInfo(cMensagem, 'Teste com fDias2Anos')
    FWRestArea(aArea)
    return
