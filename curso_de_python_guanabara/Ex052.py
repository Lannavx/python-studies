#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

numero = int(input('Informe um número: '))
total = 0
for c in range(1, numero + 1):
    if numero % c == 0:
        print('\033[33m', end ='') # Cor amarela para divisores
        total += 1
    else:
        print('\033[31m', end ='') # Cor vermelha para não divisores
    print(f'{c}', end=' ')
print(f'\n\033[mO numero {numero} foi divisivel {total} vezes')
if total == 2:
    print('E por isso ele é PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO!')    
   

        