# Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.

import random

# Solicita ao usuário o número de elementos a serem gerados
quantidade_numeros = int(input('Quantos números você deseja gerar? '))

# Inicializa uma lista vazia para armazenar os números
lista_numeros = []

# Loop para gerar números aleatórios entre 1 e 100
for _ in range(quantidade_numeros):
    numeros_aleatorios = random.randint(1, 100)
    lista_numeros.append(numeros_aleatorios)

# Calcula o menor, o maior valor e a soma dos números na lista
menor_valor = min(lista_numeros)
maior_valor = max(lista_numeros)
soma = sum(lista_numeros)


print(f'Conjunto de números: {lista_numeros}')
print(f'''O menor valor é: {menor_valor}
O maior valor é: {maior_valor}
E a soma de todos os valores é: {soma}''')