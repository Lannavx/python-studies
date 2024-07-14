# Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados dos elementos do vetor.

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  

# Inicializa a variável que armazenará a soma dos quadrados 
soma_dos_quadrados = 0

for numero in lista:
    # Cada número é elevado ao quadrado e somado à variável
    soma_dos_quadrados += numero ** 2

print(f'A soma dos quadrados dos elementos do vetor é de {soma_dos_quadrados}')
