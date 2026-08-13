# Esse exemplo faz parte da série do YouTube, Maratona de Exemplos, do canal Terminal de Informação, 
#     caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2023/11/05/abrindo-uma-consulta-padrao-da-sxb-usando-a-funcao-conpad1-maratona-advpl-e-tl-089/
# Bibliotecas
# PREPROCESSOR: #Include "TOTVS.ch"
# {Protheus.doc} User Function zExe089
# Exemplo de como abrir uma tela de consulta padrão (SXB)
# @type Function
# @author Atilio
# @since 09/12/2022
# @obs 
#     Função Conpad1
#     Parâmetros
#         + Compatibilidade
#         + Compatibilidade
#         + Compatibilidade
#         + Nome da consulta padrão / específica da SXB
#         + Expressão de retorno no lugar da usada na SXB
#         + Compatibilidade
#         + Define se será só visualização (.T.) ou se terá outros botões como Incluir (.F.) dependendo do cadastro na SXB
#         + Conteúdo que já deixará a consulta posicionada
#         + Define se o LookUp veio de um campo
#         + Conteúdo respectivo ao cVar
#     Retorno
#         + .T. se o usuário clicou em confirmar ou .F. se ele cancelou a tela
# 
#     **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
def u_zExe089():
    aArea = FWGetArea()
    cCodPesq = 'C00002'
    DbSelectArea('SA1')
    SA1.DbSetOrder(1)
    # Filial + Código + Loja
    # Mostra a consulta padrão de nome SA1 (na SXB)
    if ConPad1(None, None, None, 'SA1'):
        # Se a consulta foi confirmada, mostra o Cliente selecionado
        FWAlertSuccess('Cliente selecionado foi ' + aCpoRet[1], 'Teste Conpad1')

    # Mostra a consulta padrão de nome SA1 (na SXB) já posicionando no Cliente de código C00002
    if ConPad1(None, None, None, 'SA1', None, None, None, 'cCodPesq'):
        # Se a consulta foi confirmada, mostra o Cliente selecionado
        FWAlertSuccess('Cliente selecionado foi ' + aCpoRet[1], 'Teste Conpad1')

    FWRestArea(aArea)
    return
