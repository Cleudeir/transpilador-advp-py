# Esse exemplo faz parte da série do YouTube, Maratona de Exemplos, do canal Terminal de Informação, 
#     caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2024/03/18/consumindo-um-get-atraves-da-httpget-maratona-advpl-e-tl-301/
# Bibliotecas
# PREPROCESSOR: #Include "TOTVS.ch"
# {Protheus.doc} User Function zExe299
# Conversões entre horas e minutos
# @type  Function
# @author Atilio
# @since 22/02/2023
# @obs 
# 
#     Função hToM
#     Parâmetros
#         Recebe um número de horas
#     Retorno
#         Retorna o número total de minutos
# 
#     Função mToH
#     Parâmetros
#         Recebe um número de minutos
#     Retorno
#         Retorna a hora, minuto e segundos no formato "hh:mm"
# 
#     **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
def u_zExe300():
    aArea = FWGetArea()
    nResultado = 0
    cHoras = ''
    # Busca os minutos através de uma hora
    nResultado = hToM('10:25')
    FWAlertInfo('10:25 horas dá um total de ' + cValToChar(nResultado) + ' minutos!', 'Exemplo hToM')
    # Busca uma hora através dos minutos
    cHoras = mToH(640)
    FWAlertInfo('640 minutos dá um total de ' + cHoras + '!', 'Exemplo mToH')
    FWRestArea(aArea)
    return
