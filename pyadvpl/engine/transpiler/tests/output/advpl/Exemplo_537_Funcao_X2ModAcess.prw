// caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2024/07/14/criando-um-webservice-soap-com-wsservice-maratona-advpl-e-tl-536/
// Bibliotecas
#Include "TOTVS.ch"
// {Protheus.doc} User Function zExe537
// Função que busca o modo de compartilhamento de uma tabela (X2_MODO)
// @type Function
// @author Atilio
// @since 07/04/2023
// Função X2ModAcess
// Parâmetros
// Recebe o alias da tabela que será analisada
// Retorno
// Retorna o modo de compartilhamento encontrado
// **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
USER FUNCTION zExe537()
    LOCAL aArea, cTabela, cModo

    aArea := FWGetArea()
    cTabela := ""
    cModo := ""
    // Busca de uma tabela que seja compartilhada
    cTabela := "SB1"
    cModo := X2ModAcess(cTabela)
    FWAlertInfo("Para a tabela '" + cTabela + "' o modo de compartilhamento é '" + cModo + "'", "Teste 1 X2ModAcess")
    // Busca de uma tabela que seja exclusiva
    cTabela := "SC5"
    cModo := X2ModAcess(cTabela)
    FWAlertInfo("Para a tabela '" + cTabela + "' o modo de compartilhamento é '" + cModo + "'", "Teste 2 X2ModAcess")
    FWRestArea(aArea)
    RETURN
