# Esse exemplo faz parte da série do YouTube, Maratona de Exemplos, do canal Terminal de Informação, 
#     caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2024/02/17/configurando-a-impressao-atraves-da-fwprintsetup-maratona-advpl-e-tl-240/
# Bibliotecas
# PREPROCESSOR: #Include "TOTVS.ch"
# PREPROCESSOR: #Include "FWPrintSetup.ch"
# Constantes
# PREPROCESSOR: #Define PAD_LEFT			0					//Alinhamento Esquerda
# PREPROCESSOR: #Define PAD_RIGHT			1					//Alinhamento Direita
# PREPROCESSOR: #Define PAD_CENTER			2					//Alinhamento Centralizado
# PREPROCESSOR: #Define IMP_SPOOL           2
oSetupRel = None
# {Protheus.doc} User Function zExe240
# Imprime a etiqueta via fwmsprinter
# @type  Function
# @author Atilio
# @since 20/02/2023
# @see https://tdn.totvs.com/display/public/framework/FWPrintSetup
# @obs 
# 
#     **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
def u_zExe240():
    aArea = FWGetArea()
    aPergs = []
    cCodProd = Space(TamSX3('B1_COD')[1])
    # Adiciona os parâmetros que serão exibidos
    aAdd(aPergs, [1, 'Produto', cCodProd, '', '.T.', 'SB1', '.T.', 60, True])
    # Se a pergunta for confirmada
    if ParamBox(aPergs, 'Informe os parâmetros', None, None, None, None, None, None, None, None, False, False):
        cCodProd = Alltrim(MV_PAR01)
        fImprEtq()

    FWRestArea(aArea)
    return Static

def fImprEtq():
    oPrint = None
    oBrush = TBrush().New(None, RGB(0, 0, 0))
    nAltura = 1200
    nLargura = 1200
    nLinAux = 0
    lNegrito = True
    lSublinhado = True
    lItalico = True
    cNomeFont = 'Arial'
    oFontDadN = TFont().New(cNomeFont, None, -15, None, lNegrito, None, None, None, None, not lSublinhado, not lItalico)
    oFontRoda = TFont().New(cNomeFont, None, -13, None, lNegrito, None, None, None, None, not lSublinhado, not lItalico)
    DbSelectArea('SB1')
    SB1.DbSetOrder(1)
    # Filial + Produto
    if SB1.MsSeek(FWxFilial('SB1') + cCodProd):
        # Criando a impressão
        oPrint = FwMsPrinter().New('ETQPRODU', None, True, GetTempPath(), True)
        # Se ainda não tiver configuração de Setup
        while ValType(oSetupRel) == 'U':
            fConfImpr()

        # Se for direto para impressora
        if oSetupRel.GetProperty(PD_PRINTTYPE) == IMP_SPOOL:
            oPrint.nDevice = IMP_SPOOL
            oPrint.cPrinter = oSetupRel.aOptions()[PD_VALUETYPE]

        oPrint.StartPage()
        # Imprimindo o cabeçalho (imagem e mensagem)
        oPrint.SayBitmap(75, 10, '\\x_imagens\\logo.png', 105, 105)
        oPrint.Say(130, nLargura - 490, 'Terminal de Informação', oFontDadN, None, None, None, PAD_CENTER)
        oPrint.Line(250, 0, 250, nAltura)
        nLinAux = 290
        oPrint.Say(nLinAux, 30, 'Etiqueta de Produto', oFontDadN, None, None, None, PAD_LEFT)
        nLinAux += 80
        # Descrição
        oPrint.Say(nLinAux, 30, 'Descrição:', oFontDadN, None, None, None, PAD_LEFT)
        oPrint.Say(nLinAux, 340, Alltrim(SB1.B1_DESC), oFontDadN, None, None, None, PAD_LEFT)
        nLinAux += 80
        # Data e Validade
        oPrint.Say(nLinAux, 30, 'Tipo:', oFontDadN, None, None, None, PAD_LEFT)
        oPrint.Say(nLinAux, 340, SB1.B1_TIPO, oFontDadN, None, None, None, PAD_LEFT)
        oPrint.Say(nLinAux, 580, 'U.M.:', oFontDadN, None, None, None, PAD_LEFT)
        oPrint.Say(nLinAux, 850, SB1.B1_UM, oFontDadN, None, None, None, PAD_LEFT)
        nLinAux += 80
        # Código de Barras
        oPrint.FwMsBar('CODE128', 12, 1, Alltrim(cCodProd), oPrint, False, None, None, None, None, None, None, None, False, None, None)
        nLinAux += 240
        # Dados finais
        oPrint.FillRect([nLinAux - 20, 0, nAltura - 250, nLargura - 20], oBrush)
        oPrint.Say(nLinAux + 30, 30, 'PRODUTO', oFontDadN, None, RGB(255, 255, 255), None, PAD_LEFT)
        oPrint.Say(nLinAux + 140, 30, cCodProd, oFontRoda, None, RGB(255, 255, 255), None, PAD_LEFT)
        oPrint.Say(nLinAux + 20, nLargura - 720, 'Se tiver dúvidas', oFontRoda, None, RGB(255, 255, 255), None, PAD_CENTER)
        oPrint.Say(nLinAux + 60, nLargura - 720, 'entre em contato conosco', oFontRoda, None, RGB(255, 255, 255), None, PAD_CENTER)
        oPrint.Say(nLinAux + 100, nLargura - 720, 'através do e-Mail', oFontRoda, None, RGB(255, 255, 255), None, PAD_CENTER)
        oPrint.Say(nLinAux + 140, nLargura - 720, 'contato@atiliosistemas.com', oFontRoda, None, RGB(255, 255, 255), None, PAD_CENTER)
        # Mandando para o spool de impressão
        oPrint.Print()
    else:
        FWAlertError('Produto não encontrado', 'Falha')

    return Static

def fConfImpr():
    aDevice = ['DISCO', 'SPOOL', 'EMAIL', 'EXCEL', 'HTML', 'PDF']
    oSetup = None
    cSession = GetPrinterSession()
    cDevice = If_(Empty(fwGetProfString(cSession, 'PRINTTYPE', 'SPOOL', True)), 'PDF', fwGetProfString(cSession, 'PRINTTYPE', 'SPOOL', True))
    nPrintType = aScan(aDevice, lambda x: x == cDevice)
    nOrientation = 1
    # If(fwGetProfString(cSession, "ORIENTATION", "PORTRAIT", .T.) == "PORTRAIT", 1, 2)
    nLocal = 2
    # If(fwGetProfString(cSession, "LOCAL", "SERVER", .T.) == "SERVER", 1, 2)
    nFlags = PD_ISTOTVSPRINTER + PD_DISABLEPAPERSIZE + PD_DISABLEPREVIEW + PD_DISABLEMARGIN
    # Cria o setup do relatório
    oSetup = FWPrintSetup().New(nFlags, 'ETIQUETA')
    oSetup.SetPropert(PD_DESTINATION, nLocal)
    oSetup.SetPropert(PD_ORIENTATION, nOrientation)
    oSetup.SetPropert(PD_PRINTTYPE, nPrintType)
    oSetupRel = None
    # Se a tela for confirmada, atualiza o setup default do relatório
    if oSetup.Activate() == PD_OK:
        if oSetup.GetProperty(PD_PRINTTYPE) == IMP_SPOOL and oSetup.GetProperty(PD_DESTINATION) == 2:
            oSetupRel = oSetup
        else:
            FWAlertInfo('Escolha o tipo SPOOL e LOCAL para impressão!')


    return
