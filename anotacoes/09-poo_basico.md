# 🐍 Programação Orientada a Objetos (POO) com Python

## 📖 Introdução

A **Programação Orientada a Objetos (POO)** é um paradigma de programação que organiza o código em torno de **objetos**. Esses objetos representam entidades do mundo real e possuem **características (atributos)** e **comportamentos (métodos)**.

Essa abordagem facilita a **modularização**, **reutilização** e **extensibilidade** do código, tornando-o mais organizado e fácil de manter.

Os conceitos fundamentais da POO são:

- **Classe:** Define as características e comportamentos dos objetos.
- **Objeto:** É uma instância da classe; podemos usar diretamente os objetos, enquanto a classe é apenas o "molde".

---

## 🔑 Paradigmas de Programação

Um **paradigma de programação** é um estilo de organizar e escrever código.  
No Python, temos suporte a diferentes paradigmas:

- **Estruturado:** O código é organizado em funções e estruturas de controle (if, for, while, etc.).  
- **Orientado a Objetos:** O código é organizado em torno de classes e objetos.  

---

## 🏗️ Conceitos de Classes e Objetos

### 1️⃣ O que são Classes e Objetos?

- **Classe:** É como um molde que define as características (atributos) e ações (métodos) de um grupo de objetos.
- **Objeto:** É a **instância** de uma classe, ou seja, algo criado a partir da classe. Cada objeto pode ter valores diferentes para os mesmos atributos.

### 2️⃣ Estrutura de uma Classe

```python
class Pessoa:  # Definição da classe
    def __init__(self, nome, idade):  # Método construtor (inicializa atributos)
        self.nome = nome  # atributo nome
        self.idade = idade  # atributo idade

    def apresentar(self):  # Método (comportamento)
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")
```

### 3️⃣ Instanciando um Objeto

```python
# Criando um objeto (instância da classe Pessoa)
p1 = Pessoa("Maria", 30)
p1.apresentar()  # Chama o método do objeto
```

---

## 🌍 Exemplos do Mundo Real

### Classe e Objetos - Exemplo com Carros

```python
class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.ligado = False

    def ligar(self):
        self.ligado = True
        print(f"O carro {self.modelo} está ligado.")

    def desligar(self):
        self.ligado = False
        print(f"O carro {self.modelo} está desligado.")
```

### Instanciando Objetos

```python
carro1 = Carro("Fiat", "Uno", 2010)
carro2 = Carro("Volkswagen", "Gol", 2020)

carro1.ligar()
carro2.desligar()
```

---

## 🧐 O que significa **instanciar um objeto**?

Instanciar um objeto significa **criar** um objeto a partir de uma classe.  
A classe é como uma planta de uma casa; a instância é a casa construída a partir dessa planta.

Cada objeto instanciado pode ter valores diferentes para os atributos definidos na classe.

---

## 🎯 Resolvendo Problemas com Orientação a Objetos

Exemplo: Criar um sistema para gerenciar alunos.

```python
class Aluno:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

    def exibir_dados(self):
        print(f"Aluno: {self.nome}, Matrícula: {self.matricula}")


aluno1 = Aluno("João", 123)
aluno2 = Aluno("Maria", 456)

aluno1.exibir_dados()
aluno2.exibir_dados()
```

---

📁 **Local:** `/anotacoes/9-poo_basico.md`  
✍️ Autor: [Andre Almeida](https://github.com/llandrell)
