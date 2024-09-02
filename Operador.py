from Pessoa import Pessoa

class Operador (Pessoa):
    def __init__(self, nome: str, cpf: str, endereco: str, telefone: str, email: str, data_nascimento: str, senha: str, percentualComissao: float, salario: float) -> None:
        super().__init__(nome, cpf, endereco, telefone, email, data_nascimento)
        self.login = False
        self.senha = senha
        self.percentualComissao = percentualComissao
        self.salario = salario
        
    
        
        