#Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

#Forma 1
nome = str(input('Informe seu nome completo: ')).lower()
condicao = 'silva' in nome
print(f'Seu nome tem Silva? {condicao}')

#Forma 2
nome = str(input('Informe seu nome completo: ')).strip()
condicao = 'silva' in nome.lower() 
print(f'Seu nome tem Silva? {condicao}')