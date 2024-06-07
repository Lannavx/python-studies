'''O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99 e agora possui uma loja de conveniências. 
Faça um programa que implemente uma caixa registradora rudimentar. 
O programa deverá receber um número desconhecido de valores referentes aos preços das mercadorias. 
Um valor zero deve ser informado pelo operador para indicar o final da compra. 
O programa deve então mostrar o total da compra e perguntar o valor em dinheiro que o cliente forneceu, 
para então calcular e mostrar o valor do troco. Após esta operação, o programa deverá voltar ao ponto inicial, 
para registrar a próxima compra. A saída deve ser conforme o exemplo abaixo:

Lojas Tabajara 
Produto 1: R$ 2.20
Produto 2: R$ 5.80
Produto 3: R$ 0
Total: R$ 8.00
Dinheiro: R$ 20.00
Troco: R$ 12.00
'''

# Loop principal para manter a operação contínua
while True:

    # Inicializa as variáveis necessárias para o cálculo
    cont_produto = 0
    soma_valor = 0
    lista_mercadoria = [] # lista principal

    print('Caixa Tabajara')
    print('Digite 0 para encerrar a contagem de produtos.')

    # Loop interno para coletar os preços dos produtos
    while True:
        cont_produto += 1
        valor_mercadoria = float(input(f'Informe o valor do Produto {cont_produto}: R$ '))

        # Condição de parada: se o valor informado for 0, encerra a coleta de produtos
        if valor_mercadoria == 0:
            break
                
        # Adiciona uma lista de produto e preço à lista principal e soma ao total        
        lista_mercadoria.append([cont_produto, valor_mercadoria])     
        soma_valor += valor_mercadoria

    # Verifica se de fato algum produto foi adicionado
    if cont_produto > 1:
        print(f'O total da compra é de R${soma_valor:.2f}')
   
        # Solicita o valor pago pelo cliente e calcula o troco    
        pagamento = float(input('Informe o valor em dinheiro para pagamento: R$'))
        troco = pagamento - soma_valor

        # Mostra o resumo da compra
        print('-' * 5)
        print('Lojas Tabajara')
        for produto in lista_mercadoria: 
            print(f'Produto {produto[0]} - R$ {produto[1]:.2f}')

        print(f'Total: R$ {soma_valor:.2f} \nDinheiro: R$ {pagamento:.2f} \nTroco: R$ {troco:.2f} ')
        print('-' * 5)
    
    # Se nenhum produto foi informado, volta pro inicio
    else:
        print('Nenhum produto foi registrado. Reiniciando...')
        print('-' * 5) 

