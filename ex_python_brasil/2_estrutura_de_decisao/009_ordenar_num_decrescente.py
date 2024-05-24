# Faça um Programa que leia três números e mostre-os em ordem decrescente.

numero_1 = int(input('Informe um número: '))
numero_2 = int(input('Informe mais um número: '))
numero_3 = int(input('Informe outro número: '))

# Cria uma lista com os números informados
lista_numeros = [numero_1, numero_2, numero_3]

# Ordena a lista em ordem decrescente com o parâmetro reverse=True
lista_numeros.sort(reverse=True)

print(lista_numeros)