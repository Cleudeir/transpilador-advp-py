# Esse exemplo faz parte da série do YouTube, Maratona de Exemplos, do canal Terminal de Informação, 
#     caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2023/10/30/extraindo-informacoes-de-um-objeto-com-a-funcao-classdataarr-maratona-advpl-e-tl-083/
# Bibliotecas
# PREPROCESSOR: #Include "TOTVS.ch"
# {Protheus.doc} User Function zExe083
# Exemplo de como extrair informações de um objeto para uma variável
# @type Function
# @author Atilio
# @since 09/12/2022
# @obs 
#     Função ClassDataArr
#     Parâmetros
#         + Recebe um objeto instanciado
#     Retorno
#         + Retorna um array com todos os atributos
# 
#     **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
def u_zExe083():
    aArea = FWGetArea()
    aInfo = None
    oObjeto = None
    # Instancia uma classe
    oObjeto = TFont().New('Tahoma', None, -12)
    # Extrai a informação para um Array
    aInfo = ClassDataArr(oObjeto)
    # Exibe uma mensagem com o tamannho do array
    FWAlertInfo('O array aInfo tem ' + cValToChar(Len(aInfo)) + ' elemento(s)', 'Teste de ClassDataArr')
    FWRestArea(aArea)
    return
