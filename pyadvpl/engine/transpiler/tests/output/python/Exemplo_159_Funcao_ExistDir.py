# Esse exemplo faz parte da série do YouTube, Maratona de Exemplos, do canal Terminal de Informação, 
#     caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2024/01/07/validando-se-uma-pasta-existe-com-a-funcao-existdir-maratona-advpl-e-tl-159/
# Bibliotecas
# PREPROCESSOR: #Include "TOTVS.ch"
# {Protheus.doc} User Function zExe159
# Verifica se uma pasta existe
# @type Function
# @author Atilio
# @since 18/12/2022
# @see https://tdn.totvs.com/display/tec/ExistDir
# @obs 
#     Função ExistCpo
#     Parâmetros
#         + cPath        , Caractere   , Nome da pasta a ser validada
#         + uParam2      , Indefinido  , Compatibilidade
#         + lChangeCase  , Lógico      , Se .T. tudo será convertido para minúsculo senão se .F. mantém a informação original
#     Retorno
#         + lRet         , Lógico      , .T. Se a pasta existir ou .F. se ela não existir
# 
#     **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
def u_zExe159():
    aArea = FWGetArea()
    cPastaSO = 'C:\\spool\\'
    cPastaInt = '\\x_teste\\'
    # Teste 1 verificando a pasta no S.O.
    if not ExistDir(cPastaSO):
        MakeDir(cPastaSO)
        FWAlertSuccess("Pasta '" + cPastaSO + "' criada", 'Teste 1 Pasta S.O. - ExistDir')
    else:
        FWAlertInfo("Pasta '" + cPastaSO + "' já existe", 'Teste 1 Pasta S.O. - ExistDir')

    # Teste 2 verificando a pasta na Protheus Data
    if not ExistDir(cPastaInt):
        MakeDir(cPastaInt)
        FWAlertSuccess("Pasta '" + cPastaInt + "' criada", 'Teste 2 Pasta Interna - ExistDir')
    else:
        FWAlertInfo("Pasta '" + cPastaInt + "' já existe na Protheus Data", 'Teste 2 Pasta Interna - ExistDir')

    FWRestArea(aArea)
    return
