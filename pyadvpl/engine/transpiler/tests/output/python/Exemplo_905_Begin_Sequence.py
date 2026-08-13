# PREPROCESSOR: #Include "TOTVS.ch"
# {Protheus.doc} zEx905
# Exemplo complexo de BEGIN SEQUENCE / RECOVER
# @author Antigravity
# @since 13/05/2026
def u_zEx905():
    nDivisor = 0
    nResultado = 0
    try:
        ConOut('Iniciando processo de divisÃ£o...')
        if nDivisor == 0:
            ConOut('Erro: DivisÃ£o por zero!')
            Break_

        nResultado = 100 / nDivisor
        ConOut('Resultado: ' + cValToChar(nResultado))
    except Exception:
        ConOut('Processo interrompido!')

    ConOut('Fim do exemplo.')
    return None
