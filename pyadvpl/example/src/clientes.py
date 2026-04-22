from pyadvpl import db, ui, protheus

def u_ExemploCli():
    """
    Função de exemplo: Consulta de Clientes (SA1)
    """
    mv_parm = protheus.SuperGetMV("MV_ESTADO", "SP")
    ui.MsgInfo(f"Iniciando busca no estado: {mv_parm}")

    SA1 = db.Table("SA1")
    SA1.go_top()

    nCont = 0
    while not SA1.eof():
        # Acesso idiomático ao campo
        if SA1.A1_EST == mv_parm:
            nCont += 1
            if nCont == 1:
                ui.MsgAlert(f"Primeiro cliente encontrado: {SA1.A1_NOME}")
        
        SA1.skip()

    if ui.MsgYesNo(f"Encontrei {nCont} clientes. Deseja ver o resumo?"):
        ui.MsgInfo("Consulta finalizada com sucesso!")

    return None
