'''Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. 
No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag)'''

flag = 999
soma = 0
total = 0
while True:
    num = int(input('Informe um número. Digite 999 para parar o programa: '))
    if num == flag:
        break
    total += 1
    soma += num
print(f'Foram digitados {total} números e a soma desses valores foi de {soma}')    
