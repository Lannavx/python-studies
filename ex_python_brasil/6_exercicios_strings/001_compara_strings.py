'''Tamanho de strings. Faça um programa que leia 2 strings e informe o conteúdo delas seguido do seu comprimento. 
Informe também se as duas strings possuem o mesmo comprimento e são iguais ou diferentes no conteúdo.

Compara duas strings
String 1: Brasil Hexa 2006
String 2: Brasil! Hexa 2006!
Tamanho de "Brasil Hexa 2006": 16 caracteres
Tamanho de "Brasil! Hexa 2006!": 18 caracteres
As duas strings são de tamanhos diferentes.
As duas strings possuem conteúdo diferente.
'''

def informar_tamanho(string_1, string_2):
    '''Informa o tamanho de caracteres de cada string'''
    tamanho_string_1 = len(string_1)
    tamanho_string_2 = len(string_2)
    return tamanho_string_1, tamanho_string_2

def comparar_tamanho(tamanho_string_1, tamanho_string_2):
    '''Compara se as duas strings possuem o mesmo tamanho'''
    if tamanho_string_1 != tamanho_string_2:
        return 'diferentes'
    else:
        return 'iguais'

def comparar_conteudo(string_1, string_2):
    '''Compara se as duas strings possuem o mesmo conteudo'''
    if string_1 != string_2:
        return 'diferente'
    else:
        return 'iguais'

def exibir_resultado(string_1, string_2, tamanho_string_1, tamanho_string_2, tamanho, conteudo):
    '''Exibe o resultado após as comparações'''
    print('\nCompare duas strings')
    print(f'String 1: {string_1}')
    print(f'String 2: {string_2}')
    print(f'Tamanho de "{string_1}": {tamanho_string_1} caracteres')
    print(f'Tamanho de "{string_2}": {tamanho_string_2} caracteres')
    print(f'As duas strings são de tamanhos {tamanho}')
    print(f'As duas strings possuem conteúdo {conteudo}')

# Solicita duas strings ao usuário
print('Escreva abaixo duas palavras ou frases para comparação!')
string_1 = input('Informe uma frase ou palavra: ').strip()
string_2 = input('Informe outra frase ou palavra: ').strip()

# Executa e armazena os resultados das funções
tamanho_string_1, tamanho_string_2 = informar_tamanho(string_1, string_2)
tamanho = comparar_tamanho(tamanho_string_1, tamanho_string_2)
conteudo = comparar_conteudo(string_1, string_2)

exibir_resultado(string_1, string_2, tamanho_string_1, tamanho_string_2, tamanho, conteudo)



