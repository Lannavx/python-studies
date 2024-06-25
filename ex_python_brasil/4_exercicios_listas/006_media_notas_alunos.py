''' Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno, 
imprima o número de alunos com média maior ou igual a 7.0. '''

# Inicia as variáveis
num_notas = 4
num_alunos = 10
cont_aluno = 0

# Lista para armazenar a média de cada aluno
media_aluno = []

# Loop para processar cada um dos 10 alunos
for _ in range (num_alunos):
    nome_aluno = input('Informe o nome do aluno: ')
    notas = [] # Lista para armazenar as notas do aluno atual

    # Loop para coletar as quatro notas do aluno e adicionar na lista de notas
    for num in range(num_notas):
        nota_alunos = float(input(f'Informe a {num + 1}ª nota de {nome_aluno}: '))

        notas.append(nota_alunos)

    # Calcula a média das notas do aluno e armazena a média do aluno atual
    media = sum(notas) / num_notas
    media_aluno.append(media) 

    # Verifica se a média do aluno é maior ou igual a 7 e conta a quantidade de alunos que se aplica a essa condição
    if media >= 7:
        cont_aluno += 1


# Exibe o resultado
print(f'O número de alunos com média maior ou igual a 7.0 é de: {cont_aluno} alunos')            