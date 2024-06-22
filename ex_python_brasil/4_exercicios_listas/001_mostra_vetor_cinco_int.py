# Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.

# Importa o módulo random para gerar números aleatórios
import random

# Inicializa uma lista vazia para armazenar os números
lista = []

# Loop que itera 5 vezes, gerando 5 números
for numeros in range(5):

    # Gera um número aleatório entre 0 e 5 e os adiciona a lista
    numeros = random.randrange(0, 6)
    lista.append(numeros)

# Exibe os números
print(lista)