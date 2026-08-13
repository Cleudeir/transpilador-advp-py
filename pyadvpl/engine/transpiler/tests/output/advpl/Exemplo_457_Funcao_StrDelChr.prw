// caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2024/06/04/removendo-caracteres-de-uma-string-atraves-da-strdelchr-maratona-advpl-e-tl-457/
// Bibliotecas
#Include "TOTVS.ch"
// {Protheus.doc} User Function zExe457
// Remove alguns caracteres de uma string
// @type Function
// @author Atilio
// @since 31/03/2023
// Função StrDelChr
// Parâmetros
// Recebe a string a ser analisada
// Recebe um array com os textos a serem removidos
// Retorno
// Retorna o texto formatado
// **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
USER FUNCTION zExe457()
    LOCAL aArea, cTexto, aRetirar, cNovo

    aArea := FWGetArea()
    cTexto := ""
    aRetirar := {  }
    cNovo := ""
    // Monta as informações e aciona a remoçaõ de caracteres
    cTexto := "A aranha arranha a rã. A rã arranha a aranha. Nem a aranha arranha a rã. Nem a rã arranha a aranha."
    aRetirar := { "a", "m", " " }
    cNovo := StrDelChr(cTexto, aRetirar)
    // Exibe a mensagem
    FWAlertInfo(cNovo, "Teste de StrDelChr")
    FWRestArea(aArea)
    RETURN
