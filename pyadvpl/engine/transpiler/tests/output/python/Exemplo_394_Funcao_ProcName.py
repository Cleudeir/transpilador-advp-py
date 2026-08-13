# Esse exemplo faz parte da série do YouTube, Maratona de Exemplos, do canal Terminal de Informação, 
#     caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2024/05/04/adicionando-aspas-nos-extremos-de-uma-string-com-a-putaspas-maratona-advpl-e-tl-395/
# Bibliotecas
# PREPROCESSOR: #Include "TOTVS.ch"
# {Protheus.doc} User Function zExe394
# Retorna o nome dos processos na pilha de chamadas
# @type Function
# @author Atilio
# @since 28/03/2023
# @see https://tdn.totvs.com/display/tec/ProcName
# @obs 
# 
#     Função ProcName
#     Parâmetros
#         + nAtivacao    , Numérico      , Número do processo (iniciando com 0 de Atual)
#     Retorno
#         + cRet         , Caractere     , Nome do processo
# 
#     **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
def u_zExe394():
    aArea = FWGetArea()
    nAtual = 0
    cProcAtu = ''
    cMensagem = ''
    # Enquanto for verdadeiro
    while True:
        # Busca o nome do processo atual
        cProcAtu = ProcName(nAtual)
        # Se existir, incrementa a mensagem
        if not Empty(cProcAtu):
            cMensagem += '#' + StrZero(nAtual, 4) + ' - ' + cProcAtu + CRLF
            # Senão, encerra o laço
        else:
            break

        # Incrementa o contador dos processos
        nAtual += 1

    # Exibe os processos encontrados
    ShowLog(cMensagem)
    FWRestArea(aArea)
    return
