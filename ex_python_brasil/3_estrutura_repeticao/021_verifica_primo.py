''' Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. 
Um número primo é aquele que é divisível somente por ele mesmo e por 1.'''

continuar = 'S'

# Loop principal que continua enquanto o usuário desejar
while continuar == 'S':
    numero = int(input('Informe um número: '))

    # Assume inicialmente que o número é primo
    primo = True

    # Verifica se o número tem divisores além de 1 e ele mesmo
    for i in range(2, numero):        
        if numero % i == 0:
            # Se encontrar um divisor, define primo como False e sai do loop
            primo = False
            break

    # Após verificar todos os possíveis divisores, decide se o número é primo ou não        
    if primo:
        print(f'{numero} é primo!')
    else:
        print(f'{numero} não é primo!')

    continuar = input('Gostaria de ver mais números? [S/N]: ').strip().upper()[0]  

print('Até breve!')