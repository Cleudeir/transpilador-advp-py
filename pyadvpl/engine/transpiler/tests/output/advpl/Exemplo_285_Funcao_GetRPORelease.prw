// caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2024/03/10/buscando-informacoes-de-onde-esta-rodando-o-smartclient-com-getrmtinfo-maratona-advpl-e-tl-284/
// Bibliotecas
#Include "TOTVS.ch"
// {Protheus.doc} User Function zExe285
// Retorna a versão do Repositório de Objetos
// @type  Function
// @author Atilio
// @since 21/02/2023
// Função GetRPORelease
// Parâmetros
// Não possui parâmetros
// Retorno
// Retorna a versão
// **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
USER FUNCTION zExe285()
    LOCAL aArea, cMensagem

    aArea := FWGetArea()
    cMensagem := ""
    // Busca a informação e exibe
    cMensagem := "A versão do RPO é: " + GetRPORelease()
    FWAlertInfo(cMensagem, "Teste GetRPORelease")
    FWRestArea(aArea)
    RETURN
