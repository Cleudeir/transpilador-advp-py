// caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2024/06/06/buscando-conteudos-de-tags-atraves-da-striptags-maratona-advpl-e-tl-460/
// Bibliotecas
#Include "TOTVS.ch"
// {Protheus.doc} User Function zExe460
// Realiza a busca de valores dentro de uma tag (XML)
// @type Function
// @author Atilio
// @since 31/03/2023
// Função StripTags
// Parâmetros
// Valor a ser Analisado
// Define se irá limpar valores antes de retornar
// Retorno
// Retorna a string encontrada dentro das tags
// **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
USER FUNCTION zExe460()
    LOCAL aArea, cOriginal, cNovo

    aArea := FWGetArea()
    cOriginal := ""
    cNovo := ""
    // Monta uma string com tags e depois remove e exibe
    cOriginal := "<nome>daniel atilio</nome>"
    cNovo := StripTags(cOriginal, .F.)
    FWAlertInfo("O resultado é: " + cNovo, "Teste StripTags")
    FWRestArea(aArea)
    RETURN
