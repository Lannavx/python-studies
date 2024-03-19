'''Crie um programa que leia o nome completo de uma pessoa e mostre: 
- O nome com todas as letras maiúsculas e minúsculas.
- Quantas letras ao todo (sem considerar espaços).
- Quantas letras tem o primeiro nome.'''

nome = input('Qual o seu nome: ')
print(nome.upper())
print(nome.lower())
letras = nome.split()
print(f'Seu nome tem o total de: {len(''.join(letras))} letras')
print(f'O seu primeiro nome tem {len(letras[0])} letras')

#Outra forma de fazer

nome = str((input('Digite seu nome completo: '))).strip()
print('Analisando seu nome...')
print(f'Seu nome em maiúsculas é {nome.upper()}')
print(f'Seu nome em minúsculas é {nome.lower()}')
print(f'Seu nome tem ao todo {len(nome)-nome.count(' ')}')
print(f'Seu primeiro nome tem {nome.find(' ')} letras')
