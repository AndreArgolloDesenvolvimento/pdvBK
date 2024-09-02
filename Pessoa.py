class Pessoa:
    def __init__(self, nome:str, cpf:str, endereco:str, telefone:str, email:str, data_nascimento:str) -> None:
        self.nome = nome
        self.cpf = cpf
        self.endereco = endereco
        self.telefone = telefone
        self.email = email
        self.data_nascimento = data_nascimento
        
    def comer(self,comida):
        return f'{self.nome} está comendo {comida}'        

pessoa = Pessoa('André','12345678900','teste testesteste, teste.','(71)99999-9999','andre@gmail.com','14/07/1975')
pessoa2 = Pessoa('Elaine','12345678900','teste testesteste, teste.','(71)99999-9999','andre@gmail.com','14/07/1975')
print(pessoa.comer('Feijão'))
print(pessoa2.comer('Peixe'))

    
    