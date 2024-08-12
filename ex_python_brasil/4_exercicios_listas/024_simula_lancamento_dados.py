'''Faça um programa que simule um lançamento de dados. 
Lance o dado 100 vezes e armazene os resultados em um vetor . 
Depois, mostre quantas vezes cada valor foi conseguido. 
Dica: use um vetor de contadores(1-6) e uma função para gerar numeros aleatórios, simulando os lançamentos dos dados.'''

from random import randint

# Inicializa a lista com número e contagem
numeros_contador =[[1,0], [2,0], [3,0], [4,0], [5,0], [6,0]]
jogadas = []

# Função para gerar números aleatórios de 1 a 6
def gerar_numero_aleatorio():
    return randint(1,6)

# Simula 100 jogadas e atualiza contagens diretamente
for _ in range(100):
    jogada = gerar_numero_aleatorio()
    jogadas.append(jogada)
    numeros_contador[jogada - 1][1] += 1

# Exibe os resultados
print(f'Lances: {", ".join(map(str, jogadas))}')

print(f'\nContagem de cada valor:\n') 
for num, contagem in numeros_contador:
    print(f'Número {num} foi obtido {contagem} vezes')