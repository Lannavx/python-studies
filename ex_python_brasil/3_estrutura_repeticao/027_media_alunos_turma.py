''' Faça um programa que calcule o número médio de alunos por turma. 
Para isto, peça a quantidade de turmas e a quantidade de alunos para cada turma. As turmas não podem ter mais de 40 alunos.'''  

# Solicita ao usuário o número de turmas
turmas = int(input('Informe o número de turmas: '))

soma_alunos = 0

print('-' * 10)

for i in range(turmas):

    # Solicita a quantidade de alunos para cada turma
    quantidade_alunos = int(input(f'Informe os alunos da turma {i+1}: '))

    # Verifica se a quantidade de alunos excede o máximo permitido
    while quantidade_alunos > 40:
        print('Número de alunos por turma atingido! As turmas não podem ter mais de 40 alunos.')
        quantidade_alunos = int(input(f'Informe os alunos da turma {i+1} novamente: '))

    # Adiciona a quantidade válida de alunos à soma total
    soma_alunos += quantidade_alunos

# Calcula a média de alunos por turma
media = soma_alunos / turmas

print('-' * 10)

print(f'A média de alunos por turma é {media:.2f}')