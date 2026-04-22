#include 'protheus.ch'

// Exemplo de código legado para ser convertido para Python
User Function ExemploLegado()
    Local nI := 0
    Local cMsg := "Iniciando processamento..."
    
    MsgAlert(cMsg)
    
    For nI := 1 To 10
        If nI % 2 == 0
            ConOut("Número par: " + cValToChar(nI))
        EndIf
    Next
    
    Return Nil
