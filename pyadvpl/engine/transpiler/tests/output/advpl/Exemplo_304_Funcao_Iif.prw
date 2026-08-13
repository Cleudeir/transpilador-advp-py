// caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2024/03/20/fazendo-um-teste-condicional-com-iif-maratona-advpl-e-tl-304/
// Bibliotecas
#Include "Totvs.ch"
// {Protheus.doc} zExe304
// Exemplo de estrutura de condicao com Iif
// @type  Function
// @author Atilio
// @since 22/02/2023
// @see https://tdn.totvs.com/display/tec/iif
// Função Iif
// Parâmetros
// Expressão que será testada (tem que dar .T. ou .F.)
// Valor que será retornado se a expressão der .T.
// Valor que será retornado se a expressão der .F.
// Retorno
// Valor que será retornado depende da expressão passada
// **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
USER FUNCTION zExe304()
    LOCAL aArea, nMesAtu, nMesAniv, cMsg

    aArea := FWGetArea()
    nMesAtu := Month(Date())
    nMesAniv := 7
    cMsg := ""
    cMsg := Nil
    FWAlertInfo(cMsg, "Teste de Iif")
    // If nMesAtu == nMesAniv
    // cMsg := "ANIVERSARIANTE"
    // Else
    // cMsg := "AINDA NAO"
    // EndIf
    // nValor := Iif(A == B, Iif(B == C, 7, Iif(C == D, 4, 9)), 3)
    // If A == B
    // If B == C
    // nValor := 7
    // Else
    // If C == D
    // nValor := 4
    // Else
    // nValor := 9
    // EndIf
    // EndIf
    // Else
    // nValor := 3
    // EndIf
    FWRestArea(aArea)
    RETURN
