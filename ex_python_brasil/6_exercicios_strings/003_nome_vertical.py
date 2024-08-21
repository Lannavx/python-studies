'''Nome na vertical. Faça um programa que solicite o nome do usuário e imprima-o na vertical.

F
U
L
A
N
O
'''
# Solicita ao usuário que digite um nome
nome = input('Digite seu nome: ').strip().upper()

# Imprime o nome na vertical
for letra in nome:
    print(letra)