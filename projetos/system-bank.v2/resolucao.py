from abc import ABC, abstractclassmethod, abstractproperty
from datetime import datetime



class Cliente:  # Define a classe Cliente, que representa um cliente do banco

    def __init__(self, endereco):  # Método construtor que é chamado quando criamos um objeto Cliente
        self.endereco = endereco  # Armazena o endereço do cliente no atributo 'endereco'
        self.contas = []          # Inicializa uma lista vazia para armazenar as contas vinculadas a esse cliente

    def realizar_transacao(self, conta, transacao):  # Método para realizar uma transação em uma conta específica
        transacao.resgistrar(conta)  # chamo o método 'registrar' da transação, para executar a transação na conta
                                   

    def adicionar_conta(self, conta):  # Método para adicionar uma conta à lista de contas do cliente
        self.contas.append(conta)     # Adiciona o objeto 'conta' à lista 'contas' do cliente
                        
class PessoaFisica(Cliente):  
    # Define a classe PessoaFisica que herda da classe Cliente.
    # Ou seja, PessoaFisica é um tipo especializado de Cliente, com mais atributos específicos.

    def __init__(self, nome, data_nasc, cpf, endereco):
        # Construtor da classe PessoaFisica, que será chamado para criar objetos dessa classe.
        # Recebe nome, data de nascimento, CPF e endereço como parâmetros.

        super().__init__(endereco)  
        # Chama o construtor da superclasse Cliente para inicializar o atributo 'endereco'.
        # Isso evita repetir código e garante que o atributo 'endereco' seja configurado corretamente.

        self.nome = nome  
        # Armazena o nome da pessoa física no atributo 'nome'.

        self.data_nasc = data_nasc  
        # Armazena a data de nascimento no atributo 'data_nasc'.

        self.cpf = cpf  
        # Armazena o CPF (Cadastro de Pessoa Física) no atributo 'cpf'.

class Conta:
    def __init__(self, num_conta, cliente):
        # Construtor da classe Conta, que recebe o número da conta e o cliente associado.

        self._saldo = 0  
        # Atributo privado para armazenar o saldo da conta, inicializado com zero.

        self._num_conta = num_conta  
        # Atributo privado para armazenar o número da conta.

        self._agencia = "0001"  
        # Atributo privado para armazenar a agência da conta, neste caso fixo em "0001".

        self._cliente = cliente  
        # Atributo privado que guarda a referência ao cliente dono da conta.

        self.historico = Historico()  
        # Atributo privado que guarda o histórico de transações da conta.
        .

    @classmethod
    def nova_conta(cls, cliente, num_conta):
        # Método de classe para criar uma nova instância da conta,
        # recebendo o cliente e número da conta, e retornando o objeto Conta.

        return cls(num_conta, cliente)  
        # Retorna uma nova instância da classe Conta, chamando o construtor.

    @property
    def saldo(self):
        # Getter para o saldo da conta, permite acessar 'saldo' como um atributo.

        return self._saldo  
        # Retorna o valor atual do saldo privado.

    @property
    def num_conta(self):
        # Getter para o número da conta, acesso seguro e controlado.

        return self._num_conta  
        # Retorna o número da conta.

    @property
    def agencia(self):
        # Getter para a agência da conta.

        return self._agencia  
        # Retorna a agência (fixa como "0001" neste código).
    
    @property
