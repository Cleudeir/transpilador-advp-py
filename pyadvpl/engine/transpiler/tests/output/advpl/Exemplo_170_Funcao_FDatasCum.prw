// caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2024/01/13/buscando-datas-de-um-intervalo-com-fdatascum-maratona-advpl-e-tl-170/
// Bibliotecas
#Include "TOTVS.ch"
// {Protheus.doc} User Function zExe170
// Retorna as datas de um intervalo
// @type Function
// @author Atilio
// @since 19/12/2022
// Função FDatasCum
// Parâmetros
// + Período a ser validado sendo 1= Diário; 2= Compatibilidade (Semanal); 3= Decendial; 4= Mensal
// + Data de referência
// Retorno
// + Array com as datas do intervalo encontrado
// **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
USER FUNCTION zExe170()
    LOCAL aArea, dDataRef, aDiario, aDecendial, aMensal, cMensagem

    aArea := FWGetArea()
    dDataRef := Date()
    aDiario := {  }
    aDecendial := {  }
    aMensal := {  }
    cMensagem := ""
    // Busca os períodos
    aDiario := FDatasCum("1", dDataRef)
    aDecendial := FDatasCum("3", dDataRef)
    aMensal := FDatasCum("4", dDataRef)
    // Monta a mensagem com os períodos
    cMensagem += "Diario: " + CenArr2Str(aDiario[1], ";") + CRLF
    cMensagem += "Decendio: " + CenArr2Str(aDecendial[1], ";") + CRLF
    cMensagem += "Mensal: " + CenArr2Str(aMensal[1], ";")
    FWAlertInfo(cMensagem, "Teste com FDatasCum")
    FWRestArea(aArea)
    RETURN
