#Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.

s = 0
for num in range(1,501,2):
    if num % 3 == 0:
        print(num, end=' ')
        s+=num
print(f'A soma entre esses valores é de {s}')

#Forma do Professor

soma= 0
cont = 0
for c in range(1,501,2):
    if c % 3 == 0:
        cont = cont + 1
        soma = soma + c
print(f'A soma de todos os {cont} valores solicitados é {soma}')
