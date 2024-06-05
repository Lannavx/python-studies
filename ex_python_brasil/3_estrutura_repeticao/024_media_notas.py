# Faça um programa que calcule o mostre a média aritmética de N notas.

# Solicita ao usuário o número de notas
quantidade_notas = int(input('Informe quantas notas você deseja calcular a média: '))

# Inicializa a soma das notas
soma_notas = 0

# Loop para coletar e somar as notas
for i in range(quantidade_notas):

    nota = float(input(f'Informe sua {i + 1}ª nota: '))
    soma_notas += nota  

# Calcula a média das notas
media = soma_notas / quantidade_notas

# Exibe a média aritmética
print(f'A média aritmética das notas é: {media:.2f}')
