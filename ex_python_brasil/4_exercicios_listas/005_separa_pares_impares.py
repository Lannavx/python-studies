''' Faça um Programa que leia 20 números inteiros e armazene-os num vetor. 
Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. 
Imprima os três vetores.'''

from random import randint

# Inicializa as listas para armazenar todos os números, pares e ímpares
lista_numeros = []
lista_impar = []
lista_par = []

# Loop para gerar 20 números aleatórios
for _ in range(20):
    numeros = randint(0,100)

    lista_numeros.append(numeros)

    # Classifica o número como par ou ímpar e adiciona à lista correspondente
    if numeros % 2 == 0:
        lista_par.append(numeros)
    else:
        lista_impar.append(numeros)     

# Exibe os resultados
print(f'Todos os números: {lista_numeros}')
print(f'Números Pares: {lista_par}')    
print(f'Números Impares: {lista_impar}') 