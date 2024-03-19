#Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

#Forma 1
maior = 0
menor = 0
for pessoa in range(1,6):
    peso = float(input(f'Informe o peso da {pessoa}ª pessoa: '))
    if pessoa == 1:
        maior = peso
        menor = peso 
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso    
print(f'O maior peso foi o de {maior}Kg e o menor peso foi o de {menor}Kg')