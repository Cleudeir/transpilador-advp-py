#include 'protheus.ch'

// Legacy code sample to be converted to Python
User Function LegacySample()
    Local nI := 0
    Local cMsg := "Iniciando processamento..."
    
    MsgAlert(cMsg)
    
    For nI := 1 To 10
        If nI % 2 == 0
            ConOut("Número par: " + cValToChar(nI))
        EndIf
    Next
    
    Return Nil
