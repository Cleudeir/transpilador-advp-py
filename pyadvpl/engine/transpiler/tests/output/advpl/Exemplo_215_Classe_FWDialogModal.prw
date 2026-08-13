// caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2024/02/04/criando-dialogs-com-a-fwdialogmodal-maratona-advpl-e-tl-215/
// Bibliotecas
#Include "TOTVS.ch"
// {Protheus.doc} User Function zExe215
// Exemplo de função que cria uma dialog
// @type Function
// @author Atilio
// @since 20/02/2023
// @see https://tdn.totvs.com/display/public/framework/FwDialogModal
// **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
USER FUNCTION zExe215()
    LOCAL aArea, oDlgAux, nJanAltu, nJanLarg, bBlocoTst, cJanTitulo

    aArea := FWGetArea()
    oDlgAux := Nil
    nJanAltu := 100
    nJanLarg := 200
    bBlocoTst := Nil
    cJanTitulo := "Tela usando FWDialogModal"
    // Instancia a classe, criando uma janela
    oDlgAux := FWDialogModal():New()
    oDlgAux:SetTitle(cJanTitulo)
    oDlgAux:SetSize(nJanAltu, nJanLarg)
    oDlgAux:EnableFormBar(.T.)
    oDlgAux:CreateDialog()
    oDlgAux:CreateFormBar()
    oDlgAux:AddButton("Teste", bBlocoTst, "Teste", Nil, .T., .F., .T., Nil, Nil)
    // Aqui antes de abrir a tela, caso você queira usar essa classe, pode usar o método oDlgAux:GetPanelMain()
    // e instanciar os objetos apontando para esse painel
    oDlgAux:Activate()
    FWRestArea(aArea)
    RETURN
