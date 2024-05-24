'''
Faça um Programa que verifique se uma letra digitada é "F" ou "M". 
Conforme a letra, escreva: F - Feminino, M - Masculino, Sexo Inválido.
'''

sexo = input('Informe seu sexo [F/M]: ').upper().strip()

if sexo == 'F':
    print('F - Feminino')
elif sexo == 'M':
    print('M - Masculino')    
else:
    print('Sexo inválido!')    