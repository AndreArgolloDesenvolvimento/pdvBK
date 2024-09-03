import Produto

class Bebida(Produto):
    def __init__(self,nome: str,preco: float,tipo: str,marca: str,quantidade: int):
        super.__init__(nome,preco)
        self.tipo = tipo
        self.marca = marca
        self.quantidade = quantidade
        