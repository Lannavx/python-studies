''' Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro. 
Depois modifique o programa para que ele mostre os números um ao lado do outro.'''

print('Números na Vertical')  
for numeros in range(1,21):
    print(numeros) 

print('-' * 5)    

print('Números na Horizontal')  
for numeros in range(1, 21):
    print(numeros, end='')
    # Verifica se é o último número para decidir se coloca ponto ou traço
    print(' - ' if numeros < 20 else '.', end='')
