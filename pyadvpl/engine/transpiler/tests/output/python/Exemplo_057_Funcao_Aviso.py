# Esse exemplo faz parte da série do YouTube, Maratona de Exemplos, do canal Terminal de Informação, 
#     caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2023/10/04/exibindo-mensagens-com-a-funcao-aviso-maratona-advpl-e-tl-057/
# Bibliotecas
# PREPROCESSOR: #Include "TOTVS.ch"
# {Protheus.doc} User Function zExe057
# Exemplo de função que mostra uma mensagem de aviso na tela
# @type Function
# @author Atilio
# @since 05/12/2022
# @see https://tdn.totvs.com/display/public/framework/Aviso
# @obs 
#     Função Aviso
#     Parâmetros
#         + cTitulo         , Caracter   , Mensagem no Título
#         + cMsg            , Caracter   , Mensagem que será exibida na tela
#         + aBotoes         , Array      , Array com as opções dos botões
#         + nSize           , Numérico   , Tamanho da janela (podendo ser 1, 2 ou 3)
#         + cText           , Caracter   , Título da Descrição (dentro da janela)
#         + nRotAutDefault  , Numérico   , Opção padrão em caso de rotina automática
#         + cBitmap         , Caracter   , Nome da imagem BITMAP dentro do Repositório (descontinuado a partir do Protheus 12)
#         + lEdit           , Lógico     , Se .T. permitir editar a mensagem senão se for .F. não permite
#         + nTimer          , Numérico   , Tempo para exibir a mensagem em milissegundos
#         + nOpcPadrao      , Numérico   , Número da opção padrão do array
#     Retorno
#         + nOpcAviso       , Numérico   , Retorna a opção clicada pelo usuário
# 
#     **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
def u_zExe057():
    aArea = FWGetArea()
    cMsg = 'Terminal de Informação'
    nOpc = 0
    cMsgRet = cMsg
    # Mensagem pequena normal
    Aviso('Título Exemplo 1', cMsg, ['OK'], 1, 'Sub Título')
    # Mensagem média com botões
    nOpc = Aviso('Título Exemplo 2 (Botões)', cMsg, ['Sim', 'Não', 'Talvez'], 2, 'Sub Título')
    if nOpc == 1:
        FWAlertInfo('Clicou no Sim', 'Atenção')

    # Mensagem grande sendo possível editar
    Aviso('Título Exemplo 3 (Editável)', ref_(cMsgRet), ['OK'], 3, 'Sub Título', None, None, True)
    FWAlertInfo(cMsgRet, 'Conteúdo digitado')
    # Mensagem que fecha sozinha depois de 5 segundos
    cMsg += ' (tela será fechada em 5 segundos)'
    Aviso('Título Exemplo 4 (Timer)', cMsg, ['OK'], 2, 'Sub Título', None, None, None, 5000)
    FWRestArea(aArea)
    return
