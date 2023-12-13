'''Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem,
cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.'''

#Forma 1
distancia = float(input('Qual a distância da viagem em km? '))   
if distancia <= 200:
   preço = distancia * 0.50
   print(f'Sua viagem é {distancia}km, logo sua passagem custa R${preço:.2f}')
else:
   preço = distancia * 0.45
   print(f'Sua viagem é {distancia}km, logo sua passagem custa R${preço:.2f}')

#Forma 2   

distancia = float(input('Qual a distância da viagem em km? '))
print(f'Você está prestes a começar uma viagem de {distancia}km,')          
if distancia <= 200:
   preço = distancia * 0.50
else:
   preço = distancia * 0.45
print(f'E o preço da sua passagem será de R${preço:.2f}')

#Forma 3 - If simplificado

distancia = float(input('Qual a distância da viagem em km? '))
print(f'Você está prestes a começar uma viagem de {distancia}km,')          
preço = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print(f'E o preço da sua passagem será de R${preço:.2f}')