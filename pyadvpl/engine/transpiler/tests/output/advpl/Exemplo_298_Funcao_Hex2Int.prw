// caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2024/03/17/convertendo-hexa-para-decimal-com-a-hex2int-maratona-advpl-e-tl-298/
// Bibliotecas
#Include "TOTVS.ch"
// {Protheus.doc} User Function zExe298
// Faz a conversão de uma string com um valor hexadecimal para um valor numérico
// @type  Function
// @author Atilio
// @since 22/02/2023
// Função Hex2Int
// Parâmetros
// Recebe a string com o valor hexadecimal
// Retorno
// Retorna o valor numérico decimal
// **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
USER FUNCTION zExe298()
    LOCAL aArea, cHexa, nValor

    aArea := FWGetArea()
    cHexa := "4174696C696F"
    nValor := 0
    // Convertendo e mostrando o resultado (de hexa para numérico)
    nValor := Hex2Int(cHexa)
    FWAlertInfo("A conversão de '" + cHexa + "' deu o valor '" + cValToChar(nValor) + "' ", "Exemplo Hex2Int")
    FWRestArea(aArea)
    RETURN
