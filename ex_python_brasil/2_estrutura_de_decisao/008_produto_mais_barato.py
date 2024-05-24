'''Faça um programa que pergunte o preço de três produtos e 
informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.'''

# Produto 1
produto_1 = input('Informe o nome de um produto: ').strip()
valor_1 = float(input(f'Informe o valor de {produto_1}: R$ '))

# Produto 2
produto_2 = input('Informe o nome de outro produto: ').strip()
valor_2 = float(input(f'Informe o valor de {produto_2}: R$ '))

# Produto 3
produto_3 = input('Informe o nome de mais um produto: ').strip()
valor_3 = float(input(f'Informe o valor de {produto_3}: R$ '))

# Inicializa com o valor e o nome do primeiro produto
menor_valor = valor_1
produto_barato = produto_1

# Verifica se o segundo produto é mais barato e atualiza as variaveis no caso de condição verdadeira
if valor_2 < menor_valor:
    menor_valor = valor_2
    produto_barato = produto_2

# Verifica se o terceiro produto é mais barato e atualiza as variaveis no caso de condição verdadeira
if valor_3 < menor_valor:
    menor_valor = valor_3  
    produto_barato = produto_3

print(f'Considerado o menor valor, o produto que você deve comprar é {produto_barato} que custa R${menor_valor:.2f}')