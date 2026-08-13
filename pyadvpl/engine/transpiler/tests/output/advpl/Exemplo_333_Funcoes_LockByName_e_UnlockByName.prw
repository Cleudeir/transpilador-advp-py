// caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2024/04/03/criando-travas-de-execucao-com-lockbyname-e-unlockbyname-maratona-advpl-e-tl-333/
// Bibliotecas
#Include "Totvs.ch"
// {Protheus.doc} User Function zExe333
// Trava a execução de uma rotina caso outro usuário já tenha começado
// @type Function
// @author Atilio
// @since 12/03/2023
// @see https://tdn.totvs.com/pages/releaseview.action?pageId=6814894 e https://tdn.totvs.com/pages/releaseview.action?pageId=6814897
// Função LockByName
// Parâmetros
// + cName    , Caractere , Define o nome do semáforo que será validado ou criado
// + lEmpresa , Lógico    , Define se o controle será por empresa
// + lFilial  , Lógico    , Define se o controle será por filial
// Retorno
// + lCreated , Lógico    , .T. se criou o semáforo com sucesso ou .F. se já existia o semáforo
// Função UnlockByName
// Parâmetros
// + cName    , Caractere , Define o nome do semáforo que será validado ou criado
// + lEmpresa , Lógico    , Define se o controle será por empresa
// + lFilial  , Lógico    , Define se o controle será por filial
// Retorno
// Função naõ tem retorno
// **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
USER FUNCTION zExe333()
    LOCAL aArea

    aArea := FWGetArea()
    // Se não conseguir travar, quer dizer que algum usuário já esta executando
    If .NOT. LockByName("zExe333_lock", .T., .F.)
        FWAlertError("Atenção, outro usuário já está executando essa rotina!", "Falha no Lock")
        // Senão, aciona o processamento das rotinas
    Else
        Processa(Nil, "Exportando...")
        // Aciona o destravamento do lock
        UnLockByName("zExe333_lock", .T., .F.)
    EndIf
    FWRestArea(aArea)
    RETURN Static

FUNCTION fSuaRotina()
    FWAlertInfo("Em construção", "Teste")
    RETURN
