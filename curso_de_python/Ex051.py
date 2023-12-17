#Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

#Forma 1

pa = 0
primeiro_termo = int(input('Informe o primeiro termo: '))
razao = int(input('Informe a razão da PA: '))
print(primeiro_termo, end = ' > ')
for c in range(1,10):
    pa += razao
    print(f'{pa + primeiro_termo}', end = ' > ')
print('Fim')    

#Forma do Professor

primeiro = int(input('Informe o primeiro termo: '))
razao = int(input('Informe a razão da PA: '))
decimo = primeiro + (10 -1) * razao
for c in range(primeiro, decimo + razao, razao):
    print(f'{c}', end = ' > ')
print('Acabou')