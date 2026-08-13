# Esse exemplo faz parte da série do YouTube, Maratona de Exemplos, do canal Terminal de Informação, 
#     caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2024/06/27/aplicando-uma-mascara-atraves-da-transform-maratona-advpl-e-tl-503/
# Bibliotecas
# PREPROCESSOR: #Include "TOTVS.ch"
# {Protheus.doc} User Function zExe502
# Cria paineis em uma Dialog
# @type Function
# @author Atilio
# @since 27/03/2023
# @see https://tdn.totvs.com/display/tec/TPanel
# @obs 
# 
#     **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
def u_zExe502():
    aArea = FWGetArea()
    nCorFundo = RGB(238, 238, 238)
    nJanAltura = 301
    nJanLargur = 338
    cJanTitulo = 'Exemplo TPanel'
    lDimPixels = True
    lCentraliz = True
    nObjLinha = 0
    nObjColun = 0
    nObjLargu = 0
    nObjAltur = 0
    cFontNome = 'Tahoma'
    oFontPadrao = TFont().New(cFontNome, None, -12)
    oFontNegrit = TFont().New(cFontNome, None, -12, None, True)
    oDialogPvt = None
    bBlocoIni = lambda : None
    # Aqui voce pode acionar funcoes customizadas que irao ser acionadas ao abrir a dialog
    # objeto0
    oSayObj0 = None
    cSayObj0 = 'Normal'
    # objeto1
    oGetObj1 = None
    xGetObj1 = sToD('')
    # Se o get for data para inicilizar use dToS(''), se for numerico inicie com 0
    # objeto2
    oSayObj2 = None
    cSayObj2 = 'Com ReadOnly'
    # objeto3
    oGetObj3 = None
    xGetObj3 = Space(10)
    # Se o get for data para inicilizar use dToS(''), se for numerico inicie com 0
    # objeto4
    oSayObj4 = None
    cSayObj4 = 'Inativo'
    # objeto5
    oGetObj5 = None
    xGetObj5 = Space(10)
    # Se o get for data para inicilizar use dToS(''), se for numerico inicie com 0
    # objeto6
    oSayObj6 = None
    cSayObj6 = 'PlaceHolder'
    # objeto7
    oGetObj7 = None
    xGetObj7 = Space(10)
    # Se o get for data para inicilizar use dToS(''), se for numerico inicie com 0
    # objeto8
    oSayObj8 = None
    cSayObj8 = 'Com F3'
    # objeto9
    oGetObj9 = None
    xGetObj9 = Space(10)
    # Se o get for data para inicilizar use dToS(''), se for numerico inicie com 0
    # objeto10
    oSayObj10 = None
    cSayObj10 = 'Com Picture'
    # objeto11
    oGetObj11 = None
    xGetObj11 = 0
    # Se o get for data para inicilizar use dToS(''), se for numerico inicie com 0
    # objeto12
    oSayObj12 = None
    cSayObj12 = 'Com Valid'
    # objeto13
    oGetObj13 = None
    xGetObj13 = 0
    # Se o get for data para inicilizar use dToS(''), se for numerico inicie com 0
    # objeto14
    oBtnObj14 = None
    cBtnObj14 = 'Button'
    bBtnObj14 = lambda : MsgInfo('Clicou no OK', 'Atenção')
    # Cria a dialog
    oDialogPvt = TDialog().New(0, 0, nJanAltura, nJanLargur, cJanTitulo, None, None, None, None, None, nCorFundo, None, None, lDimPixels)
    # Criando um agrupamento ao redor dos says e gets
    nObjLinha = 2
    nObjColun = 2
    nObjLargu = nJanLargur / 2 - 2
    nObjAltur = nJanAltura / 2 - 2 - 25
    oPanCampo = TPanel().New(nObjLinha, nObjColun, '', oDialogPvt, None, None, None, None, RGB(255, 200, 200), nObjLargu, nObjAltur)
    # objeto0 - usando a classe TSay
    nObjLinha = 4 + 10
    nObjColun = 4
    nObjLargu = 40
    nObjAltur = 6
    oSayObj0 = TSay().New(nObjLinha, nObjColun, lambda : cSayObj0, oDialogPvt, None, oFontPadrao, None, None, None, lDimPixels, None, None, nObjLargu, nObjAltur, None, None, None, None, None)
    # objeto1 - usando a classe TGet
    nObjLinha = 3 + 10
    nObjColun = 49
    nObjLargu = 100
    nObjAltur = 10
    oGetObj1 = TGet().New(nObjLinha, nObjColun, lambda u: ((xGetObj1 := u) if PCount() > 0 else xGetObj1), oDialogPvt, nObjLargu, nObjAltur, None, None, None, None, oFontPadrao, None, None, lDimPixels)
    # oGetObj1:cPlaceHold := 'Digite aqui um texto...'   //Texto que sera exibido no campo antes de ter conteudo
    # oGetObj1:cF3        := 'Codigo da consulta padrao' //Codigo da consulta padrao / F3 que sera habilitada
    # oGetObj1:bValid     := {|| fFuncaoVld()}           //Funcao para validar o que foi digitado
    # oGetObj1:lReadOnly  := .T.                         //Para permitir o usuario clicar mas nao editar o campo
    # oGetObj1:lActive    := .F.                         //Para deixar o campo inativo e o usuario nao conseguir nem clicar
    # oGetObj1:Picture      := '@!'                        //Mascara / Picture do campo
    # objeto2 - usando a classe TSay
    nObjLinha = 19 + 10
    nObjColun = 4
    nObjLargu = 45
    nObjAltur = 6
    oSayObj2 = TSay().New(nObjLinha, nObjColun, lambda : cSayObj2, oDialogPvt, None, oFontPadrao, None, None, None, lDimPixels, None, None, nObjLargu, nObjAltur, None, None, None, None, None)
    # objeto3 - usando a classe TGet
    nObjLinha = 18 + 10
    nObjColun = 49
    nObjLargu = 100
    nObjAltur = 10
    oGetObj3 = TGet().New(nObjLinha, nObjColun, lambda u: ((xGetObj3 := u) if PCount() > 0 else xGetObj3), oDialogPvt, nObjLargu, nObjAltur, None, None, None, None, oFontPadrao, None, None, lDimPixels)
    # oGetObj3:cPlaceHold := 'Digite aqui um texto...'   //Texto que sera exibido no campo antes de ter conteudo
    # oGetObj3:cF3        := 'Codigo da consulta padrao' //Codigo da consulta padrao / F3 que sera habilitada
    # oGetObj3:bValid     := {|| fFuncaoVld()}           //Funcao para validar o que foi digitado
    oGetObj3.lReadOnly = True
    # Para permitir o usuario clicar mas nao editar o campo
    # oGetObj3:lActive    := .F.                         //Para deixar o campo inativo e o usuario nao conseguir nem clicar
    # oGetObj3:Picture      := '@!'                        //Mascara / Picture do campo
    # objeto4 - usando a classe TSay
    nObjLinha = 34 + 10
    nObjColun = 4
    nObjLargu = 45
    nObjAltur = 6
    oSayObj4 = TSay().New(nObjLinha, nObjColun, lambda : cSayObj4, oDialogPvt, None, oFontPadrao, None, None, None, lDimPixels, None, None, nObjLargu, nObjAltur, None, None, None, None, None)
    # objeto5 - usando a classe TGet
    nObjLinha = 33 + 10
    nObjColun = 49
    nObjLargu = 100
    nObjAltur = 10
    oGetObj5 = TGet().New(nObjLinha, nObjColun, lambda u: ((xGetObj5 := u) if PCount() > 0 else xGetObj5), oDialogPvt, nObjLargu, nObjAltur, None, None, None, None, oFontPadrao, None, None, lDimPixels)
    # oGetObj5:cPlaceHold := 'Digite aqui um texto...'   //Texto que sera exibido no campo antes de ter conteudo
    # oGetObj5:cF3        := 'Codigo da consulta padrao' //Codigo da consulta padrao / F3 que sera habilitada
    # oGetObj5:bValid     := {|| fFuncaoVld()}           //Funcao para validar o que foi digitado
    # oGetObj5:lReadOnly  := .T.                         //Para permitir o usuario clicar mas nao editar o campo
    oGetObj5.lActive = False
    # Para deixar o campo inativo e o usuario nao conseguir nem clicar
    # oGetObj5:Picture      := '@!'                        //Mascara / Picture do campo
    # objeto6 - usando a classe TSay
    nObjLinha = 49 + 10
    nObjColun = 4
    nObjLargu = 45
    nObjAltur = 6
    oSayObj6 = TSay().New(nObjLinha, nObjColun, lambda : cSayObj6, oDialogPvt, None, oFontPadrao, None, None, None, lDimPixels, None, None, nObjLargu, nObjAltur, None, None, None, None, None)
    # objeto7 - usando a classe TGet
    nObjLinha = 48 + 10
    nObjColun = 49
    nObjLargu = 100
    nObjAltur = 10
    oGetObj7 = TGet().New(nObjLinha, nObjColun, lambda u: ((xGetObj7 := u) if PCount() > 0 else xGetObj7), oDialogPvt, nObjLargu, nObjAltur, None, None, None, None, oFontPadrao, None, None, lDimPixels)
    oGetObj7.cPlaceHold = 'Digite aqui um texto...'
    # Texto que sera exibido no campo antes de ter conteudo
    # oGetObj7:cF3        := 'Codigo da consulta padrao' //Codigo da consulta padrao / F3 que sera habilitada
    # oGetObj7:bValid     := {|| fFuncaoVld()}           //Funcao para validar o que foi digitado
    # oGetObj7:lReadOnly  := .T.                         //Para permitir o usuario clicar mas nao editar o campo
    # oGetObj7:lActive    := .F.                         //Para deixar o campo inativo e o usuario nao conseguir nem clicar
    # oGetObj7:Picture      := '@!'                        //Mascara / Picture do campo
    # objeto8 - usando a classe TSay
    nObjLinha = 64 + 10
    nObjColun = 4
    nObjLargu = 45
    nObjAltur = 6
    oSayObj8 = TSay().New(nObjLinha, nObjColun, lambda : cSayObj8, oDialogPvt, None, oFontPadrao, None, None, None, lDimPixels, None, None, nObjLargu, nObjAltur, None, None, None, None, None)
    # objeto9 - usando a classe TGet
    nObjLinha = 63 + 10
    nObjColun = 49
    nObjLargu = 100
    nObjAltur = 10
    oGetObj9 = TGet().New(nObjLinha, nObjColun, lambda u: ((xGetObj9 := u) if PCount() > 0 else xGetObj9), oDialogPvt, nObjLargu, nObjAltur, None, None, None, None, oFontPadrao, None, None, lDimPixels, None, None, None, None, None, None, None, None, None, None, None, None, None, True)
    # oGetObj9:cPlaceHold := 'Digite aqui um texto...'   //Texto que sera exibido no campo antes de ter conteudo
    oGetObj9.cF3 = 'SB1'
    # Codigo da consulta padrao / F3 que sera habilitada
    # oGetObj9:bValid     := {|| fFuncaoVld()}           //Funcao para validar o que foi digitado
    # oGetObj9:lReadOnly  := .T.                         //Para permitir o usuario clicar mas nao editar o campo
    # oGetObj9:lActive    := .F.                         //Para deixar o campo inativo e o usuario nao conseguir nem clicar
    # oGetObj9:Picture      := '@!'                        //Mascara / Picture do campo
    # objeto10 - usando a classe TSay
    nObjLinha = 79 + 10
    nObjColun = 4
    nObjLargu = 45
    nObjAltur = 6
    oSayObj10 = TSay().New(nObjLinha, nObjColun, lambda : cSayObj10, oDialogPvt, None, oFontPadrao, None, None, None, lDimPixels, None, None, nObjLargu, nObjAltur, None, None, None, None, None)
    # objeto11 - usando a classe TGet
    nObjLinha = 78 + 10
    nObjColun = 49
    nObjLargu = 100
    nObjAltur = 10
    oGetObj11 = TGet().New(nObjLinha, nObjColun, lambda u: ((xGetObj11 := u) if PCount() > 0 else xGetObj11), oDialogPvt, nObjLargu, nObjAltur, None, None, None, None, oFontPadrao, None, None, lDimPixels)
    # oGetObj11:cPlaceHold := 'Digite aqui um texto...'   //Texto que sera exibido no campo antes de ter conteudo
    # oGetObj11:cF3        := 'Codigo da consulta padrao' //Codigo da consulta padrao / F3 que sera habilitada
    # oGetObj11:bValid     := {|| fFuncaoVld()}           //Funcao para validar o que foi digitado
    # oGetObj11:lReadOnly  := .T.                         //Para permitir o usuario clicar mas nao editar o campo
    # oGetObj11:lActive    := .F.                         //Para deixar o campo inativo e o usuario nao conseguir nem clicar
    oGetObj11.Picture = '@E 999.99'
    # Mascara / Picture do campo
    # objeto12 - usando a classe TSay
    nObjLinha = 94 + 10
    nObjColun = 4
    nObjLargu = 45
    nObjAltur = 6
    oSayObj12 = TSay().New(nObjLinha, nObjColun, lambda : cSayObj12, oDialogPvt, None, oFontPadrao, None, None, None, lDimPixels, None, None, nObjLargu, nObjAltur, None, None, None, None, None)
    # objeto13 - usando a classe TGet
    nObjLinha = 93 + 10
    nObjColun = 49
    nObjLargu = 100
    nObjAltur = 10
    oGetObj13 = TGet().New(nObjLinha, nObjColun, lambda u: ((xGetObj13 := u) if PCount() > 0 else xGetObj13), oDialogPvt, nObjLargu, nObjAltur, None, None, None, None, oFontPadrao, None, None, lDimPixels)
    # oGetObj13:cPlaceHold := 'Digite aqui um texto...'   //Texto que sera exibido no campo antes de ter conteudo
    # oGetObj13:cF3        := 'Codigo da consulta padrao' //Codigo da consulta padrao / F3 que sera habilitada
    oGetObj13.bValid = lambda : fValidVlr()
    # Funcao para validar o que foi digitado
    # oGetObj13:lReadOnly  := .T.                         //Para permitir o usuario clicar mas nao editar o campo
    # oGetObj13:lActive    := .F.                         //Para deixar o campo inativo e o usuario nao conseguir nem clicar
    oGetObj13.Picture = '@E 999'
    # Mascara / Picture do campo
    # Criando um agrupamento ao redor dos botões e sem texto
    nObjLinha = nJanAltura / 2 - 23
    nObjColun = 2
    nObjLargu = nJanLargur / 2 - 2
    nObjAltur = nJanAltura / 2 - 2
    oPanBotao = TPanel().New(nObjLinha, nObjColun, '', oDialogPvt, None, None, None, None, RGB(200, 200, 255), nObjLargu, nObjAltur)
    # objeto14 - usando a classe TButton
    nObjLinha = nJanAltura / 2 - 20
    nObjColun = 12
    nObjLargu = nJanLargur / 2 - 24
    nObjAltur = 15
    oBtnObj14 = TButton().New(nObjLinha, nObjColun, cBtnObj14, oDialogPvt, bBtnObj14, nObjLargu, nObjAltur, None, oFontPadrao, None, lDimPixels)
    # Ativa e exibe a janela
    oDialogPvt.Activate(None, None, None, lCentraliz, None, None, bBlocoIni)
    FWRestArea(aArea)
    return Static

def fValidVlr():
    aArea = FWGetArea()
    lRet = True
    if xGetObj13 > 0:
        lRet = True
    else:
        lRet = False
        Alert('Falha na validação')

    FWRestArea(aArea)
    return lRet
