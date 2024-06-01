# Faça um programa que leia 5 números e informe o maior número.

import random

# Inicializa uma lista vazia para armazenar os números
numeros = []

# Loop para gerar 5 números aleatórios entre 1 e 100
for i in range(5):
    numero = random.randint(1, 100)
    numeros.append(numero)
    print(f"O {i+1}º número gerado é: {numero}")

# Encontra o maior número
maior_numero = max(numeros)

print("O maior número é:", maior_numero)
