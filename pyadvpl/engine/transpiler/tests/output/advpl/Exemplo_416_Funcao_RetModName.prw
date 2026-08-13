// caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2024/05/15/armazenando-as-respostas-de-parametros-em-um-array-com-a-retmvpar-maratona-advpl-e-tl-417/
// Bibliotecas
#Include "TOTVS.ch"
// {Protheus.doc} User Function zExe416
// Retorna os módulos do sistema
// @type Function
// @author Atilio
// @since 22/02/2023
// Função RetModName
// Parâmetros
// Define se é para listar também o Configurador (.T.) ou não (.F.)
// Retorno
// Retorna um array com todos os módulos do sistema
// **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
USER FUNCTION zExe416()
    LOCAL aArea, aModulos

    aArea := FWGetArea()
    aModulos := {  }
    // Busca o nome do módulo logado
    aModulos := RetModName(.T.)
    // Exibe uma mensagem de teste
    FWAlertInfo("Foi encontrado " + cValToChar(Len(aModulos)) + " modulo(s) ", "Teste RetModName")
    FWRestArea(aArea)
    RETURN
