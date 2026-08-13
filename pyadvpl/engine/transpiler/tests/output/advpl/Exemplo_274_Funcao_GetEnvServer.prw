// caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2024/03/05/buscando-informacoes-de-funcoes-com-a-getfuncarray-maratona-advpl-e-tl-275/
// Bibliotecas
#Include "TOTVS.ch"
// {Protheus.doc} User Function zExe274
// Retorna o nome do ambiente (apo / environment) que esta rodando o sistema
// @type  Function
// @author Atilio
// @since 21/02/2023
// @see https://tdn.totvs.com/display/tec/GetEnvServer
// Função GetEnvServer
// Parâmetros
// Não possui parâmetros
// Retorno
// + cRet     , Caractere      , Nome do Environment
// **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
USER FUNCTION zExe274()
    LOCAL aArea, cMensagem

    aArea := FWGetArea()
    cMensagem := ""
    // Busca a informação e exibe
    cMensagem := "O nome do ambiente que esta rodando o sistema é: " + GetEnvServer()
    FWAlertInfo(cMensagem, "Teste GetEnvServer")
    FWRestArea(aArea)
    RETURN
