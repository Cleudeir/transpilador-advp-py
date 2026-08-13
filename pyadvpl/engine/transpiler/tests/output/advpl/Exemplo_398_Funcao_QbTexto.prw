// caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2024/05/06/exibindo-mensagens-no-console-log-com-a-qout-maratona-advpl-e-tl-399/
// Bibliotecas
#Include "TOTVS.ch"
// {Protheus.doc} User Function zExe398
// Quebra uma string em um array até encontrar o caractere, ou até dar o tamanho estipulado
// @type Function
// @author Atilio
// @since 28/03/2023
// Função QbTexto
// Parâmetros
// Frase que será verificada
// Tamanho de caracteres por linha do array
// Caractere que será considerado para a quebra
// Retorno
// O array formatado
// **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
USER FUNCTION zExe398()
    LOCAL aArea, cFrase, nTamanho, aDados

    aArea := FWGetArea()
    cFrase := "A aranha arranha a rã. A rã arranha a aranha. Nem a aranha arranha a rã. Nem a rã arranha a aranha."
    nTamanho := 30
    aDados := {  }
    // Quebra a frase em um array com tamanho delimitado
    aDados := QbTexto(cFrase, nTamanho, ".")
    FWAlertInfo("A frase deu " + cValToChar(Len(aDados)) + " linhas", "Teste QbTexto")
    FWRestArea(aArea)
    RETURN
