# Esse exemplo faz parte da série do YouTube, Maratona de Exemplos, do canal Terminal de Informação, 
#     caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2023/08/20/operadores-and-e-or-para-utilizacao-em-condicoes-maratona-advpl-e-tl-012/
# Bibliotecas
# PREPROCESSOR: #Include "TOTVS.ch"
# {Protheus.doc} User Function zExe012
# Exemplo de como utilizar os operadores .And. e .Or. nos testes
# @type Function
# @author Atilio
# @since 26/11/2022
# @see https://tdn.engpro.totvs.com.br/display/tec/Operadores+Comuns
# @obs
#     **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
def u_zExe012():
    aArea = FWGetArea()
    nVar1 = 2
    nVar2 = 2
    # Somente se a primeira condição E a segunda forem verdadeiras
    if nVar1 == nVar2 and fTstFunc():
        FWAlertInfo('Resultado é verdadeiro', 'Teste com .And.')

    # Se a primeira condição OU a segunda for verdadeira
    if fTstFunc() or FWAlertYesNo('Pergunta de Teste', 'Continua?'):
        FWAlertInfo('Resultado é verdadeiro', 'Teste com .Or.')

    FWRestArea(aArea)
    return Static

def fTstFunc():
    lRet = True
    return lRet
