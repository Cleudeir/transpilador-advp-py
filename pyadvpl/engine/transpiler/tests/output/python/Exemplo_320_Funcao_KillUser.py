# Esse exemplo faz parte da série do YouTube, Maratona de Exemplos, do canal Terminal de Informação, 
#     caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2024/03/28/buscando-ultimo-dia-do-mes-com-a-lastdate-maratona-advpl-e-tl-321/
# Bibliotecas
# PREPROCESSOR: #Include "Protheus.ch"
# {Protheus.doc} User Function zExe320
# Formata uma string justificando o texto
# @type Function
# @author Atilio
# @since 25/02/2023
# @see https://tdn.totvs.com/display/tec/KillUser
# @obs 
#     KillUser
#     Parâmetros
#         + UserName       , Caractere    , Nome do usuário conectado no SmartClient
#         + ComputerName   , Caractere    , Nome do computador que esta com o SmartClient aberto
#         + ThreadId       , Numérico     , Indica o número da Thread entre ao AppServer e SmartClient
#         + ServerName     , Caractere    , Indica o servidor onde esta rodando o AppServer
#     Retorno
#         Função não tem retorno
# 
#     **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
def u_zExe320():
    aArea = GetArea()
    aThreads = []
    nConexAtu = 1
    nTentativa = 1
    nMaxTenta = 10
    # Pega todos os usuários conectados
    aThreads = GetUserInfoArray()
    # Enquanto houver tentativas para finalizar as threads
    while nTentativa <= nMaxTenta:
        # Percorre todas as conexões
        # Pega novamente todos os usuários conectados
        aThreads = GetUserInfoArray()
        # Se ainda houver registros, aumenta a tentativa e espera 1 segundo
        if Len(aThreads) > 1:
            nTentativa += 1
            Sleep(1000)
            # Senão finaliza o laço de repetição
        else:
            break


    RestArea(aArea)
    return
