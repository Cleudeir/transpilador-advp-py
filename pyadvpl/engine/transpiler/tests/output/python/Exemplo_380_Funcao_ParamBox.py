# Esse exemplo faz parte da série do YouTube, Maratona de Exemplos, do canal Terminal de Informação, 
#     caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2024/04/27/abrindo-uma-tela-de-parametros-com-a-parambox-maratona-advpl-e-tl-380/
# Bibliotecas
# PREPROCESSOR: #Include "TOTVS.ch"
# {Protheus.doc} User Function zExe380
# Abre uma tela de parâmetros para o usuário informar nos campos
# @type Function
# @author Atilio
# @since 28/03/2023
# @obs 
# 
#     Função ParamBox
#     Parâmetros
#         Array com as definições das perguntas
#         Título da Janela
#         Array de retorno caso queira utilizar no lugar das variáveis MV_PAR**
#         Bloco de código executado ao clicar em Confirmar
#         Array de outros botões que serão exibidos na tela
#         Define se a janela será aberta centralizada (.T.) ou não (.F.)
#         Define a coordenada em x que a janela será aberta
#         Define a coordenada em y que a janela será aberta
#         Nome do Objeto / Wizard, em que a pergunta será exibida dentro
#         Nome da rotina que esta carregando (que depois será salva no profile caso seja gravado)
#         Define se os botões de salvar estarão habilitados
#         Define se será salvo por perfil de usuário
#     Retorno
#         Retorna .T. se foi clicado em Confirmar ou .F. se foi em Cancelar
# 
#     Obs.: Caso queiram fazer validações no ParamBox, recomendo a leitura desse artigo:
#     https://terminaldeinformacao.com/2021/12/02/como-fazer-validacoes-em-um-parambox/
# 
#     Obs.2: Caso desejam ver as posições de cada uma das opções do Array com as definições
#     de perguntas, recomendo a leitura do artigo disponibilizado pelo pessoal do BlackTDN:
#     https://www.blacktdn.com.br/2012/05/para-quem-precisar-desenvolver-uma.html
# 
#     **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
def u_zExe380():
    aArea = FWGetArea()
    fExempSimp()
    fExempComp()
    FWRestArea(aArea)
    return Static

def fExempSimp():
    aPergs = []
    cProdDe = Space(TamSX3('B1_COD')[1])
    cProdAt = Space(TamSX3('B1_COD')[1])
    dDataDe = FirstDate(Date())
    dDataAt = LastDate(dDataDe)
    nTipo = 3
    # Adiciona as perguntas utilizadas na tela de parâmetros
    aAdd(aPergs, [1, 'Produto De', cProdDe, '', "ExistCPO('SB1')", 'SB1', '.T.', 60, False])
    aAdd(aPergs, [1, 'Produto Até', cProdAt, '', "ExistCPO('SB1')", 'SB1', '.T.', 60, True])
    aAdd(aPergs, [1, 'Data De', dDataDe, '', '.T.', '', '.T.', 80, False])
    aAdd(aPergs, [1, 'Data Até', dDataAt, '', '.T.', '', '.T.', 80, True])
    aAdd(aPergs, [2, 'Tipo do Filtro', nTipo, ['1=Não Bloqueados', '2=Somente Bloqueados', '3=Ambos'], 90, '.T.', False])
    # Se a pergunta foi confirmada
    if ParamBox(aPergs, 'Informe os parâmetros'):
        MV_PAR05 = Val(cValToChar(MV_PAR05))
        FWAlertSuccess('Pergunta confirmada', 'Teste Simples de ParamBox')

    return Static

def fExempComp():
    aPergs = []
    cProduto = Space(TamSX3('B1_COD')[1])
    nTipoCmb = 3
    nTipoRad = 3
    lFiltArm = True
    lFiltGrp = True
    cArquivo = 'C:\\spool\\teste.txt'
    # Adiciona as perguntas utilizadas na tela de parâmetros
    aAdd(aPergs, [1, '01 (Get) - Informe o Produto', cProduto, '', "ExistCPO('SB1')", 'SB1', '.T.', 60, True])
    aAdd(aPergs, [2, '02 (Combo) - Tipo', nTipoCmb, ['1=Não Bloqueados', '2=Somente Bloqueados', '3=Ambos'], 90, '.T.', False])
    aAdd(aPergs, [3, '03 (Radio) - Tipo', nTipoRad, ['1=Não Bloqueados', '2=Somente Bloqueados', '3=Ambos'], 90, '.T.', False, '.T.'])
    aAdd(aPergs, [4, '04 (CheckBox) - Filtra Armazém 01', lFiltArm, 'Sim, será filtrado', 90, '.T.', False])
    aAdd(aPergs, [5, '05 (CheckBox) - Filtra Grupo G001', lFiltGrp, 100, '.T.'])
    aAdd(aPergs, [6, '06 (File) - Caminho do arquivo', cArquivo, '', '.T.', '.T.', 100, False, 'Arquivos txt|*.txt| Arquivos csv|*.csv', 'C:\\spool\\', GETF_LOCALHARD + GETF_NETWORKDRIVE, True])
    aAdd(aPergs, [7, '07 (Filtro) - Filtro específico', 'SB1', '', True])
    aAdd(aPergs, [8, '08 (Password) - Informe a Senha', 'beluga', '', '.T.', '', '.T.', 60, True])
    aAdd(aPergs, [9, '09 (Say) - Apenas uma frase', 100, 20, True])
    aAdd(aPergs, [10, '10 (Range) - Range de dados', '', 'SB1', 110, 'C', 50, '.T.'])
    aAdd(aPergs, [11, '11 (Memo) - Digite uma frase', 'aaaa', '.T.', '.T.', False])
    aAdd(aPergs, [12, '12 (Filtro) - Informe o filtro', 'SB1', '', '.T.'])
    # Se a pergunta foi confirmada
    if ParamBox(aPergs, 'Informe os parâmetros', None, None, None, None, None, None, None, None, False, False):
        MV_PAR02 = Val(cValToChar(MV_PAR02))
        MV_PAR03 = Val(cValToChar(MV_PAR03))
        FWAlertSuccess('Pergunta confirmada', 'Teste Completo de ParamBox')

    return
