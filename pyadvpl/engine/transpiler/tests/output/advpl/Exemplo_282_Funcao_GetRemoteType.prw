// caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2024/03/09/buscando-conteudos-dentro-do-rpo-com-a-getresarray-maratona-advpl-e-tl-283/
// Bibliotecas
#Include "TOTVS.ch"
// {Protheus.doc} User Function zExe282
// Retorna o tipo de estação que esta executando o Protheus
// @type  Function
// @author Atilio
// @since 21/02/2023
// @see https://tdn.totvs.com/display/tec/GetRemoteType
// Função GetRemoteType
// Parâmetros
// + cLibVersion , Caractere   , Busca a versão da LIB usada por referência
// Retorno
// + nRet        , Numérico    , Retorna em qual sistema esta executando a rotina
// **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
USER FUNCTION zExe282()
    LOCAL aArea, cMensagem, cLibUsada, nTipo

    aArea := FWGetArea()
    cMensagem := ""
    cLibUsada := ""
    nTipo := 0
    // Busca as informações sobre o remote
    nTipo := GetRemoteType(@ cLibUsada)
    // Monta a mensagem a ser exibida
    If nTipo = - 1
        cMensagem += "Job, Web ou Sem Remote"
    ElseIf nTipo = 1
        cMensagem += "Windows"
    ElseIf nTipo = 2
        cMensagem += "Linux / Unix-Like"
    EndIf
    cMensagem += " - " + cLibUsada
    // Exibe uma mensagem com os programas
    FWAlertInfo(cMensagem, "Teste GetRemoteType")
    FWRestArea(aArea)
    RETURN
