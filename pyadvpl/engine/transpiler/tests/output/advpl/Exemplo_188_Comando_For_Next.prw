// caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2024/01/22/fazendo-um-laco-de-repeticao-com-for-next-maratona-advpl-e-tl-188/
// Bibliotecas
#Include "TOTVS.ch"
// {Protheus.doc} User Function zExe188
// Faz um laço de repetição de um valor até outro
// @type Function
// @author Atilio
// @since 21/12/2022
// @see https://tdn.totvs.com/display/public/framework/FOR+...+NEXT
// **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
USER FUNCTION zExe188()
    LOCAL aArea, nAtual, aNomes, cPares, cMsg

    aArea := FWGetArea()
    nAtual := 0
    aNomes := {  }
    cPares := ""
    cMsg := ""
    // Percorrendo de 1 a 10
    // Adicionando nomes no array
    aAdd(aNomes, "Daniel")
    aAdd(aNomes, "Atilio")
    aAdd(aNomes, "Terminal de Informação")
    // Percorrendo o array de nomes
    FWAlertInfo("Pares: " + cPares + CRLF + "Nomes: " + cMsg, "Teste de For ... Next")
    FWRestArea(aArea)
    RETURN
