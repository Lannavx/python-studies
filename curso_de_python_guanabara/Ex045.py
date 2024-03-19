#Crie um programa que faça o computador jogar Jokenpô com você.

from random import randint
lista_jogo = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)
print('''Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
jogador = int(input('Sua jogada: '))
print('-='*12)
print(f'O computador jogou {lista_jogo[computador]}')
print(f'Você jogou {lista_jogo[jogador]}')
print('-='*12)
if jogador == 0 and computador == 2:
    print('Pedra ganha de Tesoura! Você ganhou!')
elif jogador == 0 and computador== 1:
    print('Pedra perde de Papel! Você perdeu!')    
elif jogador == 0 and computador == 0:
    print('Empate!') 
elif jogador == 1 and computador == 2:
    print('Papel perde de Tesoura! Você perdeu!')     
elif jogador == 1 and computador == 1:
    print('Empate!')  
elif jogador == 1 and computador == 0:
    print('Papel ganha de Pedra! Você ganhou!')  
elif jogador == 2 and computador == 2:
    print('Empate!')     
elif jogador == 2 and computador == 1:
    print('Tesoura ganha de Papel! Você ganhou!')
elif jogador == 2 and computador == 0:
    print('Tesoura perde de Pedra! Você perdeu')  
