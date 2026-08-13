# Esse exemplo faz parte da série do YouTube, Maratona de Exemplos, do canal Terminal de Informação, 
#     caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2024/04/02/validando-se-o-programa-esta-rodando-no-sigamdi-com-a-ljismdi-maratona-advpl-e-tl-330/
# Bibliotecas
# PREPROCESSOR: #Include "Totvs.ch"
# {Protheus.doc} User Function zExe331
# Carrega um objeto em memória com uma imagem do repositório do Protheus
# @type Function
# @author Atilio
# @since 12/03/2023
# @see https://tdn.totvs.com/pages/releaseview.action?pageId=6815071
# @obs 
# 
#     Função LoadBitmap
#     Parâmetros
#         + uParam1    , Indefinido   , Compatibilidade
#         + cNome      , Caractere    , Nome da imagem no repositório
#     Retorno
#         + oObjeto    , Objeto       , Objeto com a imagem carregada
# 
#     Obs.: Apesar de em muitos lugares utilizarem a GetResources(), hoje não é mais necessário, sendo que essa
#     função foi até descontinuada (ela retorna sempre Nil)
# 
#     **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
def u_zExe331():
    aArea = FWGetArea()
    oImagem = None
    # Busca a imagem no repositório
    oImagem = LoadBitmap(None, 'BR_VERDE')
    FWRestArea(aArea)
    return
