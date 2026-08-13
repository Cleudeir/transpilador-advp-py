# PREPROCESSOR: #Include "TOTVS.ch"
# {Protheus.doc} zEx901
# Exemplo complexo de FWDialogModal
# @author Antigravity
# @since 13/05/2026
def u_zEx901():
    oDlg = None
    oPanel = None
    cNome = Space(30)
    oDlg = FWDialogModal().New()
    oDlg.SetTitle('Cadastro RÃ¡pido de Cliente')
    oDlg.SetSize(300, 400)
    # Simula obtenÃ§Ã£o de painel
    oPanel = oDlg.GetPanel()
    # Adiciona controles
    oDlg.AddSay(oPanel, 10, 10, 'Nome do Cliente:')
    oDlg.AddGet(oPanel, 10, 100, lambda u: (cNome if u == None else (cNome := u)), 120, 20)
    # BotÃµes com aÃ§Ãµes
    oDlg.AddButton('Confirmar', lambda o: [u_Confirma(cNome), oDlg.DeActivate()])
    oDlg.AddButton('Cancelar', lambda : oDlg.DeActivate())
    oDlg.Activate()
    return Static

def u_Confirma(cNome):
    if Empty(cNome):
        FWAlertWarning('O nome nÃ£o pode ser vazio!', 'Aviso')
    else:
        FWAlertInfo('Cliente ' + cNome + ' confirmado com sucesso!', 'Sucesso')

    return
