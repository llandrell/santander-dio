from abc import ABC, abstractmethod
from datetime import datetime

# -------------------------
# Classes de domínio
# -------------------------

class Cliente:
    # Classe que representa um cliente (pessoa) que pode ter várias contas.
    def __init__(self, endereco):
        # Construtor: cria um Cliente com um endereço e lista de contas vazia.
        self.endereco = endereco                    # armazena o endereço do cliente
        self.contas = []                            # lista de contas vinculadas ao cliente

    def realizar_transacao(self, conta, transacao):
        # Método de conveniência: delega para a transação executar-se sobre a conta.
        # 'transacao' é um objeto que implementa o método registrar(conta).
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        # Adiciona uma conta à lista de contas do cliente.
        # Útil para manter o relacionamento cliente -> contas.
        self.contas.append(conta)


class PessoaFisica(Cliente):
    # PessoaFisica é um tipo de Cliente com atributos pessoais.
    def __init__(self, nome, data_nasc, cpf, endereco):
        # Construtor: chama o construtor da superclasse para configurar 'endereco'.
        super().__init__(endereco)                  # inicializa o endereço e a lista de contas
        self.nome = nome                            # nome do cliente pessoa física
        self.data_nasc = data_nasc                  # data de nascimento (string ou date)
        self.cpf = cpf                              # CPF (identificador)


class Conta:
    # Classe base para tipos de conta (ex.: ContaCorrente). Guarda saldo, número, agência e histórico.
    def __init__(self, num_conta, cliente):
        # Construtor da conta: inicializa estado interno.
        self._saldo = 0                             # saldo interno — trate como privado
        self._num_conta = num_conta                 # número da conta
        self._agencia = "0001"                      # agência fixa como exemplo
        self._cliente = cliente                     # referência ao objeto Cliente dono da conta
        self._historico = Historico()               # objeto Historico para armazenar operações

    @classmethod
    def nova_conta(cls, cliente, num_conta):
        # Factory method: facilita criar uma conta, mantendo controle de parâmetros.
        # Note que a ordem passada ao construtor é (num_conta, cliente).
        return cls(num_conta, cliente)

    @property
    def saldo(self):
        # Getter para saldo — lê o atributo privado.
        return self._saldo

    @property
    def num_conta(self):
        # Getter para número da conta.
        return self._num_conta

    @property
    def agencia(self):
        # Getter para agência.
        return self._agencia

    @property
    def cliente(self):
        # Retorna o cliente dono da conta.
        return self._cliente

    @property
    def historico(self):
        # Retorna o histórico associado à conta.
        return self._historico

    def sacar(self, valor):
        # Realiza um saque simples.
        # Validamos entrada primeiro: valores <= 0 não são aceitos.
        if valor <= 0:
            print("\n@@@ Operação falhou! Valor para saque deve ser maior que zero. @@@")
            return False

        # Agora verificamos saldo suficiente.
        saldo = self._saldo
        excedeu_saldo = valor > saldo
        if excedeu_saldo:
            print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")
            return False

        # Se passou nas validações, efetua o saque.
        self._saldo -= valor
        print("\n=== Saque realizado com sucesso! ===")
        return True

    def depositar(self, valor):
        # Realiza um depósito simples.
        # Só aceita depósitos maiores que zero; retorna True se feito, False caso contrário.
        if valor > 0:
            self._saldo += valor
            print("+++ Depósito realizado com sucesso +++")
            return True
        else:
            print("Operação falhou, valor informado inválido")
            return False


class ContaCorrente(Conta):
    # Conta corrente com limite por saque e limite de número de saques.
    def __init__(self, num_conta, cliente, limite=500, limite_saque=3):
        super().__init__(num_conta, cliente)        # inicializa atributos da classe base
        self.limite = limite                        # limite máximo por saque
        self.limite_saque = limite_saque            # número máximo de saques permitidos

    def sacar(self, valor):
        # Conta o número de saques já registrados no histórico.
        # Usamos a propriedade historico.transacoes (lista de dicionários).
        numeros_saques = sum(
            1 for transacao in self.historico.transacoes
            if transacao["tipo"] == Saque.__name__
        )

        # Validações: limite por valor e limite por quantidade.
        excedeu_limite = valor > self.limite
        excedeu_saque = numeros_saques >= self.limite_saque  # >= para bloquear quando já atingiu limite

        if excedeu_limite:
            print("Operação falhou!! O valor do saque excedeu o limite")
            return False

        if excedeu_saque:
            print("Operação falhou! Número de saques excedido")
            return False

        # Se passou nas validações específicas da ContaCorrente, delega para Conta.sacar.
        return super().sacar(valor)

    def __str__(self):
        # Representação textual da conta — útil para debug/impressão.
        return (
            f"Agência : \t{self.agencia}\n"
            f"C/C:\t\t{self.num_conta}\n"
            f"Titular:\t{self.cliente.nome}"
        )


class Historico:
    # Guarda a lista de transações efetuadas para uma conta.
    def __init__(self):
        self._transacoes = []                      # lista interna de dicionários de transação

    @property
    def transacoes(self):
        # Retorna a lista (somente leitura idealmente).
        return self._transacoes

    def add_transacao(self, transacao):
        # Adiciona uma transação ao histórico gravando tipo, valor e timestamp.
        self._transacoes.append({
            "tipo": transacao.__class__.__name__,   # ex.: "Saque" ou "Deposito"
            "valor": transacao.valor,               # valor (positivo) — tipo indica retirada ou depósito
            "data": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
        })


class Transacao(ABC):
    # Classe abstrata que define o contrato para transações.
    @property
    @abstractmethod
    def valor(self):
        # A propriedade 'valor' deve ser implementada nas subclasses.
        pass

    @abstractmethod
    def registrar(self, conta):
        # O método registrar executa a transação na conta passada.
        pass


class Saque(Transacao):
    # Implementação concreta de Saque.
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        # Tenta sacar na conta; só registra no histórico se o saque for bem-sucedido.
        sucesso_transacao = conta.sacar(self.valor)
        if sucesso_transacao:
            conta.historico.add_transacao(self)


class Deposito(Transacao):
    # Implementação concreta de Depósito.
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        # Tenta depositar; registra apenas se a operação retornar True.
        sucesso_transacao = conta.depositar(self.valor)
        if sucesso_transacao:
            conta.historico.add_transacao(self)




def main():
    clientes = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            depositar(clientes)        
        elif opcao == "s":
            sacar(clientes)
        elif opcao == "e":
            exibir_extrato(clientes)
        elif opcao == "nu":
            criar_cliente(clientes)
        elif opcao == "nc":
            num_conta = len(contas) + 1
            criar_conta(num_conta, clientes, contas)
        elif opcao == "lc":
            lista_contas(contas)
        elif opcao == "q":
            break