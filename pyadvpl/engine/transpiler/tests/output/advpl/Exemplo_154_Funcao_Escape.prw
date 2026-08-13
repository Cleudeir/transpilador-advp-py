// caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2024/01/05/montando-a-estrutura-de-um-produto-com-as-funcoes-estrut2-e-fimestrut2-maratona-advpl-e-tl-155/
// Bibliotecas
#Include "TOTVS.ch"
// {Protheus.doc} User Function zExe154
// Função que retira caracteres especiais de um conteúdo web (como URL)
// @type Function
// @author Atilio
// @since 18/12/2022
// Função Escape
// Parâmetros
// Recebe a string que terá os caracteres transformados
// Retorno
// Retorna a string com os caracteres já transformados
// **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
USER FUNCTION zExe154()
    LOCAL aArea, cOriginal, cConverti

    aArea := FWGetArea()
    cOriginal := ""
    cConverti := ""
    // Convertendo uma URL que possua espaços
    cOriginal := "terminal de informação"
    cConverti := Escape(cOriginal)
    FWAlertInfo("A conversão de '" + cOriginal + "' deu '" + cConverti + "' ", "Exemplo Escape")
    FWRestArea(aArea)
    RETURN
