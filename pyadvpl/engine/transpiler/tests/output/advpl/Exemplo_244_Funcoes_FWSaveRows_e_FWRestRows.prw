// caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2024/02/19/buscando-todos-usuarios-cadastrados-atraves-da-fwsfallusers-maratona-advpl-e-tl-245/
// Bibliotecas
#Include "Totvs.ch"
// {Protheus.doc} User Function zExe244
// Armazena a posição na grid da tela e depois volta
// @type Function
// @author Atilio
// @since 20/02/2023
// @see https://tdn.totvs.com/display/public/framework/FWSaveRows e https://tdn.totvs.com/display/public/framework/FWRestRows
// Função FWSaveRows
// Parâmetros
// + oModel         , Objeto          , Modelo de dados em memória
// Retorno
// + aRet           , Array           , Array com as posições que serão recuperadas
// Função FWRestRows
// Parâmetros
// + aIDs           , Array           , Array com as posições
// + oModel         , Objeto          , Modelo de dados
// Retorno
// Função não tem retorno
// **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
USER FUNCTION zExe244()
    LOCAL aArea, aSaveLines, oModelPad, oModelGrid

    aArea := FWGetArea()
    aSaveLines := FWSaveRows()
    // Pegando os modelos de dados
    oModelPad := FWModelActive()
    oModelGrid := oModelPad:GetModel("DA1DETAIL")
    // Adicionando uma linha
    oModelGrid:AddLine()
    FWRestRows(aSaveLines)
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
            aAdd(xRet, { "* Salvar e Voltar a Posição", "", Nil, "Salv. Volt. Pos." })
        EndIf
    EndIf
    FWRestArea(aArea)
    RETURN xRet
