# Esse exemplo faz parte da série do YouTube, Maratona de Exemplos, do canal Terminal de Informação, 
#     caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2024/02/02/criando-graficos-atraves-da-fwchartfactory-maratona-advpl-e-tl-210/
# Bibliotecas
# PREPROCESSOR: #Include "TOTVS.ch"
# {Protheus.doc} User Function zExe211
# Exemplo de função que traz o código da empresa logada
# @type Function
# @author Atilio
# @since 20/02/2023
# @see https://tdn.totvs.com/pages/releaseview.action?pageId=6815128
# @obs 
#     Função FWCodEmp
#     Parâmetros
#         + cAlias    , Caractere , Alias da tabela que será validada
#     Retorno
#         + cEmp      , Caractere , Código da Empresa
# 
#     **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
def u_zExe211():
    aArea = FWGetArea()
    cEmprLog = ''
    cFiliLog = ''
    cMensag = ''
    # Pega a empresa logada
    cEmprLog = FWCodEmp()
    # Pega a filial logada
    cFiliLog = FWCodFil()
    # Exibe uma mensagem
    cMensag = "Estou logado na empresa '" + cEmprLog + "' e na filial '" + cFiliLog + "'!"
    FWAlertInfo(cMensag, 'Teste de FWCodEmp')
    FWRestArea(aArea)
    return
