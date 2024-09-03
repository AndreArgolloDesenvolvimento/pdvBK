import uuid

def generate_sku():
    return str(uuid.uuid4()).split('-')[0].upper()


class Produto:
    def __init__(self, nome: str, preco: float) -> None:
        self.nome = nome
        self.preco = preco
        self.sku = generate_sku()
        
#produto1 = Produto('Batata Frita Grande',15)
#print(produto1.__dict__)