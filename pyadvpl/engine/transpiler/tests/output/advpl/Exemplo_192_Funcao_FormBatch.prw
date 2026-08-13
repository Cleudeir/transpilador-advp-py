// caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2024/01/24/abrindo-uma-tela-com-botoes-atraves-da-formbatch-maratona-advpl-e-tl-192/
// Bibliotecas
#Include "TOTVS.ch"
// {Protheus.doc} User Function zExe192
// Função que abre uma tela com a opção de continuar, cancelar ou setar parâmetros
// @type Function
// @author Atilio
// @since 11/02/2023
// @see https://tdn.totvs.com/pages/releaseview.action?pageId=24346908
// Função FormBatch
// Parâmetros
// + cTitle       , Caractere         , Título da Janela
// + aSays        , Array             , Array com as linhas que serão exibidas na tela
// + aButtons     , Array             , Array com as ações dos botões
// + bValid       , Bloco de Código   , Bloco de Código na validação da tela
// + nAltura      , Numérico          , Altura da janela em Pixels
// + nLargura     , Numérico          , Largura da janela em Pixels
// Retorno
// Função não tem retorno
// **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
USER FUNCTION zExe192()
    LOCAL aArea, aTexto, aBotoes, nContinua, cTitulo

    aArea := FWGetArea()
    aTexto := {  }
    aBotoes := {  }
    nContinua := 0
    cTitulo := "Processamento de Dados"
    // Monta o texto que será exibido na tela
    aAdd(aTexto, "Essa é uma rotina para processamento de informações")
    aAdd(aTexto, "--")
    aAdd(aTexto, "A primeira linha do arquivo deve conter o nome dos campos")
    aAdd(aTexto, "ex.: B1_COD;B1_TIPO;B1_DESC;B1_GRUPO;")
    aAdd(aTexto, "")
    aAdd(aTexto, "As demais linhas devem conter o conteúdo que será importado")
    aAdd(aTexto, "ex.: 00001;PA;Banana;G001;")
    aAdd(aTexto, "")
    aAdd(aTexto, "Para prosseguir com o processamento clique no botão Ok")
    // Monta os botões que serão exibidos
    aAdd(aBotoes, { 1, .T., Nil })
    aAdd(aBotoes, { 2, .T., Nil })
    aAdd(aBotoes, { 5, .T., Nil })
    // Abre a tela
    FormBatch(cTitulo, aTexto, aBotoes)
    // Se o usuário clicou no Confirmar
    If nContinua = 1
        // Aqui você aciona a sua função se o usuário clicou no botão confirmar
    EndIf
    FWRestArea(aArea)
    RETURN
