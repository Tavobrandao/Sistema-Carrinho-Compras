# Sistema de Carrinho de Compras

Este repositório contém o diagrama de classes UML e o código de implementação de um sistema de carrinho de compras desenvolvido em Python usando o framework Django.

## Diagrama de Classes UML

O diagrama de classes UML do sistema foi projetado para atender aos seguintes requisitos:

1. Um cliente pode adicionar um ou mais itens ao seu carrinho, e cada item está associado a um catálogo de produtos.

2. O sistema permite armazenar os dados básicos do cliente e manter um catálogo de itens disponíveis para compra.

3. O sistema registra os detalhes de cada compra (pedido), incluindo os itens comprados, e permite que o cliente visualize o histórico de pedidos.

4. Cada pedido está associado a uma data e hora da compra.

### Estrutura do Diagrama de Classes:

![Sistema de carrinho de compras](https://github.com/user-attachments/assets/d6710ee6-6d47-47cd-8f4c-be09e66fc40d)

1. **Cliente:** Representa o cliente com atributos como idCliente, nome e email.

2. **Carrinho:** Representa o carrinho de compras associado a um cliente, com atributos como idCarrinho, idCliente (FK) e criadoEm.

3. **Produto:** Representa os produtos disponíveis no catálogo, com atributos como idProduto, nome e preco.

4. **ItemCarrinho:** Representa os itens adicionados ao carrinho, vinculados por idCarrinho (FK), idProduto (FK) e quantidade.

5. **Pedido:** Representa uma compra finalizada, associada a um cliente e com atributos como idPedido, idCliente (FK), dataHora e total.

6. **ItemPedido:** Representa os itens comprados em um pedido, vinculados por idPedido (FK), idProduto (FK) quantidade e precoUnitario.

## Tecnologias Usadas

### Linguagem de Programação:

**Python:** Linguagem utilizada para a implementação do sistema.

### Framework:

**Django:** Framework web utilizado para criar aplicações robustas e escaláveis, facilitando a implementação de padrões MVC (Model-View-Controller).

## Como Usar

### 1. Clonar o Repositório

https://github.com/Tavobrandao/Sistema-Carrinho-Compras.git

### 2. Instalar Dependências
Crie um ambiente virtual e instale as dependências:

```bash
python -m venv venv
```
```bash
source venv/bin/activate # Linux/Mac
```
```bash
venv\Scripts\activate  # Windows 
```
```bash
pip install -r requirements.txt
```

### 3. Configurar o Banco de Dados
Rode as migrações:

```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Rodar o Servidor de Desenvolvimento

```bash
python manage.py runserver
```

Acesse o sistema em http://127.0.0.1:8000/admin/.
