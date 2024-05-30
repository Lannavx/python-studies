'''O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:

                      Até 5 Kg           Acima de 5 Kg
File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg

Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, 
porém não há limites para a quantidade de carne por cliente. 
Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total da compra. 
Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal, 
contendo as informações da compra: tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.'''

# Tratamento de erro no caso de valor inválido
try:
    carne = input('''Informe o tipo de carne comprada: [F] File Duplo, [A] Alcatra, [P] Picanha: ''').strip().upper()
    if carne not in ['F', 'A', 'P']:
        print('Tipo de carne inválido. Por favor, escolha [F] para File Duplo, [A] para Alcatra ou [P] para Picanha.')
        exit()
    kg_carne = float(input('Informe a quantidade de KG de carne comprada: '))
except ValueError:
    print('Por favor, insira números válidos.')
    exit()

# Menu de pagamento
pagamento = input('''Opções para pagamento:
[1] À vista
[2] Crédito
[3] Débito                       
[4] Cartão Tabajara
Informe a forma de pagamento conforme menu: ''')

# Define o preço por Kg com base no tipo de carne e na quantidade
if carne == 'F':
    tipo_carne = 'File Duplo'
    if kg_carne > 5:
        preco_kg = 5.80
    else:
        preco_kg = 4.90    
elif carne == 'A':
    tipo_carne = 'Alcatra'
    if kg_carne > 5:
        preco_kg = 6.80
    else:
        preco_kg = 5.90   
else:
    tipo_carne = 'Picanha' 
    if kg_carne > 5:
        preco_kg = 7.80
    else:
        preco_kg = 6.90   

# Calcula o valor total
valor_total = kg_carne * preco_kg

# Determina o tipo de pagamento e aplica o desconto se for o caso
if pagamento == '1':
    tipo_pagamento = 'À vista'
    desconto = 0
    valor_final = valor_total
elif pagamento == '2':
    tipo_pagamento = 'Crédito'
    desconto = 0
    valor_final = valor_total 
elif pagamento == '3':
    tipo_pagamento = 'Débito'
    desconto = 0
    valor_final = valor_total          
elif pagamento == '4':
    tipo_pagamento = 'Cartão Tabajara'
    desconto = valor_total * 0.05
    valor_final = valor_total - desconto
else:
    print('Opção de pagamento inválida.')
    exit()         

print()

print('=' * 5 ,'Cupom Fiscal', '=' * 5 )
print(f'''Tipo e quantidade de carne: {kg_carne}kgs de {tipo_carne}
Preço total: R${valor_total:.2f}
Tipo de pagamento: {tipo_pagamento}
Valor do desconto (aplicável no Cartão Tabajara): R${desconto:.2f}
Valor a pagar: R${valor_final:.2f}
''')    