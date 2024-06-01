# Faça um programa que leia 5 números e informe a soma e a média dos números.

import random

# Inicializa uma lista vazia para armazenar os números
numeros = []

# Loop para gerar 5 números aleatórios entre 1 e 100
for i in range(5):
    numero = random.randint(1, 100)
    numeros.append(numero)
    print(f'O {i+1}º número gerado é: {numero}')

# Calcula a soma e a média
soma = sum(numeros)
media = soma / 5

print('O soma dos número é',soma)
print('A média dos número é',media)