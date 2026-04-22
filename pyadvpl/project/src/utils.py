from pyadvpl import Date

def u_CheckDate():
    dHoje = Date.today()
    return dHoje.to_str()
