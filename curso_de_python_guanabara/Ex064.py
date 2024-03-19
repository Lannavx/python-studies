'''Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. 
No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).'''


numero = 0
flag = 999
total = 0
soma = 0
while numero != flag:
    numero = int(input('Digite um número qualquer. Ao digitar 999 o programa irá parar: '))
    total += 1
    soma += numero
print(f'Ao todo foram mostrados {total - 1} números e a soma entre eles é de {soma - flag}')

#Outra forma

numero = 0
flag = 999
total = 0
soma = 0
numero = int(input('Digite um número qualquer. Ao digitar 999 o programa irá parar: '))
while numero != flag:
    total += 1
    soma += numero
    numero = int(input('Digite um número qualquer. Ao digitar 999 o programa irá parar: '))
print(f'Ao todo foram mostrados {total} números e a soma entre eles é de {soma}')




