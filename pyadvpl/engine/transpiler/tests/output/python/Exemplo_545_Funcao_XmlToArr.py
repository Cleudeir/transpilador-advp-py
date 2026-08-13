# Esse exemplo faz parte da série do YouTube, Maratona de Exemplos, do canal Terminal de Informação, 
#     caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2024/07/18/transformando-um-conteudo-xml-em-objeto-com-xmlparser-e-xmlparserfile-maratona-advpl-e-tl-544/
# Bibliotecas
# PREPROCESSOR: #Include "TOTVS.ch"
# {Protheus.doc} User Function zExe545
# Converte um nó para uma variável Array separado da estrutura (diferente da XmlNode2Arr)
# @type Function
# @author Atilio
# @since 07/04/2023
# @obs 
#     Função XmlToArr
#     Parâmetros
#         Nó do objeto XML instanciado
#     Retorno
#         Retorna um Array conforme as informações contidas dentro do Nó
# 
#     **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
def u_zExe545():
    aArea = FWGetArea()
    cXML = ''
    oXML = None
    cAviso = ''
    cErro = ''
    aDados = []
    # Monta o XML que será convertido em um Objeto
    cXML = '<?xml version="1.0"?>' + CRLF
    cXML += '<detalhes>' + CRLF
    cXML += '  <nome>Atilio</nome>' + CRLF
    cXML += '  <idade>29</idade>' + CRLF
    cXML += '  <gostaDeLer>sim</gostaDeLer>' + CRLF
    cXML += '  <sites>' + CRLF
    cXML += '    <site item="1">' + CRLF
    cXML += '\t  <nome>Terminal de Informacao</nome>' + CRLF
    cXML += '\t  <url>terminaldeinformacao.com</url>' + CRLF
    cXML += '\t</site>' + CRLF
    cXML += '\t<site item="2">' + CRLF
    cXML += '\t  <nome>Atilio Sistemas</nome>' + CRLF
    cXML += '\t  <url>atiliosistemas.com</url>' + CRLF
    cXML += '\t</site>' + CRLF
    cXML += '  </sites>' + CRLF
    cXML += '</detalhes>' + CRLF
    # Transformando o XML (texto) em um objeto
    oXML = XmlParser(cXML, '_', ref_(cAviso), ref_(cErro))
    # Se houve alguma falha
    if not Empty(cErro):
        FWAlertError('Houve um erro na conversão do texto para objeto: ' + cErro, "Falha no 'parse' do XML")
    else:
        # Realiza a conversão inteira para um Array
        aDados = XmlToArr(oXML._detalhes()._gostaDeLer())
        # Se houver informações, mostra mensagem
        if Len(aDados) > 0:
            FWAlertSuccess('Objeto convertido para Array!', 'Teste XmlToArr')


    FWRestArea(aArea)
    return
