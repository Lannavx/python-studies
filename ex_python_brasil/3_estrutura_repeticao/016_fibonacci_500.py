# A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,... Faça um programa que gere a série até que o valor seja maior que 500.

# Inicializa os dois primeiros termos da sequência de Fibonacci
termo1, termo2 = 0, 1

print('Sequência de Fibonacci:')

# Exibe o primeiro termo
print(termo1, end=' ')

# Laço while para gerar termos da sequência de Fibonacci até que exceda 500
while termo2 <= 500:
    print(termo2, end=' ')

    # Atualiza as variáveis para o próximo termo
    termo3 = termo1 + termo2
    termo1 = termo2
    termo2 = termo3

