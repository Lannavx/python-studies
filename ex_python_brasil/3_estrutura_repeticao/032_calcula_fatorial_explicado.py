'''Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. 
Ex.: 5!=5.4.3.2.1=120. A saída deve ser conforme o exemplo abaixo:
Fatorial de: 5
5! =  5 . 4 . 3 . 2 . 1 = 120'''

# Solicita um número inteiro ao usuário
num = int(input('Informe um número para ver o seu fatorial: '))

# Cabeçalho do fatorial
print(f'Fatorial de: {num}')
print(f'{num}! = ', end='')

# Inicializa a variável para armazenar o resultado do fatorial
resultado = 1

# Loop que itera de 'num' até 1 em ordem decrescente
for n in range(num, 0, -1):

    # Multiplica o resultado pelo número atual do loop para calcular o fatorial
    resultado *= n 
    
    # Imprime o número atual e prepara para o próximo, determinando o separador adequado
    print(n, end=' ')
    print('.' if n > 1 else ' = ', end=' ')

# Exibe o resultado final do fatorial
print(resultado)