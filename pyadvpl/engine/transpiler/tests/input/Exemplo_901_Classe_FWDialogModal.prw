#Include "TOTVS.ch"

/*/{Protheus.doc} zEx901
Exemplo complexo de FWDialogModal
@author Antigravity
@since 13/05/2026
/*/
User Function zEx901()
    Local oDlg
    Local oPanel
    Local cNome := Space(30)
    
    oDlg := FWDialogModal():New()
    oDlg:SetTitle("Cadastro Rápido de Cliente")
    oDlg:SetSize(300, 400)
    
    // Simula obtenção de painel
    oPanel := oDlg:GetPanel()
    
    // Adiciona controles
    oDlg:AddSay(oPanel, 10, 10, "Nome do Cliente:")
    oDlg:AddGet(oPanel, 10, 100, {|u| Iif(u == Nil, cNome, cNome := u)}, 120, 20)
    
    // Botões com ações
    oDlg:AddButton("Confirmar", {|o| u_Confirma(cNome), oDlg:DeActivate()})
    oDlg:AddButton("Cancelar", {|| oDlg:DeActivate()})
    
    oDlg:Activate()
Return

Static Function u_Confirma(cNome)
    If Empty(cNome)
        FWAlertWarning("O nome não pode ser vazio!", "Aviso")
    Else
        FWAlertInfo("Cliente " + cNome + " confirmado com sucesso!", "Sucesso")
    EndIf
Return
