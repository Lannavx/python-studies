'''Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. 
Caso esteja errado, peça a digitação novamente até ter um valor correto.'''

sexo = ''
while sexo != 'M' and sexo != 'F':
    sexo = input('Informe o seu sexo [M/F]: ').strip().upper()
    if sexo != 'M' and sexo != 'F':
        print('Informação inválida! Por favor, tente novamente!')
print('Dado registrado com sucesso!')

#Outra forma

sexo = str(input('Informe seu sexo [M/F]: ')).strip().upper()
while sexo not in 'MmFf':
    sexo = input('Informação inválida! Por favor, informe seu sexo: ').strip().upper()
print('Dado registrado com sucesso!')
