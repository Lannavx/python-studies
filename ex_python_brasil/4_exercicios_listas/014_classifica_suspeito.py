'''Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. 
As perguntas são:
a. "Telefonou para a vítima?"
b. "Esteve no local do crime?"
c. "Mora perto da vítima?"
d. "Devia para a vítima?"
e. "Já trabalhou com a vítima?" 
O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", 
entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".'''

perguntas = [
    'Telefonou para a vítima?',
    'Esteve no local do crime?',
    'Mora perto da vítima?',
    'Devia para a vítima?',
    'Já trabalhou com a vítima?'
]

print('Investigação sobre Crime')
print('-' * 30)

respostas_positivas = 0

# Itera sobre a lista de perguntas, fazendo cada uma ao usuário
for pergunta in perguntas: 
    print(pergunta)
    resposta = input('Informe sua resposta: ').strip().lower()[0]
    print()

    # Garante que a resposta seja válida
    while resposta not in ['s', 'n']:
        print('\nPor favor, responda com sim ou não!\n')
        print(pergunta)
        resposta = input('Informe sua resposta novamente: ').strip().lower()[0]
        print()
    
    # Conta a resposta como positiva se a resposta for "sim"
    if resposta == 's':
        respostas_positivas += 1

print('\nComputando dados...\n')

# Avalia as respostas
if respostas_positivas == 5:
    print('Você é o assassino!')
elif respostas_positivas >= 3:
    print('Você é cúmplice!')
elif respostas_positivas == 2:
    print('Você é suspeito!')
else:
    print('Você é inocente!')
