# Exemplo completo testando os stubs implementados:
#     - FWBrowse, FWMBrowse
#     - FWDialogModal
#     - MsNewProcess
#     - FWRest, HttpGet, HttpPost
#     - XmlParser, XmlNode2Arr, IsXmlNode
#     - JsonObject, ArrToJson
# PREPROCESSOR: #Include "TOTVS.ch"
def u_zTestStubs():
    aArea = FWGetArea()
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
    return Static

def fTestFWBrowse():
    oBrowse = None
    aArea = FWGetArea()
    oBrowse = FWBrowse().New()
    oBrowse.SetAlias('SA1')
    oBrowse.SetQuery('SELECT * FROM SA1')
    oBrowse.AddColumn('Codigo', lambda o: SA1.A1_COD, 'C', 6, 0)
    oBrowse.AddLegend("SA1->A1_MSBLQL == '1'", 'RED', 'Bloqueado')
    oBrowse.DisableFilter()
    oBrowse.DisableConfig()
    oBrowse.DisableReport()
    oBrowse.DisableSeek()
    oBrowse.SetDataTable()
    oBrowse.Activate()
    FWRestArea(aArea)
    return Static

def fTestFWDialogModal():
    oDlg = None
    aArea = FWGetArea()
    oDlg = FWDialogModal().New()
    oDlg.SetTitle('Teste Dialog')
    oDlg.SetSize(300, 400)
    oDlg.CreateDialog()
    oDlg.AddButton('Ok', lambda : oDlg.DeActivate(), 'Ok')
    oDlg.Activate()
    FWRestArea(aArea)
    return Static

def fTestMsNewProcess():
    oProcess = None
    aArea = FWGetArea()
    oProcess = MsNewProcess().New(lambda : True, 'Processando', 'Aguarde...', True)
    oProcess.SetRegs(100)
    oProcess.SetRegua1(50)
    oProcess.SetRegua2(10)
    oProcess.SetText('Iniciando...')
    oProcess.IncRegs()
    oProcess.IncRegua1('Item 1')
    oProcess.IncRegua2('Sub-item 1')
    oProcess.Activate()
    FWRestArea(aArea)
    return Static

def fTestFWRest():
    oRest = None
    aArea = FWGetArea()
    oRest = FWRest().New('https://viacep.com.br/ws')
    oRest.SetPath('/17054679/json/')
    oRest.SetTimeout(30)
    FWRestArea(aArea)
    return Static

def fTestHttpGet():
    cResult = ''
    aArea = FWGetArea()
    cResult = HttpGet('https://viacep.com.br/ws/17054679/json/', None, 30)
    if not Empty(cResult):
        FWAlertInfo('HttpGet ok', 'Teste HttpGet')

    FWRestArea(aArea)
    return Static

def fTestHttpPost():
    cResult = ''
    aArea = FWGetArea()
    cResult = HttpPost('https://httpbin.org/post', None, "{'teste': true}", 30)
    FWRestArea(aArea)
    return Static

def fTestXmlParser():
    cXML = ''
    oXML = None
    oDetalhes = None
    cAviso = ''
    cErro = ''
    aArea = FWGetArea()
    cXML = '<?xml version="1.0"?>'
    cXML += '<detalhes>'
    cXML += '  <nome>Teste</nome>'
    cXML += '  <idade>30</idade>'
    cXML += '  <ativo>sim</ativo>'
    cXML += '</detalhes>'
    oXML = XmlParser(cXML, '_')
    if IsXmlNode(oXML, '_detalhes'):
        oDetalhes = oXML._detalhes()
        if AttIsMemberOf(oDetalhes, '_nome'):
            xResult = XMLChildEx(oDetalhes, '_NOME')

        if XmlNodeExist(oDetalhes, '_idade'):
            aDados = XmlToArr(oDetalhes._idade())


    FWRestArea(aArea)
    return Static

def fTestJsonObject():
    cJson = ''
    jDados = None
    cError = ''
    aArea = FWGetArea()
    cJson = '{"nome": "Teste", "idade": 30}'
    jDados = JsonObject().New()
    cError = jDados.FromJson(cJson)
    if Empty(cError):
        cNome = jDados.GetJsonObject('nome')

    FWRestArea(aArea)
    return Static

def fTestArrToJson():
    aDados = []
    cResult = ''
    aArea = FWGetArea()
    aAdd(aDados, ['nome', 'Teste'])
    aAdd(aDados, ['idade', 30])
    cResult = ArrToJson(aDados)
    FWRestArea(aArea)
    return
