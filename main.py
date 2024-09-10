import Loja

while True:
    opcao = input('''
    Selecione uma das opções:
          
          1 - CADASTRAR OPERADOR
          2 - LISTAR OPERADORES
          3 - CADASTRAR PRODUTO
          4 - LISTAR PRODUTOS
          5 - CADASTRAR CLIENTE
          6 - LISTAR CLIENTES
          7 - SAIR
    ''')
    
    match opcao:
        case '1': 
            print('OPERADOR ')
            nome = input('Nome: ')
            cpf = input('CPF: ')
            endereco = input('Endereco: ')
            telefone = input('Telefone: ')
            email = input('E-mail: ')
            data_nascimento = input('Data de Nascimento: ')
            senha = input('Senha: ')
            percentualComissao = ('% Comissão: ')
            salario = ('Salário: ')
            
        case '2':
        case '3':
        case '4':
        case '5':
        case '6':
        case '7':
            break
        case _:
            print('Opção inválida!!!')
            
        
