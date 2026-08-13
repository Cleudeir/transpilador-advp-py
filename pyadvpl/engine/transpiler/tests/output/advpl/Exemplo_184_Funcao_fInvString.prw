// caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2024/01/20/buscando-o-primeiro-dia-de-um-mes-com-a-firstdate-maratona-advpl-e-tl-185/
// Bibliotecas
#Include "TOTVS.ch"
// {Protheus.doc} User Function zExe184
// Função que inverte uma string
// @type Function
// @author Atilio
// @since 21/12/2022
// Função fInvString
// Parâmetros
// + String original que será invertida
// Retorno
// + String já invertida
// **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
USER FUNCTION zExe184()
    LOCAL aArea, cNome, cAoContr

    aArea := FWGetArea()
    cNome := "daniel"
    cAoContr := Nil
    // Deixa a string de forma invertida
    cAoContr := fInvString(cNome)
    // Mostra o resultado
    FWAlertInfo("'" + cNome + "' ao contrário é '" + cAoContr + "'", "Teste fInvString")
    FWRestArea(aArea)
    RETURN
