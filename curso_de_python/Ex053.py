'''Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
Exemplos de palíndromos: APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.'''

#Forma 1 com fatiamento
frase = str(input('Digite uma frase qualquer: ')).replace(' ', '').strip().upper()
frase_invertida = frase[::-1]
print(f'O inverso de {frase} é {frase_invertida}')
if frase_invertida == frase:
    print('A frase digitada é um Palíndromo!')
else:
    print('A frase digitada não é um Palíndromo!')


#Forma 2 com for
frase = str(input('Digite uma frase qualquer: ')).replace(' ', '').strip().upper()
frase_invertida = ''
for letras in frase:
    frase_invertida = letras + frase_invertida
print(f'O inverso de {frase} é {frase_invertida}')
if frase_invertida == frase:
    print('A frase digitada é um Palíndromo!')
else:
    print('A frase digitada não é um Palíndromo!')  

#Forma do Professor

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print(f'O inverso de {frase} é {inverso}')    
if inverso == junto:
    print('A frase digitada é um Palíndromo!')
else:
    print('A frase digitada não é um Palíndromo!')