// caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2024/02/13/interceptando-modelo-ou-view-em-mvc-com-fwmodelactive-e-fwviewactive-maratona-advpl-e-tl-233/
// Bibliotecas
#Include "Totvs.ch"
#Include "FWMVCDef.ch"
// {Protheus.doc} User Function zExe233
// Busca o Modelo ou a Visualização em memória
// @type Function
// @author Atilio
// @since 20/02/2023
// @see https://tdn.totvs.com/display/public/framework/FWModelActive e https://tdn.totvs.com/display/public/framework/FWViewActive
// **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
USER FUNCTION zExe233()
    LOCAL aArea, oModel, oModelGrid, oView

    aArea := FWGetArea()
    oModel := FWModelActive()
    oModelGrid := oModel:GetModel("DA1DETAIL")
    oView := FWViewActive()
    // Altera um campo da memória
    oModel:SetValue("DA0MASTER", "DA0_DESCRI", "Olá - " + Time())
    // Posiciona na terceira linha e atualiza a tela
    oModelGrid:GoLine(3)
    oView:Refresh()
    FWRestArea(aArea)
    RETURN

USER FUNCTION OMSA010()
    LOCAL aArea, aParam, xRet, oObj, cIdPonto, cIdModel

    aArea := FWGetArea()
    aParam := PARAMIXB
    xRet := .T.
    oObj := Nil
    cIdPonto := ""
    cIdModel := ""
    // Se tiver parametros
    If aParam <> Nil
        // Pega informacoes dos parametros
        oObj := aParam[1]
        cIdPonto := aParam[2]
        cIdModel := aParam[3]
        // Para a inclusao de botoes na ControlBar
        If cIdPonto = "BUTTONBAR"
            xRet := {  }
            aAdd(xRet, { "* Atualizar Tela", "", Nil, "Atu. Tela" })
        EndIf
    EndIf
    FWRestArea(aArea)
    RETURN xRet
