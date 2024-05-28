'''Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e
depois informar quantas notas de cada valor serão fornecidas. 

As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. 
O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina.
a. Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
b. Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, 
quatro notas de 10, uma nota de 5 e quatro notas de 1.'''

valor = int(input('Informe o valor para saque: R$'))

cont_1 = 0
cont_5 = 0
cont_10 = 0
cont_50 = 0
cont_100 = 0

if 10 <= valor <= 600:
    # Enquanto o valor for maior que 0, distribui as notas de acordo com o valor disponível
    while valor > 0:
        if valor >= 100:
            valor -= 100
            cont_100 += 1
        elif valor >= 50:
            valor -= 50   
            cont_50 += 1 
        elif valor >= 10:
            valor -= 10
            cont_10 += 1
        elif valor >= 5:
            valor -= 5
            cont_5 += 1
        elif valor >= 1:
            valor -= 1
            cont_1 += 1
    print('=' * 25)
    print(f'Retire na boca do caixa: ')

else:
    print('Número fora do intervalo permitido. O valor mínimo é de 10 reais e o máximo de 600 reai')

# Imprime a quantidade de notas de cada valor, se houver
if cont_100 > 0:
    print(f'{cont_100} notas de 100')
if cont_50 > 0:
    print(f'{cont_50} notas de 50')
if cont_10 > 0:
    print(f'{cont_10} notas de 10') 
if cont_5 > 0:
    print(f'{cont_5} notas de 5')
if cont_1 > 0:
    print(f'{cont_1} notas de 1')               

