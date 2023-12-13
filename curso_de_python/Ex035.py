#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

r1 = float(input('Informe o comprimento de uma reta: '))
r2 = float(input('Informe o comprimento de outra reta: '))
r3 = float(input('Informe o comprimento de mais uma reta: '))

if r1 < r2 + 3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('As retas podem formar um triângulo!')
else:
    print('As retas não podem formar um triângulo!')

