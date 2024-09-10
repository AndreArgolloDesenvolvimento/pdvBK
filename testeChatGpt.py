class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
    
    def __str__(self):
        return f"{self.nome}: R${self.preco:.2f}"


class Pedido:
    def __init__(self):
        self.produtos = []
    
    def adicionar_produto(self, produto, quantidade):
        self.produtos.append((produto, quantidade))
    
    def calcular_total(self):
        total = sum(produto.preco * quantidade for produto, quantidade in self.produtos)
        return total
    
    def gerar_resumo(self):
        resumo = "Resumo do Pedido:\n"
        for produto, quantidade in self.produtos:
            resumo += f"{produto.nome} x{quantidade} - R${produto.preco * quantidade:.2f}\n"
        resumo += f"Total: R${self.calcular_total():.2f}"
        return resumo


class Hamburgueria:
    def __init__(self):
        self.produtos = []
        self.pedido_atual = Pedido()
    
    def adicionar_produto(self, nome, preco):
        produto = Produto(nome, preco)
        self.produtos.append(produto)
        print(f"Produto adicionado: {produto}")
    
    def iniciar_pedido(self):
        self.pedido_atual = Pedido()
        print("Novo pedido iniciado.")
    
    def adicionar_item_ao_pedido(self, nome, quantidade):
        produto = next((p for p in self.produtos if p.nome == nome), None)
        if produto:
            self.pedido_atual.adicionar_produto(produto, quantidade)
            print(f"Adicionado {quantidade} x {produto.nome} ao pedido.")
        else:
            print(f"Produto {nome} não encontrado.")
    
    def finalizar_pedido(self):
        print(self.pedido_atual.gerar_resumo())
        self.pedido_atual = Pedido()  # Reseta o pedido atual após finalizar


# Exemplo de uso
if __name__ == "__main__":
    hamburgueria = Hamburgueria()

    # Adicionar produtos
    hamburgueria.adicionar_produto("Hambúrguer Clássico", 15.00)
    hamburgueria.adicionar_produto("Batata Frita", 7.00)
    hamburgueria.adicionar_produto("Refrigerante", 5.00)

    # Iniciar um novo pedido
    hamburgueria.iniciar_pedido()
    hamburgueria.adicionar_item_ao_pedido("Hambúrguer Clássico", 2)
    hamburgueria.adicionar_item_ao_pedido("Batata Frita", 1)
    hamburgueria.adicionar_item_ao_pedido("Refrigerante", 3)

    # Finalizar o pedido
    hamburgueria.finalizar_pedido()
