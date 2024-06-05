'''Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário. 
O programa deverá mostrar também o número de divisões que ele executou para encontrar os números primos. 
Serão avaliados o funcionamento, o estilo e o número de testes (divisões) executados.'''

import math

# Solicita ao usuário um número para definir o limite superior do intervalo
numeros = int(input('Informe um número para verificar todos os primos até ele: '))

cont_divisoes = 0  # Inicializa o contador de divisões

print(f'Os números primos entre 1 e {numeros} são:')

# Loop para verificar cada número no intervalo de 2 a numeros
for num in range(2, numeros + 1):

    # Assume inicialmente que o número é primo
    primo = True  

    # Checa divisibilidade apenas até a raiz quadrada para determinar se é primo.
    for i in range(2, int(math.sqrt(num)) + 1):
        cont_divisoes += 1  # Incrementa o contador de divisões

        if num % i == 0:
            primo = False
            break

    # Imprime o número se for primo        
    if primo:
        print(num, end=' ')

# Após verificar todos os números, exibe o total de divisões realizadas
print(f'\nForam realizadas {cont_divisoes} divisões no total.')





    
