# Esse exemplo faz parte da série do YouTube, Maratona de Exemplos, do canal Terminal de Informação, 
#     caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2024/06/25/abrindo-videos-e-musicas-atraves-da-tmediaplayer-maratona-advpl-e-tl-498/
# Bibliotecas
# PREPROCESSOR: #Include "TOTVS.ch"
# {Protheus.doc} User Function zExe498
# Abre o Windows Media Player em uma Dialog
# @type Function
# @author Atilio
# @since 04/04/2023
# @see https://tdn.totvs.com/display/tec/TMediaPlayer
# @obs 
# 
#     O exemplo dessa dialog foi baseado no link acima disponível no TDN
# 
#     **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
def u_zExe498():
    aArea = FWGetArea()
    nCorFundo = RGB(238, 238, 238)
    nJanAltura = 500
    nJanLargur = 800
    cJanTitulo = 'Exemplo TMediaPlayer'
    lDimPixels = True
    lCentraliz = True
    nObjLinha = 0
    nObjColun = 0
    nObjLargu = 0
    nObjAltur = 0
    lShowBar = False
    lIsMute = False
    nVolume = 70
    cFontNome = 'Tahoma'
    oFontPadrao = TFont().New(cFontNome, None, -12)
    oMedia = None
    oBtnOpen = None
    bBtnOpen = lambda : oMedia.OpenFile(FWInputBox('Escolha o arquivo', 'C:\\OBS\\'))
    oBtnPlay = None
    bBtnPlay = lambda : oMedia.Play()
    oBtnPause = None
    bBtnPause = lambda : oMedia.Pause()
    oBtnStop = None
    bBtnStop = lambda : oMedia.Stop()
    oBtnSetVol = None
    bBtnSetVol = lambda : oMedia.SetVolume(Val(FWInputBox('Insira o volume (0 a 100)', cValToChar(oMedia.nVolume()))))
    oBtnGetVol = None
    bBtnGetVol = lambda : FWAlertInfo('O volume está em ' + cValToChar(oMedia.nVolume()), 'Teste TMediaPlayer')
    oBtnShoBar = None
    bBtnShoBar = lambda : [(lShowBar := not lShowBar), oMedia.SetShowBar(lShowBar)]
    oBtnRepeat = None
    bBtnRepeat = lambda : (setattr(oMedia, 'nPlayCount', Val(FWInputBox('Defina o número de repetições', cValToChar(oMedia.nPlayCount())))) or Val(FWInputBox('Defina o número de repetições', cValToChar(oMedia.nPlayCount()))))
    oBtnMute = None
    bBtnMute = lambda : [(lIsMute := not lIsMute), oMedia.SetMute(lIsMute)]
    # Cria a dialog
    oDialogPvt = TDialog().New(0, 0, nJanAltura, nJanLargur, cJanTitulo, None, None, None, None, None, nCorFundo, None, None, lDimPixels)
    # Cria o Media Player
    nObjLinha = 3
    nObjColun = 3
    nObjLargu = nJanLargur / 2 - 56
    nObjAltur = nJanAltura / 2 - 3
    oMedia = TMediaPlayer().New(nObjLinha, nObjColun, nObjLargu, nObjAltur, oDialogPvt, 'C:\\OBS\\Vídeos Prontos\\intro_free.mp4', nVolume, lShowBar)
    # Cria os botões na direita
    nObjLinha = 3
    nObjColun = nJanLargur / 2 - 50
    nObjLargu = 47
    nObjAltur = 15
    oBtnOpen = TButton().New(nObjLinha + nObjAltur + 3 * 0, nObjColun, 'Abrir Arq.', oDialogPvt, bBtnOpen, nObjLargu, nObjAltur, None, oFontPadrao, None, lDimPixels)
    oBtnPlay = TButton().New(nObjLinha + nObjAltur + 3 * 1, nObjColun, 'Play', oDialogPvt, bBtnPlay, nObjLargu, nObjAltur, None, oFontPadrao, None, lDimPixels)
    oBtnPause = TButton().New(nObjLinha + nObjAltur + 3 * 2, nObjColun, 'Pausar', oDialogPvt, bBtnPause, nObjLargu, nObjAltur, None, oFontPadrao, None, lDimPixels)
    oBtnStop = TButton().New(nObjLinha + nObjAltur + 3 * 3, nObjColun, 'Parar', oDialogPvt, bBtnStop, nObjLargu, nObjAltur, None, oFontPadrao, None, lDimPixels)
    oBtnSetVol = TButton().New(nObjLinha + nObjAltur + 3 * 4, nObjColun, 'Def. Volume', oDialogPvt, bBtnSetVol, nObjLargu, nObjAltur, None, oFontPadrao, None, lDimPixels)
    oBtnGetVol = TButton().New(nObjLinha + nObjAltur + 3 * 5, nObjColun, 'Ver Volume', oDialogPvt, bBtnGetVol, nObjLargu, nObjAltur, None, oFontPadrao, None, lDimPixels)
    oBtnShoBar = TButton().New(nObjLinha + nObjAltur + 3 * 6, nObjColun, 'Mostr.Barra', oDialogPvt, bBtnShoBar, nObjLargu, nObjAltur, None, oFontPadrao, None, lDimPixels)
    oBtnRepeat = TButton().New(nObjLinha + nObjAltur + 3 * 7, nObjColun, 'Repetir', oDialogPvt, bBtnRepeat, nObjLargu, nObjAltur, None, oFontPadrao, None, lDimPixels)
    oBtnMute = TButton().New(nObjLinha + nObjAltur + 3 * 8, nObjColun, 'Mudo', oDialogPvt, bBtnMute, nObjLargu, nObjAltur, None, oFontPadrao, None, lDimPixels)
    # Ativa e exibe a janela
    oDialogPvt.Activate(None, None, None, lCentraliz)
    FWRestArea(aArea)
    return
