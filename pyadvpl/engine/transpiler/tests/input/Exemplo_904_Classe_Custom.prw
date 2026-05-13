#Include "TOTVS.ch"

/*/{Protheus.doc} zEx904
Exemplo de definição e uso de classe customizada
@author Antigravity
@since 13/05/2026
/*/
CLASS CustomClass
    DATA cNome
    DATA nId
    METHOD New()
    METHOD Processa()
ENDCLASS

METHOD New() CLASS CustomClass
    ::cNome := ""
    ::nId := 0
RETURN self

METHOD Processa() CLASS CustomClass
    FWAlertInfo("Processando objeto: " + ::cNome, "Sucesso")
RETURN

User Function zEx904()
    Local oObj := CustomClass():New()
    oObj:cNome := "Teste Complexo"
    oObj:Processa()
Return
