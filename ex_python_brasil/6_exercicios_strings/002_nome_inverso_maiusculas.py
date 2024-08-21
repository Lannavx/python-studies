'''Nome ao contrário em maiúsculas. 
Faça um programa que permita ao usuário digitar o seu nome e em seguida mostre o nome do usuário de 
trás para frente utilizando somente letras maiúsculas. 
Dica: lembre−se que ao informar o nome o usuário pode digitar letras maiúsculas ou minúsculas.'''

# Solicita ao usuário que digite um nome
nome = input('Digite seu nome: ').strip().upper()

# Inverte o nome
nome_invertido = nome[::-1]

# Exibe o resultado
print(f'Seu nome de trás para frente é: {nome_invertido}')
