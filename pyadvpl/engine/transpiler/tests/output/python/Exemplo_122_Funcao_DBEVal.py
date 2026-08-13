# Esse exemplo faz parte da série do YouTube, Maratona de Exemplos, do canal Terminal de Informação, 
#     caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2023/12/08/executando-um-bloco-de-codigo-em-um-alias-com-dbeval-maratona-advpl-e-tl-122/
# Bibliotecas
# PREPROCESSOR: #Include "TOTVS.ch"
# {Protheus.doc} User Function zExe122
# Executa um bloco de código no alias
# @type Function
# @author Atilio
# @since 14/12/2022
# @see https://tdn.totvs.com/display/tec/DBEVal
# @obs 
#     Função DBEVal
#     Parâmetros
#         + bBlock           , Bloco de Código  , Bloco de código a ser executado
#         + bFirstCondition  , Bloco de Código  , Bloco de código com condição em caso de inserção de registro
#         + bSecondCondition , Bloco de Código  , Segundo bloco de código com condição em caso de inserção de registro
#         + nCount           , Numérico         , Número máximo de registros a serem processados
#         + nRecno           , Numérico         , RecNo do único registro a ser processado
#         + lRest            , Lógico           , Indica que os demais registros serão processados
#     Retorno
#         Função não tem retorno
# 
#     **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
def u_zExe122():
    aArea = FWGetArea()
    nTotal = 0
    bBloco = lambda : None
    aProds = []
    DbSelectArea('SB1')
    SB1.DbSetOrder(1)
    # B1_FILIAL + B1_COD
    # Define o bloco de código
    bBloco = lambda : ((nTotal := nTotal + 1) if 'A' in Upper(SB1.B1_DESC) else None)
    # Executa o bloco de código
    SB1.DbGoTop()
    SB1.DbEVal(bBloco)
    # Mostra o resultado
    FWAlertInfo('Existe(m) ' + cValToChar(nTotal) + " produto(s) que  tem a letra 'A' na descrição!", 'Teste 1 DbEVal')
    # Define o bloco de código
    bBloco = lambda : aAdd(aProds, [SB1.B1_COD, SB1.B1_DESC, SB1.RecNo()])
    # Executa o bloco de código
    SB1.DbGoTop()
    SB1.DbEVal(bBloco)
    # Mostra o resultado
    FWAlertInfo('Existe(m) ' + cValToChar(Len(aProds)) + ' produto(s) no Array!', 'Teste 2 DbEVal')
    FWRestArea(aArea)
    return
