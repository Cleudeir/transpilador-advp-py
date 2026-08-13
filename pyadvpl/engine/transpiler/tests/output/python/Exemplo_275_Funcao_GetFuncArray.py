# Esse exemplo faz parte da série do YouTube, Maratona de Exemplos, do canal Terminal de Informação, 
#     caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2024/03/05/buscando-o-nome-do-ambiente-com-a-getenvserver-maratona-advpl-e-tl-274/
# Bibliotecas
# PREPROCESSOR: #Include "TOTVS.ch"
# {Protheus.doc} User Function zExe275
# Busca informações de uma função (ou de várias dependendo da máscara)
# @type  Function
# @author Atilio
# @since 21/02/2023
# @see https://tdn.totvs.com/display/tec/GetFuncArray
# @obs 
# 
#     Função GetFuncArray
#     Parâmetros
#         + cMascara  , Caractere    , Nome da máscara de pesquisa
#         + aTipo     , Array        , Tipos de arquivos
#         + aArquivo  , Array        , Nome dos arquivos
#         + aLinha    , Array        , Linha da compilação das funções
#         + aData     , Array        , Data da modificação dos arquivos
#         + aHora     , Array        , Hora da modificação dos arquivos
#     Retorno
#         + aScr      , Array        , Retorna um array que contém o nome das funções
#     
#     **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
def u_zExe275():
    aArea = FWGetArea()
    cFuncao = 'MATA???'
    cTexto = ''
    nAtual = 0
    aRet = []
    aType = []
    aFile = []
    aLine = []
    aDate = []
    aTime = []
    # Busca as informações da função
    aRet = GetFuncArray(cFuncao, ref_(aType), ref_(aFile), ref_(aLine), ref_(aDate), ref_(aTime))
    # Exibe o que encontrou
    ShowLog(cTexto)
    FWRestArea(aArea)
    return
