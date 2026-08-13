# Esse exemplo faz parte da série do YouTube, Maratona de Exemplos, do canal Terminal de Informação, 
#     caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2024/02/13/interceptando-modelo-ou-view-em-mvc-com-fwmodelactive-e-fwviewactive-maratona-advpl-e-tl-233/
# Bibliotecas
# PREPROCESSOR: #Include "Totvs.ch"
# PREPROCESSOR: #Include "FWMVCDef.ch"
# {Protheus.doc} User Function zExe233
# Busca o Modelo ou a Visualização em memória
# @type Function
# @author Atilio
# @since 20/02/2023
# @see https://tdn.totvs.com/display/public/framework/FWModelActive e https://tdn.totvs.com/display/public/framework/FWViewActive
# @obs 
# 
#     **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
def u_zExe233():
    aArea = FWGetArea()
    oModel = FWModelActive()
    oModelGrid = oModel.GetModel('DA1DETAIL')
    oView = FWViewActive()
    # Altera um campo da memória
    oModel.SetValue('DA0MASTER', 'DA0_DESCRI', 'Olá - ' + Time())
    # Posiciona na terceira linha e atualiza a tela
    oModelGrid.GoLine(3)
    oView.Refresh()
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
            aAdd(xRet, ['* Atualizar Tela', '', lambda : u_zExe233(), 'Atu. Tela'])


    FWRestArea(aArea)
    return xRet
