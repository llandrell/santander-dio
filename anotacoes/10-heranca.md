# 🧬 Herança em Python

## 📖 O que é Herança?

A **herança** é um dos conceitos fundamentais da Programação Orientada a Objetos (POO).  
Ela permite que uma classe (chamada de **classe filha** ou **subclasse**) herde atributos e métodos de outra classe (chamada de **classe pai**, **classe base** ou **superclasse**).

---

## 🎯 Conceito de Herança

- Facilita o **reaproveitamento de código**.
- Permite criar uma hierarquia de classes mais organizada e modular.
- A classe filha herda comportamentos e características da classe pai e pode **adicionar ou sobrescrever** funcionalidades.

---

## 🏗️ Classe Pai (ou Base)

A **classe pai** é a classe genérica que contém os atributos e métodos comuns às classes filhas.  
Ela serve como modelo base para as subclasses.

```python
class Animal:
    def __init__(self, nome):
        self.nome = nome

    def emitir_som(self):
        print("O animal emite um som genérico.")
```

---

## ✅ Benefícios da Herança

1. **Reutilização de código**: evita duplicações.
2. **Organização**: facilita a manutenção e extensão.
3. **Especialização**: subclasses podem especializar comportamentos herdados.

---

## ⚠️ Pontos Negativos

- Pode gerar **alto acoplamento** entre classes (quando mal utilizada).
- Herança excessiva pode dificultar a leitura e a manutenção do código.
- Alterações na superclasse podem impactar todas as subclasses.

---

## 📝 Sintaxe da Herança

A herança é definida passando a classe pai entre parênteses ao declarar a classe filha:

```python
class ClasseFilha(ClassePai):
    pass
```

---

## 🔹 Herança Simples

Na **herança simples**, uma classe herda diretamente de uma única classe pai.

### Exemplo prático:

```python
class Animal:
    def __init__(self, nome):
        self.nome = nome

    def emitir_som(self):
        print("Som genérico")

class Cachorro(Animal):  # Cachorro herda de Animal
    def emitir_som(self):
        print(f"{self.nome} diz: Au Au!")

# Uso
dog = Cachorro("Rex")
dog.emitir_som()  # Rex diz: Au Au!
```

---

## 🔹 Herança Múltipla

Na **herança múltipla**, uma classe pode herdar de **mais de uma classe pai**.

### Exemplo prático:

```python
class Mamifero:
    def amamentar(self):
        print("Amamentando filhotes")

class Aquatico:
    def nadar(self):
        print("Nadando")

class Baleia(Mamifero, Aquatico):  # Herança múltipla
    pass

# Uso
b = Baleia()
b.amamentar()  # Amamentando filhotes
b.nadar()      # Nadando
```

⚠️ **Atenção:** Em casos de métodos com o mesmo nome em classes diferentes, o Python segue a ordem de herança definida na declaração (MRO – Method Resolution Order).

---

## 🔍 Herança Específica (Sobrescrita e `super()`)

- Subclasses podem **sobrescrever métodos** da classe pai.
- O método `super()` é usado para chamar a implementação da superclasse.

### Exemplo prático:

```python
class Pessoa:
    def __init__(self, nome):
        self.nome = nome

    def apresentar(self):
        print(f"Olá, eu sou {self.nome}")

class Estudante(Pessoa):
    def __init__(self, nome, curso):
        super().__init__(nome)  # Chama o construtor da classe pai
        self.curso = curso

    def apresentar(self):
        super().apresentar()  # Chama o método da classe pai
        print(f"Sou estudante de {self.curso}")

# Uso
e = Estudante("Ana", "Python")
e.apresentar()
```

**Saída:**
```
Olá, eu sou Ana
Sou estudante de Python
```

---

## 🧠 Conclusão

A herança é uma ferramenta poderosa da POO, mas deve ser usada com cuidado.  
Em alguns casos, **composição** (uma classe usando outra como atributo) pode ser mais adequada.

---

✍️ Autor: [Andre Almeida](https://github.com/llandrell)
📁 Local: `/anotacoes/heranca_python.md`