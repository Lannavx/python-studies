'''Utilize uma lista para resolver o problema a seguir. Uma empresa paga seus vendedores com base em comissões. 
O vendedor recebe $200 por semana mais 9 por cento de suas vendas brutas daquela semana. 
Por exemplo, um vendedor que teve vendas brutas de $3000 em uma semana recebe $200 mais 9 por cento de $3000, ou seja, um total de $470. 
Escreva um programa (usando um array de contadores) que determine quantos vendedores receberam salários nos seguintes intervalos de valores:
a. $200 - $299
b. $300 - $399
c. $400 - $499
d. $500 - $599
e. $600 - $699
f. $700 - $799
g. $800 - $899
h. $900 - $999
i. $1000 em diante

Desafio: Crie ma fórmula para chegar na posição da lista a partir do salário, sem fazer vários ifs aninhados.'''

# Lista para contar o número de vendedores em cada faixa de salário
salarios = [0] * 9

# Lista para coletar as vendas brutas
vendas_brutas = []

# Loop para entrada das vendas brutas de cada vendedor
while True:
    entrada = input('Informe o valor das vendas brutas do vendedor ou digite "sair" para encerrar: ')
    
    if entrada.lower() == 'sair':
        break

    vendas_brutas.append(float(entrada))  

# Processa cada venda bruta
for venda in vendas_brutas:

    # Calcula o salário total
    salario_total = 200 + 0.09 * venda
    
    # Determina o índice na lista salarios
    if salario_total < 1000:
        indice = int((salario_total - 200) // 100)
    else:
        indice = 8  # Todos os valores $1000 ou mais vão para a última posição

    # Incrementa o contador apropriado
    salarios[indice] += 1

# Imprime o resultado
faixas = [
    '$200 - $299', '$300 - $399', '$400 - $499', '$500 - $599',
    '$600 - $699', '$700 - $799', '$800 - $899', '$900 - $999', '$1000 em diante'
]

print()
print('Quantidade de vendedores por faixa salarial: ')
for i in range(len(salarios)):
    print(f'{faixas[i]}: {salarios[i]}')









