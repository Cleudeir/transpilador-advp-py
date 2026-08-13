// caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2024/03/09/buscando-o-tipo-de-estacao-que-esta-rodando-o-sistema-com-getremotetype-maratona-advpl-e-tl-282/
// Bibliotecas
#Include "TOTVS.ch"
// {Protheus.doc} User Function zExe283
// Busca arquivos contidos dentro do RPO
// @type  Function
// @author Atilio
// @since 21/02/2023
// @see https://tdn.totvs.com/display/tec/GetResArray
// Função GetResArray
// Parâmetros
// + cMask       , Caractere   , Indica a máscara de pesquisa
// + nRPO        , Caractere   , Indica se quer pesquisar em [1] RPO Padrão; [2] RPO TLPP; [3] RPO Custom; Ou se não for informado nada será nos 3
// Retorno
// + aRet        , Array       , Retorna os arquivos encontrados no repositório
// **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
USER FUNCTION zExe283()
    LOCAL aArea, aArquivos, cArqui, cMensagem

    aArea := FWGetArea()
    aArquivos := {  }
    cArqui := ""
    cMensagem := ""
    // Busca todos os arquivos que sejam do tipo PNG
    aArquivos := GetResArray("*.png")
    // Percorre os fontes incrementando a mensagem
    aEval(aArquivos, Nil)
    // Exibe uma mensagem com os programas
    ShowLog(cMensagem)
    FWRestArea(aArea)
    RETURN
