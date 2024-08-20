'''Jogo de Craps. 
Faça um programa que implemente um jogo de Craps. 
O jogador lança um par de dados, obtendo um valor entre 2 e 12. 
Se, na primeira jogada, você tirar 7 ou 11, você um "natural" e ganhou. 
Se você tirar 2, 3 ou 12 na primeira jogada, isto é chamado de "craps" e você perdeu. 
Se, na primeira jogada, você fez um 4, 5, 6, 8, 9 ou 10,este é seu "Ponto". 
Seu objetivo agora é continuar jogando os dados até tirar este número novamente. 
Você perde, no entanto, se tirar um 7 antes de tirar este Ponto novamente.'''

from random import randint

# Constantes com as regras do jogo
LISTA_CRAPS = [2,3,12]
LISTA_PONTO = [4,5,6,8,9,10]
LISTA_NATURAL_OU_PERDE = [7,11]

# Inicia a rodada do jogo
rodada = 1

def lancar_dado():
    '''Lança o dado com números entre 2 e 12 '''
    numero = randint(2, 12)
    print(f'Número: {numero}')
    return numero

def verificar_pontuacao(numero_tirado=int):
    '''Verifica a pontuação do jogo, fornecendo informações por rodada'''

    # Verificações da primeira rodada
    if rodada == 1: 
        if numero_tirado in LISTA_CRAPS:
            print('Você perdeu!')
            return 0
        elif numero_tirado in LISTA_NATURAL_OU_PERDE:
            print('Você é um Natural e ganhou o jogo!')
            return 0

    # Verificações após a primeira rodada
    if numero_tirado in LISTA_CRAPS:
        print('Nada aconteceu, próxima rodada!')

    if numero_tirado in LISTA_PONTO:
        print('Ponto!')

    if numero_tirado in LISTA_NATURAL_OU_PERDE:
        print('Você perdeu!')
        return 0

# Loop principal do jogo que controla a sequência de jogadas
jogar_dado = 1
while jogar_dado != 0:
    jogar_dado = int(input('Você está jogando Craps! Para rolar os dados, digite "1", para sair digite "0": '))

    if jogar_dado == 1:
        numero_tirado = lancar_dado()
        jogar_dado = verificar_pontuacao(numero_tirado)

        rodada += 1
