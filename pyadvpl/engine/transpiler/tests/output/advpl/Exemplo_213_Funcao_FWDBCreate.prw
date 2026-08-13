// caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2024/02/03/criando-uma-tabela-no-banco-com-a-fwdbcreate-maratona-advpl-e-tl-213/
// Bibliotecas
#Include "TOTVS.ch"
// {Protheus.doc} User Function zExe213
// Exemplo de função que cria uma tabela no banco de dados
// @type Function
// @author Atilio
// @since 20/02/2023
// @see https://tdn.totvs.com/display/public/framework/FWDBCreate
// Função FWDBCreate
// Parâmetros
// + cName         , Caractere , Nome da tabela que será criada
// + aStruct       , Array     , Array com a estrutura de campos (posições: [1] nome do campo; [2] tipo do campo; [3] tamanho do campo; [4] decimais do campo)
// + cDriver       , Caractere , Driver utilizado na criação da tabela
// + lRecnoAutoInc , Lógico    , .T. se define que usará RecNo com auto incremento
// Retorno
// Função não tem retorno
// **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
USER FUNCTION zExe213()
    LOCAL aArea, cTableTmp, aStruct

    aArea := FWGetArea()
    cTableTmp := "PRODTMP"
    aStruct := {  }
    // Define os campos que terão na tabela
    aAdd(aStruct, { "CODIGO", "C", 6, 0 })
    aAdd(aStruct, { "NOME", "C", 50, 0 })
    // Aciona a criação da tabela no Banco de Dados
    FWDBCreate(cTableTmp, aStruct, "TOPCONN", .T.)
    FWRestArea(aArea)
    RETURN
