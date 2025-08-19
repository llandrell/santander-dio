# 🗄️ Tipos de Banco de Dados

Neste documento, vamos aprofundar o estudo sobre os **tipos de bancos de dados** e suas principais características.  

---
# Banco de Dados Relacional (RDBMS)

Os **bancos de dados relacionais** são os mais tradicionais e utilizados em sistemas de informação.  
Eles armazenam **dados estruturados** em **tabelas** (linhas e colunas), onde cada linha representa um registro e cada coluna representa um campo do registro.  

A grande vantagem dos bancos de dados relacionais é a capacidade de **relacionar informações entre tabelas diferentes** através de **chaves primárias** e **chaves estrangeiras**.

---

### Exemplos de Bancos de Dados Relacionais:
- **SQL Server (Microsoft)**
- **Oracle Database**
- **MySQL**
- **PostgreSQL**
- **MariaDB**
- **SQLite**

---

### Exemplos de Relacionamentos entre Tabelas

1. **Relacionamento 1:1 (Um para Um)**  
   Cada registro em uma tabela está relacionado a **apenas um** registro em outra tabela.  
   - Exemplo:  
     - Tabela **Usuário**  
     - Tabela **Perfil**  
     - Um usuário tem apenas um perfil associado.

2. **Relacionamento 1:N (Um para Muitos)**  
   Um registro em uma tabela pode estar relacionado a **vários registros** em outra tabela.  
   - Exemplo:  
     - Tabela **Cliente**  
     - Tabela **Pedidos**  
     - Um cliente pode fazer vários pedidos.

3. **Relacionamento N:M (Muitos para Muitos)**  
   Vários registros em uma tabela podem estar relacionados a vários registros em outra tabela.  
   Normalmente é criada uma tabela intermediária (tabela de junção).  
   - Exemplo:  
     - Tabela **Aluno**  
     - Tabela **Curso**  
     - Um aluno pode estar matriculado em vários cursos, e um curso pode ter vários alunos.  
     - Tabela de junção: **Aluno_Curso**

---

📌 **Resumo:**  
Os bancos de dados relacionais são a base de muitos sistemas modernos, oferecendo organização, integridade dos dados e a possibilidade de consultas complexas com **SQL (Structured Query Language)**.
"""a
---

### 🔹 Exemplo de tabelas relacionais:

**Tabela Clientes**
| id_cliente | nome       | email              |
|------------|-----------|--------------------|
| 1          | João      | joao@email.com     |
| 2          | Maria     | maria@email.com    |

**Tabela Pedidos**
| id_pedido | id_cliente | produto   | valor  |
|-----------|-----------|----------|--------|
| 101       | 1         | Teclado  | 120.00 |
| 102       | 2         | Mouse    | 80.00  |
| 103       | 1         | Monitor  | 900.00 |

➡ Aqui temos um **relacionamento 1:N (um para muitos)** entre a tabela `Clientes` e `Pedidos`.  
Um cliente pode ter **vários pedidos**, mas cada pedido pertence a apenas **um cliente**.
--- 
