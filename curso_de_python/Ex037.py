'''Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
 1 para binário, 2 para octal e 3 para hexadecimal.'''

numero = int(input('Informe um número qualquer: '))
print('''Escolha uma das bases para conversão:
[1] Conversão para Binário
[2] Conversão para Octal
[3] Conversão para Hexadecimal''')
opção = int(input('Digite a sua opção: '))
if opção == 1:
    print(f'{numero} convertido para Binário é igual a {bin(numero)[2:]}')
elif opção == 2:
    print(f'{numero} convertido para Octal é igual a {oct(numero)[2:]}')
elif opção == 3:
    print(f'{numero} convertido para Hexadecimal é igual a {hex(numero)[2:]}')
else: 
    print('Opção inválida! Tente novamente!')   