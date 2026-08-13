// caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2024/02/10/selecionando-filiais-com-fwlistbranches-maratona-advpl-e-tl-226/
// Bibliotecas
#Include "Totvs.ch"
// {Protheus.doc} User Function zExe227
// Carrega as informações das empresas para um array
// @type Function
// @author Atilio
// @since 20/02/2023
// @see https://tdn.totvs.com/display/public/framework/FWLoadSM0
// Função FWLoadSM0
// Parâmetros
// + lForce        , Lógico      , Indica se deve forçar a atualização do array
// + lChkUser      , Lógico      , Indica se irá exibir apenas as filiais que o usuário tem acesso
// Retorno
// + aEmpresas       Array       , Informações das filiais e empresas da SM0 (a posição dos campos pode ser encontrada no link do TDN acima)
// **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
USER FUNCTION zExe227()
    LOCAL aArea, aEmpresas, nAtual

    aArea := FWGetArea()
    aEmpresas := {  }
    nAtual := 0
    // Carrega as empresas para a variável
    aEmpresas := FWLoadSM0()
    // Percorre as empresas
    FWRestArea(aArea)
    RETURN
