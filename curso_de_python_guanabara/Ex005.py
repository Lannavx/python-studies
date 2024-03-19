
#Faça um  programa que leia um númro inteiro e mostre na tela o seu sucessor e seu antecessor

n1 = int(input('Digite um numero: '))
a = n1 - 1
s = n1 + 1
print(f'O sucessor de {n1} é {s}')
print(f'O antecessor de {n1} é {a}')

# Outra forma de fazer

n1 = int(input('Digite um numero: '))
print(f'O sucessor de {n1} é {(n1+1)}')
print(f'O antecessor de {n1} é {(n1-1)}')