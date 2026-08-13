// caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2024/01/07/validando-se-uma-pasta-existe-com-a-funcao-existdir-maratona-advpl-e-tl-159/
// Bibliotecas
#Include "TOTVS.ch"
// {Protheus.doc} User Function zExe159
// Verifica se uma pasta existe
// @type Function
// @author Atilio
// @since 18/12/2022
// @see https://tdn.totvs.com/display/tec/ExistDir
// Função ExistCpo
// Parâmetros
// + cPath        , Caractere   , Nome da pasta a ser validada
// + uParam2      , Indefinido  , Compatibilidade
// + lChangeCase  , Lógico      , Se .T. tudo será convertido para minúsculo senão se .F. mantém a informação original
// Retorno
// + lRet         , Lógico      , .T. Se a pasta existir ou .F. se ela não existir
// **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
USER FUNCTION zExe159()
    LOCAL aArea, cPastaSO, cPastaInt

    aArea := FWGetArea()
    cPastaSO := "C:\spool\"
    cPastaInt := "\x_teste\"
    // Teste 1 verificando a pasta no S.O.
    If .NOT. ExistDir(cPastaSO)
        MakeDir(cPastaSO)
        FWAlertSuccess("Pasta '" + cPastaSO + "' criada", "Teste 1 Pasta S.O. - ExistDir")
    Else
        FWAlertInfo("Pasta '" + cPastaSO + "' já existe", "Teste 1 Pasta S.O. - ExistDir")
    EndIf
    // Teste 2 verificando a pasta na Protheus Data
    If .NOT. ExistDir(cPastaInt)
        MakeDir(cPastaInt)
        FWAlertSuccess("Pasta '" + cPastaInt + "' criada", "Teste 2 Pasta Interna - ExistDir")
    Else
        FWAlertInfo("Pasta '" + cPastaInt + "' já existe na Protheus Data", "Teste 2 Pasta Interna - ExistDir")
    EndIf
    FWRestArea(aArea)
    RETURN
