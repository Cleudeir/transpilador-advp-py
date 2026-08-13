// caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2024/06/21/criando-agrupamentos-atraves-da-tgroup-maratona-advpl-e-tl-490/
// Bibliotecas
#Include "TOTVS.ch"
// {Protheus.doc} User Function zExe490
// Cria agrupadores em uma Dialog
// @type Function
// @author Atilio
// @since 04/04/2023
// @see https://tdn.totvs.com/display/tec/TGroup
// **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
USER FUNCTION zExe490()
    LOCAL aArea, nCorFundo, nJanAltura, nJanLargur, cJanTitulo, lDimPixels, lCentraliz, nObjLinha, nObjColun, nObjLargu, nObjAltur, cFontNome, oFontPadrao, oFontNegrit, oDialogPvt, bBlocoIni, oSayObj0, cSayObj0, oGetObj1, xGetObj1, oSayObj2, cSayObj2, oGetObj3, xGetObj3, oSayObj4, cSayObj4, oGetObj5, xGetObj5, oSayObj6, cSayObj6, oGetObj7, xGetObj7, oSayObj8, cSayObj8, oGetObj9, xGetObj9, oSayObj10, cSayObj10, oGetObj11, xGetObj11, oSayObj12, cSayObj12, oGetObj13, xGetObj13, oBtnObj14, cBtnObj14, bBtnObj14, oGrpCampo, oGrpBotao

    aArea := FWGetArea()
    nCorFundo := RGB(238, 238, 238)
    nJanAltura := 301
    nJanLargur := 338
    cJanTitulo := "Exemplo TGroup"
    lDimPixels := .T.
    lCentraliz := .T.
    nObjLinha := 0
    nObjColun := 0
    nObjLargu := 0
    nObjAltur := 0
    cFontNome := "Tahoma"
    oFontPadrao := TFont():New(cFontNome, Nil, - 12)
    oFontNegrit := TFont():New(cFontNome, Nil, - 12, Nil, .T.)
    oDialogPvt := Nil
    bBlocoIni := Nil
    // Aqui voce pode acionar funcoes customizadas que irao ser acionadas ao abrir a dialog
    // objeto0
    oSayObj0 := Nil
    cSayObj0 := "Normal"
    // objeto1
    oGetObj1 := Nil
    xGetObj1 := sToD("")
    // Se o get for data para inicilizar use dToS(''), se for numerico inicie com 0
    // objeto2
    oSayObj2 := Nil
    cSayObj2 := "Com ReadOnly"
    // objeto3
    oGetObj3 := Nil
    xGetObj3 := Space(10)
    // Se o get for data para inicilizar use dToS(''), se for numerico inicie com 0
    // objeto4
    oSayObj4 := Nil
    cSayObj4 := "Inativo"
    // objeto5
    oGetObj5 := Nil
    xGetObj5 := Space(10)
    // Se o get for data para inicilizar use dToS(''), se for numerico inicie com 0
    // objeto6
    oSayObj6 := Nil
    cSayObj6 := "PlaceHolder"
    // objeto7
    oGetObj7 := Nil
    xGetObj7 := Space(10)
    // Se o get for data para inicilizar use dToS(''), se for numerico inicie com 0
    // objeto8
    oSayObj8 := Nil
    cSayObj8 := "Com F3"
    // objeto9
    oGetObj9 := Nil
    xGetObj9 := Space(10)
    // Se o get for data para inicilizar use dToS(''), se for numerico inicie com 0
    // objeto10
    oSayObj10 := Nil
    cSayObj10 := "Com Picture"
    // objeto11
    oGetObj11 := Nil
    xGetObj11 := 0
    // Se o get for data para inicilizar use dToS(''), se for numerico inicie com 0
    // objeto12
    oSayObj12 := Nil
    cSayObj12 := "Com Valid"
    // objeto13
    oGetObj13 := Nil
    xGetObj13 := 0
    // Se o get for data para inicilizar use dToS(''), se for numerico inicie com 0
    // objeto14
    oBtnObj14 := Nil
    cBtnObj14 := "Button"
    bBtnObj14 := Nil
    // Cria a dialog
    oDialogPvt := TDialog():New(0, 0, nJanAltura, nJanLargur, cJanTitulo, Nil, Nil, Nil, Nil, Nil, nCorFundo, Nil, Nil, lDimPixels)
    // Criando um agrupamento ao redor dos says e gets
    nObjLinha := 2
    nObjColun := 2
    nObjLargu := nJanLargur / 2 - 2
    nObjAltur := nJanAltura / 2 - 2 - 25
    oGrpCampo := TGroup():New(nObjLinha, nObjColun, nObjAltur, nObjLargu, "Labels e Campos:", oDialogPvt, Nil, Nil, lDimPixels)
    oGrpCampo->oFont := oFontNegrit
    // objeto0 - usando a classe TSay
    nObjLinha := 4 + 10
    nObjColun := 4
    nObjLargu := 40
    nObjAltur := 6
    oSayObj0 := TSay():New(nObjLinha, nObjColun, Nil, oDialogPvt, Nil, oFontPadrao, Nil, Nil, Nil, lDimPixels, Nil, Nil, nObjLargu, nObjAltur, Nil, Nil, Nil, Nil, Nil)
    // objeto1 - usando a classe TGet
    nObjLinha := 3 + 10
    nObjColun := 49
    nObjLargu := 100
    nObjAltur := 10
    oGetObj1 := TGet():New(nObjLinha, nObjColun, Nil, oDialogPvt, nObjLargu, nObjAltur, Nil, Nil, Nil, Nil, oFontPadrao, Nil, Nil, lDimPixels)
    // oGetObj1:cPlaceHold := 'Digite aqui um texto...'   //Texto que sera exibido no campo antes de ter conteudo
    // oGetObj1:cF3        := 'Codigo da consulta padrao' //Codigo da consulta padrao / F3 que sera habilitada
    // oGetObj1:bValid     := {|| fFuncaoVld()}           //Funcao para validar o que foi digitado
    // oGetObj1:lReadOnly  := .T.                         //Para permitir o usuario clicar mas nao editar o campo
    // oGetObj1:lActive    := .F.                         //Para deixar o campo inativo e o usuario nao conseguir nem clicar
    // oGetObj1:Picture      := '@!'                        //Mascara / Picture do campo
    // objeto2 - usando a classe TSay
    nObjLinha := 19 + 10
    nObjColun := 4
    nObjLargu := 45
    nObjAltur := 6
    oSayObj2 := TSay():New(nObjLinha, nObjColun, Nil, oDialogPvt, Nil, oFontPadrao, Nil, Nil, Nil, lDimPixels, Nil, Nil, nObjLargu, nObjAltur, Nil, Nil, Nil, Nil, Nil)
    // objeto3 - usando a classe TGet
    nObjLinha := 18 + 10
    nObjColun := 49
    nObjLargu := 100
    nObjAltur := 10
    oGetObj3 := TGet():New(nObjLinha, nObjColun, Nil, oDialogPvt, nObjLargu, nObjAltur, Nil, Nil, Nil, Nil, oFontPadrao, Nil, Nil, lDimPixels)
    // oGetObj3:cPlaceHold := 'Digite aqui um texto...'   //Texto que sera exibido no campo antes de ter conteudo
    // oGetObj3:cF3        := 'Codigo da consulta padrao' //Codigo da consulta padrao / F3 que sera habilitada
    // oGetObj3:bValid     := {|| fFuncaoVld()}           //Funcao para validar o que foi digitado
    oGetObj3->lReadOnly := .T.
    // Para permitir o usuario clicar mas nao editar o campo
    // oGetObj3:lActive    := .F.                         //Para deixar o campo inativo e o usuario nao conseguir nem clicar
    // oGetObj3:Picture      := '@!'                        //Mascara / Picture do campo
    // objeto4 - usando a classe TSay
    nObjLinha := 34 + 10
    nObjColun := 4
    nObjLargu := 45
    nObjAltur := 6
    oSayObj4 := TSay():New(nObjLinha, nObjColun, Nil, oDialogPvt, Nil, oFontPadrao, Nil, Nil, Nil, lDimPixels, Nil, Nil, nObjLargu, nObjAltur, Nil, Nil, Nil, Nil, Nil)
    // objeto5 - usando a classe TGet
    nObjLinha := 33 + 10
    nObjColun := 49
    nObjLargu := 100
    nObjAltur := 10
    oGetObj5 := TGet():New(nObjLinha, nObjColun, Nil, oDialogPvt, nObjLargu, nObjAltur, Nil, Nil, Nil, Nil, oFontPadrao, Nil, Nil, lDimPixels)
    // oGetObj5:cPlaceHold := 'Digite aqui um texto...'   //Texto que sera exibido no campo antes de ter conteudo
    // oGetObj5:cF3        := 'Codigo da consulta padrao' //Codigo da consulta padrao / F3 que sera habilitada
    // oGetObj5:bValid     := {|| fFuncaoVld()}           //Funcao para validar o que foi digitado
    // oGetObj5:lReadOnly  := .T.                         //Para permitir o usuario clicar mas nao editar o campo
    oGetObj5->lActive := .F.
    // Para deixar o campo inativo e o usuario nao conseguir nem clicar
    // oGetObj5:Picture      := '@!'                        //Mascara / Picture do campo
    // objeto6 - usando a classe TSay
    nObjLinha := 49 + 10
    nObjColun := 4
    nObjLargu := 45
    nObjAltur := 6
    oSayObj6 := TSay():New(nObjLinha, nObjColun, Nil, oDialogPvt, Nil, oFontPadrao, Nil, Nil, Nil, lDimPixels, Nil, Nil, nObjLargu, nObjAltur, Nil, Nil, Nil, Nil, Nil)
    // objeto7 - usando a classe TGet
    nObjLinha := 48 + 10
    nObjColun := 49
    nObjLargu := 100
    nObjAltur := 10
    oGetObj7 := TGet():New(nObjLinha, nObjColun, Nil, oDialogPvt, nObjLargu, nObjAltur, Nil, Nil, Nil, Nil, oFontPadrao, Nil, Nil, lDimPixels)
    oGetObj7->cPlaceHold := "Digite aqui um texto..."
    // Texto que sera exibido no campo antes de ter conteudo
    // oGetObj7:cF3        := 'Codigo da consulta padrao' //Codigo da consulta padrao / F3 que sera habilitada
    // oGetObj7:bValid     := {|| fFuncaoVld()}           //Funcao para validar o que foi digitado
    // oGetObj7:lReadOnly  := .T.                         //Para permitir o usuario clicar mas nao editar o campo
    // oGetObj7:lActive    := .F.                         //Para deixar o campo inativo e o usuario nao conseguir nem clicar
    // oGetObj7:Picture      := '@!'                        //Mascara / Picture do campo
    // objeto8 - usando a classe TSay
    nObjLinha := 64 + 10
    nObjColun := 4
    nObjLargu := 45
    nObjAltur := 6
    oSayObj8 := TSay():New(nObjLinha, nObjColun, Nil, oDialogPvt, Nil, oFontPadrao, Nil, Nil, Nil, lDimPixels, Nil, Nil, nObjLargu, nObjAltur, Nil, Nil, Nil, Nil, Nil)
    // objeto9 - usando a classe TGet
    nObjLinha := 63 + 10
    nObjColun := 49
    nObjLargu := 100
    nObjAltur := 10
    oGetObj9 := TGet():New(nObjLinha, nObjColun, Nil, oDialogPvt, nObjLargu, nObjAltur, Nil, Nil, Nil, Nil, oFontPadrao, Nil, Nil, lDimPixels, Nil, Nil, Nil, Nil, Nil, Nil, Nil, Nil, Nil, Nil, Nil, Nil, Nil, .T.)
    // oGetObj9:cPlaceHold := 'Digite aqui um texto...'   //Texto que sera exibido no campo antes de ter conteudo
    oGetObj9->cF3 := "SB1"
    // Codigo da consulta padrao / F3 que sera habilitada
    // oGetObj9:bValid     := {|| fFuncaoVld()}           //Funcao para validar o que foi digitado
    // oGetObj9:lReadOnly  := .T.                         //Para permitir o usuario clicar mas nao editar o campo
    // oGetObj9:lActive    := .F.                         //Para deixar o campo inativo e o usuario nao conseguir nem clicar
    // oGetObj9:Picture      := '@!'                        //Mascara / Picture do campo
    // objeto10 - usando a classe TSay
    nObjLinha := 79 + 10
    nObjColun := 4
    nObjLargu := 45
    nObjAltur := 6
    oSayObj10 := TSay():New(nObjLinha, nObjColun, Nil, oDialogPvt, Nil, oFontPadrao, Nil, Nil, Nil, lDimPixels, Nil, Nil, nObjLargu, nObjAltur, Nil, Nil, Nil, Nil, Nil)
    // objeto11 - usando a classe TGet
    nObjLinha := 78 + 10
    nObjColun := 49
    nObjLargu := 100
    nObjAltur := 10
    oGetObj11 := TGet():New(nObjLinha, nObjColun, Nil, oDialogPvt, nObjLargu, nObjAltur, Nil, Nil, Nil, Nil, oFontPadrao, Nil, Nil, lDimPixels)
    // oGetObj11:cPlaceHold := 'Digite aqui um texto...'   //Texto que sera exibido no campo antes de ter conteudo
    // oGetObj11:cF3        := 'Codigo da consulta padrao' //Codigo da consulta padrao / F3 que sera habilitada
    // oGetObj11:bValid     := {|| fFuncaoVld()}           //Funcao para validar o que foi digitado
    // oGetObj11:lReadOnly  := .T.                         //Para permitir o usuario clicar mas nao editar o campo
    // oGetObj11:lActive    := .F.                         //Para deixar o campo inativo e o usuario nao conseguir nem clicar
    oGetObj11->Picture := "@E 999.99"
    // Mascara / Picture do campo
    // objeto12 - usando a classe TSay
    nObjLinha := 94 + 10
    nObjColun := 4
    nObjLargu := 45
    nObjAltur := 6
    oSayObj12 := TSay():New(nObjLinha, nObjColun, Nil, oDialogPvt, Nil, oFontPadrao, Nil, Nil, Nil, lDimPixels, Nil, Nil, nObjLargu, nObjAltur, Nil, Nil, Nil, Nil, Nil)
    // objeto13 - usando a classe TGet
    nObjLinha := 93 + 10
    nObjColun := 49
    nObjLargu := 100
    nObjAltur := 10
    oGetObj13 := TGet():New(nObjLinha, nObjColun, Nil, oDialogPvt, nObjLargu, nObjAltur, Nil, Nil, Nil, Nil, oFontPadrao, Nil, Nil, lDimPixels)
    // oGetObj13:cPlaceHold := 'Digite aqui um texto...'   //Texto que sera exibido no campo antes de ter conteudo
    // oGetObj13:cF3        := 'Codigo da consulta padrao' //Codigo da consulta padrao / F3 que sera habilitada
    oGetObj13->bValid := Nil
    // Funcao para validar o que foi digitado
    // oGetObj13:lReadOnly  := .T.                         //Para permitir o usuario clicar mas nao editar o campo
    // oGetObj13:lActive    := .F.                         //Para deixar o campo inativo e o usuario nao conseguir nem clicar
    oGetObj13->Picture := "@E 999"
    // Mascara / Picture do campo
    // Criando um agrupamento ao redor dos botões e sem texto
    nObjLinha := nJanAltura / 2 - 23
    nObjColun := 2
    nObjLargu := nJanLargur / 2 - 2
    nObjAltur := nJanAltura / 2 - 2
    oGrpBotao := TGroup():New(nObjLinha, nObjColun, nObjAltur, nObjLargu, "", oDialogPvt, Nil, Nil, lDimPixels)
    // objeto14 - usando a classe TButton
    nObjLinha := nJanAltura / 2 - 20
    nObjColun := 12
    nObjLargu := nJanLargur / 2 - 24
    nObjAltur := 15
    oBtnObj14 := TButton():New(nObjLinha, nObjColun, cBtnObj14, oDialogPvt, bBtnObj14, nObjLargu, nObjAltur, Nil, oFontPadrao, Nil, lDimPixels)
    // Ativa e exibe a janela
    oDialogPvt:Activate(Nil, Nil, Nil, lCentraliz, Nil, Nil, bBlocoIni)
    FWRestArea(aArea)
    RETURN Static

FUNCTION fValidVlr()
    LOCAL aArea, lRet

    aArea := FWGetArea()
    lRet := .T.
    If xGetObj13 > 0
        lRet := .T.
    Else
        lRet := .F.
        Alert("Falha na validação")
    EndIf
    FWRestArea(aArea)
    RETURN lRet
