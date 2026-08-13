// caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2024/03/13/separando-informacoes-de-um-telefone-com-gettel-fisgettel-e-nfegettel-maratona-advpl-e-tl-290/
// Bibliotecas
#Include "TOTVS.ch"
// {Protheus.doc} User Function zExe291
// Busca a pasta temporária para usar no sistema
// @type  Function
// @author Atilio
// @since 21/02/2023
// @see https://tdn.totvs.com/display/tec/GetTempPath
// Função GetTempPath
// Parâmetros
// + lLocal     , Lógico        , Indica se retorna o diretório padrão onde roda o smartclient (.T.) ou appserver (.F.)
// + lWeb       , Lógico        , Retorna o diretório web temporário (para caso de rodar em navegador)
// Retorno
// + cRet       , Caractere     , Retorna o caminho da pasta temporária
// **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
USER FUNCTION zExe291()
    LOCAL aArea, cPasta

    aArea := FWGetArea()
    cPasta := Nil
    // Busca as informações do campo
    cPasta := GetTempPath()
    FWAlertInfo("A pasta é: " + cPasta, "Teste 1 GetTempPath")
    // Busca as informações do campo
    cPasta := GetTempPath(.F.)
    FWAlertInfo("A pasta é: " + cPasta, "Teste 2 GetTempPath")
    FWRestArea(aArea)
    RETURN
