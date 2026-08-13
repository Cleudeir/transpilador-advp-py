# Esse exemplo faz parte da série do YouTube, Maratona de Exemplos, do canal Terminal de Informação, 
#     caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2023/12/06/efetivando-manipulacoes-de-registros-com-dbcommit-e-dbcommitall-maratona-advpl-e-tl-120/
# Bibliotecas
# PREPROCESSOR: #Include "TOTVS.ch"
# {Protheus.doc} User Function zExe120
# Efetiva a gravação de dados de um alias ou de todos os alias alterados
# @type Function
# @author Atilio
# @since 13/12/2022
# @see https://tdn.totvs.com/display/tec/DBCommit e https://tdn.totvs.com/display/tec/DBCommitAll
# @obs 
#     Função DbCommit
#     Não possui parâmetros nem retorno
# 
#     Função DbCommitAll
#     Não possui parâmetros nem retorno
# 
#     **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
def u_zExe120():
    aArea = FWGetArea()
    cDescAtu = ''
    cNomeAtu = ''
    DbSelectArea('SB1')
    SB1.DbSetOrder(1)
    # B1_FILIAL + B1_COD
    SB1.DbGoTop()
    DbSelectArea('SA1')
    SA1.DbSetOrder(1)
    # A1_FILIAL + A1_COD + A1_LOJA
    SA1.DbGoTop()
    # Exemplo com apenas 1 alias
    with Transaction():
        # Se conseguir posicionar no produto
        if SB1.MsSeek(FWxFilial('SB1') + 'F0003'):
            cDescAtu = Alltrim(SB1.B1_DESC) + '...'
            # Atualiza a Descrição
            RecLock('SB1', False)
            SB1.B1_DESC = cDescAtu
            SB1.MsUnlock()

        # Salva todas as alterações pendentes
        if FWAlertYesNo('Deseja salvar a alteração no produto?', 'Continua (DbCommit)?'):
            SB1.DbCommit()
        else:
            DisarmTransaction()


    # Inicia o controle de transações
    with Transaction():
        # Se conseguir posicionar no produto
        if SB1.MsSeek(FWxFilial('SB1') + 'F0003'):
            cDescAtu = Alltrim(SB1.B1_DESC) + '...'
            # Atualiza a Descrição
            RecLock('SB1', False)
            SB1.B1_DESC = cDescAtu
            SB1.MsUnlock()

        # Se conseguir posicionar no cliente
        if SA1.MsSeek(FWxFilial('SA1') + 'C00003'):
            cNomeAtu = Alltrim(SA1.A1_NOME) + '...'
            # Atualiza o nome
            RecLock('SA1', False)
            SA1.A1_NOME = cNomeAtu
            SA1.MsUnlock()

        # Salva todas as alterações pendentes
        if FWAlertYesNo('Deseja salvar todas as alterações?', 'Continua (DbCommitAll)'):
            DbCommitAll()
        else:
            DisarmTransaction()

        # Encerra a transação

    FWRestArea(aArea)
    return
