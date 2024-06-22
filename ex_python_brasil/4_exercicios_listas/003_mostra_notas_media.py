# Faça um Programa que leia 4 notas, mostre as notas e a média na tela.

# Inicializa uma lista vazia para armazenar as notas e define o número de notas a serem lidas
lista_notas = []
num_notas = 4

# Loop que coleta as notas do usuário e adiciona a nota inserida à lista
for nota in range(num_notas):
    notas = float(input(f'Informe a {nota + 1}ª nota: '))

    lista_notas.append(notas)

# Calcula a média das notas na lista
media = sum(lista_notas) / num_notas

# Exibe os resultados
print(f'\nAs notas são: {lista_notas}')
print(f'E a média é de {media:.2f}')