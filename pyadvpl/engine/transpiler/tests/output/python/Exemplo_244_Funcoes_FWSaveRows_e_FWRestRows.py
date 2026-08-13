# Esse exemplo faz parte da série do YouTube, Maratona de Exemplos, do canal Terminal de Informação, 
#     caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2024/02/19/buscando-todos-usuarios-cadastrados-atraves-da-fwsfallusers-maratona-advpl-e-tl-245/
# Bibliotecas
# PREPROCESSOR: #Include "Totvs.ch"
# {Protheus.doc} User Function zExe244
# Armazena a posição na grid da tela e depois volta
# @type Function
# @author Atilio
# @since 20/02/2023
# @see https://tdn.totvs.com/display/public/framework/FWSaveRows e https://tdn.totvs.com/display/public/framework/FWRestRows
# @obs 
# 
#     Função FWSaveRows
#     Parâmetros
#         + oModel         , Objeto          , Modelo de dados em memória
#     Retorno
#         + aRet           , Array           , Array com as posições que serão recuperadas
# 
#     Função FWRestRows
#     Parâmetros
#         + aIDs           , Array           , Array com as posições
#         + oModel         , Objeto          , Modelo de dados
#     Retorno
#         Função não tem retorno
# 
#     **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
def u_zExe244():
    aArea = FWGetArea()
    aSaveLines = FWSaveRows()
    # Pegando os modelos de dados
    oModelPad = FWModelActive()
    oModelGrid = oModelPad.GetModel('DA1DETAIL')
    # Adicionando uma linha
    oModelGrid.AddLine()
    FWRestRows(aSaveLines)
    FWRestArea(aArea)
    return

def u_OMSA010():
    aArea = FWGetArea()
    aParam = PARAMIXB
    xRet = True
    oObj = None
    cIdPonto = ''
    cIdModel = ''
    # Se tiver parametros
    if aParam != None:
        # Pega informacoes dos parametros
        oObj = aParam[1]
        cIdPonto = aParam[2]
        cIdModel = aParam[3]
        # Para a inclusao de botoes na ControlBar
        if cIdPonto == 'BUTTONBAR':
            xRet = []
            aAdd(xRet, ['* Salvar e Voltar a Posição', '', lambda : u_zExe244(), 'Salv. Volt. Pos.'])


    FWRestArea(aArea)
    return xRet
