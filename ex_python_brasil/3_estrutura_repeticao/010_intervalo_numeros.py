# Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.

num_um = int(input('Informe um número: '))
num_dois = int(input('Informe outro número: '))

# Ajusta os valores de início e fim para excluir os números inseridos e mostrar apenas o intervalo
inicio = min(num_um, num_dois) + 1
fim = max(num_um, num_dois) - 1

# Verifica se existe algum número no intervalo para imprimir
if inicio <= fim:
    print('-' * 30)
    print(f'O intervalo de números entre {num_um} e {num_dois} é: ')

    # Usa o laço for para imprimir diretamente cada número no intervalo
    for numeros in range(inicio, fim + 1):
        print(numeros, end='')
        print(' - ' if numeros != fim else '.', end='')
else:
    print("Não há números no intervalo entre os valores inseridos.")

