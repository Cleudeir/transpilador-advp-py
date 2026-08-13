# Esse exemplo faz parte da série do YouTube, Maratona de Exemplos, do canal Terminal de Informação, 
#     caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2023/10/11/tratando-execucoes-e-erros-com-begin-sequence-end-maratona-advpl-e-tl-064/
# Bibliotecas
# PREPROCESSOR: #Include "TOTVS.ch"
# {Protheus.doc} User Function zExe064
# Exemplo de como realizar tratativas e recuperar caso haja falhas
# @type Function
# @author Atilio
# @since 06/12/2022
# @see https://tdn.totvs.com/display/public/framework/BEGIN+SEQUENCE+...+END
# @obs 
# 
#     **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
def u_zExe064():
    aArea = FWGetArea()
    cError = ''
    bError = ErrorBlock(lambda oError: (cError := oError.Description()))
    nVar = 1
    cVar = 'A'
    # Inicio a utilização da tentativa
    try:
        nVariavel = nVar + cVar
    except Exception:
        pass

    # Restaurando bloco de erro do sistema
    ErrorBlock(bError)
    # Se houve erro, será mostrado ao usuário
    if not Empty(cError):
        FWAlertError('Houve um erro na fórmula digitada: ' + CRLF + CRLF + cError, 'Teste com Begin Sequence')

    FWRestArea(aArea)
    return
