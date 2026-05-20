/*
    Exemplo completo testando os stubs implementados:
    - FWBrowse, FWMBrowse
    - FWDialogModal
    - MsNewProcess
    - FWRest, HttpGet, HttpPost
    - XmlParser, XmlNode2Arr, IsXmlNode
    - JsonObject, ArrToJson
*/

#Include "TOTVS.ch"

User Function zTestStubs()
    Local aArea := FWGetArea()

    fTestFWBrowse()
    fTestFWDialogModal()
    fTestMsNewProcess()
    fTestFWRest()
    fTestHttpGet()
    fTestHttpPost()
    fTestXmlParser()
    fTestJsonObject()
    fTestArrToJson()

    FWRestArea(aArea)
Return

Static Function fTestFWBrowse()
    Local oBrowse
    Local aArea := FWGetArea()

    oBrowse := FWBrowse():New()
    oBrowse:SetAlias("SA1")
    oBrowse:SetQuery("SELECT * FROM SA1")
    oBrowse:AddColumn("Codigo", {|o| SA1->A1_COD}, "C", 6, 0)
    oBrowse:AddLegend("SA1->A1_MSBLQL == '1'", "RED", "Bloqueado")
    oBrowse:DisableFilter()
    oBrowse:DisableConfig()
    oBrowse:DisableReport()
    oBrowse:DisableSeek()
    oBrowse:SetDataTable()
    oBrowse:Activate()

    FWRestArea(aArea)
Return

Static Function fTestFWDialogModal()
    Local oDlg
    Local aArea := FWGetArea()

    oDlg := FWDialogModal():New()
    oDlg:SetTitle("Teste Dialog")
    oDlg:SetSize(300, 400)
    oDlg:CreateDialog()
    oDlg:AddButton("Ok", {|| oDlg:DeActivate()}, "Ok")
    oDlg:Activate()

    FWRestArea(aArea)
Return

Static Function fTestMsNewProcess()
    Local oProcess
    Local aArea := FWGetArea()

    oProcess := MsNewProcess():New({|| .T.}, "Processando", "Aguarde...", .T.)
    oProcess:SetRegs(100)
    oProcess:SetRegua1(50)
    oProcess:SetRegua2(10)
    oProcess:SetText("Iniciando...")
    oProcess:IncRegs()
    oProcess:IncRegua1("Item 1")
    oProcess:IncRegua2("Sub-item 1")
    oProcess:Activate()

    FWRestArea(aArea)
Return

Static Function fTestFWRest()
    Local oRest
    Local aArea   := FWGetArea()

    oRest := FWRest():New("https://viacep.com.br/ws")
    oRest:SetPath("/17054679/json/")
    oRest:SetTimeout(30)

    FWRestArea(aArea)
Return

Static Function fTestHttpGet()
    Local cResult := ""
    Local aArea   := FWGetArea()

    cResult := HttpGet("https://viacep.com.br/ws/17054679/json/", , 30)

    If ! Empty(cResult)
        FWAlertInfo("HttpGet ok", "Teste HttpGet")
    EndIf

    FWRestArea(aArea)
Return

Static Function fTestHttpPost()
    Local cResult := ""
    Local aArea   := FWGetArea()

    cResult := HttpPost("https://httpbin.org/post", , "{'teste': true}", 30)

    FWRestArea(aArea)
Return

Static Function fTestXmlParser()
    Local cXML    := ""
    Local oXML
    Local oDetalhes
    Local cAviso  := ""
    Local cErro   := ""
    Local aArea   := FWGetArea()

    cXML := '<?xml version="1.0"?>'
    cXML += '<detalhes>'
    cXML += '  <nome>Teste</nome>'
    cXML += '  <idade>30</idade>'
    cXML += '  <ativo>sim</ativo>'
    cXML += '</detalhes>'

    oXML := XmlParser(cXML, "_")

    If IsXmlNode(oXML, "_detalhes")
        oDetalhes := oXML:_detalhes

        If AttIsMemberOf(oDetalhes, "_nome")
            xResult := XMLChildEx(oDetalhes, "_NOME")
        EndIf

        If XmlNodeExist(oDetalhes, "_idade")
            aDados := XmlToArr(oDetalhes:_idade)
        EndIf
    EndIf

    FWRestArea(aArea)
Return

Static Function fTestJsonObject()
    Local cJson    := ""
    Local jDados
    Local cError   := ""
    Local aArea    := FWGetArea()

    cJson := '{"nome": "Teste", "idade": 30}'

    jDados := JsonObject():New()
    cError := jDados:FromJson(cJson)

    If Empty(cError)
        cNome := jDados:GetJsonObject("nome")
    EndIf

    FWRestArea(aArea)
Return

Static Function fTestArrToJson()
    Local aDados  := {}
    Local cResult := ""
    Local aArea   := FWGetArea()

    aAdd(aDados, {"nome", "Teste"})
    aAdd(aDados, {"idade", 30})

    cResult := ArrToJson(aDados)

    FWRestArea(aArea)
Return
