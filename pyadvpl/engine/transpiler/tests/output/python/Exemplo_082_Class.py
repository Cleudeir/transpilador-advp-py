# Esse exemplo faz parte da série do YouTube, Maratona de Exemplos, do canal Terminal de Informação, 
#     caso queira ver esse exemplo rodando em vídeo, acesse o seguinte link:     https://terminaldeinformacao.com/2023/10/29/montando-classes-com-metodos-e-atributos-usando-class-maratona-advpl-e-tl-082/
# Bibliotecas
# PREPROCESSOR: #Include "TOTVS.ch"
# {Protheus.doc} User Function zExe082
# Exemplo de como criar e utilizar uma classe
# @type Function
# @author Atilio
# @since 09/12/2022
# @see https://tdn.totvs.com/pages/viewpage.action?pageId=6063065
# @obs 
# 
#     **** Apoie nosso projeto, se inscreva em https://www.youtube.com/TerminalDeInformacao ****
def u_zExe082():
    aArea = FWGetArea()
    oPessoa = None
    cNome = 'José'
    dNascimento = sToD('19850712')
    # Instanciando o objeto através da classe Pessoa
    oPessoa = zPessoaTst().New(cNome, dNascimento)
    # Chamando um método da classe
    oPessoa.MostraIdade()
    FWRestArea(aArea)
    return Class_
    zPessoaTst
    # Atributos
    Data
    cNome
    Data
    nIdade
    Data
    dNascimento
    # Métodos

# Method New for class 
def _New(self, ):
    CONSTRUCTOR

# Method MostraIdade for class 
def _MostraIdade(self, ):
    EndClass
    # {Protheus.doc} New
    # Método que cria a instância com a classe zPessoaTst
    # @author Atilio
    # @since 13/12/2015
    # @version 1.0
    #     @param cNome, Caracter, Nome da Pessoa
    #     @param dNascimento, Data, Data de Nascimento da Pessoa
    #     @example
    #     oObjeto := zPessoaTst():New("João", sToD("19800712"))

# Method New for class zPessoaTst
def zPessoaTst_New(self, cNome, dNascimento):
    # Atribuindo valores nos atributos do objeto instanciado
    self.cNome = cNome
    self.dNascimento = dNascimento
    self.nIdade = fCalcIdade(dNascimento)
    return self
    # {Protheus.doc} MostraIdade
    # Método que mostra a idade da pessoa
    # @author Atilio
    # @since 13/12/2015
    # @version 1.0
    #     @example
    #     oObjeto:MostraIdade()

# Method MostraIdade for class zPessoaTst
def zPessoaTst_MostraIdade(self, ):
    cMsg = ''
    # Criando e mostrando a mensagem
    cMsg = 'A <b>pessoa</b> ' + self.cNome() + ' tem ' + cValToChar(self.nIdade()) + ' anos!'
    MsgInfo(cMsg, 'Atenção')
    return Static

def fCalcIdade(dNascimento):
    nIdade = None
    # Chamando a função YearSub para subtrair os anos de uma data
    nIdade = DateDiffYear(Date(), dNascimento)
    return nIdade
