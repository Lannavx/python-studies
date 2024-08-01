'''Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. 
Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual, 
e em que mês elas ocorreram (mostrar o mês por extenso: 1 - Janeiro, 2 - Fevereiro, . . . ).'''

from random import randint

MESES_ANO = 12

total_temperatura = 0

# Lista de listas que contém os nomes dos meses e uma temperatura inicializada em 0
meses = [ ['Janeiro', 0], ['Fevereiro', 0], ['Março', 0], ['Abril', 0], ['Maio', 0],
          ['Junho', 0], ['Julho', 0], ['Agosto', 0], ['Setembro', 0], ['Outubro', 0],
         ['Novembro', 0], ['Dezembro', 0]]


# Loop que percorre cada mês do ano e atribui uma temperatura aleatória ao segundo elemento de cada sublista
for i in range(MESES_ANO):
    meses[i][1] = (randint(0,40))
    
    # Acumula as temperaturas para calcular a média
    total_temperatura += meses[i][1]

media_temperatura = total_temperatura / MESES_ANO

print(f'A média anual de temperatura é de {media_temperatura:.2f}°C')

# Loop que verifica cada mês na lista e verifica se a temperatura do mês é maior que a média
print('\nTemperaturas acima da média anual: ')
for mes in meses:
    if mes[1] > media_temperatura:
        print(f'{mes[0]}: {mes[1]}°C')



