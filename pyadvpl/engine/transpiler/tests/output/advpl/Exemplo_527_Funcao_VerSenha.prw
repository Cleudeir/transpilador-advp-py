// caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2024/07/09/validando-acessos-de-um-usuario-atraves-da-versenha-maratona-advpl-e-tl-527/
// Bibliotecas
#Include "TOTVS.ch"
// {Protheus.doc} User Function zExe527
// Verificando se usuário tem determinado acesso
// @type Function
// @author Atilio
// @since 06/04/2023
// @see https://tdn.totvs.com/pages/releaseview.action?pageId=6815010
// Função VerSenha
// Parâmetros
// + nOpc      , Numérico     , Número do acesso a ser verificado
// Retorno
// + lAcess    , Lógico       , Retorna .T. caso o usuário tenha acesso ou .F. se não
// Para ver a lista de acessos, veja no link: https://tdn.totvs.com/pages/releaseview.action?pageId=221546134
// **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
USER FUNCTION zExe527()
    LOCAL aArea, nAcesso

    aArea := FWGetArea()
    nAcesso := 138
    If VerSenha(nAcesso)
        FWAlertSuccess("O usuário pode usar o acesso 138 (Localizar Rotinas / Ctrl+R)", "Teste VerSenha")
    Else
        FWAlertError("Usuário não pode usar o acesso 138!", "Teste VerSenha")
    EndIf
    FWRestArea(aArea)
    RETURN
