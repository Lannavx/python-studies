# Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares.

# Contadores para números pares e ímpares
cont_par = 0
cont_impar = 0

print('Informe um número por vez até que tenhamos 10 números!')
for i in range(1, 11):
    numero = int(input(f'Informe o {i}º número: '))

    # Verifica se o número é par e incrementa o contador correspondente
    if numero % 2 == 0:
        cont_par += 1
    else:
        cont_impar += 1

print(f'A quantidade de números pares é de {cont_par} e a quantidade de números impares é de {cont_impar}.')   