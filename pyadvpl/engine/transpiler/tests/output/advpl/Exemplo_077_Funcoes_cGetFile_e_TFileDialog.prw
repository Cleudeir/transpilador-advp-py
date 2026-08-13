// caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2023/10/24/navegando-em-pastas-com-as-funcoes-cgetfile-e-tfiledialog-maratona-advpl-e-tl-077/
// Bibliotecas
#Include "TOTVS.ch"
// {Protheus.doc} User Function zExe077
// Exemplo de telas para selecionar arquivos
// @type Function
// @author Atilio
// @since 08/12/2022
// @see https://tdn.totvs.com/display/tec/cGetFile e https://tdn.totvs.com/display/tec/tFileDialog
// Função cGetFile
// Parâmetros
// + cMascara     , Caractere      , Máscara de arquivos
// + cTitulo      , Caractere      , Título da janela
// + nMascPadrao  , Numérico       , Indica o número da máscara
// + cDirInicial  , Caractere      , Pasta inicial
// + lSalvar      , Lógico         , Se .T. será usado um botão Salvar se não será usado o botão Abrir
// + nOpcoes      , Numérico       , Opções da janela ( GETF_MULTISELECT ; GETF_NOCHANGEDIR ; GETF_LOCALFLOPPY ; GETF_LOCALHARD ; GETF_NETWORKDRIVE ; GETF_SHAREWARE ; GETF_RETDIRECTORY ; GETF_HIDDENDIR ; GETF_SYSDIR ; )
// + lArvore      , Lógico         , Se .T. irá exibir pasta da Protheus Data senão só da máquina local
// + lKeepCase    , Lógico         , Se .T. mantém o nome original senão retorna o nome tudo minúsculo
// Retorno
// + cRet         , Caractere      , Retorna o nome do arquivo selecionado
// Função TFileDialog
// Parâmetros
// + cMascara     , Caractere      , Máscara de arquivos
// + cTitulo      , Caractere      , Título da janela
// + nParam3      , Numérico       , Compatibilidade (não utilizado)
// + cDirInicial  , Caractere      , Pasta inicial
// + lSalvar      , Lógico         , Se .T. será usado um botão Salvar se não será usado o botão Abrir
// + nOpcoes      , Numérico       , Opções da janela (se não passar nada será apenas um arquivo; se usar GETF_MULTISELECT será múltiplos arquivos; se usar GETF_RETDIRECTORY será usado pastas)
// Retorno
// + cRet         , Caractere      , Retorna o nome do(s) arquivo(s) selecionado(s) ou da pasta selecionada conforme nOpcoes
// **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
USER FUNCTION zExe077()
    LOCAL aArea, cDirIni, cTipArq, cTitulo, lSalvar, cArqSel, cPasta

    aArea := FWGetArea()
    cDirIni := GetTempPath()
    cTipArq := ""
    cTitulo := ""
    lSalvar := .F.
    cArqSel := ""
    cPasta := ""
    // cGetFile - Seleção de arquivo txt / xml podendo alterar pasta (local e servidor)
    cArqSel := cGetFile("Arquivo TXT|*.txt| Arquivo XML|*.xml", "Selecao de Arquivos", 0, "C:\TOTVS\", .F., GETF_LOCALHARD + GETF_NETWORKDRIVE, .T.)
    // [ lArvore]
    If .NOT. Empty(cArqSel)
        FWAlertInfo("O arquivo escolhido é " + cArqSel, "Teste 1 - cGetFile")
    EndIf
    // cGetFile - Seleção de arquivo txt sem opção de alterar pasta
    cArqSel := cGetFile("Selecione um Arquivo (*.*)|*.*", "Selecao de Arquivos", 0, "C:\TOTVS\", .F., GETF_LOCALHARD + GETF_NETWORKDRIVE + GETF_NOCHANGEDIR, .F.)
    // [ lArvore]
    If .NOT. Empty(cArqSel)
        FWAlertInfo("Arquivos escolhido: " + cArqSel, "Teste 2 - cGetFile")
    EndIf
    // TFileDialog - Selecionando apenas 1 arquivo
    cTipArq := "Todas extensões (*.*) | Arquivos texto (*.txt) | Arquivos com separações (*.csv)"
    cTitulo := "Seleção de Arquivos para Processamento"
    cArqSel := tFileDialog(cTipArq, cTitulo, Nil, cDirIni, lSalvar, Nil, Nil)
    If .NOT. Empty(cArqSel)
        FWAlertInfo("O arquivo selecionado foi: " + cArqSel, "Teste 1 - TFileDialog")
    EndIf
    // TFileDialog - Selecionando mais de 1 arquivo
    cTipArq := "Todas extensões (*.*) | Arquivos imagem (*.png) | Arquivos imagem (*.jpg)"
    cTitulo := "Seleção de Múltiplos Arquivos para Processamento"
    cArqSel := tFileDialog(cTipArq, cTitulo, Nil, cDirIni, lSalvar, GETF_MULTISELECT)
    If .NOT. Empty(cArqSel)
        FWAlertInfo("Arquivo(s) selecionado(s): " + cArqSel, "Teste 2 - TFileDialog")
    EndIf
    // TFileDialog - Selecionando uma pasta
    cTipArq := ""
    cTitulo := "Seleção de Pasta para Salvar arquivo"
    cPasta := tFileDialog(cTipArq, cTitulo, Nil, cDirIni, lSalvar, GETF_RETDIRECTORY)
    If .NOT. Empty(cPasta)
        FWAlertInfo("Pasta Selecionada: " + cPasta, "Teste 3 - TFileDialog")
    EndIf
    FWRestArea(aArea)
    RETURN
