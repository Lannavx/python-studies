'''Crie um programa que leia o ano de nascimento de sete pessoas. 
No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
Considere a maior idade como 21 anos'''

#Forma 1
from datetime import date
ano_atual = date.today().year
cont = 0
for c in range(1,8):
    ano_nascimento = int(input(f'Informe o ano de nascimento da {c}ª pessoa: '))
    if ano_atual - ano_nascimento < 21:
        cont += 1
print(f'Considerando os anos informados, {7 - cont} deles já atingiram a maioridade e {cont} ainda são de menor.')

#Forma 2

from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pessoa in range(1,8):
    nascimento = int(input(f'Informe o ano de nascimento da {pessoa}ª pessoa: '))
    idade = atual - nascimento
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1    
print(f'Considerando os anos informados, {totmaior} deles já atingiram a maioridade e {totmenor} ainda são de menor.')
