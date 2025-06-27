
# Tipos e Operadores em Python

## Tipos Básicos de Dados

. OBS: Python é uma linguagem de tipagem dinâmica e forte. Vamos entender isso:
Tipagem dinâmica

    O tipo da variável é determinado em tempo de execução (runtime), não precisa ser declarado explicitamente.

    Você pode reatribuir a variável para outro tipo sem erro.
    
- **int**: números inteiros, como 10, -5, 0  
- **float**: números decimais, como 3.14, -0.001  
- **str**: sequências de caracteres (texto), por exemplo: `"Olá, Mundo!"`  
- **bool**: valores booleanos, `True` ou `False`  
- **NoneType**: valor nulo, representado por `None`

## Operadores Aritméticos

| Operador | Descrição          | Exemplo      | Resultado |
|---------|--------------------|--------------|-----------|
| `+`     | Adição             | `2 + 3`      | `5`       |
| `-`     | Subtração          | `5 - 1`      | `4`       |
| `*`     | Multiplicação      | `4 * 3`      | `12`      |
| `/`     | Divisão            | `10 / 2`     | `5.0`     |
| `//`    | Divisão inteira    | `10 // 3`    | `3`       |
| `%`     | Resto da divisão   | `10 % 3`     | `1`       |
| `**`    | Exponenciação      | `2 ** 3`     | `8`       |

## Operadores Relacionais (Comparação)

| Operador | Descrição         | Exemplo     | Resultado |
|----------|-------------------|-------------|-----------|
| `==`     | Igualdade         | `2 == 2`    | `True`    |
| `!=`     | Diferente         | `2 != 3`    | `True`    |
| `>`      | Maior que         | `5 > 3`     | `True`    |
| `<`      | Menor que         | `3 < 5`     | `True`    |
| `>=`     | Maior ou igual    | `3 >= 3`    | `True`    |
| `<=`     | Menor ou igual    | `2 <= 3`    | `True`    |

## Operadores Lógicos

| Operador | Descrição           | Exemplo           | Resultado |
|----------|---------------------|-------------------|-----------|
| `and`    | E lógico            | `True and False`  | `False`   |
| `or`     | Ou lógico           | `True or False`   | `True`    |
| `not`    | Negação             | `not True`        | `False`   |

## Operadores de Atribuição

| Operador | Descrição           | Exemplo     | Equivale a    |
|----------|---------------------|-------------|---------------|
| `=`      | Atribuição simples  | `x = 5`     | `x = 5`       |
| `+=`     | Soma e atribui      | `x += 3`    | `x = x + 3`   |
| `-=`     | Subtrai e atribui   | `x -= 2`    | `x = x - 2`   |
| `*=`     | Multiplica e atribui| `x *= 4`    | `x = x * 4`   |
| `/=`     | Divide e atribui    | `x /= 2`    | `x = x / 2`   |
| `//=`    | Divisão inteira e atribui | `x //= 3` | `x = x // 3` |
| `%=`     | Módulo e atribui    | `x %= 5`    | `x = x % 5`   |
| `**=`    | Potência e atribui  | `x **= 2`   | `x = x ** 2`  |

## Operadores com Strings

- **Concatenação:**  
  ```python
  "Olá, " + "mundo!"  # Resultado: "Olá, mundo!"
  ```
- **Repetição:**  
  ```python
  "A" * 5  # Resultado: "AAAAA"
