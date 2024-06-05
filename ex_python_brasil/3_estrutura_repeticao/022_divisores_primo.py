# Altere o programa de cálculo dos números primos, informando, caso o número não seja primo, por quais números ele é divisível.

continuar = 'S'

# Loop principal que continua enquanto o usuário desejar
while continuar == 'S':
    numero = int(input('Informe um número: '))

    # Assume inicialmente que o número é primo
    primo = True

    # Lista para armazenar os divisores do número, caso não seja primo
    divisores = []

    # Verifica se o número tem divisores além de 1 e ele mesmo
    for i in range(2, numero):        
        if numero % i == 0:
            # Se encontrar um divisor, adiciona à lista de divisores
            divisores.append(i)
            primo = False
            
    # Após verificar todos os possíveis divisores, decide se o número é primo ou não        
    if primo and numero != 1:  # Garante que o número 1 não seja considerado primo
        print(f'{numero} é primo!')
    elif numero == 1:
        print('1 não é primo por definição.')
    else:
        print(f'{numero} não é primo e é divisível por {divisores}.')
        

    continuar = input('Gostaria de ver mais números? [S/N]: ').strip().upper()[0]  

print('Até breve!')