// caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2024/02/27/compactando-e-descompactando-arquivos-com-fzip-e-funzip-maratona-advpl-e-tl-260/
// Bibliotecas
#Include "TOTVS.ch"
// {Protheus.doc} User Function zExe261
// Função que abre uma tela para seleção de registros conforme um Array
// @type  Function
// @author Atilio
// @since 21/02/2023
// Função F_Opcoes
// Parâmetros
// + Define a variável de retorno
// + Define o texto do título da janela
// + Define o array de linhas da grid
// + Define os códigos das linhas da grid
// + Mantido por compatibilidade
// + Mantido por compatibilidade
// + Define se será a seleção de apenas 1 linha por vez
// + Tamanho da string da chave
// + Número máximo de elementos
// + Inclui botões para múltipla seleção
// + Define se será montado através de um X3_CBOX
// + Qual é o campo para montagem das opções
// + Não permite ordenação
// + Não permite pesquisar
// + Força o retorno como Array
// + Acionado em consulta F3
// Retorno
// Retorna .T. se foi confirmado ou .F. se foi cancelado
// **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
USER FUNCTION zExe261()
    LOCAL aArea, aRet, cTitulo, aOpc, cRet

    aArea := FWGetArea()
    aRet := {  }
    cTitulo := "Regiões do Brasil"
    aOpc := {  }
    cRet := ""
    // Define as opções que serão exibidas
    aAdd(aOpc, "Norte")
    aAdd(aOpc, "Nordeste")
    aAdd(aOpc, "Centro Oeste")
    aAdd(aOpc, "Sudeste")
    aAdd(aOpc, "Sul")
    // Define as opções de retorno (conforme o aOpc acima)
    cRet := "000000001000000002000000003000000004000000005"
    // Abre a tela para a seleção
    If F_Opcoes(@ aRet, cTitulo, aOpc, cRet, 12, 49, .T., 9, 999, .F., .F., Nil, .F., .F., .T., Nil)
        FWAlertInfo("A opção marcada foi " + aRet[1], "Teste F_Opcoes")
    EndIf
    FWRestArea(aArea)
    RETURN
