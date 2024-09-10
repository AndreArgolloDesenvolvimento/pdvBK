import Produto

class Bebida(Produto):
    def __init__(self,nome:str,preco:float,tipo:str,marca:str,quantidade:int):
        super.__init__(nome,preco,tipo)
        self.marca = marca
        self.quantidade = quantidade
        
    def saida_estoque(self,sku,quantidade) -> str:
        if sku == self.sku:
            if quantidade <= self.quantidade:
                self.quantidade -= quantidade
                return 'Saída efetuada com sucesso'
            else:
                return 'Saldo insuficiente'
        else:
            return 'Sku inexistente'
    
    def entrada_estoque(self,sku,quantidade) -> str:
        if sku == self.sku:
            self.quantidade += quantidade
            return 'Entrada efetuada com sucesso'
        else:
            return 'Sku inexistente'
        
        
            
            

    