#Include "TOTVS.ch"

/*/{Protheus.doc} zEx905
Exemplo complexo de BEGIN SEQUENCE / RECOVER
@author Antigravity
@since 13/05/2026
/*/
User Function zEx905()
    Local nDivisor := 0
    Local nResultado := 0
    
    BEGIN SEQUENCE
        ConOut("Iniciando processo de divisão...")
        
        If nDivisor == 0
            ConOut("Erro: Divisão por zero!")
            Break
        EndIf
        
        nResultado := 100 / nDivisor
        ConOut("Resultado: " + cValToChar(nResultado))
        
    RECOVER
        ConOut("Processo interrompido!")
    END SEQUENCE
    
    ConOut("Fim do exemplo.")
Return Nil
