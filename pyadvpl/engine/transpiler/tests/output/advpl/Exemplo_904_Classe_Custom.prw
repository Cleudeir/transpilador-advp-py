#Include "TOTVS.ch"
// {Protheus.doc} zEx904
// Exemplo de definição e uso de classe customizada
// @author Antigravity
// @since 13/05/2026
CLASS_
CustomClass
DATA
cNome
DATA
nId
FUNCTION _New(self)
    RETURN Nil

FUNCTION _Processa(self)
    ENDCLASS
    RETURN Nil

// Method New for class CustomClass
FUNCTION CustomClass_New(self)
    ::cNome := ""
    ::nId := 0
    RETURN self

// Method Processa for class CustomClass
FUNCTION CustomClass_Processa(self)
    FWAlertInfo("Processando objeto: " + ::cNome(), "Sucesso")
    RETURN

USER FUNCTION zEx904()
    LOCAL oObj

    oObj := CustomClass():New()
    oObj->cNome := "Teste Complexo"
    oObj:Processa()
    RETURN
