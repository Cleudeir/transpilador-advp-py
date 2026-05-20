/*
    Exemplo completo demonstrando:
    - BEGIN TRANSACTION / END TRANSACTION
    - BeginSQL / EndSQL com COLUMN
    - PRIVATE e PUBLIC variables
*/

#Include "TOTVS.ch"

User Function zExemploCompleto()
    Local aArea := FWGetArea()
    Local lSucesso := .T.
    PRIVATE cMsgLog := ""
    PUBLIC nTotalRegistros := 0
    
    // Inicia transacao
    Begin Transaction
        // Consulta com SQL nativo
        BeginSql Alias "SQL_CLIENTES"
            COLUMN A1_COD AS CHAR
            COLUMN A1_NOME AS CHAR
            COLUMN A1_SALDO AS DECIMAL
            
            SELECT A1_COD, A1_NOME, A1_SALDO
            FROM %table:SA1% SA1
            WHERE SA1.A1_FILIAL = %xFilial:SA1%
              AND SA1.%notDel%
            ORDER BY A1_NOME
        EndSql
        
        // Processa resultados
        While ! SQL_CLIENTES->(EoF())
            nTotalRegistros++
            cMsgLog := "Cliente: " + SQL_CLIENTES->A1_NOME
            
            // Atualiza saldo
            If SQL_CLIENTES->A1_SALDO > 1000
                RecLock('SA1', .F.)
                    SA1->A1_X_STATUS := "VIP"
                SA1->(MsUnlock())
            EndIf
            
            SQL_CLIENTES->(DbSkip())
        EndDo
        
        SQL_CLIENTES->(DbCloseArea())
        
        // Se houve erro, cancela transacao
        If nTotalRegistros == 0
            DisarmTransaction()
            lSucesso := .F.
        EndIf
    End Transaction
    
    If lSucesso
        FWAlertInfo("Processados " + cValToChar(nTotalRegistros) + " registros.", "Sucesso")
    Else
        FWAlertWarning("Nenhum registro encontrado.", "Atencao")
    EndIf
    
    FWRestArea(aArea)
Return
