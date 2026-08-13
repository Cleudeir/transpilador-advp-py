# Esse exemplo faz parte da série do YouTube, Maratona de Exemplos, do canal Terminal de Informação, 
#     caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2023/11/09/copiando-dados-com-o-comando-copy-to-maratona-advpl-e-tl-093/
# Bibliotecas
# PREPROCESSOR: #Include "TOTVS.ch"
# {Protheus.doc} User Function zExe093
# Exemplo para copiar dados de uma tabela para um arquivo
# @type Function
# @author Atilio
# @since 11/12/2022
# @obs 
#     Também é possível mandar direto para uma porta de impressão, por exemplo:
#     cTexto := "teste"
#     MemoWrite("c:\teste\arquivo.txt", cTexto)
#     Copy File "c:\teste\arquivo.txt" To LPT1
# 
#     **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
def u_zExe093():
    aArea = FWGetArea()
    cPasta = GetTempPath()
    cArquivo = 'produtos.txt'
    cDelim = ''
    DbSelectArea('SB1')
    SB1.DbSetOrder(1)
    # Filial + Código
    # Realiza a exportação
    Copy
    To(cPasta + cArquivo)
    DELIMITED
    WITH_(cDelim)
    # Abre o arquivo
    ShellExecute('OPEN', cArquivo, '', cPasta, 1)
    FWRestArea(aArea)
    return
