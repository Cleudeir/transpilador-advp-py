// caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2024/04/22/validando-o-nivel-de-um-usuario-com-a-niveluser-maratona-advpl-e-tl-370/
// Bibliotecas
#Include "TOTVS.ch"
// {Protheus.doc} User Function zExe371
// Retorna o nome da tabela do dicionário de dados
// @type Function
// @author Atilio
// @since 28/03/2023
// Função NomeTab
// Parâmetros
// Recebe o Alias da Tabela
// Retorno
// Retorna o Nome da Tabela
// Função Sx2Name
// Parâmetros
// Recebe o Alias da Tabela
// Retorno
// Retorna o Nome da Tabela
// **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
USER FUNCTION zExe371()
    LOCAL aArea, cTabela, cNome

    aArea := FWGetArea()
    cTabela := ""
    cNome := ""
    // Define a tabela e busca o nome dela
    cTabela := "SA1"
    cNome := NomeTab(cTabela)
    FWAlertInfo("O nome da tabela '" + cTabela + "' é '" + cNome + "'", "Teste NomeTab")
    // Define a tabela e busca o nome dela
    cTabela := "SA2"
    cNome := Sx2Name(cTabela)
    FWAlertInfo("O nome da tabela '" + cTabela + "' é '" + cNome + "'", "Teste Sx2Name")
    FWRestArea(aArea)
    RETURN
