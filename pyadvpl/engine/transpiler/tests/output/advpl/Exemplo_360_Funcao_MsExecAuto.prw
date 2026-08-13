// caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2024/04/17/atualizando-informacoes-atraves-da-msexecauto-maratona-advpl-e-tl-360/
// Bibliotecas
#Include "TOTVS.ch"
// {Protheus.doc} User Function zExe360
// Executa uma rotina de forma automática
// @type Function
// @author Atilio
// @since 26/03/2023
// @see https://tdn.totvs.com/pages/releaseview.action?pageId=566489232
// Função MsExecAuto
// Parâmetros
// + Bloco de código que será executado
// + Parâmetros (1 a 15) que serão passados na rotina
// Retorno
// Função não tem Retorno
// **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
USER FUNCTION zExe360()
    LOCAL aArea, aDados, lAutomatico, cPastaErro, cNomeErro, cTextoErro, aLogErro, nLinhaErro, lMsErroAuto, lMSHelpAuto, lAutoErrNoFile

    aArea := FWGetArea()
    aDados := {  }
    lAutomatico := IsBlind()
    cPastaErro := "\x_logs\"
    cNomeErro := ""
    cTextoErro := ""
    aLogErro := {  }
    nLinhaErro := 0
    lMsErroAuto := .F.
    // Se for automático sem tela, declara outras variáveis para não exibir a tela
    If lAutomatico
        lMSHelpAuto := .T.
        lAutoErrNoFile := .T.
    EndIf
    // Adiciona os campos
    aAdd(aDados, { "B1_COD", "F0001", Nil })
    aAdd(aDados, { "B1_DESC", "Teste", Nil })
    aAdd(aDados, { "B1_TIPO", "PA", Nil })
    aAdd(aDados, { "B1_UM", "KG", Nil })
    aAdd(aDados, { "B1_LOCPAD", "01", Nil })
    aAdd(aDados, { "B1_GRUPO", "G001", Nil })
    // Chama a inclusão
    MsExecAuto(Nil, aDados, 3)
    // Se houve erro, mostra a mensagem
    If lMsErroAuto
        // Se for automático, irá gravar o log dentro da Protheus Data
        If lAutomatico
            cPastaErro := "\x_logs\"
            cNomeErro := "erro_sb1_" + dToS(Date()) + "_" + StrTran(Time(), ":", "-") + ".txt"
            // Se a pasta de erro não existir, cria ela
            If .NOT. ExistDir(cPastaErro)
                MakeDir(cPastaErro)
            EndIf
            // Pegando log do ExecAuto, percorrendo e incrementando o texto
            aLogErro := GetAutoGRLog()
            // Criando o arquivo txt e incrementa o log
            MemoWrite(cPastaErro + cNomeErro, cTextoErro)
            // Senão, exibe a tela de erro
        Else
            MostraErro()
        EndIf
    Else
        FWAlertSuccess("Produto incluido com sucesso", "Sucesso no ExecAuto")
    EndIf
    FWRestArea(aArea)
    RETURN
