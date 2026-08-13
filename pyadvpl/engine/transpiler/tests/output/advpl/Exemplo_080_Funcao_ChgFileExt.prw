// caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2023/10/27/mudando-a-extensao-do-nome-de-um-arquivo-com-a-funcao-chgfileext-maratona-advpl-e-tl-080/
// Bibliotecas
#Include "TOTVS.ch"
// {Protheus.doc} User Function zExe080
// Exemplo de como alterar a extensão de um arquivo
// @type Function
// @author Atilio
// @since 08/12/2022
// Função ChgFileExt
// Parâmetros
// + Filename     , Caractere    , Nome do arquivo original
// + Extension    , Caractere    , Nova extensão do arquivo
// Retorno
// + Filename     , Caractere    , Nome que será do novo arquivo
// **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
USER FUNCTION zExe080()
    LOCAL aArea, cArqOrig, cNovExten, cArqNovo

    aArea := FWGetArea()
    cArqOrig := "C:\spool\tst.txt"
    cNovExten := ".log"
    cArqNovo := Nil
    // Verificando como vai ser o novo nome do arquivo
    cArqNovo := ChgFileExt(cArqOrig, cNovExten)
    // Cria o arquivo novo com o conteúdo do antigo
    MemoWrite(cArqNovo, MemoRead(cArqOrig))
    // Exibe a mensagem
    FWAlertSuccess("Arquivo novo: " + cArqNovo, "Exemplo de ChgFileExt")
    FWRestArea(aArea)
    RETURN
