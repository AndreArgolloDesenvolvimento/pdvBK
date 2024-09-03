import Produto

class Alimento(Produto):
    
    def __init__(self,nome: str,preco: float, vegano: bool):
        super().__init__(nome,preco)
        self.ingredientes = []
        self.vegano = vegano

