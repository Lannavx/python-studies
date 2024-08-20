'''Embaralha palavra. 
Construa uma função que receba uma string como parâmetro e devolva outra string com os carateres embaralhados. 
Por exemplo: se função receber a palavra python, pode retornar npthyo, ophtyn ou qualquer outra combinação possível, de forma aleatória. 
Padronize em sua função que todos os caracteres serão devolvidos em caixa alta ou caixa baixa, independentemente de como foram digitados.'''

import random

def embaralhar_palavra(palavra=str):
    '''Embaralha palavra recebida após transforma-la em lista'''
    palavra_lista = list(palavra)
    random.shuffle(palavra_lista) 
    resultado = ''.join(palavra_lista)
    return resultado

# Solicita ao usuário uma palavra
palavra = input('Digite qualquer palavra: ').lower()

# Exibe a palavra embaralhada na tela
print(embaralhar_palavra(palavra))

