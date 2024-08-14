''' Faça um programa, com uma função que necessite de um argumento. 
A função retorna o valor de caractere "P", se seu argumento for positivo, e "N", se seu argumento for zero ou negativo.'''

import random

def classificar_numero(numero):
    '''Recebe um argumento e retorna "P" se o número for positivo, e "N" se for zero ou negativo'''
    if numero > 0:
        return 'P'
    else:
        return 'N'    

# Gera um número inteiro aleatório entre -100 e 100
numero = random.randint(-100, 100)

# Chama a função e imprime o resultado
print(f'O número gerado foi {numero} e ele é {classificar_numero(numero)}')
