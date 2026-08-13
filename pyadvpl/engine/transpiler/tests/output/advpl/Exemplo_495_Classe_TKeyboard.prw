// caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2024/06/23/criando-um-teclado-virtual-com-tkeyboard-maratona-advpl-e-tl-495/
// Bibliotecas
#Include "TOTVS.ch"
// {Protheus.doc} User Function zExe495
// Cria um teclado virtual em uma Dialog
// @type Function
// @author Atilio
// @since 04/04/2023
// **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
USER FUNCTION zExe495()
    LOCAL aArea, nCorFundo, nJanAltura, nJanLargur, cJanTitulo, lDimPixels, lCentraliz, nObjLinha, nObjColun, nObjLargu, nObjAltur, nTamanText, cFontNome, oFontPadrao, oDialogPvt, bBlocoIni, oGetTeste, xGetTeste, oKey

    aArea := FWGetArea()
    nCorFundo := RGB(238, 238, 238)
    nJanAltura := 251
    nJanLargur := 470
    cJanTitulo := "Exemplo TKeyboard"
    lDimPixels := .T.
    lCentraliz := .T.
    nObjLinha := 0
    nObjColun := 0
    nObjLargu := 0
    nObjAltur := 0
    nTamanText := 50
    cFontNome := "Tahoma"
    oFontPadrao := TFont():New(cFontNome, Nil, - 12)
    oDialogPvt := Nil
    bBlocoIni := Nil
    // Aqui voce pode acionar funcoes customizadas que irao ser acionadas ao abrir a dialog
    oGetTeste := Nil
    xGetTeste := Space(nTamanText)
    oKey := Nil
    // Cria a dialog
    oDialogPvt := TDialog():New(0, 0, nJanAltura, nJanLargur, cJanTitulo, Nil, Nil, Nil, Nil, Nil, nCorFundo, Nil, Nil, lDimPixels)
    // objeto1 - usando a classe TGet
    nObjLinha := 3
    nObjColun := 3
    nObjLargu := nJanLargur / 2 - 6
    nObjAltur := 10
    oGetTeste := TGet():New(nObjLinha, nObjColun, Nil, oDialogPvt, nObjLargu, nObjAltur, Nil, Nil, Nil, Nil, oFontPadrao, Nil, Nil, lDimPixels)
    // Definindo que quando o get for clicado, será vinculado ao teclado virtual
    oGetTeste->bGotFocus := Nil
    // Criando o teclado virtual
    nObjLinha := 19
    nObjColun := 3
    oKey := TKeyboard():New(nObjLinha, nObjColun, 2, oDialogPvt)
    // Definindo que ficará vinculado ao get criado anteriomente
    oKey:SetVars(oGetTeste, nTamanText)
    // Definindo uma ação ao clicar no -Enter-
    oKey:SetEnter(Nil)
    // Ativa e exibe a janela
    oDialogPvt:Activate(Nil, Nil, Nil, lCentraliz, Nil, Nil, bBlocoIni)
    FWRestArea(aArea)
    RETURN
