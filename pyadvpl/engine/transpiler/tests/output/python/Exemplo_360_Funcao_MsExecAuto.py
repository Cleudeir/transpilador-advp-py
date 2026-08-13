# Esse exemplo faz parte da série do YouTube, Maratona de Exemplos, do canal Terminal de Informação, 
#     caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2024/04/17/atualizando-informacoes-atraves-da-msexecauto-maratona-advpl-e-tl-360/
# Bibliotecas
# PREPROCESSOR: #Include "TOTVS.ch"
# {Protheus.doc} User Function zExe360
# Executa uma rotina de forma automática
# @type Function
# @author Atilio
# @since 26/03/2023
# @see https://tdn.totvs.com/pages/releaseview.action?pageId=566489232
# @obs 
#     Função MsExecAuto
#     Parâmetros
#         + Bloco de código que será executado
#         + Parâmetros (1 a 15) que serão passados na rotina
#     Retorno
#         Função não tem Retorno
# 
#     **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
def u_zExe360():
    aArea = FWGetArea()
    aDados = []
    lAutomatico = IsBlind()
    cPastaErro = '\\x_logs\\'
    cNomeErro = ''
    cTextoErro = ''
    aLogErro = []
    nLinhaErro = 0
    lMsErroAuto = False
    # Se for automático sem tela, declara outras variáveis para não exibir a tela
    if lAutomatico:
        lMSHelpAuto = True
        lAutoErrNoFile = True

    # Adiciona os campos
    aAdd(aDados, ['B1_COD', 'F0001', None])
    aAdd(aDados, ['B1_DESC', 'Teste', None])
    aAdd(aDados, ['B1_TIPO', 'PA', None])
    aAdd(aDados, ['B1_UM', 'KG', None])
    aAdd(aDados, ['B1_LOCPAD', '01', None])
    aAdd(aDados, ['B1_GRUPO', 'G001', None])
    # Chama a inclusão
    MsExecAuto(lambda x, y: MATA010(x, y), aDados, 3)
    # Se houve erro, mostra a mensagem
    if lMsErroAuto:
        # Se for automático, irá gravar o log dentro da Protheus Data
        if lAutomatico:
            cPastaErro = '\\x_logs\\'
            cNomeErro = 'erro_sb1_' + dToS(Date()) + '_' + StrTran(Time(), ':', '-') + '.txt'
            # Se a pasta de erro não existir, cria ela
            if not ExistDir(cPastaErro):
                MakeDir(cPastaErro)

            # Pegando log do ExecAuto, percorrendo e incrementando o texto
            aLogErro = GetAutoGRLog()
            # Criando o arquivo txt e incrementa o log
            MemoWrite(cPastaErro + cNomeErro, cTextoErro)
            # Senão, exibe a tela de erro
        else:
            MostraErro()

    else:
        FWAlertSuccess('Produto incluido com sucesso', 'Sucesso no ExecAuto')

    FWRestArea(aArea)
    return
