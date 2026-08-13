// caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2024/05/31/copiando-arquivos-atraves-da-smcopy-maratona-advpl-e-tl-448/
// Bibliotecas
#Include "TOTVS.ch"
// {Protheus.doc} User Function zExe448
// Exemplo de como utilizar a função SmCopy
// @type Function
// @author Atilio
// @since 31/03/2023
// @obs Função SmCopy
// Parâmetros
// + Arquivo de Origem com o caminho da pasta (podendo ser também da Protheus Data)
// + Arquivo de Destino com o caminho da pasta (podendo ser também da Protheus Data)
// Retorno
// + Retorna .T. se a cópia foi bem sucedida ou Retorna .F. se a cópia fracassou
// **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
USER FUNCTION zExe448()
    LOCAL aArea, cArqOrigem, cArqDestino

    aArea := FWGetArea()
    cArqOrigem := "C:\Spool\arquivo.txt"
    cArqDestino := "C:\Spool\arquivo_copia.txt"
    // Se a cópia for bem sucedida
    If SmCopy(cArqOrigem, cArqDestino)
        FWAlertSucess("Cópia do arquivo realizada com sucesso!", "Sucesso")
    Else
        FWAlertError("Falha ao copiar o arquivo, verifique o privilégio ou se existe a pasta destino!", "Falha")
    EndIf
    FWRestArea(aArea)
    RETURN
