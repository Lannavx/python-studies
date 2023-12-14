'''A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, 
de acordo com a idade:
- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JÚNIOR
- Até 25 anos: SÊNIOR
- Acima de 25 anos: MASTER'''

from datetime import date
ano = int(input('Informe o ano do seu nascimento: '))
data = date.today().year
idade = (data - ano)

if idade <= 9:
    print(f'Você tem {idade} anos, logo sua categoria é MIRIM')
elif idade <= 14:
    print(f'Você tem {idade} anos, logo sua categoria é INFANTIL')   
elif idade <= 19:
    print(f'Você tem {idade} anos, logo sua categoria é JUNIOR')     
elif idade <= 25:
    print(f'Você tem {idade} anos, logo sua categoria é SÊNIOR')
else:
    print(f'Você tem {idade} anos, logo sua categoria é MASTER')