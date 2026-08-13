// caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2024/03/26/buscando-data-e-hora-com-milissegundos-com-jurtime-e-jurtimestamp-maratona-advpl-e-tl-317/
// Bibliotecas
#Include "TOTVS.ch"
// {Protheus.doc} User Function zExe316
// Converte texto ou arquivo para um objeto JSON
// @type Function
// @author Atilio
// @since 25/02/2023
// @see https://tdn.totvs.com/display/tec/Classe+JsonObject
// **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
USER FUNCTION zExe316()
    LOCAL aArea, cJsonText, jDados, cError, aSites, cMensagem, nAtual

    aArea := FWGetArea()
    cJsonText := ""
    jDados := Nil
    cError := Nil
    aSites := Nil
    cMensagem := ""
    nAtual := Nil
    // Monta o JSON que será convertido em um Objeto
    cJsonText := "{" + CRLF
    cJsonText += "  "nome":"Atilio"," + CRLF
    cJsonText += "  "idade":29," + CRLF
    cJsonText += "  "gostaDeLer":true," + CRLF
    cJsonText += "  "sites":[" + CRLF
    cJsonText += "    {"nome":"Terminal de Informacao", "url":"terminaldeinformacao.com"}," + CRLF
    cJsonText += "	  {"nome":"Atilio Sistemas", "url":"atiliosistemas.com"}" + CRLF
    cJsonText += "  ]" + CRLF
    cJsonText += "}" + CRLF
    // Transformando o JSON (texto) em um objeto
    jDados := JsonObject():New()
    cError := jDados:FromJson(cJsonText)
    // Se tiver algum erro no Parse, encerra a execução
    If .NOT. Empty(cError)
        FWAlertError("Houve um erro na conversão do texto para objeto: " + cErro, "Falha no 'parse' do JSON")
    Else
        // Começa a montar uma mensagem
        cMensagem += "Nome: " + jDados:GetJsonObject("nome") + CRLF + CRLF
        // Busca os sites
        aSites := jDados:GetJsonObject("sites")
        // Se encontrou um Array, percorre adicionando a mensagem
        If ValType(aSites) = "A"
        EndIf
        // Exibindo a mensagem
        FWAlertInfo(cMensagem, "Exemplo de JsonObject")
    EndIf
    FWRestArea(aArea)
    RETURN
