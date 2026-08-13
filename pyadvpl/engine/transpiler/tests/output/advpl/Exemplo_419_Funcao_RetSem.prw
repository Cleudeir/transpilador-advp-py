// caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2024/05/16/buscando-o-numero-da-semana-com-a-retsem-maratona-advpl-e-tl-419/
// Bibliotecas
#Include "TOTVS.ch"
// {Protheus.doc} User Function zExe419
// Retorna o número da semana do ano conforme uma data
// @type Function
// @author Atilio
// @since 22/02/2023
// Função RetSegunda
// Parâmetros
// Recebe uma data de referência
// Retorno
// Retorna o número da semana conforme a data passada
// **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
USER FUNCTION zExe419()
    LOCAL aArea, dDataRef, nSemana

    aArea := FWGetArea()
    dDataRef := Date()
    nSemana := Nil
    // Busca a semana da data de referência
    nSemana := RetSem(dDataRef)
    // Exibe uma mensagem
    FWAlertInfo("Para a data '" + dToC(dDataRef) + "', é a semana '" + cValToChar(nSemana) + "' do ano", "Teste RetSem")
    FWRestArea(aArea)
    RETURN
