// caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2024/03/02/buscando-o-nome-da-banco-atraves-da-getdatabase-maratona-advpl-e-tl-269/
// Bibliotecas
#Include "TOTVS.ch"
// {Protheus.doc} User Function zExe269
// Retorna o nome do tipo da conexão com a base de dados usada no AppServer com o DbAccess
// @type  Function
// @author Atilio
// @since 21/02/2023
// Função GetDataBase
// Parâmetros
// Não possui parâmetros
// Retorno
// Retorna o tipo da base em caractere
// **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
USER FUNCTION zExe269()
    LOCAL aArea, cMensagem

    aArea := FWGetArea()
    cMensagem := ""
    // Busca a informação e exibe
    cMensagem := "O tipo da conexão usada é: " + GetDataBase()
    FWAlertInfo(cMensagem, "Teste GetDataBase")
    FWRestArea(aArea)
    RETURN
