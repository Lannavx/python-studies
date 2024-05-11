'''
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append - Adiciona um item ao final
    insert - Adiciona um item no índice escolhido
    pop - Remove do final ou do índice escolhido
    del - apaga um índice
    clear - limpa a lista
    extend - estende a lista
    + - concatena listas
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
'''

# É interessante trabalhar com alterações no fim da lista caso a mesma seja extensa

# Exercício - exiba os índices da lista

lista = ['Maria', 'Helena', 'Luiz']
lista.append('Joao')

indice = 0
for nome in lista:
    indice += 1
    print(indice - 1, nome, type(nome))    

# Outra forma
    
lista = ['Maria', 'Helena', 'Luiz']
lista.append('Joao')

indices = range(len(lista))

for indice in indices:
    print(indice, lista[indice] , type(lista[indice]))    