// caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2024/03/06/fazendo-backup-de-atalhos-e-restaurando-com-getkeys-e-restkeys-maratona-advpl-e-tl-276/
// Bibliotecas
#Include "TOTVS.ch"
// {Protheus.doc} User Function zExe277
// Retorna um array com a última query executada via Embedded
// @type  Function
// @author Atilio
// @since 21/02/2023
// @see https://tdn.totvs.com/display/public/framework/Embedded+SQL
// Função GetLastQuery
// Parâmetros
// Não possui parâmetros
// Retorno
// Retorna um array com as posições [1] Alias aberto; [2] Query executada; [3] Campos convertidos na query; [4] Se foi ou não utilizado ChangeQuery; [5] Tempo que demorou para executar
// **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
USER FUNCTION zExe277()
    LOCAL aArea, cTipos, cWhere, aQuery

    aArea := FWGetArea()
    cTipos := "PI;PA;"
    cWhere := "%B1_TIPO IN " + FormatIn(cTipos, ";") + " AND B1_LOCPAD = '01'%"
    aQuery := {  }
    // Construindo a consulta
    BeginSql Alias "SQL_SB1"
        COLUMN B1_UCOM AS DATE

        SELECT B1_COD , B1_DESC , B1_UCOM FROM % table : SB1 % SB1 WHERE B1_FILIAL = % xFilial : SB1 % AND B1_MSBLQL != '1' AND % Exp : cWhere % AND SB1 . % notDel %
    EndSql
    aQuery := GetLastQuery()
    RETURN

    RETURN Nil
