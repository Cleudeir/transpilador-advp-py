# Esse exemplo faz parte da série do YouTube, Maratona de Exemplos, do canal Terminal de Informação, 
#     caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2023/10/13/executando-queries-com-os-comandos-beginsql-e-endsql-maratona-advpl-e-tl-066/
# Bibliotecas
# PREPROCESSOR: #Include "TOTVS.ch"
# {Protheus.doc} User Function zExe066
# Exemplo de como fazer queries com linguagem nativa em AdvPL
# @type Function
# @author Atilio
# @since 06/12/2022
# @see https://tdn.totvs.com/display/public/framework/Embedded+SQL
# @obs 
# 
#     **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
def u_zExe066():
    aArea = FWGetArea()
    cTipos = 'PI;PA;'
    cWhere = '%B1_TIPO IN ' + FormatIn(cTipos, ';') + " AND B1_LOCPAD = '01'%"
    nRegs = 0
    # Construindo a consulta
    with BeginSQL(alias="SQL_SB1") as sql:
        sql.column("B1_UCOM", "DATE")
        sql.query("""SELECT B1_COD , B1_DESC , B1_UCOM FROM % table : SB1 % SB1 WHERE B1_FILIAL = % xFilial : SB1 % AND B1_MSBLQL != '1' AND % Exp : cWhere % AND SB1 . % notDel %""")
        # Enquanto houver registros
        while not SQL_SB1.EoF():
            nRegs += 1
            SQL_SB1.DbSkip()

        SQL_SB1.DbCloseArea()
        FWAlertInfo('Foram processados ' + cValToChar(nRegs) + ' produtos.', 'Atenção')
        FWRestArea(aArea)
        return

