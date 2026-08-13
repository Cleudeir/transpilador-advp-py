// caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2024/03/27/justificando-um-texto-com-a-justificatxt-maratona-advpl-e-tl-319/
// Bibliotecas
#Include "TOTVS.ch"
// {Protheus.doc} User Function zExe319
// Formata uma string justificando o texto
// @type Function
// @author Atilio
// @since 25/02/2023
// JustificaTXT
// Parâmetros
// Recebe a frase a ser formatada
// Recebe a quantidade de caracteres para formatação
// Recebe se deve pular a linha ao encontrar -enter- na frase
// Retorno
// Retorna um Array com as linhas formatadas
// **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
USER FUNCTION zExe319()
    LOCAL aArea, cFrase, aDados, cMensagem, nAtual

    aArea := FWGetArea()
    cFrase := "O rato roeu a roupa do Rei de roma, a rainha com raiva resolveu remendar. Num ninho de mafagafos, cinco mafagafinhos há! Quem os desmafagafizá-los, um bom desmafagafizador será."
    aDados := ""
    cMensagem := ""
    nAtual := 0
    // Justifica o texto
    aDados := JustificaTXT(cFrase, 30)
    // Percorre as linhas e monta a mensagem
    // Exibe a mensagem
    ShowLog(cMensagem)
    FWRestArea(aArea)
    RETURN
