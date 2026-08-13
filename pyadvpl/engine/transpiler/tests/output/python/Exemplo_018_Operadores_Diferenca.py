# Esse exemplo faz parte da série do YouTube, Maratona de Exemplos, do canal Terminal de Informação, 
#     caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2023/08/26/operadores-de-diferenca-maratona-advpl-e-tl-018/
# Bibliotecas
# PREPROCESSOR: #Include "TOTVS.ch"
# {Protheus.doc} User Function zExe016
# Exemplo de como utilizar os operadores de diferença (<> ou # ou !=)
# @type Function
# @author Atilio
# @since 26/11/2022
# @see https://tdn.engpro.totvs.com.br/display/tec/Operadores+Comuns
# @obs
#     **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
def u_zExe018():
    aArea = FWGetArea()
    cVar1 = 'Daniel'
    cVar2 = 'Atilio'
    # Usando o sinal de menor/maior
    if cVar1 != cVar2:
        FWAlertInfo('Variáveis são diferentes', 'Primeiro If')

    # Usando sustenido
    if cVar1:
        # PREPROCESSOR: # cVar2
        FWAlertInfo('Variáveis são diferentes', 'Segundo If')

    # Usando o diferente igual
    if cVar1 != cVar2:
        FWAlertInfo('Variáveis são diferentes', 'Terceiro If')

    # Usando a NEGAÇÃO DE EXATAMENTE igual
    if not cVar1 == cVar2:
        FWAlertInfo('Variáveis são diferentes', 'Quarto If')

    FWRestArea(aArea)
    return
