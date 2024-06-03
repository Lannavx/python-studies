# Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.

# Solicita ao usuário o número de elementos a serem gerados
quantidade_numeros = int(input('Quantos números você deseja gerar? '))

# Inicializa uma lista vazia para armazenar os números
numeros = []

# Loop para solicitação de números ao usuário
for i in range(quantidade_numeros):
    while True:  # Loop infinito que só quebra quando um número válido é inserido
        numero = int(input(f'Digite o número {i + 1}: '))

        # Verifica se o número está dentro do intervalo permitido
        if 0 <= numero <= 1000:  
            numeros.append(numero)
            break  # Sai do loop interno se o número for válido
        
        print('Número inválido! O número deve estar entre 0 e 1000.')

# Calcula o menor, o maior valor e a soma dos números na lista
menor_valor = min(numeros)
maior_valor = max(numeros)
soma = sum(numeros)

print(f'Conjunto de números: {numeros}')
print(f'''O menor valor é: {menor_valor}
O maior valor é: {maior_valor}
E a soma de todos os valores é: {soma}''') 



