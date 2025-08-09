from abc import ABC, abstractmethod
from datetime import datetime




def criar_cliente_pf():
    endereco = input("Endereço: ")
    cpf = input("CPF: ")
    nome = input("Nome: ")
    data_str = input("Data de nascimento (dd/mm/aaaa): ")
    data_nascimento = datetime.strptime(data_str, "%d/%m/%Y").date()
    
    cliente = Pessoa_Fisica(endereco, cpf, nome, data_nascimento)
    return cliente

def criar_conta_corrente(cliente):
    numero_conta = int(input("Número da conta: "))
    agencia = input("Agência: ")
    conta = Conta_Corrente(cliente, numero_conta, agencia)
    cliente.adicionar_conta(conta)
    return conta

class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def adicionar_conta(self, conta):
        self.contas.append(conta)

    def realizar_transacao(self, conta, transacao):
        if isinstance(transacao, Saque):
            return conta.sacar(transacao.valor)
        elif isinstance(transacao, Deposito):
            return conta.depositar(transacao.valor)
        else:
            return False
        

        
class Pessoa_Fisica(Cliente):
    
    def __init__(self, endereco, cpf, nome, data_nascimento):
        super().__init__(endereco)
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento

class Conta:
    def __init__(self, cliente, numero_conta, agencia, saldo_inicial=0.0):
        self.cliente = cliente
        self.saldo = saldo_inicial
        self.numero_conta = numero_conta
        self.agencia = agencia
        self.historico = Historico()


 

    def sacar(self, valor):
        if valor > 0 and self.saldo >= valor:
            self.saldo -= valor
  
            self.historico.adicionar_transacao(Saque(valor))
            return True
        

        else:
            return False     
        
    
    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.historico.adicionar_transacao(Deposito(valor))
            return True
        

        else:
            return False     
        
    def mostrar_saldo(self):
        return self.saldo

    def extrato(self):
        for transacao in self.historico.listar_transacoes():
            print(transacao)

class Conta_Corrente(Conta):
    def __init__(self, cliente, numero_conta, agencia, saldo_inicial=0):
        super().__init__(cliente, numero_conta, agencia, saldo_inicial)

        self.limite = 1000
        self.numero_saques = 0
        self.limite_saques = 3

    def sacar(self, valor):
        if (valor > 0 and self.saldo + self.limite >= valor and self.numero_saques < self.limite_saques):
            self.saldo -= valor
            self.numero_saques += 1
            self.historico.adicionar_transacao(Saque(valor))
            return True
        

        else:
            return False    
     



class Historico:
    def __init__(self):
        self.transacoes = []

    def adicionar_transacao(self, transacao):
        self.transacoes.append(transacao)

    def listar_transacoes(self):
        return self.transacoes

class Transacao(ABC):
    def __init__(self, valor):
        self.valor = valor


    @abstractmethod
    def registrar(self, conta):
        pass

    def __str__(self):
        return f"{self.tipo}: R$ {self.valor:.2f}"

class Saque(Transacao):
    def __init__(self, valor):
        super().__init__(valor)
        self.tipo = "Saque"

    def registrar(self, conta):
        # Já descontado no método sacar, só registra
        conta.historico.adicionar_transacao(self)

class Deposito(Transacao):
    def __init__(self, valor):
        super().__init__(valor)
        self.tipo = "Depósito"

    def registrar(self, conta):
        conta.historico.adicionar_transacao(self)



def menu():
    print("\nEscolha uma opção:")
    print("1 - Depositar")
    print("2 - Sacar")
    print("3 - Mostrar saldo")
    print("4 - Mostrar extrato")
    print("5 - Sair")

clientes = []

cliente = criar_cliente_pf()
conta = criar_conta_corrente(cliente)
clientes.append(cliente)

while True:
    menu()
    try:
        opcao = int(input("Opção: "))
    except ValueError:
        print("Opção inválida. Digite um número entre 1 e 5.")
        continue

    if opcao == 1:
        try:
            valor = float(input("Valor a depositar: "))
        except ValueError:
            print("Valor inválido. Digite um número válido.")
            continue

        sucesso = cliente.realizar_transacao(conta, Deposito(valor))
        print("Depósito realizado!" if sucesso else "Falha no depósito.")

    elif opcao == 2:
        try:
            valor = float(input("Valor a sacar: "))
        except ValueError:
            print("Valor inválido. Digite um número válido.")
            continue

        sucesso = cliente.realizar_transacao(conta, Saque(valor))
        print("Saque realizado!" if sucesso else "Falha no saque.")

    elif opcao == 3:
        print(f"Saldo atual: R$ {conta.mostrar_saldo():.2f}")

    elif opcao == 4:
        print("Extrato:")
        conta.extrato()

    elif opcao == 5:
        print("Saindo...")
        break

    else:
        print("Opção inválida. Digite um número entre 1 e 5.")