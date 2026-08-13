// Exemplo completo testando os stubs implementados:
// - FWBrowse, FWMBrowse
// - FWDialogModal
// - MsNewProcess
// - FWRest, HttpGet, HttpPost
// - XmlParser, XmlNode2Arr, IsXmlNode
// - JsonObject, ArrToJson
#Include "TOTVS.ch"
USER FUNCTION zTestStubs()
    LOCAL aArea

    aArea := FWGetArea()
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
    RETURN Static

FUNCTION fTestFWBrowse()
    LOCAL oBrowse, aArea

    oBrowse := Nil
    aArea := FWGetArea()
    oBrowse := FWBrowse():New()
    oBrowse:SetAlias("SA1")
    oBrowse:SetQuery("SELECT * FROM SA1")
    oBrowse:AddColumn("Codigo", Nil, "C", 6, 0)
    oBrowse:AddLegend("SA1->A1_MSBLQL == '1'", "RED", "Bloqueado")
    oBrowse:DisableFilter()
    oBrowse:DisableConfig()
    oBrowse:DisableReport()
    oBrowse:DisableSeek()
    oBrowse:SetDataTable()
    oBrowse:Activate()
    FWRestArea(aArea)
    RETURN Static

FUNCTION fTestFWDialogModal()
    LOCAL oDlg, aArea

    oDlg := Nil
    aArea := FWGetArea()
    oDlg := FWDialogModal():New()
    oDlg:SetTitle("Teste Dialog")
    oDlg:SetSize(300, 400)
    oDlg:CreateDialog()
    oDlg:AddButton("Ok", Nil, "Ok")
    oDlg:Activate()
    FWRestArea(aArea)
    RETURN Static

FUNCTION fTestMsNewProcess()
    LOCAL oProcess, aArea

    oProcess := Nil
    aArea := FWGetArea()
    oProcess := MsNewProcess():New(Nil, "Processando", "Aguarde...", .T.)
    oProcess:SetRegs(100)
    oProcess:SetRegua1(50)
    oProcess:SetRegua2(10)
    oProcess:SetText("Iniciando...")
    oProcess:IncRegs()
    oProcess:IncRegua1("Item 1")
    oProcess:IncRegua2("Sub-item 1")
    oProcess:Activate()
    FWRestArea(aArea)
    RETURN Static

FUNCTION fTestFWRest()
    LOCAL oRest, aArea

    oRest := Nil
    aArea := FWGetArea()
    oRest := FWRest():New("https://viacep.com.br/ws")
    oRest:SetPath("/17054679/json/")
    oRest:SetTimeout(30)
    FWRestArea(aArea)
    RETURN Static

FUNCTION fTestHttpGet()
    LOCAL cResult, aArea

    cResult := ""
    aArea := FWGetArea()
    cResult := HttpGet("https://viacep.com.br/ws/17054679/json/", Nil, 30)
    If .NOT. Empty(cResult)
        FWAlertInfo("HttpGet ok", "Teste HttpGet")
    EndIf
    FWRestArea(aArea)
    RETURN Static

FUNCTION fTestHttpPost()
    LOCAL cResult, aArea

    cResult := ""
    aArea := FWGetArea()
    cResult := HttpPost("https://httpbin.org/post", Nil, "{'teste': true}", 30)
    FWRestArea(aArea)
    RETURN Static

FUNCTION fTestXmlParser()
    LOCAL cXML, oXML, oDetalhes, cAviso, cErro, aArea, xResult, aDados

    cXML := ""
    oXML := Nil
    oDetalhes := Nil
    cAviso := ""
    cErro := ""
    aArea := FWGetArea()
    cXML := "<?xml version="1.0"?>"
    cXML += "<detalhes>"
    cXML += "  <nome>Teste</nome>"
    cXML += "  <idade>30</idade>"
    cXML += "  <ativo>sim</ativo>"
    cXML += "</detalhes>"
    oXML := XmlParser(cXML, "_")
    If IsXmlNode(oXML, "_detalhes")
        oDetalhes := oXML:_detalhes()
        If AttIsMemberOf(oDetalhes, "_nome")
            xResult := XMLChildEx(oDetalhes, "_NOME")
        EndIf
        If XmlNodeExist(oDetalhes, "_idade")
            aDados := XmlToArr(oDetalhes:_idade())
        EndIf
    EndIf
    FWRestArea(aArea)
    RETURN Static

FUNCTION fTestJsonObject()
    LOCAL cJson, jDados, cError, aArea, cNome

    cJson := ""
    jDados := Nil
    cError := ""
    aArea := FWGetArea()
    cJson := "{"nome": "Teste", "idade": 30}"
    jDados := JsonObject():New()
    cError := jDados:FromJson(cJson)
    If Empty(cError)
        cNome := jDados:GetJsonObject("nome")
    EndIf
    FWRestArea(aArea)
    RETURN Static

FUNCTION fTestArrToJson()
    LOCAL aDados, cResult, aArea

    aDados := {  }
    cResult := ""
    aArea := FWGetArea()
    aAdd(aDados, { "nome", "Teste" })
    aAdd(aDados, { "idade", 30 })
    cResult := ArrToJson(aDados)
    FWRestArea(aArea)
    RETURN
