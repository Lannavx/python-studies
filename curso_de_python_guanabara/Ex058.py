'''Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. 
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.'''


palpite = 1
from random import randint    
print('Ei, vamos jogar um jogo! Vou pensar em um número entre 0 e 10 e você precisa adinvinhar qual é!')
print('Valendoo!')
numero_secreto = randint(0,10)
numero_usuario = int(input('Informe o seu palpite: '))
while numero_usuario != numero_secreto:
    numero_usuario = int(input('Você errou! Tente novamente: '))
    palpite += 1
print(f'Parabéns, você acertou! Foram necessárias {palpite} tentativas!')

#Outra forma

from random import randint    
print('Ei, vamos jogar um jogo! Vou pensar em um número entre 0 e 10 e você precisa adinvinhar qual é!')
print('Valendoo!')
numero_secreto = randint(0,10)
acertou = False
palpite = 0
while not acertou:
    numero_usuario = int(input('Informe o seu palpite: '))
    palpite += 1
    if numero_usuario == numero_secreto:
        acertou = True
    else:
        if numero_usuario < numero_secreto:
            print('Mais...tente novamente!')
        elif numero_usuario > numero_secreto:
            print('Menos...tente novamente!')   
print(f'Parabéns, você acertou! Foram necessárias {palpite} tentativas!')