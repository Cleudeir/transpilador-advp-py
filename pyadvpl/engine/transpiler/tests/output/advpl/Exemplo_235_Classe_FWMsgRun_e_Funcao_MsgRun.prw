// caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2024/02/14/gerando-e-abrindo-o-excel-com-fwmsexcel-fwmsexcelxlsx-e-msexcel-maratona-advpl-e-tl-234/
// Bibliotecas
#Include "TOTVS.ch"
// {Protheus.doc} User Function zExe235
// Exemplo de barras de processamento
// @type Function
// @author Atilio
// @since 20/02/2023
// @see https://tdn.totvs.com/display/public/framework/FWMsgRun e https://tdn.totvs.com/display/tec/MsgRun
// Função FWMsgRun
// Parâmetros
// + oComponent    , Objeto            , Componente que será sobreposto com o painel
// + bAction       , Bloco de Código   , Bloco que será executado
// + cHeader       , Caractere         , Título da janela
// + cText         , Caractere         , Texto que será apresentado
// Retorno
// Não tem retorno
// Função MsgRun
// Parâmetros
// + cText         , Caractere         , Texto que será apresentado
// + cHeader       , Caractere         , Título da janela
// + bBlock        , Bloco de Código   , Bloco que será executado
// Retorno
// Não tem retorno
// **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
USER FUNCTION zExe235()
    LOCAL aArea, nTotal, aDados

    aArea := FWGetArea()
    nTotal := 0
    aDados := Array(1000000)
    // Mostra qualquer mensagem
    MsgRun("Lendo informações...", "Teste", Nil)
    // Mostra a barra que fica carregando
    FWMsgRun(Nil, Nil, "Processando", "Buscando informações")
    FWRestArea(aArea)
    RETURN Static

FUNCTION fCorre(oSay)
    LOCAL nAtual

    nAtual := 0
    // Percorre o array e define o texto
    RETURN
