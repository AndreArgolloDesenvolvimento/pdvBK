from datetime import datetime

class Venda:
    def __init__(self,listaProdutos: dict,cliente: dict,operador: dict,formaPagamento: dict):
        self.documento = 0
        self.dataEmissao = datetime.now().time
        self.total = 0
        self.listaProdutos = listaProdutos
        self.cliente = cliente
        self.operador = operador
        self.formaPagamento = formaPagamento
        