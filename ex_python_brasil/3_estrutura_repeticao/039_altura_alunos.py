'''Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o 
número do aluno e o segundo representando a sua altura em centímetros. 
Encontre o aluno mais alto e o mais baixo. 
Mostre o número do aluno mais alto e o número do aluno mais baixo, junto com suas alturas.'''

# Inicia as variáveis
aluno_mais_alto = 0
aluno_mais_baixo = float('inf')
num_aluno_mais_alto = num_aluno_mais_baixo = 0

# Loop para entrada de dados
for i in range(10):
    numero_aluno = int(input(f'Informe o número do {i + 1}º aluno: '))
    altura = float(input('Informe a altura do aluno: '))

    # Verifica se a altura atual é a maior registrada e atualiza o número do aluno
    if altura > aluno_mais_alto:
        aluno_mais_alto = altura
        num_aluno_mais_alto = numero_aluno

    # Verifica se a altura atual é a menor registrada e atualiza o número do aluno    
    if altura < aluno_mais_baixo:
        aluno_mais_baixo = altura
        num_aluno_mais_baixo = numero_aluno     

# Exibe os resultados
print(f'O número do aluno mais alto é {num_aluno_mais_alto} e sua altura é de {aluno_mais_alto:.2f} cm')    
print(f'O número do aluno mais baixo é {num_aluno_mais_baixo} e sua altura é de {aluno_mais_baixo:.2f} cm')    