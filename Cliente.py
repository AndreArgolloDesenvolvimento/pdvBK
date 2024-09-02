from Pessoa import Pessoa

class Cliente (Pessoa):
    def __init__(self, nome: str, cpf: str, endereco: str, telefone: str, email: str, data_nascimento: str, cupom:str) -> None:
        super().__init__(nome, cpf, endereco, telefone, email, data_nascimento)
        self.cupom = cupom
        self.pontuacao = 0
    
    def comprar(self, ):
        ...
    
    def devolver(self):
        ...
    
    def usarPontuacao(self):
        ...
        
    def usarCupom(self):
        ...
        
        

