# Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.

from random import randint

# Inicializa as variáveis
list_numeros = []
multiplicacao = 1 

# Loop para gerar 5 números aleatórios e adicioná-los à lista
for _ in range(5):
    numero = randint(0, 50)

    list_numeros.append(numero)

    # Multiplica cada número ao acumulador
    multiplicacao *= numero  

# Calcula a soma dos números na lista
soma = sum(list_numeros)

# Exibe os resultados
print(f'Lista de números: {list_numeros}')
print(f'A soma dos números é de {soma} e a multiplicação é de {multiplicacao}')


