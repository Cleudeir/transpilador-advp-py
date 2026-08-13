// caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2023/11/14/validando-se-um-campo-esta-em-uso-pelo-sistema-com-a-funcao-cpousado-maratona-advpl-e-tl-098/
// Bibliotecas
#Include "TOTVS.ch"
// {Protheus.doc} User Function zExe098
// Verifica se um campo esta marcado como usado no Protheus
// @type Function
// @author Atilio
// @since 11/12/2022
// Função CpoUsado
// Parâmetros
// + Nome do campo
// Retorno
// + .T. se o campo estiver sendo usado ou .F. se não
// **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
USER FUNCTION zExe098()
    LOCAL aArea, cCampo

    aArea := FWGetArea()
    cCampo := "B1_SEGUM"
    // Testa se o campo é usado
    If CpoUsado(cCampo)
        FWAlertSuccess("O campo é usado", "Teste CpoUsado")
    Else
        FWAlertError("O campo não é usado", "Teste CpoUsado")
    EndIf
    FWRestArea(aArea)
    RETURN
