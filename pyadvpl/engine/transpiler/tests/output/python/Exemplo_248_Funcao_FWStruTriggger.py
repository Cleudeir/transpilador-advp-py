# Esse exemplo faz parte da série do YouTube, Maratona de Exemplos, do canal Terminal de Informação, 
#     caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2024/02/21/buscando-informacoes-das-perguntas-com-a-fwsx1util-maratona-advpl-e-tl-249/
# Bibliotecas
# PREPROCESSOR: #Include "Totvs.ch"
# PREPROCESSOR: #Include "FWMVCDef.ch"
# Variveis Estaticas
cTitulo = 'Grupo de Produtos'
cAliasMVC = 'SBM'
# {Protheus.doc} User Function zExe248
# Grupo de Produtos (teste de FWStruTrigger)
# @author Atilio
# @since 20/02/2023
# @version 1.0
# @type function
# @obs Codigo gerado automaticamente pelo Autumn Code Maker
# @see https://tdn.totvs.com/display/public/framework/FwStruTrigger e http://autumncodemaker.com
# @obs 
#     
# 	Função FWStruTrigger
#     Parâmetros
# 		+ cDom           , Caractere       , Campo Origem
# 		+ cCDom          , Caractere       , Campo Destino
# 		+ cRegra         , Caractere       , Regra de Preenchimento
# 		+ lSeek          , Lógico          , Irá Posicionar?
# 		+ cAlias         , Caractere       , Alias de Posicionamento
# 		+ nOrdem         , Numérico        , Índice de Posicionamento
# 		+ cChave         , Caractere       , Chave de Posicionamento
# 		+ cCondic        , Caractere       , Condição para execução do gatilho
# 		+ cSequen        , Caractere       , Sequência do gatilho
#     Retorno
#         + aRetorno       , Array           , Array com os dados que serão necessários para a Struct
# 
#     **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
def u_zExe248():
    aArea = FWGetArea()
    oBrowse = None
    aRotina = []
    # Definicao do menu
    aRotina = MenuDef()
    # Instanciando o browse
    oBrowse = FWMBrowse().New()
    oBrowse.SetAlias(cAliasMVC)
    oBrowse.SetDescription(cTitulo)
    oBrowse.DisableDetails()
    # Ativa a Browse
    oBrowse.Activate()
    FWRestArea(aArea)
    return None
    # {Protheus.doc} MenuDef
    # Menu de opcoes na funcao zExe248
    # @author Atilio
    # @since 20/02/2023
    # @version 1.0
    # @type function
    # @obs Codigo gerado automaticamente pelo Autumn Code Maker
    # @see http://autumncodemaker.com

def s_MenuDef():
    aRotina = []
    # Adicionando opcoes do menu
    ADD
    OPTION
    aRotina
    TITLE
    'Visualizar'
    ACTION
    'VIEWDEF.Exemplo_248_Funcao_FWStruTriggger'
    OPERATION
    1
    ACCESS
    0
    ADD
    OPTION
    aRotina
    TITLE
    'Incluir'
    ACTION
    'VIEWDEF.Exemplo_248_Funcao_FWStruTriggger'
    OPERATION
    3
    ACCESS
    0
    ADD
    OPTION
    aRotina
    TITLE
    'Alterar'
    ACTION
    'VIEWDEF.Exemplo_248_Funcao_FWStruTriggger'
    OPERATION
    4
    ACCESS
    0
    ADD
    OPTION
    aRotina
    TITLE
    'Excluir'
    ACTION
    'VIEWDEF.Exemplo_248_Funcao_FWStruTriggger'
    OPERATION
    5
    ACCESS
    0
    return aRotina
    # {Protheus.doc} ModelDef
    # Modelo de dados na funcao zExe248
    # @author Atilio
    # @since 20/02/2023
    # @version 1.0
    # @type function
    # @obs Codigo gerado automaticamente pelo Autumn Code Maker
    # @see http://autumncodemaker.com

def s_ModelDef():
    oStruct = FWFormStruct(1, cAliasMVC)
    oModel = None
    bPre = None
    bPos = None
    bCommit = None
    bCancel = None
    aGatilhos = []
    nAtual = None
    # Adicionando um gatilho, do codigo para data
    aAdd(aGatilhos, FWStruTriggger('BM_GRUPO', 'BM_DESC', "'Grupo ' + Replicate('x', 10)", False, '', 0, '', None, '01'))
    aAdd(aGatilhos, FWStruTriggger('BM_DESC', 'BM_PROORI', "'1'", False, '', 0, '', None, '01'))
    # Percorrendo os gatilhos e adicionando na Struct
    # Cria o modelo de dados para cadastro
    oModel = MPFormModel().New('zExe248M', bPre, bPos, bCommit, bCancel)
    oModel.AddFields('SBMMASTER', None, oStruct)
    oModel.SetDescription('Modelo de dados - ' + cTitulo)
    oModel.GetModel('SBMMASTER').SetDescription('Dados de - ' + cTitulo)
    oModel.SetPrimaryKey([])
    return oModel
    # {Protheus.doc} ViewDef
    # Visualizacao de dados na funcao zExe248
    # @author Atilio
    # @since 20/02/2023
    # @version 1.0
    # @type function
    # @obs Codigo gerado automaticamente pelo Autumn Code Maker
    # @see http://autumncodemaker.com

def s_ViewDef():
    oModel = ModelDef()
    oStruct = FWFormStruct(2, cAliasMVC)
    oView = None
    # Cria a visualizacao do cadastro
    oView = FWFormView().New()
    oView.SetModel(oModel)
    oView.AddField('VIEW_SBM', oStruct, 'SBMMASTER')
    oView.CreateHorizontalBox('TELA', 100)
    oView.SetOwnerView('VIEW_SBM', 'TELA')
    return oView
