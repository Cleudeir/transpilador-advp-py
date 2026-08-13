# Esse exemplo faz parte da série do YouTube, Maratona de Exemplos, do canal Terminal de Informação, 
#     caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2023/08/09/operador-de-contido-em-maratona-advpl-e-tl-001/
# Bibliotecas
# PREPROCESSOR: #Include "TOTVS.ch"
# {Protheus.doc} User Function zExe001
# Exemplo de como utilizar o operador $ (cifrão), para ver se um conteúdo texto está contido em outro
# @type Function
# @author Atilio
# @since 26/11/2022
# @see https://tdn.engpro.totvs.com.br/display/tec/Operadores+Comuns
# @obs
#     **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
def u_zExe001():
    aArea = FWGetArea()
    cLetra = 'a'
    cNome = 'ATILIO'
    # Se a letra estiver "contida" na variável do nome
    if cLetra in cNome:
        FWAlertInfo('A letra esta contida no Nome', 'Teste 1')

    # Se a letra (tudo maiúscula) estiver "contida" na variável do nome (tudo maiúscula)
    if Upper(cLetra) in cNome:
        FWAlertInfo('A letra esta contida no Nome (variáveis tudo maiúsculas)', 'Teste 2')

    FWRestArea(aArea)
    return
