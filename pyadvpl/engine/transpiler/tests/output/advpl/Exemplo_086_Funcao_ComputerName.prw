// caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2023/11/02/buscando-o-nome-da-maquina-com-computername-maratona-advpl-e-tl-086/
// Bibliotecas
#Include "TOTVS.ch"
// {Protheus.doc} User Function zExe086
// Exemplo de como buscar o nome do computador que esta executando o Protheus
// @type Function
// @author Atilio
// @since 09/12/2022
// @see https://tdn.totvs.com/display/tec/ComputerName
// Função ComputerName
// Retorno
// + cRet     , Caractere    , Nome da máquina
// **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
USER FUNCTION zExe086()
    LOCAL aArea, cNomePC

    aArea := FWGetArea()
    cNomePC := ""
    // Busca o nome do computador e mostra em uma mensagem
    cNomePC := ComputerName()
    FWAlertSuccess("O nome do computador é " + cNomePC, "Teste ComputerName")
    FWRestArea(aArea)
    RETURN
