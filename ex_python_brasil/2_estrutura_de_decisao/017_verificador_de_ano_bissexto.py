# Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto.

print('Ano Bissexto')
ano = int(input('Informe um ano para verificação: '))

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print('O ano informado é bissexto!')
else:
    print('O ano informado não é bissexto!')
