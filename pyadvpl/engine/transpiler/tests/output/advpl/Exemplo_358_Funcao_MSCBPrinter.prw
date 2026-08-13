// caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2024/04/16/abrindo-o-banco-de-conhecimento-com-a-msdocument-maratona-advpl-e-tl-359/
// Bibliotecas
#Include "TOTVS.ch"
#Include "TopConn.ch"
// {Protheus.doc} User Function zExe358
// Realiza a impressão de uma etiqueta em uma impressora térmica
// @type Function
// @author Atilio
// @since 26/03/2023
// @see https://tdn.totvs.com/display/public/mp/MSCBPrinter+-+Configura+Impressora+--+30557
// Função MSCBPrinter
// Parâmetros
// + cModelPrt   , Caractere        , String com o nome do modelo da impressora
// + cPorta      , Caractere        , String com o número da porta
// + nDensidade  , Numérico         , Número com densidade
// + nTamanho    , Numérico         , Tamanho da etiqueta em milímetros
// + lSrv        , Lógico           , Se .T. imprime no servidor se .F. na estação
// + nPorta      , Numérico         , Número da porta (outro server)
// + cServer     , Caractere        , Endereço de IP (outro server)
// + cEnv        , Caractere        , Ambiente (outro server)
// + nMemoria    , Numérico         , Número do bloco de memória da impressora
// + cFila       , Caractere        , Pasta onde será gravada a fila de impressão
// + lDrvWin     , Lógico           , Indica se será usado os drivers instalados no Windows
// + cPathSpool  , Caractere        , Diretório do spooler de impressão que irá controlar a fila
// Retorno
// Função não tem retorno
// **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
USER FUNCTION zExe358()
    LOCAL aArea, aPergs, cPedido

    aArea := FWGetArea()
    aPergs := {  }
    cPedido := Space(TamSX3("C5_NUM")[1])
    // Adicionando os parametros do ParamBox
    aAdd(aPergs, { 1, "Pedido", cPedido, "", ".T.", "SC5", ".T.", 80, .F. })
    // MV_PAR01
    // Se a pergunta for confirma, cria as definicoes do relatorio
    If ParamBox(aPergs, "Informe os parâmetros", Nil, Nil, Nil, Nil, Nil, Nil, Nil, Nil, .F., .F.)
        Processa(Nil, "Processando...")
    EndIf
    FWRestArea(aArea)
    RETURN Static

FUNCTION fMontaRel()
    LOCAL cPorta, nQtdCopias, nVolIniPvt, nVolFimPvt

    cPorta := "LPT1"
    nQtdCopias := 1
    nVolIniPvt := 1
    nVolFimPvt := 1
    DbSelectArea("SC5")
    SC5:DbSetOrder(1)
    // C5_FILIAL + C5_NUM
    DbSelectArea("SA1")
    SA1:DbSetOrder(1)
    // A1_FILIAL + A1_COD + A1_LOJA
    DbSelectArea("SA4")
    SA4:DbSetOrder(1)
    // A4_FILIAL + A4_COD
    // Somente se conseguir posicionar no pedido
    If SC5:MsSeek(FWxFilial("SC5") + MV_PAR01)
        // Cria a etiqueta com configuração de etiqueta de 80mm
        MSCBPrinter("S600", cPorta, Nil, Nil, .F.)
        MSCBChkStatus(.F.)
        // Alguns modelos exigem esse comando
        MSCBInfoEti("ETIQUETA", "ROTULO")
        MSCBBegin(nQtdCopias, 6, 81)
        // Qtde de copias, velocidade (1 a 6) e tamanho da etiqueta em mm
        MSCBBox(2, 3, 98, 78, 3)
        // Dados da Empresa com linha de separação
        MSCBSay(5, 6, "Remet.: ", "N", "0", "029, 036")
        MSCBSay(26, 6, "Nome da Empresa", "N", "0", "043, 053", .F.)
        MSCBSay(5, 13, "Rua Teste 123, Fone: 014 0000-1111", "N", "0", "024, 034")
        MSCBSay(23, 17, "CEP 17000-111, Bauru-SP", "N", "0", "024, 034")
        MSCBLineH(2, 21, 98, 3)
        // Dados do Cliente com linha de separação
        If SA1:MsSeek(FWxFilial("SA1") + SC5->C5_CLIENTE + SC5->C5_LOJACLI)
            MSCBSay(5, 22, "Codigo: " + SC5->C5_CLIENTE, "N", "0", "029, 036")
            MSCBSay(5, 26, "Cliente: " + SubStr(SA1->A1_NOME, 1, 40), "N", "0", "029, 036")
            MSCBSay(5, 30, "End.: " + Alltrim(SA1->A1_END), "N", "0", "024, 034")
            MSCBSay(5, 34, "Bairro: " + Alltrim(SA1->A1_BAIRRO) + "   CEP: " + Alltrim(SA1->A1_CEP), "N", "0", "029, 036")
            MSCBSay(5, 38, "Cidade: " + Alltrim(SA1->A1_MUN) + "   UF: " + Alltrim(SA1->A1_EST), "N", "0", "026, 036")
            MSCBSay(5, 42, "Telefone: (" + Alltrim(SA1->A1_DDD) + ") " + Alltrim(SA1->A1_TEL), "N", "0", "029, 036")
        EndIf
        MSCBLineH(2, 46, 98, 3)
        // Dados da Transportadora com linha de separação
        If SA4:MsSeek(FWxFilial("SA4") + SC5->C5_TRANSP)
            MSCBSay(5, 48, "Transp.: " + Alltrim(SA4->A4_NOME), "N", "0", "029, 036")
            MSCBSay(5, 52, "Munic.:  " + Alltrim(SA4->A4_MUN), "N", "0", "021, 031")
            MSCBSay(5, 56, "Redesp.: " + SubStr(SA4->A4_NOME, 1, 20) + " (" + SA4->A4_DDD + ") " + SA4->A4_TEL, "N", "0", "021, 031")
            MSCBSay(5, 60, Alltrim(SA4->A4_END), "N", "0", "021, 031")
            MSCBSay(5, 64, "Munic.: " + AllTrim(SubStr(SA4->A4_MUN, 1, 20)) + "/" + SA4->A4_EST, "N", "0", "021, 031")
        EndIf
        MSCBLineH(2, 68, 98, 3)
        // Dados da NF
        MSCBSay(5, 69, "Nota Fiscal: " + SC5->C5_NOTA, "N", "0", "024, 034")
        MSCBSay(5, 69, "Pedido n.: " + Alltrim(SC5->C5_NUM) + " (Consta no DANFe)", "N", "0", "024, 034")
        MSCBSay(37, 73, cValToChar(SC5->C5_VOLUME1) + " " + Upper(Alltrim(SC5->C5_ESPECI1)), "N", "0", "043, 053")
        MSCBSay(5, 73, "Volume: " + cValToChar(nVolIniPvt) + "/" + cValToChar(nVolFimPvt), "N", "0", "024, 034")
        // Finaliza a etiqueta
        MSCBEnd()
        MSCBClosePrinter()
    EndIf
    FWRestArea(aArea)
    RETURN
