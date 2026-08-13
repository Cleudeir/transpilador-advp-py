// caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2023/11/19/mudando-o-cursor-do-mouse-com-as-funcoes-cursorarrow-e-cursorwait-maratona-advpl-e-tl-103/
// Bibliotecas
#Include "TOTVS.ch"
// {Protheus.doc} User Function zExe103
// Exemplo de como mudar o cursor do mouse enquanto uma rotina entra em "loading"
// @type Function
// @author Atilio
// @since 12/12/2022
// @see https://tdn.totvs.com/display/tec/CursorArrow e https://tdn.totvs.com/display/tec/CursorWait
// Função CursorArrow
// Não tem parâmetros nem retorno
// Função CursorWait
// Não tem parâmetros nem retorno
// Nas versões mais recentes do Windows, esses comandos não surtem efeito
// **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
USER FUNCTION zExe103()
    LOCAL aArea, nTotal, aDados

    aArea := FWGetArea()
    nTotal := 0
    aDados := Array(1000000)
    // Muda o cursor para carregamento
    CursorWait()
    // Mostra qualquer mensagem
    MsgRun("Lendo informações...", "Teste", Nil)
    // Volta o cursor para flecha
    CursorArrow()
    FWRestArea(aArea)
    RETURN
