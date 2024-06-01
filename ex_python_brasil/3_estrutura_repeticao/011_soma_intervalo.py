# Altere o programa anterior para mostrar no final a soma dos números.

num_um = int(input('Informe um número: '))
num_dois = int(input('Informe outro número: '))

# Ajusta os valores de início e fim para excluir os números inseridos e mostrar apenas o intervalo
inicio = min(num_um, num_dois) + 1
fim = max(num_um, num_dois) - 1

# Inicializa a soma
soma = 0  

# Verifica se existe algum número no intervalo para imprimir
if inicio <= fim:
    print('-' * 30)
    print(f'O intervalo de números entre {num_um} e {num_dois} é: ')

    # Usa o laço for para imprimir diretamente cada número no intervalo e realizar a soma
    for numeros in range(inicio, fim + 1):
        print(numeros, end='')
        print(' - ' if numeros != fim else '', end='')
        soma += numeros
        
    print('\nE a soma desses números é de:',soma)

else:
    print('Não há números no intervalo entre os valores inseridos.')