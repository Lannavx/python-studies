# Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120

num = int(input('Informe um número para ver o seu fatorial: '))

# Inicializa o contador com o número inserido e o fatorial com 1
cont = num
fatorial = 1

print(f'Calculando {num}! = ', end='')

# Executa o loop enquanto o contador for maior que 0
while cont > 0 :
    print(cont, end='')

    print('.' if cont > 1 else ' = ', end='')

    # Multiplica o fatorial pelo valor atual do contador e atualiza o fatorial
    fatorial *= cont
    # Dimninui o contador para realização do cálculo 
    cont -= 1

print(fatorial)

