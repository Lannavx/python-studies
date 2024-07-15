''' Faça um Programa que leia dois vetores com 10 elementos cada. 
Gere um terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.'''

lista_a = [1,2,3,4,5,6,7,8,9,10]
lista_b = [11,12,13,14,15,16,17,18,19,20]

lista_c = []

# Laço para iterar sobre os índices dos elementos das listas e adicionar os valores intercalados
for i in range(10): 

    lista_c.append(lista_a[i]) 
    lista_c.append(lista_b[i]) 

print(lista_c)
