# Exemplo completo demonstrando:
#     - BEGIN TRANSACTION / END TRANSACTION
#     - BeginSQL / EndSQL com COLUMN
#     - PRIVATE e PUBLIC variables
# PREPROCESSOR: #Include "TOTVS.ch"
def u_zExemploCompleto():
    aArea = FWGetArea()
    lSucesso = True
    cMsgLog = ''
    nTotalRegistros = 0
    # Inicia transacao
    with Transaction():
        # Consulta com SQL nativo
        with BeginSQL(alias="SQL_CLIENTES") as sql:
            sql.column("A1_COD", "CHAR")
            sql.column("A1_NOME", "CHAR")
            sql.column("A1_SALDO", "DECIMAL")
            sql.query("""SELECT A1_COD , A1_NOME , A1_SALDO FROM % table : SA1 % SA1 WHERE SA1 . A1_FILIAL = % xFilial : SA1 % AND SA1 . % notDel % ORDER BY A1_NOME""")
            # Processa resultados
            while not SQL_CLIENTES.EoF():
                nTotalRegistros += 1
                cMsgLog = 'Cliente: ' + SQL_CLIENTES.A1_NOME
                # Atualiza saldo
                if SQL_CLIENTES.A1_SALDO > 1000:
                    RecLock('SA1', False)
                    SA1.A1_X_STATUS = 'VIP'
                    SA1.MsUnlock()

                SQL_CLIENTES.DbSkip()

            SQL_CLIENTES.DbCloseArea()
            # Se houve erro, cancela transacao
            if nTotalRegistros == 0:
                DisarmTransaction()
                lSucesso = False



    if lSucesso:
        FWAlertInfo('Processados ' + cValToChar(nTotalRegistros) + ' registros.', 'Sucesso')
    else:
        FWAlertWarning('Nenhum registro encontrado.', 'Atencao')

    FWRestArea(aArea)
    return
