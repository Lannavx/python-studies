'''Desenvolva um programa para verificar a nota do aluno em uma prova com 10 questões, 
o programa deve perguntar ao aluno a resposta de cada questão e ao final comparar com o 
gabarito da prova e assim calcular o total de acertos e a nota (atribuir 1 ponto por resposta certa). 
Após cada aluno utilizar o sistema deve ser feita uma pergunta se outro aluno vai utilizar o sistema. 
Após todos os alunos terem respondido informar:
Maior e Menor Acerto;
Total de Alunos que utilizaram o sistema;
A Média das Notas da Turma.
Gabarito da Prova:

01 - A
02 - B
03 - C
04 - D
05 - E
06 - E
07 - D
08 - C
09 - B
10 - A

Após concluir isto você poderia incrementar o programa permitindo que o professor digite o 
gabarito da prova antes dos alunos usarem o programa.'''

QUESTOES = 10

# Permite que o professor entre com o gabarito através de um dicionário
gabarito = {}
print('Professor, por favor, insira o gabarito das questões:')
for num in range(1, QUESTOES + 1):
    gabarito[num] = input(f'Resposta para a questão {num}: ').upper()

print()

# Variáveis para controle de notas e alunos
cont_alunos = 0
acertos_por_aluno = []

# Loop principal que permite a entrada dos alunos e coleta suas respostas
while True:
    nome_aluno = input('Aluno, informe seu nome: ')

    # Reset das variáveis para o novo aluno
    cont_acertos = 0  
    lista_respostas = []  

    # Loop que solicita as respostas do aluno para cada questão
    for i in range(QUESTOES):
        numero = i + 1
        resposta = input(f'Informe a resposta da pergunta {numero}: ').strip().upper()
        lista_respostas.append([numero, resposta])

    # Verifica cada resposta do aluno comparando com o gabarito
    for numero, resposta in lista_respostas:
        if resposta == gabarito[numero]:
            cont_acertos += 1

    # Guarda acertos do aluno atual
    acertos_por_aluno.append(cont_acertos)  
    cont_alunos += 1

    # Condição para saída da loop
    continuar = input('Outro aluno irá responder as questões? [S/N]: ').strip().upper()[0]
    if continuar == 'N':
        break

# Cálculos
max_acertos = max(acertos_por_aluno)
min_acertos = min(acertos_por_aluno)
media_acertos = sum(acertos_por_aluno) / cont_alunos

# Exibe os resultados
print()  
print(f'Maior número de acertos: {max_acertos}')
print(f'Menor número de acertos: {min_acertos}')
print(f'Total de alunos: {cont_alunos}')
print(f'Média de acertos da turma: {media_acertos:.2f}')


    


