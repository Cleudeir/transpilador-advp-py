# Esse exemplo faz parte da série do YouTube, Maratona de Exemplos, do canal Terminal de Informação, 
#     caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2024/03/31/validando-se-uma-linha-esta-apagada-numa-grid-com-a-lindelet-maratona-advpl-e-tl-327/
# Bibliotecas
# PREPROCESSOR: #Include "TOTVS.ch"
# {Protheus.doc} User Function zExe327
# Função que verifica se a linha esta apagada
# @type  Function
# @author Atilio
# @since 12/03/2023
# @obs 
# 
#     Função LinDelet
#     Parâmetros
#         Recebe um array com a linha atual
#     Retorno
#         Retorna .T. se a linha esta apagada ou .F. se não
#     
#     **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
def u_zExe327():
    aArea = FWGetArea()
    nLinha = 1
    cApagadas = ''
    # Se a pergunta for confirmada
    if FWAlertYesNo('Deseja validar todas as linhas?', 'Continua'):
        # Percorre as linhas digitadas na grid
        # Se a variavel estiver vazia, apenas mostra mensagem, senão mostra quais foram as linhas
        if Empty(cApagadas):
            FWAlertSuccess('Não há linha(s) apagada(s)', 'Sucesso')
        else:
            FWAlertError(cApagadas, 'Linhas Excluidas')


    FWRestArea(aArea)
    return

def u_A410CONS():
    aArea = FWGetArea()
    aBotoes = []
    aAdd(aBotoes, ['DBG07', lambda : u_zExe327(), '* Ver Linhas Apagadas', '* Apagadas'])
    FWRestArea(aArea)
    return aBotoes
