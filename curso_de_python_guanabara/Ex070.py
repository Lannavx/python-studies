'''Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato. '''

print('-' * 25)
print('Cadastro de Produtos')
print('-' * 25)


total = 0
cont_mais_mil = 0
produto_mais_barato = 0
cont = 0 
nome_produto_barato = ''

while True:
    produto = input('Nome do produto: ').strip()
    preco_produto = float(input('Preço do produto: R$'))
    mais_cadastro = input('Quer continuar com o cadastro? [S/N]: ').upper().strip()[0]
    cont +=1
    while mais_cadastro not in 'NS':
        print('Opção inválida! Digite S para Sim e N para Não.')
        mais_cadastro = input('Quer continuar com o cadastro? [S/N]: ').upper().strip()[0]

    total += preco_produto
 
    if preco_produto > 1000:
        cont_mais_mil += 1     
    if cont == 1 or preco_produto < produto_mais_barato: # Verifica se é o primeiro produto ou se o preço do produto atual é menor que o do produto mais barato até agora  
        produto_mais_barato = preco_produto # Atualiza o preço do produto mais barato
        nome_produto_barato = produto # Atualiza o nome do produto mais barato
    if mais_cadastro == 'N':
        break

print('-' * 40)

print(f'O total da compra é de R${total:.2f}')
print(f'Temos {cont_mais_mil} produtos custando mais de R$1000,00')
print(f'O produto mais barato é {nome_produto_barato} que custa R${produto_mais_barato:.2f}')

