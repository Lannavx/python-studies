'''Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de código. Os códigos utilizados são:
1 , 2, 3, 4  - Votos para os respectivos candidatos 
(você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
5 - Voto Nulo
6 - Voto em Branco
Faça um programa que calcule e mostre:
O total de votos para cada candidato;
O total de votos nulos;
O total de votos em branco;
A percentagem de votos nulos sobre o total de votos;
A percentagem de votos em branco sobre o total de votos. 
Para finalizar o conjunto de votos tem-se o valor zero.'''

# Inicializa as variáveis para armazenar a quantidade de votos
cont = 0
cont_votos_total = cont_votos_nulos = cont_votos_branco =  0

# Inicializa um dicionário para armazenar os candidatos e suas contagens de votos
candidatos = {1: ['Lucia', 0], 2: ['Maria', 0], 3: ['Eduarda', 0], 4: ['Ana', 0], 5: ['Voto Nulo', 0], 6: ['Voto em Branco', 0]}

# Imprime instruções e abre a votação
print('-' * 10)
print('Votação aberta!')
print('Caro eleitor, dê o seu voto!')
print('''
1 - Lucia
2 - Maria
3 - Eduarda
4 - Ana
5 - Voto Nulo
6 - Voto em Branco                    
''')

# Loop para processar os votos
while True:
    cont += 1
    voto = int(input(f'Eleitor {cont}, informe seu voto (ou 0 para sair): '))

    # Encerra a votação se o eleitor digitar 0
    if voto == 0:
        break       
    
    # Verifica se o voto é válido 
    while voto not in candidatos:
        print('Voto desconsiderado! Por favor, vote nos número correspondente a sua opção.') 
        voto = int(input(f'Eleitor {cont}, informe seu voto: '))

    # Incrementa a contagem de votos para a opção escolhida
    candidatos[voto][1] += 1

    print('Voto computado, obrigada!')

    # Contador total de votos válidos
    cont_votos_total += 1

    # Contabiliza votos nulos e votos em branco
    if voto == 5:
        cont_votos_nulos += 1

    if voto == 6:
        cont_votos_branco += 1     

print('-' * 10)

# Calcula a porcentagem de votos nulos e brancos sobre o total
porcentagem_nulo = (cont_votos_nulos / cont_votos_total) * 100    
porcentagem_branco = (cont_votos_branco / cont_votos_total) * 100 

# Imprime a contagem final de votos para cada opção escolhida e as porcentagens
print('Contagem de votos:')
for chave, valor in candidatos.items():
    print(f'{valor[0]} recebeu {valor[1]} votos!')

print(f'A porcentagem de votos nulos sobre o total de votos é de {porcentagem_nulo:.2f}%')
print(f'A porcentagem de votos em branco sobre o total de votos é de {porcentagem_branco:.2f}%')