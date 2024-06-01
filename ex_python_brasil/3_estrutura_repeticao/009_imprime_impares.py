# Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50.

for numeros in range(1,51):
    if numeros % 2 == 1:
        print(numeros, end='')
        print(' - ' if numeros < 49 else '.', end='')