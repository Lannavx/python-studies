# Faça um Programa que leia três números e mostre o maior deles.

numero_1 = int(input('Informe um número: '))
numero_2 = int(input('Informe mais um número: '))
numero_3 = int(input('Informe outro número: '))

# Inicializa a variável com o primeiro número
maior_numero = numero_1

# Compara com o segundo número e atualiza a variável maior_numero caso verdadeiro
if numero_2 > maior_numero:
    maior_numero = numero_2

# Compara com o terceiro número e atualiza a variável maior_numero caso verdadeiro
if numero_3 > maior_numero:
    maior_numero = numero_3

print(f'O maior número é: {maior_numero}') 