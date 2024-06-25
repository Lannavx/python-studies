'''Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor. 
Imprima a idade e a altura na ordem inversa a ordem lida.'''

# Inicializa as variáveis
lista_idade = []
lista_altura = []
num_pessaos = 5

# Loop para coletar informações de 5 pessoas
for num in range(num_pessaos):
    idade = int(input(f'Por favor, informe a idade da {num + 1}ª pessoa: '))
    altura = float(input('Informe agora, a altura dela: '))

    # Adiciona a idade e altura coletadas às respectivas listas
    lista_idade.append(idade)
    lista_altura.append(altura)
    
print('-' * 10)

# Exibe as listas na ordem em que as informações foram inseridas
print('Ordem Lida:')
print(f'Idade: {lista_idade}')
print(f'Altura: {lista_altura}')    

# Inverte as listas 
lista_idade.reverse()
lista_altura.reverse()
print()

# Exibe as listas na ordem inversa
print('Ordem Inversa:')
print(f'Idade: {lista_idade}')
print(f'Altura: {lista_altura}')    