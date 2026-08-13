# Esse exemplo faz parte da série do YouTube, Maratona de Exemplos, do canal Terminal de Informação, 
#     caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2024/06/14/criando-um-combo-atraves-da-tcombobox-maratona-advpl-e-tl-477/
# Bibliotecas
# PREPROCESSOR: #Include "TOTVS.ch"
# {Protheus.doc} User Function zExe477
# Classe para criar combobox em uma Dialog
# @type Function
# @author Atilio
# @since 03/04/2023
# @see https://tdn.totvs.com/display/tec/TComboBox
# @obs 
# 
#     **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
def u_zExe477():
    aArea = FWGetArea()
    nCorFundo = RGB(238, 238, 238)
    nJanAltura = 190
    nJanLargur = 245
    cJanTitulo = 'Exemplo Combo'
    lDimPixels = True
    lCentraliz = True
    nObjLinha = 0
    nObjColun = 0
    nObjLargu = 0
    nObjAltur = 0
    cFontNome = 'Tahoma'
    oFontPadrao = TFont().New(cFontNome, None, -12)
    oDialogPvt = None
    bBlocoIni = lambda : None
    # Aqui voce pode acionar funcoes customizadas que irao ser acionadas ao abrir a dialog
    # objeto0
    oSayObj0 = None
    cSayObj0 = 'Região:'
    # objeto1
    oCmbObj1 = None
    cCmbObj1 = 'XX'
    aCmbObj1 = ['XX=Nenhuma Região', 'NT=Norte', 'ND=Nordeste', 'CO=Centro Oeste', 'SD=Sudeste', 'SU=Sul']
    # objeto2
    oSayObj2 = None
    cSayObj2 = 'Estado:'
    # objeto3
    oCmbObj3 = None
    cCmbObj3 = ''
    aCmbObj3 = []
    # objeto4
    oBtnObj4 = None
    cBtnObj4 = 'Confirmar'
    bBtnObj4 = lambda : MsgInfo('Região [' + cCmbObj1 + '] e Estado [' + cCmbObj3 + ']', 'Combos escolhidos')
    # Cria a dialog
    oDialogPvt = TDialog().New(0, 0, nJanAltura, nJanLargur, cJanTitulo, None, None, None, None, None, nCorFundo, None, None, lDimPixels)
    # objeto0 - usando a classe TSay
    nObjLinha = 8
    nObjColun = 7
    nObjLargu = 28
    nObjAltur = 6
    oSayObj0 = TSay().New(nObjLinha, nObjColun, lambda : cSayObj0, oDialogPvt, None, oFontPadrao, None, None, None, lDimPixels, None, None, nObjLargu, nObjAltur, None, None, None, None, None)
    # objeto1 - usando a classe TComboBox
    nObjLinha = 17
    nObjColun = 18
    nObjLargu = 100
    nObjAltur = 12
    oCmbObj1 = TComboBox().New(nObjLinha, nObjColun, lambda u: ((cCmbObj1 := u) if PCount() > 0 else cCmbObj1), aCmbObj1, nObjLargu, nObjAltur, oDialogPvt, None, lambda : fAtuCmb(), None, None, None, lDimPixels, oFontPadrao)
    # objeto2 - usando a classe TSay
    nObjLinha = 35
    nObjColun = 7
    nObjLargu = 28
    nObjAltur = 6
    oSayObj2 = TSay().New(nObjLinha, nObjColun, lambda : cSayObj2, oDialogPvt, None, oFontPadrao, None, None, None, lDimPixels, None, None, nObjLargu, nObjAltur, None, None, None, None, None)
    # objeto3 - usando a classe TComboBox
    nObjLinha = 44
    nObjColun = 18
    nObjLargu = 100
    nObjAltur = 12
    oCmbObj3 = TComboBox().New(nObjLinha, nObjColun, lambda u: ((cCmbObj3 := u) if PCount() > 0 else cCmbObj3), aCmbObj3, nObjLargu, nObjAltur, oDialogPvt, None, None, None, None, None, lDimPixels, oFontPadrao)
    # objeto4 - usando a classe TButton
    nObjLinha = 72
    nObjColun = 70
    nObjLargu = 50
    nObjAltur = 15
    oBtnObj4 = TButton().New(nObjLinha, nObjColun, cBtnObj4, oDialogPvt, bBtnObj4, nObjLargu, nObjAltur, None, oFontPadrao, None, lDimPixels)
    # Ativa e exibe a janela
    oDialogPvt.Activate(None, None, None, lCentraliz, None, None, bBlocoIni)
    FWRestArea(aArea)
    return Static

def fAtuCmb():
    aEstados = []
    # Se for a região Norte
    if cCmbObj1 == 'NT':
        aAdd(aEstados, 'RR=Roraima')
        aAdd(aEstados, 'AP=Amapá')
        aAdd(aEstados, 'AM=Amazonas')
        aAdd(aEstados, 'PA=Pará')
        aAdd(aEstados, 'AC=Acre')
        aAdd(aEstados, 'RO=Rondônia')
        aAdd(aEstados, 'TO=Tocantins')
        # Senão se for a região Nordeste
    elif cCmbObj1 == 'ND':
        aAdd(aEstados, 'MA=Maranhão')
        aAdd(aEstados, 'PI=Piauí')
        aAdd(aEstados, 'CE=Ceará')
        aAdd(aEstados, 'RN=Rio Grande do Norte')
        aAdd(aEstados, 'PB=Paraíba')
        aAdd(aEstados, 'PE=Pernambuco')
        aAdd(aEstados, 'AL=Alagoas')
        aAdd(aEstados, 'SE=Sergipe')
        aAdd(aEstados, 'BA=Bahia')
        # Senão se for a região Centro Oeste
    elif cCmbObj1 == 'CO':
        aAdd(aEstados, 'MT=Mato Grosso')
        aAdd(aEstados, 'DF=Distrito Federal')
        aAdd(aEstados, 'GO=Goiás')
        aAdd(aEstados, 'MS=Mato Grosso do Sul')
        # Senão se for a região Sudeste
    elif cCmbObj1 == 'SD':
        aAdd(aEstados, 'MG=Minas Gerais')
        aAdd(aEstados, 'ES=Espírito Santo')
        aAdd(aEstados, 'RJ=Rio de Janeiro')
        aAdd(aEstados, 'SP=São Paulo')
        # Senão se for a região Sul
    elif cCmbObj1 == 'SU':
        aAdd(aEstados, 'PR=Paraná')
        aAdd(aEstados, 'SC=Santa Catarina')
        aAdd(aEstados, 'RS=Rio Grande do Sul')
        # Nenhuma região
    else:
        aAdd(aEstados, '')

    # Define no segundo combo o array com os estados
    oCmbObj3.SetItems(aEstados)
    oCmbObj3.Refresh()
    return
