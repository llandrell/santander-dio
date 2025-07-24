# 💰 Mini Sistema Bancário em Python

## 📘 Descrição

Projeto de um mini sistema bancário orientado para estudantes iniciantes em Python. O objetivo é aplicar conceitos fundamentais como funções, estruturas de dados, modularização, e boas práticas no uso de argumentos em funções (`*`, `/`, keyword-only, position-only).

---

## 🧩 Funcionalidades

- Cadastro de usuários (CPF único)
- Criação de contas bancárias associadas a usuários
- Menu interativo com opções por letras (`D`, `S`, `E`, etc.)
- Realização de depósitos
- Realização de saques com limites
- Exibição de extrato formatado
- Listagem de contas do sistema

---

## 🛠️ Requisitos Técnicos

- Código modularizado (uma função para cada operação)
- Uso correto de tipos de argumentos:
  - **Depósito:** argumentos por **posição apenas**
  - **Saque:** argumentos **keyword-only**
  - **Extrato:** argumento `saldo` **posicional**, `extrato` **nomeado**
- Usuários armazenados em **lista de dicionários**
- Contas bancárias armazenadas em **lista**
- Verificação de CPF único
- Formatação de endereço e CPF

---

## 🧠 Regras de Negócio

### 👤 Cadastro de Usuário
- Atributos: nome, data de nascimento, CPF (somente números), endereço completo
- Endereço no formato: `logradouro, número - bairro - cidade/UF`
- Não é permitido cadastrar dois usuários com o mesmo CPF

### 🏦 Conta Corrente
- Agência fixa: `0001`
- Número da conta: sequencial, iniciando em 1
- Um usuário pode ter várias contas
- Cada conta pertence a **apenas um usuário**

### 💸 Saques
- Máximo de **3 saques por dia**
- Limite de **R$ 500,00 por saque**
- Função com argumentos keyword-only: `*, saldo, valor, extrato, limite, numero_saques`
- Retorna novo saldo e extrato

### 💰 Depósitos
- Função com argumentos por posição: `saldo, valor, extrato, /`
- Valor deve ser positivo
- Retorna novo saldo e extrato

### 📄 Extrato
- Função com: `saldo` (posicional), `extrato` (nomeado)
- Exibe transações e saldo atual

---

## 🗂️ Estrutura de Funções Sugerida

```python
def menu(): ...
def cadastrar_usuario(usuarios): ...
def filtrar_usuario(cpf, usuarios): ...
def criar_conta_corrente(agencia, numero_conta, usuarios): ...
def listar_contas(contas): ...

def deposito(saldo, valor, extrato, /): ...
def saque(*, saldo, valor, extrato, limite, numero_saques): ...
def exibir_extrato(saldo, *, extrato): ...
``` 