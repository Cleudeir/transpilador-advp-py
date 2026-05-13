#Include "TOTVS.ch"

/*/{Protheus.doc} zEx903
Exemplo complexo de MsNewProcess
@author Antigravity
@since 13/05/2026
/*/
User Function zEx903()
    Local oProcess
    oProcess := MsNewProcess():New({|lEnd| u_ProcTest(lEnd, oProcess)}, "Processando Registros", "Aguarde...", .T.)
    oProcess:Activate()
Return

Static Function u_ProcTest(lEnd, oProcess)
    Local nTotal := 100
    Local nI := 0
    
    oProcess:SetRegs(nTotal)
    
    For nI := 1 To nTotal
        If lEnd
            Exit
        EndIf
        
        oProcess:IncRegs()
        oProcess:SetText("Processando item " + cValToChar(nI))
        
        // Simula processamento
        Sleep(10)
    Next
Return
