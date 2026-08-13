// caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2023/10/11/tratando-execucoes-e-erros-com-begin-sequence-end-maratona-advpl-e-tl-064/
// Bibliotecas
#Include "TOTVS.ch"
// {Protheus.doc} User Function zExe064
// Exemplo de como realizar tratativas e recuperar caso haja falhas
// @type Function
// @author Atilio
// @since 06/12/2022
// @see https://tdn.totvs.com/display/public/framework/BEGIN+SEQUENCE+...+END
// **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
USER FUNCTION zExe064()
    LOCAL aArea, cError, bError, nVar, cVar, nVariavel

    aArea := FWGetArea()
    cError := ""
    bError := ErrorBlock(Nil)
    nVar := 1
    cVar := "A"
    // Inicio a utilização da tentativa
    BEGIN SEQUENCE
        nVariavel := nVar + cVar
    END SEQUENCE
    // Restaurando bloco de erro do sistema
    ErrorBlock(bError)
    // Se houve erro, será mostrado ao usuário
    If .NOT. Empty(cError)
        FWAlertError("Houve um erro na fórmula digitada: " + CRLF + CRLF + cError, "Teste com Begin Sequence")
    EndIf
    FWRestArea(aArea)
    RETURN
