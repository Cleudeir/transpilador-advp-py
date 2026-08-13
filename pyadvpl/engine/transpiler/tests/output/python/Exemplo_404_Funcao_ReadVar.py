# Esse exemplo faz parte da série do YouTube, Maratona de Exemplos, do canal Terminal de Informação, 
#     caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2024/05/09/buscando-o-nome-do-campo-em-memoria-com-a-readvar-maratona-advpl-e-tl-404/
# Bibliotecas
# PREPROCESSOR: #Include "TOTVS.ch"
# {Protheus.doc} User Function zExe404
# Busca o nome do campo posicionado
# @type Function
# @author Atilio
# @since 28/03/2023
# @see https://tdn.totvs.com/pages/releaseview.action?pageId=24347037
# @obs 
#     Função ReadVar
#     Parâmetros
#         Função não tem parâmetros
#     Retorno
#         Retorna o nome do campo
# 
#     **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
def u_zExe404():
    aArea = FWGetArea()
    cCampo = ReadVar()
    xConteudo = eval(cCampo)
    # Mostra o nome do campo
    FWAlertInfo('O campo é ' + cCampo, 'Teste 1 ReadVar')
    # Mostra o conteúdo digitado no campo
    FWAlertInfo('O conteúdo é ' + cValToChar(xConteudo), 'Teste 2 ReadVar')
    FWRestArea(aArea)
    return

def u_MA010BUT():
    aArea = FWGetArea()
    aButtons = []
    # Adiciona um atalho no Shift+F5 para acionar o exemplo 404
    SetKey(K_SH_F5, lambda : u_zExe404())
    FWRestArea(aArea)
    return aButtons
