# PREPROCESSOR: #Include "TOTVS.ch"
# {Protheus.doc} zEx902
# Exemplo complexo de FWBrowse
# @author Antigravity
# @since 13/05/2026
def u_zEx902():
    oBrowse = None
    aArea = FWGetArea()
    # Abre Ã¡rea de trabalho
    DbUseArea(True, 'TOPCONN', 'SA1', 'SA1', True, False)
    oBrowse = FWBrowse().New()
    oBrowse.SetAlias('SA1')
    oBrowse.SetQuery("SELECT * FROM SA1 WHERE A1_NOME LIKE '%TESTE%'")
    # Adiciona colunas
    oBrowse.AddColumn('CÃ³digo', lambda o: SA1.A1_COD, 'C', 6, 0)
    oBrowse.AddColumn('Nome', lambda o: SA1.A1_NOME, 'C', 30, 0)
    oBrowse.SetFilter("A1_NOME != ''")
    oBrowse.Activate()
    DbCloseArea()
    FWRestArea(aArea)
    return
