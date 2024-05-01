'''
O módulo itertools em Python fornece funcionalidades eficientes para lidar com iteráveis de maneira poderosa.

zip: esta função é usada para combinar elementos de dois ou mais iteráveis em tuplas. 
Ela para de iterar assim que o iterável mais curto é esgotado.

zip_longest: o contrário de zip, zip_longest combina todos os elementos de todos os iteráveis, 
preenchendo valores ausentes com um valor predefinido (geralmente None). 
É útil quando você deseja que todos os elementos dos iteráveis sejam considerados.
'''

# Exercício - Unir listas

'''
Crie uma função zipper (como o zipper de roupas)
O trabalho dessa função será unir duas listas na ordem.
Use todos os valores da menor lista.

Ex.:
['Salvador', 'Ubatuba', 'Belo Horizonte']
['BA', 'SP', 'MG', 'RJ']

Resultado:
[('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]
'''

from itertools import zip_longest

# Forma 1 com função
def zipper(lista1, lista2):
    intervalo = min(len(l1), len(l2))
    return [(lista1[i], lista2[i]) for i in range(intervalo)]

l1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
l2 = ['BA', 'SP', 'MG', 'RJ']

print(zipper(l1,l2))

# Forma 2 com zip
l1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
l2 = ['BA', 'SP', 'MG', 'RJ']
print(list(zip(l1,l2)))

#Forma 3 com zip_longest
l1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
l2 = ['BA', 'SP', 'MG', 'RJ']
print(list(zip_longest(l1,l2, fillvalue='Sem Cidade')))

