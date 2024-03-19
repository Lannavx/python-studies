'''Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. 
O programa encerrará quando ele disser que quer mostrar 0 termos.'''

cont = 1
primeiro_termo = int(input('Informe o primeiro termo: '))
razao = int(input('Informe a razão da PA: '))
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print(f'{primeiro_termo} → ', end = '')
        primeiro_termo += razao
        cont += 1 
    print('Pausa')
    mais = int(input('Informe quantos termos você quer mostrar a mais: '))
print(f'Progressão finalizada com {total} termos mostrados')   
