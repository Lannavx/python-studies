''' Foram anotadas as idades e alturas de 30 alunos. 
Faça um Programa que determine quantos alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos.'''

from random import randint

TOTAL_ALUNOS = 30

total_altura = 0
cont_aluno_abaixo_media = 0

# Lista para armazenar dados dos alunos
alunos = []

# Gera dados aleatórios para os alunos e adiciona um dicionário com altura e idade para cada aluno
for i in range(TOTAL_ALUNOS):
    alunos.append({
        'altura': randint(130,200),
        'idade': randint(10,18),
    })

    # Acumula a soma das alturas para cálculo da média
    total_altura += alunos[i]['altura']

media_altura = total_altura / TOTAL_ALUNOS

# Itera sobre a lista para contar alunos com mais de 13 anos e altura inferior à média
for aluno in alunos:
    if aluno['idade'] > 13 and aluno['altura'] < media_altura:
        cont_aluno_abaixo_media += 1

print(f'A média de altura dos 30 alunos é de {media_altura:.0f}')        
print(f'Há {cont_aluno_abaixo_media} alunos com mais de 13 anos que possuem uma altura inferior a média!')