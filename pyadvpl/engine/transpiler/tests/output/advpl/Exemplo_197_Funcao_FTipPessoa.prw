// caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2024/01/26/formatando-datas-com-fsdateconv-maratona-advpl-e-tl-196/
// Bibliotecas
#Include "TOTVS.ch"
// {Protheus.doc} User Function zExe197
// Função que retorna o tipo de pessoa se é fisica ou juridica do Cliente ou Fornecedor
// @type Function
// @author Atilio
// @since 11/02/2023
// Função FTipPessoa
// Parâmetros
// + Tipo que deseja validar 2=Clientes ; 1=Fornecedores
// + Código e Loja de pesquisa na tabela de cliente ou fornecedor dependendo do cTipo
// Retorno
// + Retorna o tipo de pessoa se é física ou jurídica
// **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
USER FUNCTION zExe197()
    LOCAL aArea, cTipo, cChave, cRetorno

    aArea := FWGetArea()
    cTipo := "2"
    cChave := "C0000101"
    // A1_COD + A1_LOJA
    cRetorno := ""
    // Montando uma mensagem que será exibida
    cRetorno := FTipPessoa(cTipo, cChave)
    FWAlertInfo("O tipo de pessoa é: " + cRetorno, "Teste FTipPessoa")
    FWRestArea(aArea)
    RETURN
