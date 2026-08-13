#Include "TOTVS.ch"
// {Protheus.doc} zEx902
// Exemplo complexo de FWBrowse
// @author Antigravity
// @since 13/05/2026
USER FUNCTION zEx902()
    LOCAL oBrowse, aArea

    oBrowse := Nil
    aArea := FWGetArea()
    // Abre área de trabalho
    DbUseArea(.T., "TOPCONN", "SA1", "SA1", .T., .F.)
    oBrowse := FWBrowse():New()
    oBrowse:SetAlias("SA1")
    oBrowse:SetQuery("SELECT * FROM SA1 WHERE A1_NOME LIKE '%TESTE%'")
    // Adiciona colunas
    oBrowse:AddColumn("Código", Nil, "C", 6, 0)
    oBrowse:AddColumn("Nome", Nil, "C", 30, 0)
    oBrowse:SetFilter("A1_NOME != ''")
    oBrowse:Activate()
    DbCloseArea()
    FWRestArea(aArea)
    RETURN
