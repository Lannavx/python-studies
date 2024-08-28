'''Jogo de Forca. Desenvolva um jogo da forca. O programa terá uma lista de palavras lidas de um arquivo texto e escolherá uma aleatoriamente. 
O jogador poderá errar 6 vezes antes de ser enforcado.

Digite uma letra: A
-> Você errou pela 1ª vez. Tente de novo!

Digite uma letra: O
A palavra é: _ _ _ _ O

Digite uma letra: E
A palavra é: _ E _ _ O

Digite uma letra: S
-> Você errou pela 2ª vez. Tente de novo!'''

import random

# Inicia variaveis e listas
palavras_lista = []
contador = 0
palavra_formada = []

def separar_palavras_arquivo(linhas):
    '''Separa as palavras de cada linha lida do arquivo e as adiciona à lista de palavras'''
    for linha in linhas:
        palavras = linha.strip().split()
        for palavra in palavras:
            palavras_lista.append(palavra)

def criar_lacunas():
    '''Cria lacunas (underscores) representando as letras da palavra'''
    for _ in palavra_escolhida:
        palavra_formada.append('_')            

def substituir_lacuna_por_letra(letra):
    '''Substitui uma lacuna (underscores) por uma letra correta na posição adequada'''
    for i, letra_secreta in enumerate(palavra_escolhida):
        if letra == letra_secreta:
            palavra_formada[i] = letra

# Lê o arquivo e separa as palavras
with open('ex_python_brasil/6_exercicios_strings/011_palavras_jogo_forca.txt', 'r') as arquivo:
    linhas = arquivo.readlines()
    separar_palavras_arquivo(linhas)

# Escolhe aleatoriamente uma palavra para o jogo
palavra_escolhida = random.choice(palavras_lista)

criar_lacunas()

# Loop principal do jogo
while True:
    
    # Solicita uma letra ao usuário
    letra = input('\nDigite uma letra: ').upper()

    # Se a letra informada estiver na palavra escolhida, substitui a lacuna por ela e mostra o estado atual da palavra formada
    if letra in palavra_escolhida:
        substituir_lacuna_por_letra(letra)
        print(f'A palavra é: {''.join(palavra_formada)}')

        # Verifica se o jogador completou a palavra e venceu o jogo
        if ''.join(palavra_formada) == palavra_escolhida:
            print('Parabéns, você acertou!')
            break

    # Se a letra não estiver na palavra, incrementa o contador de erros e verifica se o jogador já perdeu       
    else:
        contador += 1
        if contador == 6: 
            print(f'Você errou pela {contador}ª vez e foi enforcado!')
            print('Fim do jogo!') 
            print(f'A palavra era {palavra_escolhida}!')
            break      
        else:
            print(f'Você errou pela {contador}ª vez. Tente de novo!')
