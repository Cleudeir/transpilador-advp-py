// caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2024/01/16/validando-se-um-campo-existe-com-a-funcao-fieldpos-maratona-advpl-e-tl-177/
// Bibliotecas
#Include "TOTVS.ch"
// {Protheus.doc} User Function zExe177
// Valida se um campo existe na tabela
// @type Function
// @author Atilio
// @since 20/12/2022
// @see https://tdn.totvs.com/display/tec/FieldPos
// Função FieldPos
// Parâmetros
// + cField         , Caractere   , Nome do campo
// Retorno
// + nRet           , Numérico    , Retorna a posição do campo no dicionário caso exista
// **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
USER FUNCTION zExe177()
    LOCAL aArea

    aArea := FWGetArea()
    DbSelectArea("SB1")
    // Verifica se o campo existe
    If FieldPos("B1_X_CAMPO") > 0
        // Aqui da para fazer a customização caso o campo exista
    Else
        FWAlertError("Contate o Administrador do Sistema", "O campo [B1_X_CAMPO] não foi encontrado!")
    EndIf
    FWRestArea(aArea)
    RETURN
