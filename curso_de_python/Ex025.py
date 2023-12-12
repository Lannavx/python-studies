#Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

#Forma 1
nome = str(input('Informe seu nome completo: ')).lower()
condição = 'silva' in nome
print(f'Seu nome tem Silva? {condição}')

#Forma 2
nome = str(input('Informe seu nome completo: ')).strip()
condição = 'silva' in nome.lower() 
print(f'Seu nome tem Silva? {condição}')