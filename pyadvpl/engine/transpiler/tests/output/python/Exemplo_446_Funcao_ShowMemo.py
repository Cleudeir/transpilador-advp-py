# Esse exemplo faz parte da série do YouTube, Maratona de Exemplos, do canal Terminal de Informação, 
#     caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2024/05/30/abrindo-um-arquivo-texto-com-a-showmemo-maratona-advpl-e-tl-446/
# Bibliotecas
# PREPROCESSOR: #Include "TOTVS.ch"
# {Protheus.doc} User Function zExe446
# Abre uma tela para visualização de arquivo texto
# @type Function
# @author Atilio
# @since 31/03/2023
# @obs 
#     Função ShowMemo
#     Parâmetros
#         Recebe o nome do arquivo que será aberto
#     Retorno
#         Função não tem retorno
# 
#     **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
def u_zExe446():
    aArea = FWGetArea()
    cArquivo = ''
    # Define o nome do arquivo, e abre ele em tela
    cArquivo = 'C:\\spool\\curso\\log_produtos.txt'
    ShowMemo(cArquivo)
    FWRestArea(aArea)
    return
