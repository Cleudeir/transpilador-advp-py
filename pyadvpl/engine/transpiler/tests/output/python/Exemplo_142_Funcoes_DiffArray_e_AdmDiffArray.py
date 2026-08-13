# Esse exemplo faz parte da série do YouTube, Maratona de Exemplos, do canal Terminal de Informação, 
#     caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2023/12/28/comparando-se-dois-arrays-tem-diferencas-com-diffarray-e-admdiffarray-maratona-advpl-e-tl-142/
# Bibliotecas
# PREPROCESSOR: #Include "TOTVS.ch"
# {Protheus.doc} User Function zExe142
# Retorna se há diferenças entre dois arrays
# @type Function
# @author Atilio
# @since 16/12/2022
# @obs 
#     Função DiffArray
#     Parâmetros
#         + Array a ser comparado (monodimensional)
#         + Array de comparação (monodimensional)
#     Retorno
#         + Retorna .F. se são iguais ou .T. se houver diferenças
# 
#     Função AdmDiffArray
#     Parâmetros
#         + Array a ser comparado (mono ou multidimensional)
#         + Array de comparação (mono ou multidimensional)
#     Retorno
#         + .F. se são iguais ou .T. se houver diferenças
# 
#     **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
def u_zExe142():
    aArea = FWGetArea()
    aPessoas1 = []
    aPessoas2 = []
    # Adiciona dados em ambos os arrays (monodimensional)
    aAdd(aPessoas1, 'Daniel')
    aAdd(aPessoas1, 'João')
    aAdd(aPessoas1, 'Maria')
    aAdd(aPessoas2, 'Daniel')
    aAdd(aPessoas2, 'Maria')
    aAdd(aPessoas2, 'José')
    # Faz a comparação de arrays monodimensionais
    if DiffArray(aPessoas1, aPessoas2):
        FWAlertError('Há diferenças entre os dois arrays', 'Teste com DiffArray')
    else:
        FWAlertSuccess('Não há diferenças entre os dois arrays', 'Teste com DiffArray')

    # Adiciona dados em ambos os arrays (multidimensional)
    aPessoas1 = []
    aAdd(aPessoas1, ['Daniel', sToD('19930712'), 'Bauru'])
    aAdd(aPessoas1, ['Joao', sToD('19910131'), 'Agudos'])
    aAdd(aPessoas1, ['Maria', sToD('19921231'), 'Piratininga'])
    aPessoas2 = []
    aAdd(aPessoas2, ['Daniel', sToD('19930712'), 'Bauru'])
    aAdd(aPessoas2, ['Joao', sToD('19910131'), 'Agudos'])
    aAdd(aPessoas2, ['Maria', sToD('19921231'), 'Piratininga'])
    # Faz a comparação de arrays multidimensionais
    if AdmDiffArray(aPessoas1, aPessoas2):
        FWAlertError('Há diferenças entre os dois arrays', 'Teste com AdmDiffArray')
    else:
        FWAlertSuccess('Não há diferenças entre os dois arrays', 'Teste com AdmDiffArray')

    FWRestArea(aArea)
    return
