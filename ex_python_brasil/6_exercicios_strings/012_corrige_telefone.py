'''Valida e corrige número de telefone. 
Faça um programa que leia um número de telefone, e corrija o número no caso deste conter somente 7 dígitos, acrescentando o '3' na frente. 
O usuário pode informar o número com ou sem o traço separador.

Valida e corrige número de telefone
Telefone: 461-0133
Telefone possui 7 dígitos. Vou acrescentar o digito três na frente.
Telefone corrigido sem formatação: 34610133
Telefone corrigido com formatação: 3461-0133'''

import re

def ajustar_numero(num_telefone):
    """Ajusta o número de telefone adicionando '3' na frente se tiver 7 dígitos."""
    if len(num_telefone) == 7:
        print('Telefone possui 7 dígitos. Vou acrescentar o dígito três na frente.')
        return '3' + num_telefone
    
    # Se tiver 8 dígitos, retorna o número original
    return num_telefone

def formatar_numero(num_telefone):
    """Formata o número de telefone com o traço separador, se tiver 8 dígitos."""
    if len(num_telefone) == 8:
        return f'{num_telefone[:4]}-{num_telefone[4:]}'
    return num_telefone

# Lê o número de telefone do usuário
num_telefone = input('Digite o número de telefone: ')

# Exibe o número original
print('\nValida e corrige número de telefone')
print(f'Telefone: {num_telefone}')

# Remove tudo que não for número, deixando apenas os dígitos
num_telefone = re.sub(r'[^0-9]', '', num_telefone)

# Ajusta o número, se necessário
num_corrigido = ajustar_numero(num_telefone)

# Exibe o número corrigido sem formatação
print(f'Telefone corrigido sem formatação: {num_corrigido}')

# Formata e exibe o número corrigido com formatação
num_corrigido_formatado = formatar_numero(num_corrigido)
print(f'Telefone corrigido com formatação: {num_corrigido_formatado}')
