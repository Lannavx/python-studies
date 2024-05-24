# Faça um Programa que leia três números e mostre o maior e o menor deles.

numero_1 = int(input('Informe um número: '))
numero_2 = int(input('Informe mais um número: '))
numero_3 = int(input('Informe outro número: '))

# Inicializa as variáveis maior_numero e menor_numero
maior_numero = numero_1
menor_numero = numero_1

# Verifica se os números são maiores que o maior_numero e atualiza a variavel no caso de condição verdadeira
if numero_2 > maior_numero:
    maior_numero = numero_2

if numero_3 > maior_numero:
    maior_numero = numero_3

# Verifica se os números são menores que o menor_numero e atualiza a variavel no caso de condição verdadeira
if numero_2 < menor_numero:
    menor_numero = numero_2

if numero_3 < menor_numero:
    menor_numero = numero_3


print(f'O maior número é: {maior_numero}')
print(f'O menor número é: {menor_numero}')    