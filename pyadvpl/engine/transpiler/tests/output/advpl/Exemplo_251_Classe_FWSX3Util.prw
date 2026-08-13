// caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2024/02/22/buscando-informacoes-dos-campos-atraves-da-fwsx3util-maratona-advpl-e-tl-251/
// Bibliotecas
#Include "TOTVS.ch"
// {Protheus.doc} User Function zExe251
// Classe para buscar informações da SX3 (Campos)
// @type  Function
// @author Atilio
// @since 21/02/2023
// @see https://tdn.totvs.com/display/public/framework/FWSX3Util
// **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
USER FUNCTION zExe251()
    LOCAL aArea, aDados

    aArea := FWGetArea()
    aDados := {  }
    // Busca todos os campos da tabela de produtos
    aDados := FwSX3Util():GetAllFields("SB1")
    // Exibe uma mensagem
    FWAlertInfo("Foi encontrado " + cValToChar(Len(aDados)) + " campo(s)", "Teste FWSX3Util")
    FWRestArea(aArea)
    RETURN
