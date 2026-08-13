# Esse exemplo faz parte da série do YouTube, Maratona de Exemplos, do canal Terminal de Informação, 
#     caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2024/02/19/fazendo-um-backup-das-linhas-de-grids-em-mvc-com-fwsaverows-e-fwrestrows-maratona-advpl-e-tl-244/
# Bibliotecas
# PREPROCESSOR: #Include "TOTVS.ch"
# {Protheus.doc} User Function zExe245
# Função que busca todos os usuários cadastrados
# @type  Function
# @author Atilio
# @since 20/02/2023
# @see https://tdn.totvs.com/display/public/PROT/FWSFALLUSERS
# @obs 
#     Função FWsFAllUsers
#     Parâmetros
#         + aUserList   , Array    , Informa a lista de usuários
#         + aKeyValues  , Array    , Lista com os campos que serão retornados
#         + Reservado
#         + Reservado
#         + lBlock      , Lógico   , Retorna informação de usuários bloqueados
#     Retorno
#         + aUsers      , Array    , Array com as seguintes posições [1] Id da tabela de usuários (r_e_c_n_o_) ; [2] Id do usuário ; [3] Login do Usuário ; [4] Nome do usuário ; [5] email do usuário ; [6] departamento do usuário ; [7] cargo do usuário
#     
#     **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
def u_zExe245():
    aArea = FWGetArea()
    lAcessa = False
    cUsrLogad = RetCodUsr()
    aTodosUsr = FWSfAllUsers()
    nEncontrou = 0
    aGrupos = []
    nGrupoAtu = 0
    aEmpFil = []
    # Se for admin, ele tem acesso a empresa e filial
    if FWIsAdmin():
        lAcessa = True
    else:
        # Efetua a busca pelo usuário logado
        nEncontrou = aScan(aTodosUsr, lambda x: x[2] == cUsrLogad)
        # Se encontrou o usuário
        if nEncontrou > 0:
            # Busca todos os grupos que o usuário tem acesso
            aGrupos = FWSFUsrGrps(cUsrLogad)
            # Percorre os grupos


    if lAcessa:
        FWAlertSuccess('Usuário possui acesso!', 'Teste FWSfAllUsers')

    FWRestArea(aArea)
    return
