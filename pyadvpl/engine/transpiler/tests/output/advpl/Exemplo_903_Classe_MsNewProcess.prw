#Include "TOTVS.ch"
// {Protheus.doc} zEx903
// Exemplo complexo de MsNewProcess
// @author Antigravity
// @since 13/05/2026
USER FUNCTION zEx903()
    LOCAL oProcess

    oProcess := Nil
    oProcess := MsNewProcess():New(Nil, "Processando Registros", "Aguarde...", .T.)
    oProcess:Activate()
    RETURN Static

USER FUNCTION ProcTest(lEnd, oProcess)
    LOCAL nTotal, nI

    nTotal := 100
    nI := 0
    oProcess:SetRegs(nTotal)
    RETURN
