// caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2024/06/25/abrindo-videos-e-musicas-atraves-da-tmediaplayer-maratona-advpl-e-tl-498/
// Bibliotecas
#Include "TOTVS.ch"
// {Protheus.doc} User Function zExe498
// Abre o Windows Media Player em uma Dialog
// @type Function
// @author Atilio
// @since 04/04/2023
// @see https://tdn.totvs.com/display/tec/TMediaPlayer
// O exemplo dessa dialog foi baseado no link acima disponível no TDN
// **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
USER FUNCTION zExe498()
    LOCAL aArea, nCorFundo, nJanAltura, nJanLargur, cJanTitulo, lDimPixels, lCentraliz, nObjLinha, nObjColun, nObjLargu, nObjAltur, lShowBar, lIsMute, nVolume, cFontNome, oFontPadrao, oMedia, oBtnOpen, bBtnOpen, oBtnPlay, bBtnPlay, oBtnPause, bBtnPause, oBtnStop, bBtnStop, oBtnSetVol, bBtnSetVol, oBtnGetVol, bBtnGetVol, oBtnShoBar, bBtnShoBar, oBtnRepeat, bBtnRepeat, oBtnMute, bBtnMute, oDialogPvt

    aArea := FWGetArea()
    nCorFundo := RGB(238, 238, 238)
    nJanAltura := 500
    nJanLargur := 800
    cJanTitulo := "Exemplo TMediaPlayer"
    lDimPixels := .T.
    lCentraliz := .T.
    nObjLinha := 0
    nObjColun := 0
    nObjLargu := 0
    nObjAltur := 0
    lShowBar := .F.
    lIsMute := .F.
    nVolume := 70
    cFontNome := "Tahoma"
    oFontPadrao := TFont():New(cFontNome, Nil, - 12)
    oMedia := Nil
    oBtnOpen := Nil
    bBtnOpen := Nil
    oBtnPlay := Nil
    bBtnPlay := Nil
    oBtnPause := Nil
    bBtnPause := Nil
    oBtnStop := Nil
    bBtnStop := Nil
    oBtnSetVol := Nil
    bBtnSetVol := Nil
    oBtnGetVol := Nil
    bBtnGetVol := Nil
    oBtnShoBar := Nil
    bBtnShoBar := Nil
    oBtnRepeat := Nil
    bBtnRepeat := Nil
    oBtnMute := Nil
    bBtnMute := Nil
    // Cria a dialog
    oDialogPvt := TDialog():New(0, 0, nJanAltura, nJanLargur, cJanTitulo, Nil, Nil, Nil, Nil, Nil, nCorFundo, Nil, Nil, lDimPixels)
    // Cria o Media Player
    nObjLinha := 3
    nObjColun := 3
    nObjLargu := nJanLargur / 2 - 56
    nObjAltur := nJanAltura / 2 - 3
    oMedia := TMediaPlayer():New(nObjLinha, nObjColun, nObjLargu, nObjAltur, oDialogPvt, "C:\OBS\Vídeos Prontos\intro_free.mp4", nVolume, lShowBar)
    // Cria os botões na direita
    nObjLinha := 3
    nObjColun := nJanLargur / 2 - 50
    nObjLargu := 47
    nObjAltur := 15
    oBtnOpen := TButton():New(nObjLinha + nObjAltur + 3 * 0, nObjColun, "Abrir Arq.", oDialogPvt, bBtnOpen, nObjLargu, nObjAltur, Nil, oFontPadrao, Nil, lDimPixels)
    oBtnPlay := TButton():New(nObjLinha + nObjAltur + 3 * 1, nObjColun, "Play", oDialogPvt, bBtnPlay, nObjLargu, nObjAltur, Nil, oFontPadrao, Nil, lDimPixels)
    oBtnPause := TButton():New(nObjLinha + nObjAltur + 3 * 2, nObjColun, "Pausar", oDialogPvt, bBtnPause, nObjLargu, nObjAltur, Nil, oFontPadrao, Nil, lDimPixels)
    oBtnStop := TButton():New(nObjLinha + nObjAltur + 3 * 3, nObjColun, "Parar", oDialogPvt, bBtnStop, nObjLargu, nObjAltur, Nil, oFontPadrao, Nil, lDimPixels)
    oBtnSetVol := TButton():New(nObjLinha + nObjAltur + 3 * 4, nObjColun, "Def. Volume", oDialogPvt, bBtnSetVol, nObjLargu, nObjAltur, Nil, oFontPadrao, Nil, lDimPixels)
    oBtnGetVol := TButton():New(nObjLinha + nObjAltur + 3 * 5, nObjColun, "Ver Volume", oDialogPvt, bBtnGetVol, nObjLargu, nObjAltur, Nil, oFontPadrao, Nil, lDimPixels)
    oBtnShoBar := TButton():New(nObjLinha + nObjAltur + 3 * 6, nObjColun, "Mostr.Barra", oDialogPvt, bBtnShoBar, nObjLargu, nObjAltur, Nil, oFontPadrao, Nil, lDimPixels)
    oBtnRepeat := TButton():New(nObjLinha + nObjAltur + 3 * 7, nObjColun, "Repetir", oDialogPvt, bBtnRepeat, nObjLargu, nObjAltur, Nil, oFontPadrao, Nil, lDimPixels)
    oBtnMute := TButton():New(nObjLinha + nObjAltur + 3 * 8, nObjColun, "Mudo", oDialogPvt, bBtnMute, nObjLargu, nObjAltur, Nil, oFontPadrao, Nil, lDimPixels)
    // Ativa e exibe a janela
    oDialogPvt:Activate(Nil, Nil, Nil, lCentraliz)
    FWRestArea(aArea)
    RETURN
