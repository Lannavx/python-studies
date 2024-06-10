''' Encontrar números primos é uma tarefa difícil. 
Faça um programa que gera uma lista dos números primos existentes entre 1 e um número inteiro informado pelo usuário.'''

while True:
    num = int(input('Informe um número para verificar todos os primos até ele: '))

    print(f'Os números primos entre 1 e {num} são: ')

    # Verifica cada número de 2 até 'num' para determinar se é primo
    numero_atual = 2
    while numero_atual <= num:
        primo = True  # Assume que o número é primo
        contador = 2

        # Verifica se o número é divisível por qualquer número menor que ele e maior que 1
        while contador <= numero_atual // 2:
            if numero_atual % contador == 0:
                primo = False
                break
            contador += 1

        if primo:
            print(numero_atual, end=' ')  # Imprime o número se for primo

        numero_atual += 1  # Incrementa para verificar o próximo número

    continuar = input('\nDeseja ver mais números? [S/N]: ').strip().lower()[0]
    if continuar != 's':
        break

print('Até breve!')
