// caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2024/02/20/buscando-informacoes-de-indices-com-a-fwsixutil-maratona-advpl-e-tl-246/
// Bibliotecas
#Include "TOTVS.ch"
// {Protheus.doc} User Function zExe247
// Classe para buscar informações da SM0 (Cadastro de Empresas)
// @type  Function
// @author Atilio
// @since 20/02/2023
// @see https://tdn.totvs.com/display/public/framework/FWSM0Util
// **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
USER FUNCTION zExe247()
    LOCAL aArea, cMensagem, aCampos, aEncontrou

    aArea := FWGetArea()
    cMensagem := ""
    aCampos := { "M0_CODIGO", "M0_CODFIL", "M0_NOMECOM", "M0_CGC", "M0_INSCM", "M0_CIDENT", "M0_ESTENT", "M0_ENDENT", "M0_BAIRENT", "M0_CEPENT", "M0_COMPENT", "M0_TEL" }
    aEncontrou := {  }
    // Busca os campos da filial "01"
    aEncontrou := FWSM0Util():GetSM0Data(Nil, "01", aCampos)
    // Se encontrou, monta uma mensagem e exibe
    If Len(aEncontrou) > 0
        cMensagem += "M0_NOMECOM: " + aEncontrou[3][2] + CRLF
        cMensagem += "M0_CGC: " + aEncontrou[4][2] + CRLF
        cMensagem += "M0_CIDENT: " + aEncontrou[6][2] + CRLF
        FWAlertInfo(cMensagem, "Teste FWSM0Util")
    EndIf
    FWRestArea(aArea)
    RETURN
