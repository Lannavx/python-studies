# Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.

lista_a = [1,2,3,4,5,6,7,8,9,10]
lista_b = [11,12,13,14,15,16,17,18,19,20]
lista_c = [21,22,23,24,25,26,27,28,29,30]

lista_d = []

# Laço para iterar sobre os índices dos elementos das listas e adicionar os valores intercalados
for i in range(10): 

    lista_d.append(lista_a[i]) 
    lista_d.append(lista_b[i]) 
    lista_d.append(lista_c[i]) 

print(lista_d)