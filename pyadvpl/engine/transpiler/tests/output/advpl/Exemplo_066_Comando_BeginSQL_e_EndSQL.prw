// caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2023/10/13/executando-queries-com-os-comandos-beginsql-e-endsql-maratona-advpl-e-tl-066/
// Bibliotecas
#Include "TOTVS.ch"
// {Protheus.doc} User Function zExe066
// Exemplo de como fazer queries com linguagem nativa em AdvPL
// @type Function
// @author Atilio
// @since 06/12/2022
// @see https://tdn.totvs.com/display/public/framework/Embedded+SQL
// **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
USER FUNCTION zExe066()
    LOCAL aArea, cTipos, cWhere, nRegs

    aArea := FWGetArea()
    cTipos := "PI;PA;"
    cWhere := "%B1_TIPO IN " + FormatIn(cTipos, ";") + " AND B1_LOCPAD = '01'%"
    nRegs := 0
    // Construindo a consulta
    BeginSql Alias "SQL_SB1"
        COLUMN B1_UCOM AS DATE

        SELECT B1_COD , B1_DESC , B1_UCOM FROM % table : SB1 % SB1 WHERE B1_FILIAL = % xFilial : SB1 % AND B1_MSBLQL != '1' AND % Exp : cWhere % AND SB1 . % notDel %
    EndSql
    While .NOT. SQL_SB1->( DbEof() )
        nRegs += 1
        SQL_SB1:DbSkip()
    EndDo
    RETURN

    RETURN Nil
