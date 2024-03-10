'''Faça um programa que jogue par ou ímpar com o computador. 
O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.'''

from random import randint
from time import sleep
vitorias = 0
print('-' * 25)
print('Vamos jogar Par ou Ímpar!')
print('-' * 25)
while True:
    valor_usuario = int(input('Informe um número: '))
    jogo = input('Par ou  Ímpar? [P/I]: ').strip().upper()
    while jogo not in 'PI':
        print('Opção inválida. Escolha P para Par ou I para Ímpar.')
        jogo = input('Par ou Ímpar? [P/I]: ').strip().upper()
    valor_computador = randint(0,11)
    total = valor_usuario + valor_computador
    print(f'Você jogou {valor_usuario} e o computador {valor_computador}. Total de {total}. ', end= '')
    print('DEU PAR' if total % 2 == 0 else 'DEU IMPAR')
    sleep(1)
    if jogo == 'P':
        if total % 2 == 0:
            print('Você venceu!')
            vitorias += 1    
        else:
            print('Você perdeu!')
            break
    if jogo == 'I':
        if total % 2 == 1:    
            print('Você venceu!')
            vitorias += 1    
        else:
            print('Você perdeu!')
            break
    sleep(1)    
    print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {vitorias} vezes')            