'''O cardápio de uma lanchonete é o seguinte:
Especificação   Código  Preço
Cachorro Quente 100     R$ 1,20
Bauru Simples   101     R$ 1,30
Bauru com ovo   102     R$ 1,50
Hambúrguer      103     R$ 1,20
Cheeseburguer   104     R$ 1,30
Refrigerante    105     R$ 1,00
Faça um programa que leia o código dos itens pedidos e as quantidades desejadas. 
Calcule e mostre o valor a ser pago por item (preço * quantidade) e o total geral do pedido. 
Considere que o cliente deve informar quando o pedido deve ser encerrado.'''

# Cabeçalho do cardápio
print('Bem vindo a Lanchonete 013')
print('Cardápio:')
print('-' * 10)
print('''Especificação   Código  Preço
Cachorro Quente 100     R$ 1,20
Bauru Simples   101     R$ 1,30
Bauru com ovo   102     R$ 1,50
Hambúrguer      103     R$ 1,20
Cheeseburguer   104     R$ 1,30
Refrigerante    105     R$ 1,00''')
print('-' * 10)

print()

# Dicionário contendo os itens do cardápio com códigos e preços
cardapio = {
    100: ('Cachorro Quente', 1.20),
    101: ('Bauru Simples', 1.30),
    102: ('Bauru com ovo', 1.50),
    103: ('Hambúrguer', 1.20),
    104: ('Cheeseburguer', 1.30),
    105: ('Refrigerante', 1.00)
}

lista_codigos = [] # Lista para armazenar os códigos dos produtos e as quantidades solicitadas
valor_total = 0    # Variável para acumular o valor total do pedido.

# Loop principal para coletar os pedidos dos usuários
while True:
    codigo_item = int(input('Informe o código dos itens desejados (ou 0 para sair): '))

    if codigo_item == 0:
        break

    quantidade = int(input('Informe a quantidade desejada: '))

    # Adiciona o código do item e a quantidade à lista
    lista_codigos.append([codigo_item, quantidade])
    
print()

# Verifica se foram feitos pedidos
if lista_codigos:
    print('Pedido:')

    for produto in lista_codigos:
        # Armazena a descrição(nome, preço) com base no código do produto
        descricao = cardapio[produto[0]]   

        # Calcula o valor total do item multiplicando o preço pela quantidade
        valor_item = descricao[1]  * produto[1]  

        # Adiciona o valor do item ao valor total do pedido
        valor_total += valor_item     

        # Exibe os resultados
        print(f'{produto[1]} unidades de {descricao[0]} no valor de R${valor_item :.2f}')

    print(f'Total: R${valor_total:.2f}')
else:
    print('Não foi solicitado nenhum pedido!')