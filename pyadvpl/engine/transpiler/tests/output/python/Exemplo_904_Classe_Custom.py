# PREPROCESSOR: #Include "TOTVS.ch"
# {Protheus.doc} zEx904
# Exemplo de definiÃ§Ã£o e uso de classe customizada
# @author Antigravity
# @since 13/05/2026
CLASS_
CustomClass
DATA
cNome
DATA
nId
# Method New for class 
def _New(self, ):
    pass

# Method Processa for class 
def _Processa(self, ):
    ENDCLASS

# Method New for class CustomClass
def CustomClass_New(self, ):
    self.cNome = ''
    self.nId = 0
    return self

# Method Processa for class CustomClass
def CustomClass_Processa(self, ):
    FWAlertInfo('Processando objeto: ' + self.cNome(), 'Sucesso')
    return

def u_zEx904():
    oObj = CustomClass().New()
    oObj.cNome = 'Teste Complexo'
    oObj.Processa()
    return
