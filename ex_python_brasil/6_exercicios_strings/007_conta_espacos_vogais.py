'''Conta espaços e vogais. Dado uma string com uma frase informada pelo usuário (incluindo espaços em branco), conte:

a. quantos espaços em branco existem na frase.
b. quantas vezes aparecem as vogais a, e, i, o, u.'''

def contar_vogais(string):
    '''Conta cada vogal em uma string e retorna o resultado como dicionário'''
    vogais = 'aeiou'
    resultados = {}
    for vogal in vogais:
        conta_vogal = string.count(vogal)
        resultados[vogal] = conta_vogal
    return resultados

# Solicita uma entrada ao usuário
string = input('Informe uma palavra ou frase: ').lower()

# Conta e exibe os espaços em branco na string
espacos_em_branco = string.count(' ')
print(f'Espaços em branco: {espacos_em_branco}')

# Armazena o dicionário retornado da função e itera sobre ele, imprimindo cada vogal e sua contagem
contagem_vogais = contar_vogais(string)
for vogal, quantidade in contagem_vogais.items():
    print(f'{vogal}: {quantidade}')
