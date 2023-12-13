#Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

#É um número divisível por 4, mas não é divisível por 100.
#É um número divisível por 4, por 100 e por 400.

# != >> representa "diferente / não igual"

from datetime import date
ano = int(input('Qual ano quer analisar? Coloque 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano} é Bissexto!')
else:
    print(f'O ano {ano} não é Bissexto!')