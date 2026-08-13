// caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2024/01/21/verificando-como-um-texto-e-pronunciado-usando-a-funcao-fonetica-maratona-advpl-e-tl-187/
// Bibliotecas
#Include "TOTVS.ch"
// {Protheus.doc} User Function zExe187
// Verifica como um texto é pronunciado
// @type Function
// @author Atilio
// @since 21/12/2022
// Função Fonetica
// Parâmetros
// + Texto a ser verificado
// Retorno
// + Como o texto é pronunciado
// **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
USER FUNCTION zExe187()
    LOCAL aArea, cNome, cPronunc

    aArea := FWGetArea()
    cNome := "Wanderlei Chaves"
    cPronunc := ""
    // Busca a forma que é pronunciado
    cPronunc := Fonetica(cNome)
    // Exibe o resultado
    FWAlertInfo("O nome '" + cNome + "' é pronunciado como '" + cPronunc + "'", "Teste Fonetica")
    FWRestArea(aArea)
    RETURN
