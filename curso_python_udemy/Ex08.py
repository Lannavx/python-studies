# Exercício - Jogo da palavra secreta

'''Faça um jogo para o usuário adivinhar qual a palavra secreta.
- Você vai propor uma palavra secreta qualquer e vai dar a possibilidade para o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você vai conferir se a letra digitada está na palavra secreta.
    - Se a letra digitada estiver na palavra secreta; exiba a letra;
    - Se a letra digitada não estiver na palavra secreta; exiba *.
Faça a contagem de tentativas do seu usuário.'''

import os

palavra_secreta = 'dados'
letras_acertadas = ''     # Inicializa uma string vazia para armazenar as letras corretas que o usuário adivinhar
tentativas = 0            # Contador de tentativas do usuário

print('Tente acertar a palavra secreta!')

while True:

    letra_digitada = input('Digite uma letra: ')
    tentativas += 1          # Incrementa o contador de tentativas a cada rodada

    if len(letra_digitada) > 1:
        print('Digite apenas uma letra!')
        continue

    # Verifica se a letra digitada faz parte da palavra secreta e atualiza a lista de acertos
    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada  
    
    # Representa a palavra sendo adivinhada, mostrando letras acertadas e '*' para as demais
    palavra_formada = ''     
    for letra_secreta in palavra_secreta:        
        if letra_secreta in letras_acertadas:     
            palavra_formada += letra_secreta      
        else:
            palavra_formada += '*'                
    
    print('Palavra formada:', palavra_formada)

    if palavra_formada == palavra_secreta:
        os.system('cls')   # Limpa a tela; pode precisar de ajuste dependendo do SO
        print('Parabéns, você acertou!')
        print('A palavra secreta era', palavra_secreta )
        print('Tentativas:', tentativas)

        # Reinicia as variáveis para um novo jogo
        letras_acertadas = ''
        tentativas = 0