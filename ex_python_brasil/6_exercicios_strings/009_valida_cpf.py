'''Verificação de CPF. 
Desenvolva um programa que solicite a digitação de um número de CPF no formato xxx.xxx.xxx-xx e indique se é um número válido 
ou inválido através da validação dos dígitos verificadores e dos caracteres de formatação.'''

import re

def verificar_formato(cpf):
    '''Verifica se o formato inserido pelo usuário está no padrão xxx.xxx.xxx-xx'''
    return re.fullmatch(r'\d{3}\.\d{3}\.\d{3}-\d{2}', cpf)

def validar_primeiro_digito():
    ''' Calcula e valida o primeiro dígito verificador do CPF'''
    resultado = 0
    numero_base = 10

    for num in numeros_cpf[0:9]:
        resultado += num * numero_base
        numero_base -= 1

    resto_digito_1 = (resultado * 10) % 11
    if resto_digito_1 == 10:
        resto_digito_1 = 0

    return resto_digito_1 == numeros_cpf[9]
        
def validar_segundo_digito():
    ''' Calcula e valida o segundo dígito verificador do CPF'''
    resultado = 0
    numero_base = 11
    for num in numeros_cpf[0:10]:
        resultado += num * numero_base
        numero_base -= 1

    resto_digito_2 = (resultado * 10) % 11
    if resto_digito_2 == 10:
        resto_digito_2 = 0

    return resto_digito_2 == numeros_cpf[10]

def validar_cpf():
    '''Verifica a validade geral do CPF'''
    if numeros_cpf == [numeros_cpf[0]] * 11:
        return 'CPF INVÁLIDO: Números não podem ser todos iguais.'
    
    if validar_primeiro_digito() and validar_segundo_digito():
        return 'CPF VÁLIDO'
    else:
        return 'CPF INVÁLIDO'

# Lista para armazenar os dígitos numéricos do CPF
numeros_cpf = []    

# Solicita uma entrada ao usuário
cpf = input('Informe o CPF no formato xxx.xxx.xxx-xx: ').strip() 

# Verifica o formato e segue com a validação se estiver correto
if verificar_formato(cpf):

    # Remove pontos e traços e converte cada caractere para inteiro
    cpf = cpf.replace('.', '').replace('-', '')   
    for char in cpf:
        numeros_cpf.append(int(char))

    # Imprime o resultado da validação
    print(validar_cpf())
else:
    print('CPF INVÁLIDO: Formato incorreto.')    