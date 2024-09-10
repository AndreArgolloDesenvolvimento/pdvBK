import Bebida
import Alimento
import Cliente
import Operador
import Venda

class Loja:
    def __init__(self, nome) -> None:
        self.nome = nome
        self.produtos = []
        self.clientes = []
        self.operadores = []
        self.vendas = []

    #PRODUTOS
    def cadastrar_produto(self,produto):
        self.produtos.append(produto)
        return f'Produto cadastrado: {produto}'
    
    def listar_produtos(self):
        for item in self.produtos:
            print(item.__dict__)
    
    #CLIENTES
    def cadastrar_cliente(self,cliente):
        self.clientes.append(cliente)
        return f'Cliente cadastrado: {cliente}'
    
    def listar_clientes(self):
        for item in self.clientes:
            print(item.__dict__)
    
    #OPERADORES
    def cadastrar_operador(self,operador):
        self.operadores.append(operador)
        return f'Operador cadastrado: {operador}'
    
    def listar_operadores(self):
        for item in self.operadores:
            print(item.__dict__)
    
    
    def iniciar_venda(self):
        self.venda_atual = Venda()