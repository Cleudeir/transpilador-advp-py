// caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2023/10/14/buscando-o-primeiro-e-ultimo-dia-do-ano-com-begofyea-e-endofyea-maratona-advpl-e-tl-067/
// Bibliotecas
#Include "TOTVS.ch"
// {Protheus.doc} User Function zExe067
// Busca o primeiro e último dia do ano
// @type Function
// @author Atilio
// @since 06/12/2022
// Função BegOfYea
// Parâmetros
// + Data de Referência
// Retorno
// + Data com o primeiro dia do ano
// Função EndOfYea
// Parâmetros
// + Data de Referência
// Retorno
// + Data com o último dia do ano
// **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
USER FUNCTION zExe067()
    LOCAL aArea, dDataRef, dPriDiaAno, dUltDiaAno

    aArea := FWGetArea()
    dDataRef := Date()
    dPriDiaAno := Nil
    dUltDiaAno := Nil
    // Pegando o primeiro dia do ano
    dPriDiaAno := BegOfYea(dDataRef)
    // Pegando o último dia do ano
    dUltDiaAno := EndOfYea(dDataRef)
    // Exibindo as datas
    FWAlertInfo("Data de Referência: " + dToC(dDataRef) + CRLF + "Primeiro dia do Ano: " + dToC(dPriDiaAno) + CRLF + "Último dia do Ano: " + dToC(dUltDiaAno), "Exemplo de BegOfYea e EndOfYea")
    FWRestArea(aArea)
    RETURN
