# Esse exemplo faz parte da série do YouTube, Maratona de Exemplos, do canal Terminal de Informação, 
#     caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2024/02/26/buscando-a-filial-usada-em-uma-tabela-com-fwxfilial-e-xfilial-maratona-advpl-e-tl-259/
# Bibliotecas
# PREPROCESSOR: #Include "TOTVS.ch"
# {Protheus.doc} User Function zExe258
# Classe para criar uma uma navegação de Wizard (com opção de avançar ou retroceder)
# @type  Function
# @author Atilio
# @since 21/02/2023
# @see https://tdn.totvs.com/display/public/framework/FWWizardControl
# @obs 
#     
#     **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
def u_zExe258():
    aArea = FWGetArea()
    nCorFundo = RGB(238, 238, 238)
    nJanAltura = 400
    nJanLargur = 600
    cJanTitulo = 'Exemplo FWWizardControl'
    lCentraliz = True
    lDimPixels = True
    nObjLinha = 0
    nObjColun = 0
    nObjLargu = 0
    nObjAltur = 0
    cFontNome = 'Tahoma'
    oFontPadrao = TFont().New(cFontNome, None, -12)
    oDialogPvt = None
    bBlocoIni = lambda : None
    # Aqui voce pode acionar funcoes customizadas que irao ser acionadas ao abrir a dialog
    # objeto1
    oSayInsira = None
    cSayInsira = 'Insira o Texto:'
    # objeto2
    oGetTexto = None
    cGetTexto = 'https://terminaldeinformacao.com' + Space(200)
    # objeto3
    oQrCode = None
    # objeto4
    oSayFim = None
    cSayFim = 'Wizard concluído!'
    # Objetos do Wizard
    oPanelGer = None
    oWizard = None
    # Cria a dialog
    oDialogPvt = TDialog().New(0, 0, nJanAltura, nJanLargur, cJanTitulo, None, None, None, None, None, nCorFundo, None, None, lDimPixels)
    # Cria um painel geral
    oPanelGer = TPanel().New(1, 1, '', oDialogPvt, None, None, None, RGB(0, 0, 0), RGB(254, 254, 254), nJanLargur / 2 - 1, nJanAltura / 2 - 3)
    # Instancia o Wizard
    oWizard = FWWizardControl().New(oPanelGer)
    oWizard.ActiveUISteps()
    # Página 1 do Wizard (terá um campo para o usuário digitar)
    oNewPag = oWizard.AddStep('1')
    oNewPag.SetStepDescription('Definição para usar o QRCode')
    oNewPag.SetConstruction(lambda oPanel: fCriaPag1(oPanel))
    oNewPag.SetNextAction(lambda : fValidPag1())
    oNewPag.SetCancelAction(lambda : fEncerra())
    # Página 2 do Wizard
    oNewPag = oWizard.AddStep('2', lambda oPanel: fCriaPag2(oPanel))
    oNewPag.SetStepDescription('QRCode Gerado')
    oNewPag.SetNextAction(lambda : True)
    oNewPag.SetPrevAction(lambda : True)
    oNewPag.SetCancelAction(lambda : fEncerra())
    # Página 3 do Wizard
    oNewPag = oWizard.AddStep('3', lambda oPanel: fCriaPag3(oPanel))
    oNewPag.SetStepDescription('Teste concluído')
    oNewPag.SetNextAction(lambda : fEncerra())
    oNewPag.SetPrevAction(lambda : True)
    oNewPag.SetCancelAction(lambda : fEncerra())
    # Ativa o Wizard para visualização
    oWizard.Activate()
    # Ativa e exibe a janela
    oDialogPvt.Activate(None, None, None, lCentraliz, None, None, bBlocoIni)
    FWRestArea(aArea)
    return Static

def fEncerra():
    oDialogPvt.End()
    return True

def s_fValidPag1():
    lRet = True
    # Se não houver texto para montar o QRCode, não permite prosseguir
    if Empty(cGetTexto):
        FWAlertError('Preencha algo no campo antes de prosseguir!', 'Atenção')
        lRet = False
    else:
        # Se o QRCode já tiver sido criado, atualiza ele
        if ValType(oQrCode) == 'O':
            oQrCode.SetCodeBar(cGetTexto)
            oQrCode.Refresh()


    return lRet

def s_fCriaPag1(oPanel):
    # objeto1 - usando a classe TSay
    nObjLinha = 4
    nObjColun = 4
    nObjLargu = 70
    nObjAltur = 6
    oSayInsira = TSay().New(nObjLinha, nObjColun, lambda : cSayInsira, oPanel, None, oFontPadrao, None, None, None, lDimPixels, None, None, nObjLargu, nObjAltur, None, None, None, None, None)
    # objeto2 - usando a classe TGet
    nObjLinha = 3
    nObjColun = 64
    nObjLargu = 110
    nObjAltur = 10
    oGetTexto = TGet().New(nObjLinha, nObjColun, lambda u: ((cGetTexto := u) if PCount() > 0 else cGetTexto), oPanel, nObjLargu, nObjAltur, None, None, None, None, oFontPadrao, None, None, lDimPixels)
    return Static

def fCriaPag2(oPanel):
    # objeto3 - usando a classe FWQRCode
    nObjLinha = 4
    nObjColun = 110
    nObjLargu = 160
    nObjAltur = 160
    oQrCode = FwQrCode().New([nObjLinha, nObjColun, nObjLargu, nObjAltur], oPanel, cGetTexto)
    return Static

def fCriaPag3(oPanel):
    # objeto4 - usando a classe TSay
    nObjLinha = 4
    nObjColun = 4
    nObjLargu = 200
    nObjAltur = 6
    oSayFim = TSay().New(nObjLinha, nObjColun, lambda : cSayFim, oPanel, None, oFontPadrao, None, None, None, lDimPixels, None, None, nObjLargu, nObjAltur, None, None, None, None, None)
    return
