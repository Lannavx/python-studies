''' Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar
se a média de idade da turma varia entre 0 e 25, 26 e 60, e maior que 60; 
e então, dizer se a turma é jovem, adulta ou idosa, conforme a média calculada.'''

# Solicita ao usuário o número de pessoas na turma
quantidade_pessoas = int(input('Informe quantas pessoas há na turma: '))

# Inicializa a soma das idades
soma_idade = 0

# Loop para coletar e somar as idades
for i in range(quantidade_pessoas):

    idade = int(input(f'Informe a idade da {i + 1}ª pessoa: '))
    soma_idade += idade  

# Calcula a média das idades
media = soma_idade / quantidade_pessoas

# Classifica a turma com base na média de idade
if 0 <= media <= 25:
    classificacao = "jovem"
elif 26 <= media <= 60:
    classificacao = "adulta"
else:
    classificacao = "idosa"

# Exibe a média e a classificação da turma
print(f'A média de idade é de {media:.2f}. Logo, a turma é {classificacao}.')

