#Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

cont = 1
primeiro_termo = int(input('Informe o primeiro termo: '))
razao = int(input('Informe a razão da PA: '))
print(primeiro_termo, end = ' → ')
while cont < 10:
    primeiro_termo += razao
    print(f'{primeiro_termo} → ', end = '')
    cont += 1 
print('Fim')