# PREPROCESSOR: #Include "TOTVS.ch"
# {Protheus.doc} zEx903
# Exemplo complexo de MsNewProcess
# @author Antigravity
# @since 13/05/2026
def u_zEx903():
    oProcess = None
    oProcess = MsNewProcess().New(lambda lEnd: u_ProcTest(lEnd, oProcess), 'Processando Registros', 'Aguarde...', True)
    oProcess.Activate()
    return Static

def u_ProcTest(lEnd, oProcess):
    nTotal = 100
    nI = 0
    oProcess.SetRegs(nTotal)
    return
