// caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2024/05/14/buscando-os-feriados-atraves-da-retferiados-maratona-advpl-e-tl-414/
// Bibliotecas
#Include "TOTVS.ch"
// {Protheus.doc} User Function zExe415
// Busca o código da entidade no TSS (se estiver configurado) conforme empresa e filial logadas
// @type Function
// @author Atilio
// @since 28/03/2023
// Função RetIdEnti
// Parâmetros
// Recebe se usa o TOTVS Colaboração (.T. ou .F.)
// Retorno
// Retorna o código da entidade caso o TSS esteja configurado
// **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
USER FUNCTION zExe415()
    LOCAL aArea, cIdent

    aArea := FWGetArea()
    cIdent := ""
    // Busca o código da entidade (no TSS) e exibe
    cIdent := RetIdEnti()
    FWAlertInfo("O código da Entidade é: " + cIdent, "Teste RetIdEnti")
    FWRestArea(aArea)
    RETURN
