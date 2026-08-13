# Esse exemplo faz parte da série do YouTube, Maratona de Exemplos, do canal Terminal de Informação, 
#     caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2023/10/24/navegando-em-pastas-com-as-funcoes-cgetfile-e-tfiledialog-maratona-advpl-e-tl-077/
# Bibliotecas
# PREPROCESSOR: #Include "TOTVS.ch"
# {Protheus.doc} User Function zExe077
# Exemplo de telas para selecionar arquivos
# @type Function
# @author Atilio
# @since 08/12/2022
# @see https://tdn.totvs.com/display/tec/cGetFile e https://tdn.totvs.com/display/tec/tFileDialog
# @obs 
#     Função cGetFile
#     Parâmetros
#         + cMascara     , Caractere      , Máscara de arquivos
#         + cTitulo      , Caractere      , Título da janela
#         + nMascPadrao  , Numérico       , Indica o número da máscara
#         + cDirInicial  , Caractere      , Pasta inicial
#         + lSalvar      , Lógico         , Se .T. será usado um botão Salvar se não será usado o botão Abrir
#         + nOpcoes      , Numérico       , Opções da janela ( GETF_MULTISELECT ; GETF_NOCHANGEDIR ; GETF_LOCALFLOPPY ; GETF_LOCALHARD ; GETF_NETWORKDRIVE ; GETF_SHAREWARE ; GETF_RETDIRECTORY ; GETF_HIDDENDIR ; GETF_SYSDIR ; )
#         + lArvore      , Lógico         , Se .T. irá exibir pasta da Protheus Data senão só da máquina local
#         + lKeepCase    , Lógico         , Se .T. mantém o nome original senão retorna o nome tudo minúsculo
#     Retorno
#         + cRet         , Caractere      , Retorna o nome do arquivo selecionado
# 
# 
#     Função TFileDialog
#     Parâmetros
#         + cMascara     , Caractere      , Máscara de arquivos
#         + cTitulo      , Caractere      , Título da janela
#         + nParam3      , Numérico       , Compatibilidade (não utilizado)
#         + cDirInicial  , Caractere      , Pasta inicial
#         + lSalvar      , Lógico         , Se .T. será usado um botão Salvar se não será usado o botão Abrir
#         + nOpcoes      , Numérico       , Opções da janela (se não passar nada será apenas um arquivo; se usar GETF_MULTISELECT será múltiplos arquivos; se usar GETF_RETDIRECTORY será usado pastas)
#     Retorno
#         + cRet         , Caractere      , Retorna o nome do(s) arquivo(s) selecionado(s) ou da pasta selecionada conforme nOpcoes
# 
#     **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
def u_zExe077():
    aArea = FWGetArea()
    cDirIni = GetTempPath()
    cTipArq = ''
    cTitulo = ''
    lSalvar = False
    cArqSel = ''
    cPasta = ''
    # cGetFile - Seleção de arquivo txt / xml podendo alterar pasta (local e servidor)
    cArqSel = cGetFile('Arquivo TXT|*.txt| Arquivo XML|*.xml', 'Selecao de Arquivos', 0, 'C:\\TOTVS\\', False, GETF_LOCALHARD + GETF_NETWORKDRIVE, True)
    # [ lArvore]
    if not Empty(cArqSel):
        FWAlertInfo('O arquivo escolhido é ' + cArqSel, 'Teste 1 - cGetFile')

    # cGetFile - Seleção de arquivo txt sem opção de alterar pasta
    cArqSel = cGetFile('Selecione um Arquivo (*.*)|*.*', 'Selecao de Arquivos', 0, 'C:\\TOTVS\\', False, GETF_LOCALHARD + GETF_NETWORKDRIVE + GETF_NOCHANGEDIR, False)
    # [ lArvore]
    if not Empty(cArqSel):
        FWAlertInfo('Arquivos escolhido: ' + cArqSel, 'Teste 2 - cGetFile')

    # TFileDialog - Selecionando apenas 1 arquivo
    cTipArq = 'Todas extensões (*.*) | Arquivos texto (*.txt) | Arquivos com separações (*.csv)'
    cTitulo = 'Seleção de Arquivos para Processamento'
    cArqSel = tFileDialog(cTipArq, cTitulo, None, cDirIni, lSalvar, None, None)
    if not Empty(cArqSel):
        FWAlertInfo('O arquivo selecionado foi: ' + cArqSel, 'Teste 1 - TFileDialog')

    # TFileDialog - Selecionando mais de 1 arquivo
    cTipArq = 'Todas extensões (*.*) | Arquivos imagem (*.png) | Arquivos imagem (*.jpg)'
    cTitulo = 'Seleção de Múltiplos Arquivos para Processamento'
    cArqSel = tFileDialog(cTipArq, cTitulo, None, cDirIni, lSalvar, GETF_MULTISELECT)
    if not Empty(cArqSel):
        FWAlertInfo('Arquivo(s) selecionado(s): ' + cArqSel, 'Teste 2 - TFileDialog')

    # TFileDialog - Selecionando uma pasta
    cTipArq = ''
    cTitulo = 'Seleção de Pasta para Salvar arquivo'
    cPasta = tFileDialog(cTipArq, cTitulo, None, cDirIni, lSalvar, GETF_RETDIRECTORY)
    if not Empty(cPasta):
        FWAlertInfo('Pasta Selecionada: ' + cPasta, 'Teste 3 - TFileDialog')

    FWRestArea(aArea)
    return
