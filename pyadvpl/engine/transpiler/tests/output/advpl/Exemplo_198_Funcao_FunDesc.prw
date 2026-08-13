// caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2024/01/27/buscando-a-descricao-da-funcao-aberta-atraves-da-fundesc-maratona-advpl-e-tl-198/
// Bibliotecas
#Include "TOTVS.ch"
// {Protheus.doc} User Function zExe198
// Função que retorna a descrição da rotina aberta no menu
// @type Function
// @author Atilio
// @since 11/02/2023
// @see https://tdn.totvs.com/pages/releaseview.action?pageId=6814874
// Função FunDesc
// Parâmetros
// Função não tem parâmetros
// Retorno
// + cDesc       , Caractere        , Texto com o nome da descrição da rotina no menu
// **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
USER FUNCTION zExe198()
    LOCAL aArea, cDescri

    aArea := FWGetArea()
    cDescri := ""
    // Busca a descrição e mostra
    cDescri := FunDesc()
    FWAlertInfo(cDescri, "Teste FunDesc")
    FWRestArea(aArea)
    RETURN
