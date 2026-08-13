// caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2024/01/24/executando-uma-formula-cadastrada-no-sistema-com-a-formula-maratona-advpl-e-tl-193/
// Bibliotecas
#Include "TOTVS.ch"
// {Protheus.doc} User Function zExe193
// Executa uma fórmula cadastrada na SM4
// @type Function
// @author Atilio
// @since 11/02/2023
// Função Formula
// Parâmetros
// + Código da fórmula a ser executada
// Retorno
// + Retorna o valor conforme a fórmnula executada
// **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
USER FUNCTION zExe193()
    LOCAL aArea, cFormCod, dResult

    aArea := FWGetArea()
    cFormCod := "F01"
    dResult := Nil
    // Executa a fórmula e mostra o resultado
    dResult := Formula(cFormCod)
    FWAlertInfo("O resultado é " + dToC(dResult), "Formula - Teste 1")
    FWRestArea(aArea)
    RETURN
