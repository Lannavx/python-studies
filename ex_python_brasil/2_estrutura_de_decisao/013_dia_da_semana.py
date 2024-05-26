''' Faça um Programa que leia um número e exiba o dia correspondente da semana.
(1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.'''

numero_semana = int(input('Informe um número para exibir o dia da semana correspondente (1-Domingo, 2-Segunda, etc.): '))

if numero_semana == 1:
    print('Domingo')
elif numero_semana == 2:
    print('Segunda-feira')
elif numero_semana == 3:
    print('Terça-feira')
elif numero_semana == 4:
    print('Quarta-feira')    
elif numero_semana == 5:
    print('Quinta-feira')
elif numero_semana == 6:
    print('Sexta-feira')
elif numero_semana == 7:
    print('Sábado')
else:
    print('Valor inválido! Digite um número entre e 1 e 7.')    
       