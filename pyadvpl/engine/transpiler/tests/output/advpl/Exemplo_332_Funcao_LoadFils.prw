// caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2024/04/03/buscando-as-filiais-que-o-usuario-tem-acesso-com-a-loadfils-maratona-advpl-e-tl-332/
// Bibliotecas
#Include "Totvs.ch"
// {Protheus.doc} User Function zExe332
// Retorna um array com as filiais que o usuário logado tem acesso
// @type Function
// @author Atilio
// @since 12/03/2023
// Função LoadFils
// Parâmetros
// Função não tem parâmetros
// Retorno
// Retorna um array com os códigos das filiais
// **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
USER FUNCTION zExe332()
    LOCAL aArea, aFiliais

    aArea := FWGetArea()
    aFiliais := {  }
    // Busca as filiais que o usuário tem acesso
    aFiliais := LoadFils()
    FWAlertInfo("O usuário tem acesso a '" + cValToChar(Len(aFiliais)) + "' filial(is)", "Teste LoadFils")
    FWRestArea(aArea)
    RETURN
