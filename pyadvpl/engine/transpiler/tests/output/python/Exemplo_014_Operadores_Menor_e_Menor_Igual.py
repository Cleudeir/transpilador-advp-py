# Esse exemplo faz parte da série do YouTube, Maratona de Exemplos, do canal Terminal de Informação, 
#     caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2023/08/22/operador-menor-e-menor-igual-maratona-advpl-e-tl-014/
# Bibliotecas
# PREPROCESSOR: #Include "TOTVS.ch"
# {Protheus.doc} User Function zExe014
# Exemplo de como utilizar os operadores Menor e Menor/Igual (< e <=)
# @type Function
# @author Atilio
# @since 26/11/2022
# @see https://tdn.engpro.totvs.com.br/display/tec/Operadores+Comuns
# @obs
#     **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
def u_zExe014():
    aArea = FWGetArea()
    nVar1 = 1
    nVar2 = 2
    # Somente se a variável for menor que a da direita
    if nVar1 < nVar2:
        FWAlertInfo('A nVar1 é menor que a nVar2', 'Primeiro teste')

    # Somente se a variável for menor ou igual a da direita
    if nVar1 <= nVar2:
        FWAlertInfo('A nVar1 é menor ou igual a nVar2', 'Segundo teste')

    FWRestArea(aArea)
    return
