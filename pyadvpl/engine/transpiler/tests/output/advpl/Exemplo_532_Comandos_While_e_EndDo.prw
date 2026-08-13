// caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2024/07/12/buscando-a-pasta-padrao-de-relatorios-com-a-wsplreldir-maratona-advpl-e-tl-533/
// Bibliotecas
#Include "TOTVS.ch"
// {Protheus.doc} User Function zExe532
// Efetua um laço de repetição enquanto uma condição for verdadeira
// @type Function
// @author Atilio
// @since 07/04/2023
// @see https://tdn.totvs.com/display/tec/O+Comando+WHILE...ENDDO
// **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
USER FUNCTION zExe532()
    LOCAL aArea, aAreaSA2, cMsg, nAtual

    aArea := FWGetArea()
    aAreaSA2 := SA2:FWGetArea()
    cMsg := ""
    nAtual := 0
    // Enquanto for verdadeiro
    While .T.
        // Se a pergunta for confirmada, volta o laço
        If MsgYesNo("Deseja continuar o laço?", "Atenção")
            Loop
        EndIf
    EndDo
    // Abrindo a tabela de fornecedores e posicionando no topo
    DbSelectArea("SA2")
    SA2:DbSetOrder(1)
    SA2:DbGoTop()
    // Enquanto houver dados nos fornecedores e for menos que 100 registros
    While .NOT. SA2->( DbEof() )
        nAtual += 1
        cMsg += "[" + cValToChar(nAtual) + "] " + Alltrim(SA2->A2_NOME) + ";" + CRLF
        SA2:DbSkip()
    EndDo
    // //Exemplo de utilizacao de alias
    // //Executo query QRY_SF1
    // While ! QRY_SF1->(EoF())
    // //Executo query QRY_SD1
    // While ! QRY_SD1->(EoF())
    // QRY_SD1->(DbSkip())
    // EndDo
    // QRY_SD1->(DbCloseArea())
    // QRY_SF1->(DbSkip())
    // EndDo
    // Mostrando os fornecedores
    Aviso("Atenção", cMsg, { "OK" }, 2)
    FWRestArea(aAreaSA2)
    FWRestArea(aArea)
    RETURN
