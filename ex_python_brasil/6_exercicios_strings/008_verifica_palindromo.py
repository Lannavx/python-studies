'''Palíndromo. 
Um palíndromo é uma seqüência de caracteres cuja leitura é idêntica se feita da direita para esquerda ou vice−versa. 
Por exemplo: OSSO e OVO são palíndromos. Em textos mais complexos os espaços e pontuação são ignorados. 
A frase SUBI NO ONIBUS é o exemplo de uma frase palíndroma onde os espaços foram ignorados. 
Faça um programa que leia uma seqüência de caracteres, mostre−a e diga se é um palíndromo ou não.'''

import re

print('Informe uma palavra ou frase para descobrir se ela é um palíndromo!')

# Solicita uma entrada ao usuário e coloca tudo em maiúsculo
string = input('Palavra ou frase: ').upper()

# Remove tudo que não for letra ou número
string = re.sub(r'[^A-Z0-9]', '', string) 

# Verifica se a string é um palíndromo
if string == string[::-1]:
    print('Sua palavra/frase é um palíndromo!')
else:
    print('Sua palavra/frase não é um palíndromo!')    