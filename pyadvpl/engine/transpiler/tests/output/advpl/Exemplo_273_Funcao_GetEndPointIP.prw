// caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2024/03/04/convertendo-string-para-numerico-com-getdtoval-e-val-maratona-advpl-e-tl-272/
// Bibliotecas
#Include "TOTVS.ch"
// {Protheus.doc} User Function zExe273
// Retorna o IP e porta do AppServer que esta rodando a Thread
// @type  Function
// @author Atilio
// @since 21/02/2023
// Função GetEndPointIP
// Parâmetros
// Não possui parâmetros
// Retorno
// Retorna o IP e Porta da conexão
// **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
USER FUNCTION zExe273()
    LOCAL aArea, cMensagem

    aArea := FWGetArea()
    cMensagem := ""
    // Busca a informação e exibe
    cMensagem := "Os dados de conexão são: " + GetEndPointIP()
    FWAlertInfo(cMensagem, "Teste GetEndPointIP")
    FWRestArea(aArea)
    RETURN
