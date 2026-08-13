# Esse exemplo faz parte da série do YouTube, Maratona de Exemplos, do canal Terminal de Informação, 
#     caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2023/10/10/emitindo-sons-com-as-funcoes-beep-e-tone-maratona-advpl-e-tl-063/
# Bibliotecas
# PREPROCESSOR: #Include "TOTVS.ch"
# {Protheus.doc} User Function zExe063
# Emite um sinal sonoro no computador
# @type Function
# @author Atilio
# @since 06/12/2022
# @see https://tdn.totvs.com/display/tec/Beep e https://tdn.totvs.com/display/tec/Tone
# @obs 
#     Função Beep
#     Retorno
#         + lSuccess   , Lógico     , .T. se conseguiu desparar o Beep ou .F. se não conseguiu
# 
#     Função Tone
#     Retorno
#         + lRetorno   , Lógico     , .T. se conseguiu desparar o som ou .F. se não conseguiu
# 
#     **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
def u_zExe063():
    aArea = FWGetArea()
    # Emite um som (dependendo da placa mãe)
    if Beep():
        FWAlertSuccess('Conseguiu disparar o som', 'Exemplo Beep')

    # Emite um som (dependendo da placa mãe)
    if Tone():
        FWAlertSuccess('Conseguiu disparar o som', 'Exemplo Tone')

    FWRestArea(aArea)
    return
