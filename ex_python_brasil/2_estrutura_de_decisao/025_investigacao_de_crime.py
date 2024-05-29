'''Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. 

As perguntas são:
    a. "Telefonou para a vítima?"
    b. "Esteve no local do crime?"
    c. "Mora perto da vítima?"
    d. "Devia para a vítima?"
    e. "Já trabalhou com a vítima?" 

O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". 
Caso contrário, ele será classificado como "Inocente".'''

from time import sleep

print('''
Você está sendo investigado pelo assassinato da Sra.Penelope e iremos
lhe fazer 5 perguntas e você deve responder com sinceridade!
Nós saberemos se você estiver mentindo...''')

print('-' * 40)

print('Interrogátorio:')

cont_sim = 0

pergunta_1 = input('Telefonou para a vítima?: ').strip().upper()[0]
if pergunta_1 == 'S':
    cont_sim += 1
elif pergunta_1 != 'N':
    print('Resposta inválida! Responda com sim ou não.')
    exit()

pergunta_2 = input('Esteve no local do crime?: ').strip().upper()[0]
if pergunta_2 == 'S':
    cont_sim += 1
elif pergunta_2 != 'N':
    print('Resposta inválida! Responda com sim ou não.')
    exit()

pergunta_3 = input('Mora perto da vítima?: ').strip().upper()[0]
if pergunta_3 == 'S':
    cont_sim += 1
elif pergunta_3 != 'N':
    print('Resposta inválida! Responda com sim ou não.')
    exit()

pergunta_4 = input('Devia para a vítima?: ').strip().upper()[0]
if pergunta_4 == 'S':
    cont_sim += 1
elif pergunta_4 != 'N':
    print('Resposta inválida! Responda com sim ou não.')
    exit()

pergunta_5 = input('Já trabalhou com a vítima?: ').strip().upper()[0]
if pergunta_5 == 'S':
    cont_sim += 1
elif pergunta_5 != 'N':
    print('Resposta inválida! Responda com sim ou não.')[0]
    exit()

print('-' * 40)
print('Após analise de suas respostas concluimos que...')
sleep(2)

if cont_sim == 5:
    print('Você é o Assassino e está preso!')
elif 3 <= cont_sim <= 4:
    print('Você é o Cúmplice e está preso!')
elif cont_sim == 2:
    print('Você é Suspeito! Estamos de olho em você...')
else:
    print('Você é Inocente...Está liberado. ')