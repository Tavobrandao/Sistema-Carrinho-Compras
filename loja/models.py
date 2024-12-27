from django.db import models

# Classe representando um cliente no sistema
class Cliente(models.Model):
    nome = models.CharField(max_length=255)  # Campo para armazenar o nome do cliente (máximo 255 caracteres)
    email = models.EmailField(unique=True)  # Campo para e-mail, com validação e unicidade

    def __str__(self):
        return self.nome  # Representação em string do cliente, retornando o nome

# Classe representando um produto no sistema
class Produto(models.Model):
    nome = models.CharField(max_length=255)  # Nome do produto, limitado a 255 caracteres
    preco = models.DecimalField(max_digits=10, decimal_places=2)  # Preço com até 10 dígitos e 2 casas decimais

    def __str__(self):
        return self.nome  # Representação em string do produto, retornando o nome

# Classe representando o carrinho de compras de um cliente
class Carrinho(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)  # Relacionamento com um cliente; exclui o carrinho se o cliente for excluído
    criado_em = models.DateTimeField(auto_now_add=True)  # Data e hora da criação do carrinho

    def __str__(self):
        return f"Carrinho de {self.cliente.nome}"  # Representação em string do carrinho

# Classe representando os itens contidos no carrinho de compras
class ItemCarrinho(models.Model):
    carrinho = models.ForeignKey(Carrinho, on_delete=models.CASCADE)  # Relacionamento com o carrinho
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)  # Relacionamento com o produto
    quantidade = models.PositiveIntegerField()  # Quantidade do produto no carrinho (valor positivo)

    def __str__(self):
        return f"{self.quantidade} x {self.produto.nome} (Carrinho)"  # Representação em string do item

# Classe representando um pedido realizado pelo cliente
class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)  # Relacionamento com um cliente
    data_hora = models.DateTimeField(auto_now_add=True)  # Data e hora do pedido
    total = models.DecimalField(max_digits=10, decimal_places=2)  # Total do pedido, com até 10 dígitos e 2 casas decimais

    def __str__(self):
        return f"Pedido #{self.id} de {self.cliente.nome}"  # Representação em string do pedido

# Classe representando os itens de um pedido
class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)  # Relacionamento com o pedido
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)  # Relacionamento com o produto
    quantidade = models.PositiveIntegerField()  # Quantidade do produto no pedido
    preco_unitario = models.DecimalField(max_digits=10, decimal_places=2)  # Preço unitário do produto

    def __str__(self):
        return f"{self.quantidade} x {self.produto.nome} (Pedido)"  # Representação em string do item do pedido

# Função para finalizar a compra e criar um pedido com base no carrinho do cliente
def finalizar_compra(cliente_id):
    # Obtém o carrinho do cliente
    carrinho = Carrinho.objects.get(cliente_id=cliente_id)
    # Cria um pedido associado ao cliente, com o total inicial zerado
    pedido = Pedido.objects.create(cliente=carrinho.cliente, total=0)

    total = 0  # Variável para calcular o total do pedido
    # Itera pelos itens do carrinho
    for item in carrinho.itemcarrinho_set.all():
        # Calcula o total do item (preço * quantidade) e soma ao total do pedido
        total += item.produto.preco * item.quantidade
        # Cria um item de pedido correspondente
        ItemPedido.objects.create(
            pedido=pedido,
            produto=item.produto,
            quantidade=item.quantidade,
            preco_unitario=item.produto.preco
        )
    
    # Atualiza o total do pedido e salva no banco de dados
    pedido.total = total
    pedido.save()
    # Opcional: esvazia o carrinho deletando-o
    carrinho.delete()
