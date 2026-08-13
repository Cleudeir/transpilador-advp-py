// caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2024/04/01/fazendo-backup-da-memoria-e-restaurando-com-lj7getarea-e-lj7restarea-maratona-advpl-e-tl-328/
// Bibliotecas
#Include "Totvs.ch"
// {Protheus.doc} User Function zExe328
// Faz um backup da área em memória e depois volta (de várias tabelas)
// @type Function
// @author Atilio
// @since 12/03/2023
// Função Lj7GetArea
// Parâmetros
// Recebe um array com os alias da tabela
// Retorno
// Retorna um array com cada tabela e com as posições [1] Alias ; [2] Índice Usado ; [3] Registro posicionado
// Função Lj7RestArea
// Parâmetros
// Array com as posições igual armazenadas na Lj7GetArea
// Retorno
// Não tem retorno
// **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
USER FUNCTION zExe328()
    LOCAL aArea

    aArea := Lj7GetArea({ "SB1", "SBM", "SB5" })
    // Aqui suas customizações
    Lj7RestArea(aArea)
    RETURN

USER FUNCTION A010TOK()
    LOCAL lRet

    lRet := .T.
    // Seleciona outra tabela
    DbSelectArea("SA1")
    // Aciona o exemplo
    u_zExe328()
    RETURN lRet
