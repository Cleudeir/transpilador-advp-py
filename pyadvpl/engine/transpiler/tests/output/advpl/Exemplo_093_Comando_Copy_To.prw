// caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2023/11/09/copiando-dados-com-o-comando-copy-to-maratona-advpl-e-tl-093/
// Bibliotecas
#Include "TOTVS.ch"
// {Protheus.doc} User Function zExe093
// Exemplo para copiar dados de uma tabela para um arquivo
// @type Function
// @author Atilio
// @since 11/12/2022
// Também é possível mandar direto para uma porta de impressão, por exemplo:
// cTexto := "teste"
// MemoWrite("c:\teste\arquivo.txt", cTexto)
// Copy File "c:\teste\arquivo.txt" To LPT1
// **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
USER FUNCTION zExe093()
    LOCAL aArea, cPasta, cArquivo, cDelim

    aArea := FWGetArea()
    cPasta := GetTempPath()
    cArquivo := "produtos.txt"
    cDelim := ""
    DbSelectArea("SB1")
    SB1:DbSetOrder(1)
    // Filial + Código
    // Realiza a exportação
    Copy
    To(cPasta + cArquivo)
    DELIMITED
    WITH_(cDelim)
    // Abre o arquivo
    ShellExecute("OPEN", cArquivo, "", cPasta, 1)
    FWRestArea(aArea)
    RETURN
