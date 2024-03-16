'''Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte. 
Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.'''

num_extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete',
               'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze',
               'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    num = int(input('Digite um número entre 0 e 20: '))

    while num > 20 or num < 0:
        num = int(input('Tente novamente! Digite um número entre 0 e 20: '))

    resposta = (num_extenso[num])
    print(f'Você digitou o número {resposta}')
    
    mais_num = input('Quer continuar? [S/N]: ').upper().strip()[0]
    
    while mais_num not in 'SN':
        print('Opção inválida! Digite S para Sim e N para Não.')
        mais_num = input('Quer continuar? [S/N]: ').upper().strip()[0]

    if mais_num == 'N':
        print('Até logo!')    
        break