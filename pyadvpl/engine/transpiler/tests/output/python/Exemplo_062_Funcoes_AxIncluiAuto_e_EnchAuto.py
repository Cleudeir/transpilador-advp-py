# Esse exemplo faz parte da série do YouTube, Maratona de Exemplos, do canal Terminal de Informação, 
#     caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2023/10/09/incluindo-registros-com-as-funcoes-axincluiauto-e-enchauto-maratona-advpl-e-tl-062/
# Bibliotecas
# PREPROCESSOR: #Include "TOTVS.ch"
# {Protheus.doc} User Function zExe062
# Exemplo de função para inclusão de registros quando a rotina não é em MVC e não tem ExecAuto
# @type Function
# @author Atilio
# @since 06/12/2022
# @see https://tdn.totvs.com/display/public/framework/EnchAuto
# @obs 
#     Função AxIncluiAuto
#     Parâmetros
#         + cAlias     , Caractere  , Alias da Tabela
#         + cTudoOk    , Caractere  , Função que será executada antes de confirmar a gravação (pra validar se está tudo ok)
#         + cTransact  , Caractere  , Função que será executada dentro da transação
#         + nOpcaoAuto , Numérico   , Opção que será executada sendo 3 inclusão e 4 alteração
#         + nLinha     , Numérico   , Número do RecNo caso seja uma alteração
#     Retorno
#         + Retorna 1 em caso de sucesso ou 3 em caso de falha
# 
#     Função EnchAuto
#     Parâmetros
#         + cAlias     , Caractere  , Alias da Tabela
#         + aField     , Array      , Campos utilizados sendo que as posições da linha devem ser [1] nome do campo; [2] conteúdo; [3] nulo
#         + uTudoOk    , Indefinido , Bloco de código ou função executada antes de confirmar a gravação (pra validar se esta tudo ok)
#         + nOpc       , Numérico   , Opção que será executada sendo 3 inclusão; 4 alteração e 5 exclusão
#         + aCpos      , Array      , Indica campos que serão considerados mesmo que não estejam usados na SX3
#     Retorno
#         + lValido    , Lógico     , .T. em caso de sucesso ou .F. em caso de falha
# 
#     **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
def u_zExe062():
    aArea = FWGetArea()
    cTabela = 'RC1'
    aDados = []
    cTudoOk = 'Gpm660Vld(1)'
    cTransact = 'Gpm660_PCO()'
    nRetorno = 0
    lMsErroAuto = False
    # Adiciona os campos para o ExecAuto
    aAdd(aDados, ['RC1_FILTIT', '01', None])
    aAdd(aDados, ['RC1_PREFIX', 'GPE', None])
    aAdd(aDados, ['RC1_NUMTIT', '000000006', None])
    aAdd(aDados, ['RC1_CODTIT', 'GPE', None])
    aAdd(aDados, ['RC1_DESCRI', 'GPE - Teste 3', None])
    aAdd(aDados, ['RC1_VALOR', 250, None])
    aAdd(aDados, ['RC1_EMISSA', dDataBase, None])
    aAdd(aDados, ['RC1_VENCTO', DaySum(dDataBase, 5), None])
    aAdd(aDados, ['RC1_VENREA', DaySum(dDataBase, 5), None])
    aAdd(aDados, ['RC1_TIPO', 'NF', None])
    aAdd(aDados, ['RC1_NATURE', 'NATDES0001', None])
    aAdd(aDados, ['RC1_FORNEC', 'F00003', None])
    aAdd(aDados, ['RC1_LOJA', '01', None])
    aAdd(aDados, ['RC1_DTBUSI', FirstDate(MonthSub(dDataBase, 1)), None])
    aAdd(aDados, ['RC1_DTBUSF', LastDate(MonthSub(dDataBase, 1)), None])
    # Inicializa a transação
    with Transaction():
        # Joga a tabela para a memória (M->)
        RegToMemory(cTabela, True, False)
        # Se conseguir fazer a execução automática
        if EnchAuto(cTabela, aDados, cTudoOk, 3):
            # Aciona a efetivação da gravação
            nRetorno = AxIncluiAuto(cTabela, None, cTransact, 3)
        else:
            AutoGrLog('Falha na geração da RC1!')
            MostraErro()
            DisarmTransaction()


    FWRestArea(aArea)
    return
