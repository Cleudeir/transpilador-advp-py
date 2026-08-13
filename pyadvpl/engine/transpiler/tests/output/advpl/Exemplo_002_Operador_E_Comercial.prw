// caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2023/08/10/operador-de-macro-substituicao-maratona-advpl-e-tl-002/
// Bibliotecas
#Include "TOTVS.ch"
// {Protheus.doc} User Function zExe002
// Exemplo de como utilizar o operador & (E Comercial), para fazer uma macro execução / substituição
// @type Function
// @author Atilio
// @since 26/11/2022
// @see https://tdn.engpro.totvs.com.br/pages/viewpage.action?pageId=6063087
// @obs
// **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
USER FUNCTION zExe002()
    LOCAL aArea, nVar, cTeste, cProgr

    aArea := FWGetArea()
    nVar := 10
    cTeste := "'Aaaa' + 'Bbbb'"
    cProgr := "FWAlertInfo"
    // Mostrando o conteúdo da variável com macro execução
    FWAlertInfo(eval(cTeste), "& Apenas variável")
    // Executando uma função
    __macro_call__(cProgr, "Atilio Sistemas", "& Apenas programa")
    // Executando uma expressão inteira
    eval("FWAlertInfo('Mensagem de Teste', '& Expressão inteira')")
    FWRestArea(aArea)
    RETURN
