# Esse exemplo faz parte da série do YouTube, Maratona de Exemplos, do canal Terminal de Informação, 
#     caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2024/02/28/buscando-varias-informacoes-de-uma-tabela-com-getadvfval-maratona-advpl-e-tl-263/
# Bibliotecas
# PREPROCESSOR: #Include "TOTVS.ch"
# {Protheus.doc} User Function zExe262
# Funções para manipular as grids e atualizar objetos na tela
# @type  Function
# @author Atilio
# @since 21/02/2023
# @obs 
# 
#     Função GDDeleted
#     Parâmetros
#         + Número da linha do aCols
#         + aHeader para validação (caso a tela tenha mais de uma grid)
#         + aCols para validação (caso a tela tenha mais de uma grid)
#     Retorno
#         Retorna .T. se a linha esta apagada ou .F. se não
# 
#     Função GDFieldGet
#     Parâmetros
#         + Nome do campo
#         + Número da linha do aCols
#         + Se .T. busca conteúdo na memória senão se .F. busca do aCols (padrão é .F.)
#         + aHeader para validação (caso a tela tenha mais de uma grid)
#         + aCols para validação (caso a tela tenha mais de uma grid)
#     Retorno
#         Retorna o valor do campo digitado na grid
# 
#     Função GDFieldPos
#     Parâmetros
#         + Nome do campo
#         + aHeader para validação (caso a tela tenha mais de uma grid)
#     Retorno
#         Retorna o número da coluna encontrada na grid
# 
#     Função GDFieldPut
#     Parâmetros
#         + Nome do campo
#         + Conteúdo que será atribuído ao campo
#         + Número da linha do aCols
#         + aHeader para validação (caso a tela tenha mais de uma grid)
#         + aCols para validação (caso a tela tenha mais de uma grid)
#         + Define se irá buscar o valor da memória (.T.) ou do aCols (.F.)
#     Retorno
#         Retorna o valor antes da atribuição
# 
#     GetDRefresh
#     Função não tem parâmetros nem retorno
#     
#     **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
def u_zExe262():
    aArea = FWGetArea()
    nLinha = 1
    nPosDatEnt = GDFieldPos('C6_ENTREG')
    cMensagem = ''
    # Se a pergunta for confirmada
    if FWAlertYesNo('Confirma a alteração da Data de Entrega para Hoje (coluna ' + cValToChar(nPosDatEnt) + ')?', 'Continua'):
        # Percorre as linhas digitadas na grida
        # Se tiver mensagem, exibe em tela
        if not Empty(cMensagem):
            ShowLog(cMensagem)

        # Atualiza a tela
        GetDRefresh()

    FWRestArea(aArea)
    return

def u_A410CONS():
    aArea = FWGetArea()
    aBotoes = []
    aAdd(aBotoes, ['DBG07', lambda : u_zExe262(), '* Atualizar Data de Entrega', '* Entrega'])
    FWRestArea(aArea)
    return aBotoes
