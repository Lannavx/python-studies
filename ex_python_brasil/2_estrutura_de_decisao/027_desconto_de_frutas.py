'''Uma fruteira está vendendo frutas com a seguinte tabela de preços:

                      Até 5 Kg           Acima de 5 Kg
Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg

Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, 
receberá ainda um desconto de 10% sobre este total. 
Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg)
de maças adquiridas e escreva o valor a ser pago pelo cliente.'''

# Tratamento de erro no caso de valor inválido
try:
    kg_morango = float(input('Informe a quantidade de KG de morango comprada: '))
    kg_maca = float(input('Informe a quantidade de KG de maça comprada: '))
except ValueError:
    print('Por favor, insira números válidos.') 
    exit()

# Calculo do preço dos morangos
if kg_morango > 5:
    preco_morango = 2.20
else:
    preco_morango = 2.50   

# Calculo do preço das maçãs
if kg_maca > 5:
    preco_maca = 1.50
else: 
    preco_maca = 1.80 

# Calculo do valor total para cada fruta
valor_morango = kg_morango * preco_morango
valor_maca = kg_maca * preco_maca
valor_total = valor_morango + valor_maca

print('=' * 30)
print(f'''Foram comprados {kg_morango}kg de morangos e {kg_maca}kg de maçãs.''')

# Aplica o desconto no caso de condição verdadeira
if kg_morango + kg_maca > 8 or valor_total > 25:
    desconto = valor_total * 0.10
    valor_final = valor_total - desconto
    print(f'Você ganhou 10% de desconto e o total da compra é de R${valor_final:.2f}')
else:
    valor_final = valor_total
    print(f'O total da compra é de R${valor_final:.2f}')    
   

