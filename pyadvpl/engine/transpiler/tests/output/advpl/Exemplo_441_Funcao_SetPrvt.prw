// caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2024/05/27/definindo-o-valor-de-um-parametro-de-pergunta-com-a-setmvvalue-maratona-advpl-e-tl-440/
// Bibliotecas
#Include "TOTVS.ch"
// {Protheus.doc} User Function zExe441
// Cria variáveis do escopo private através de uma função
// @type Function
// @author Atilio
// @since 31/03/2023
// Função SetPrvt
// Parâmetros
// Recebe o nome das variáveis separadas por vírgula
// Retorno
// Retorna .T. se conseguiu criar as variáveis ou .F. se não
// **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
USER FUNCTION zExe441()
    LOCAL aArea

    aArea := FWGetArea()
    // Cria as variáveis private
    SetPrvt("cBeluga,cOrca,cJubarte")
    // Aciona uma função de exemplo que vai ter acesso a essas variáveis
    fExemplo()
    FWRestArea(aArea)
    RETURN Static

FUNCTION fExemplo()
    FWAlertInfo("Teste de criação de variáveis com SetPrvt", "Teste SetPrvt")
    RETURN
