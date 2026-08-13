// caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2024/07/22/funcao-que-retorna-sempre-0-atraves-da-zero-maratona-advpl-e-tl-552/
// Bibliotecas
#Include "TOTVS.ch"
// {Protheus.doc} User Function zExe552
// Função sempre retorna 0 (foi colocado na maratona para ter um com a letra Z)
// @type Function
// @author Atilio
// @since 07/04/2023
// Função Zero
// Parâmetros
// Função não tem parâmetros
// Retorno
// Retorna sempre 0
// **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
USER FUNCTION zExe552()
    LOCAL aArea, nZero

    aArea := FWGetArea()
    nZero := 0
    // Busca o valor de zero
    nZero := Zero()
    // Exibe uma mensagem
    FWAlertInfo("Ahooooo, esse é o último vídeo da Maratona, e o valor de nZero é " + cValToChar(nZero), "Teste Zero")
    FWRestArea(aArea)
    RETURN
