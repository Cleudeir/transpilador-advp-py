// caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2024/05/30/pausando-a-execucao-do-programa-com-a-sleep-maratona-advpl-e-tl-447/
// Bibliotecas
#Include "TOTVS.ch"
// {Protheus.doc} User Function zExe447
// Pausa a execução na thread por um número de milissegundos
// @type Function
// @author Atilio
// @since 31/03/2023
// @see https://tdn.totvs.com/display/tec/Sleep
// Função Sleep
// Parâmetros
// + nSleep    , Numérico    , Quantidade de milissegundos que a Thread ficará pausada
// Retorno
// Função não tem retorno
// **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
USER FUNCTION zExe447()
    LOCAL aArea, cHrIni, cHrFim

    aArea := FWGetArea()
    cHrIni := Time()
    cHrFim := Nil
    // Pausa o processamento por 5 segundos
    Sleep(5000)
    // Pega a hora final, e mostra uma mensagem
    cHrFim := Time()
    FWAlertInfo("Hora Ini: " + cHrIni + " e Hora Fim: " + cHrFim, "Teste Sleep")
    FWRestArea(aArea)
    RETURN
