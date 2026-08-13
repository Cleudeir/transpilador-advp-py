# Esse exemplo faz parte da série do YouTube, Maratona de Exemplos, do canal Terminal de Informação, 
#     caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2024/01/11/retornando-o-nome-da-pasta-de-um-arquivo-com-a-extractpath-maratona-advpl-e-tl-167/
# Bibliotecas
# PREPROCESSOR: #Include "TOTVS.ch"
# {Protheus.doc} User Function zExe167
# Função que retorna apenas a pasta de um arquivo
# @type Function
# @author Atilio
# @since 19/12/2022
# @obs 
#     Função ExtractPath
#     Parâmetros
#         + Nome do arquivo completo
#     Retorno
#         + Apenas a pasta
# 
#     **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
def u_zExe167():
    aArea = FWGetArea()
    cArquivo = ''
    cPasta = ''
    # Descobrindo a extensão do arquivo
    cArquivo = 'C:\\spool\\relatorio.pdf'
    cPasta = ExtractPath(cArquivo)
    # Exibindo uma mensagem
    FWAlertInfo("O arquivo '" + cArquivo + "' esta na pasta '" + cPasta + "'", 'Teste com ExtractPath')
    FWRestArea(aArea)
    return
