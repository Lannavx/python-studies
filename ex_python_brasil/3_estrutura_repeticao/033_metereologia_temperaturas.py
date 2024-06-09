''' O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que 
leia um conjunto indeterminado de temperaturas, e informe ao final a menor e a maior
temperaturas informadas, bem como a média das temperaturas.'''

# Solicita ao usuário a quantidade de temperaturas
quantidade_temp = int(input('Quantos temperaturas você deseja informar? '))

# Inicializa uma lista vazia para armazenar os valores
lista_temperatura = []

# Loop para solicitação de temperaturas ao usuário
for i in range(quantidade_temp):

    temperatura = float(input(f'Digite apenas o número da {i + 1}ª temperatura: '))
    lista_temperatura.append(temperatura) # Adiciona os valores a lista

# Calcula a maior, a menor e a média temperatura
menor_valor = min(lista_temperatura)
maior_valor = max(lista_temperatura)
media = sum(lista_temperatura) / quantidade_temp

print('-' * 10)

# Imprime todas as temperaturas registradas com o símbolo de graus Celsius
print('Conjunto de temperaturas:')
for temp in lista_temperatura:
    print(f'{temp}°C', end=' ')

# Exibe os resultados
print(f'''\nMenor temperatura: {menor_valor}°C
Maior temperatura: {maior_valor}°C
A média das temperaturas é de: {media:.2f}°C''') 