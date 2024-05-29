'''Um posto está vendendo combustíveis com a seguinte tabela de descontos:

Álcool:
até 20 litros, desconto de 3% por litro
acima de 20 litros, desconto de 5% por litro

Gasolina:
até 20 litros, desconto de 4% por litro 
acima de 20 litros, desconto de 6% por litro.

Escreva um algoritmo que leia o número de litros vendidos,  o tipo de combustível 
(codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo 
cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.
'''

# Tratamento de erro no caso de valores de combustível e litros inválidos
try:
    combustivel = input('Informe o tipo de combustível comprado A-álcool, G-gasolina : ').strip().upper()
    if combustivel not in ['A', 'G']:
        print('Tipo de combustível inválido! Informe A para álcool ou G para gasolina.')
        exit()
    litros = float(input('Informe a quantidade de litros comprados: '))
except ValueError:
    print('Por favor, insira números válidos.')
    exit()

# Preços dos combustíveis
GASOLINA = 2.50
ALCOOL = 1.90

# Condição para aplicação do desconto para cada tipo de combustível e litros comprados
if combustivel == 'A':
    preco_por_litro = ALCOOL
    if litros > 20:
        desconto_por_litro = 0.05
    else:
        desconto_por_litro = 0.03
elif combustivel == 'G':
    preco_por_litro = GASOLINA
    if litros > 20:
        desconto_por_litro = 0.06
    else:
        desconto_por_litro = 0.04

# Cálculo do valor total, desconto e valor final a pagar
valor = litros * preco_por_litro
desconto = valor * desconto_por_litro
valor_final = valor - desconto

# Determinação do tipo de combustível para exibição
if combustivel == 'A':
    tipo_combustivel = "álcool"
else:
    tipo_combustivel = "gasolina"

print(f'''
Valor total da compra de {litros:.2f}L de {tipo_combustivel} com desconto de
{desconto_por_litro * 100:.0f}% é de R${valor_final:.2f}
''')

