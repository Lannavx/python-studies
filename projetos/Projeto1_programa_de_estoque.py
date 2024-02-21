'''Projeto da faculdade. 
Criação de um programa que leia entradas e saidas de um produto e mostre o saldo total de vendas ao usuário.'''

compras = []
vendas = []

while True:
    print('\nEscolha uma opção:')
    print('1 - Registrar uma compra')
    print('2 - Registrar uma venda')
    print('3 - Verificar o saldo total das vendas')
    print('4 - Sair do programa')

    escolha = input('\nDigite o número da opção desejada: ')

    if escolha == '1':
        produto = input('Informe o nome do produto: ').upper()
        quantidade = int(input('Informe a quantidade: '))
        valor_unitario = float(input('Informe o valor unitário: '))
        compras.append({"produto": produto, "quantidade": quantidade, "valor_unitario": valor_unitario})
        print(f'Registro de compra do produto {produto} concluído com sucesso!')

    elif escolha == '2':
        produto = input('Digite o nome do produto: ').upper()
        quantidade = int(input('Digite a quantidade: '))
        valor_unitario = float(input('Digite o valor unitário: '))

        produto_encontrado = False
        for compra in compras:
            if compra['produto'] == produto:
                produto_encontrado = True
                if compra['quantidade'] >= quantidade:
                    vendas.append({'produto': produto, 'quantidade': quantidade, 'valor_unitario': valor_unitario})
                    print('Venda registrada com sucesso!')
                    break
                else:
                    print('Quantidade maior que a do estoque.')
                    break
        if not produto_encontrado:
            print(' Produto não encontrado.')

    elif escolha == '3':
        print('\nCalculando o saldo total das vendas...')
        lucro_total = 0
        for venda in vendas:
            lucro_total += venda['quantidade'] * venda['valor_unitario']
        for compra in compras:
            lucro_total -= compra['quantidade'] * compra['valor_unitario']
        print(f'O lucro total é: R${lucro_total:.2f}.')

    elif escolha == '4':
        print('\nSaindo do programa...')
        break

    else:
        print('\nOpção inválida. Por favor, tente novamente.')