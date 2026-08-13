// caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2024/07/03/abrindo-um-site-com-twebchannel-e-twebengine-maratona-advpl-e-tl-514/
// Bibliotecas
#Include "TOTVS.ch"
// {Protheus.doc} User Function zExe514
// Cria uma navegação com a possibilidade de abrir páginas em html ou sites através de urls
// @type  Function
// @author Atilio
// @since 05/04/2023
// @see https://tdn.totvs.com/display/tec/TWebChannel e https://tdn.totvs.com/display/tec/TWebEngine
// **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
USER FUNCTION zExe514()
    LOCAL aArea, cRastreio, aPergs

    aArea := GetArea()
    cRastreio := "AA123456785BR"
    aPergs := {  }
    // Adiciona os parametros para a pergunta
    aAdd(aPergs, { 1, "Rastreio", cRastreio, "", ".T.", "", ".T.", 80, .T. })
    // Mostra uma pergunta com parambox para filtrar o subgrupo
    If ParamBox(aPergs, "Informe os parametros", Nil, Nil, Nil, Nil, Nil, Nil, Nil, Nil, .F., .F.)
        fMontaBusca()
    EndIf
    RestArea(aArea)
    RETURN Static

FUNCTION fMontaBusca()
    LOCAL cUrl, nJanLarg, nJanAltu, oWebChannel, nPort, oWebEngine, aComandos

    cUrl := ""
    // Tamanho da janela
    nJanLarg := 800
    nJanAltu := 600
    // Navegador Internet
    oWebChannel := Nil
    nPort := Nil
    oWebEngine := Nil
    aComandos := {  }
    // Defina a URL e os comandos que vão ser executados
    cUrl := "https://rastreamento.correios.com.br/app/index.php"
    aAdd(aComandos, "document.getElementById("objeto").value = "" + MV_PAR01 + ""; ")
    // Cria a dialog
    DEFINE
    DIALOG
    oDlg
    TITLE
    "Pesquisa de Transportadora"
    FROM_
    0
    // ,
    0
    TO
    nJanAltu
    // ,
    nJanLarg
    PIXEL
    // Prepara o conector WebSocket
    oWebChannel := TWebChannel():New()
    nPort := oWebChannel
    ::connect()
    // Cria componente
    oWebEngine := TWebEngine():New(oDlg, 0, 0, 100, 100, Nil, nPort)
    oWebEngine->bLoadFinished := Nil
    oWebEngine:navigate(cUrl)
    oWebEngine->Align := CONTROL_ALIGN_ALLCLIENT
    ACTIVATE
    DIALOG
    oDlg
    CENTERED
    RETURN Static

FUNCTION fRodaScript(cUrl)
    LOCAL nAtual

    nAtual := 0
    // Percorre os comandos
    RETURN
