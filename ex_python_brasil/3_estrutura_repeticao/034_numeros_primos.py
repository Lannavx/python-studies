'''Os números primos possuem várias aplicações dentro da Computação, por exemplo na Criptografia. 
Um número primo é aquele que é divisível apenas por um e por ele mesmo. 
Faça um programa que peça um número inteiro e determine se ele é ou não um número primo.'''

continuar = 's'

while continuar == 's':

    num = int(input('Informe um número inteiro: '))

    # Inicializa o contador e a flag que indica se o número é primo
    contador = 2
    primo = True

    # Um número deve ser maior que 1 para ser primo
    if num <= 1:
        primo = False
    else:
        # Loop para testar se num é divisível por algum número entre 2 e num-1
        while contador <= num // 2:
            if num % contador == 0:
                primo = False
                break
            contador += 1

    # Exibe o resultado
    if primo:
        print(f'{num} é um número primo.')
    else:
        print(f'{num} não é um número primo.')        

    continuar = input('Deseja ver mais números? [S/N]: ').strip().lower()[0]

print('Até breve!')