// caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2023/10/29/montando-classes-com-metodos-e-atributos-usando-class-maratona-advpl-e-tl-082/
// Bibliotecas
#Include "TOTVS.ch"
// {Protheus.doc} User Function zExe082
// Exemplo de como criar e utilizar uma classe
// @type Function
// @author Atilio
// @since 09/12/2022
// @see https://tdn.totvs.com/pages/viewpage.action?pageId=6063065
// **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
USER FUNCTION zExe082()
    LOCAL aArea, oPessoa, cNome, dNascimento

    aArea := FWGetArea()
    oPessoa := Nil
    cNome := "José"
    dNascimento := sToD("19850712")
    // Instanciando o objeto através da classe Pessoa
    oPessoa := zPessoaTst():New(cNome, dNascimento)
    // Chamando um método da classe
    oPessoa:MostraIdade()
    FWRestArea(aArea)
    RETURN Class_
    zPessoaTst
    // Atributos
    Data
    cNome
    Data
    nIdade
    Data
    dNascimento
    // Métodos

FUNCTION _New(self)
    CONSTRUCTOR
    RETURN Nil

FUNCTION _MostraIdade(self)
    EndClass
    // {Protheus.doc} New
    // Método que cria a instância com a classe zPessoaTst
    // @author Atilio
    // @since 13/12/2015
    // @version 1.0
    // @param cNome, Caracter, Nome da Pessoa
    // @param dNascimento, Data, Data de Nascimento da Pessoa
    // @example
    // oObjeto := zPessoaTst():New("João", sToD("19800712"))
    RETURN Nil

// Method New for class zPessoaTst
FUNCTION zPessoaTst_New(self, cNome, dNascimento)
    // Atribuindo valores nos atributos do objeto instanciado
    ::cNome := cNome
    ::dNascimento := dNascimento
    ::nIdade := fCalcIdade(dNascimento)
    RETURN self
    // {Protheus.doc} MostraIdade
    // Método que mostra a idade da pessoa
    // @author Atilio
    // @since 13/12/2015
    // @version 1.0
    // @example
    // oObjeto:MostraIdade()

// Method MostraIdade for class zPessoaTst
FUNCTION zPessoaTst_MostraIdade(self)
    LOCAL cMsg

    cMsg := ""
    // Criando e mostrando a mensagem
    cMsg := "A <b>pessoa</b> " + ::cNome() + " tem " + cValToChar(::nIdade()) + " anos!"
    MsgInfo(cMsg, "Atenção")
    RETURN Static

FUNCTION fCalcIdade(dNascimento)
    LOCAL nIdade

    nIdade := Nil
    // Chamando a função YearSub para subtrair os anos de uma data
    nIdade := DateDiffYear(Date(), dNascimento)
    RETURN nIdade
