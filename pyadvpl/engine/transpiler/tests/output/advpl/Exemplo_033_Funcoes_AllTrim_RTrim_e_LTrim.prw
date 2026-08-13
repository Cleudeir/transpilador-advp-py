// caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2023/09/10/funcoes-alltrim-rtrim-e-ltrim-para-remover-espacos-de-uma-expressao-maratona-advpl-e-tl-033/
// Bibliotecas
#Include "TOTVS.ch"
// {Protheus.doc} User Function zExe033
// Exemplo de função para tirar espaços de uma variável caractere com AllTrim, RTrim e LTrim
// @type Function
// @author Atilio
// @since 28/11/2022
// @see https://tdn.totvs.com/display/tec/AllTrim , https://tdn.totvs.com/display/tec/RTrim e https://tdn.totvs.com/display/tec/LTrim
// Função AllTrim
// Parâmetros
// + cText  , Caractere, Texto que terá os espaços a esquerda e direita removidos
// Retorno
// + cRet   , Caractere, Texto com os espaços removidos
// Função RTrim
// Parâmetros
// + cText  , Caractere, Texto que terá os espaços a direita removidos
// Retorno
// + cRet   , Caractere, Texto com os espaços removidos
// Função LTrim
// Parâmetros
// + cText  , Caractere, Texto que terá os espaços a esquerda removidos
// Retorno
// + cRet   , Caractere, Texto com os espaços removidos
// **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
USER FUNCTION zExe033()
    LOCAL aArea, cNome, cResult

    aArea := FWGetArea()
    cNome := Space(10) + "Daniel Atilio" + Space(10)
    cResult := ""
    // Demonstrando o conteúdo original
    cResult += "Original: '" + cNome + "'" + CRLF
    // Retirando espaços da direita e esquerda
    cResult += "AllTrim:  '" + AllTrim(cNome) + "'" + CRLF
    // Retirando apenas os espaços da direita
    cResult += "RTrim:    '" + RTrim(cNome) + "'" + CRLF
    // Retirando apenas os espaços da esquerda
    cResult += "LTrim:    '" + LTrim(cNome) + "'" + CRLF
    // Mostra o resultado das conversões
    ShowLog(cResult)
    FWRestArea(aArea)
    RETURN
