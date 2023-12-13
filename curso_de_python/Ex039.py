'''Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar 
ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento.  
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.'''

from datetime import date
ano = int(input('Informe o ano de seu nascimento: '))
data = date.today().year
idade = (data - ano)

if idade > 18:   
    print(f'Você tem {idade} anos! Já passou do tempo do alistamento! Você está atrasado em {idade-18} anos!')
elif idade  < 18:
    print(f'Você tem {idade} anos! Você ainda vai se alistar! Faltam {18-idade} anos.')    
else: 
    print(f'Você tem {idade} anos! É hora de se alistar!')