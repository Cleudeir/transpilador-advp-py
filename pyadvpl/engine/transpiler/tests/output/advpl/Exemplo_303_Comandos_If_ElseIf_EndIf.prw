// caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2024/03/19/fazendo-testes-condicionais-com-if-elseif-else-e-endif-maratona-advpl-e-tl-303/
// Bibliotecas
#Include "Totvs.ch"
// {Protheus.doc} zExe303
// Exemplo de estrutura de condicao com If, ElseIf, Else e EndIf
// @type  Function
// @author Atilio
// @since 22/02/2023
// @see https://tdn.totvs.com/display/tecen/IF+...+ENDIF
// **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
USER FUNCTION zExe303()
    LOCAL aArea, cNome

    aArea := FWGetArea()
    cNome := ""
    // Definindo 1 nome
    cNome := "Daniel"
    If Upper(cNome) = "MARIA"
        FWAlertInfo("Nome igual a MARIA", "Teste de If, ElseIf e EndIf")
    ElseIf Upper(cNome) = "JOAO"
        FWAlertInfo("Nome igual a JOAO", "Teste de If, ElseIf e EndIf")
    Else
        FWAlertInfo("O Nome nao e MARIA nem JOAO", "Teste de If, ElseIf e EndIf")
    EndIf
    FWRestArea(aArea)
    RETURN
