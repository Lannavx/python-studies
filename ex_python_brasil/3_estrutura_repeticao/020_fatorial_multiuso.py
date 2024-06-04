''' Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial
várias vezes e limitando o fatorial a números inteiros positivos e menores que 16.'''

while True:
    num = int(input('Informe um número para ver o seu fatorial: '))

    # Inicializa o contador com o número inserido e o fatorial com 1
    cont = num
    fatorial = 1

    # Verifica se o número é positivo e menor que 16
    if 0 <= num <= 16:
        print(f'Calculando {num}! = ', end='')
        
        # Executa o loop enquanto o contador for maior que 0
        while cont > 0 :
            print(cont, end='')

            print('.' if cont > 1 else ' = ', end='')

            # Multiplica o fatorial pelo valor atual do contador e atualiza o fatorial
            fatorial *= cont
            # Dimninui o contador para realização do cálculo 
            cont -= 1
     
        # Resultado do cálculo
        print(fatorial)

    else:
        print('Número inválido! O número deve ser positivo e menor que 16.')  

