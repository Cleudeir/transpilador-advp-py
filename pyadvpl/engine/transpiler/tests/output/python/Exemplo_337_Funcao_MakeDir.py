# Esse exemplo faz parte da série do YouTube, Maratona de Exemplos, do canal Terminal de Informação, 
#     caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2024/04/05/criando-pastas-com-a-makedir-maratona-advpl-e-tl-337/
# Bibliotecas
# PREPROCESSOR: #Include "Totvs.ch"
# {Protheus.doc} User Function zExe337
# Cria uma pasta no Sistema Operacional ou a partir da Protheus Data
# @type Function
# @author Atilio
# @since 12/03/2023
# @see https://tdn.totvs.com/display/tec/MakeDir
# @obs 
# 
#     Função MakeDir
#     Parâmetros
#         + cPath       , Caractere  , Nome da pasta que será criada
#         + uParam2     , Indefinido , Compatibilidade
#         + lChangeCase , Lógico     , Se .T. será convertido tudo para minúsculo senão se .F. será mantido conforme informado o cPath
#     Retorno
#         + nRet        , Numérico   , Retorna 0 em caso de sucesso
# 
#     **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
def u_zExe337():
    aArea = FWGetArea()
    cPastaSO = 'C:\\spool\\'
    cPastaInt = '\\x_teste\\'
    # Teste 1 verificando a pasta no S.O.
    if not ExistDir(cPastaSO):
        MakeDir(cPastaSO)
        FWAlertSuccess("Pasta '" + cPastaSO + "' criada", 'Teste 1 Pasta S.O. - MakeDir')
    else:
        FWAlertInfo("Pasta '" + cPastaSO + "' já existe", 'Teste 1 Pasta S.O. - MakeDir')

    # Teste 2 verificando a pasta na Protheus Data
    if not ExistDir(cPastaInt):
        MakeDir(cPastaInt)
        FWAlertSuccess("Pasta '" + cPastaInt + "' criada", 'Teste 2 Pasta Interna - MakeDir')
    else:
        FWAlertInfo("Pasta '" + cPastaInt + "' já existe na Protheus Data", 'Teste 2 Pasta Interna - MakeDir')

    FWRestArea(aArea)
    return
