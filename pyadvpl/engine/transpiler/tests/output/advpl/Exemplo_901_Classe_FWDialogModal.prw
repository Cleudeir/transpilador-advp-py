#Include "TOTVS.ch"
// {Protheus.doc} zEx901
// Exemplo complexo de FWDialogModal
// @author Antigravity
// @since 13/05/2026
USER FUNCTION zEx901()
    LOCAL oDlg, oPanel, cNome

    oDlg := Nil
    oPanel := Nil
    cNome := Space(30)
    oDlg := FWDialogModal():New()
    oDlg:SetTitle("Cadastro Rápido de Cliente")
    oDlg:SetSize(300, 400)
    // Simula obtenção de painel
    oPanel := oDlg:GetPanel()
    // Adiciona controles
    oDlg:AddSay(oPanel, 10, 10, "Nome do Cliente:")
    oDlg:AddGet(oPanel, 10, 100, Nil, 120, 20)
    // Botões com ações
    oDlg:AddButton("Confirmar", Nil)
    oDlg:AddButton("Cancelar", Nil)
    oDlg:Activate()
    RETURN Static

USER FUNCTION Confirma(cNome)
    If Empty(cNome)
        FWAlertWarning("O nome não pode ser vazio!", "Aviso")
    Else
        FWAlertInfo("Cliente " + cNome + " confirmado com sucesso!", "Sucesso")
    EndIf
    RETURN
