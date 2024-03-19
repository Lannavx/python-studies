'''Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. 

Ex: 0 - 1 - 1 - 2 - 3 - 5 - 8'''


print('-' * 30)
print('Sequência de Fibonacci')
print('-' * 30)
n = int(input('Informe quantos termos você quer mostrar: '))

# Inicializa os dois primeiros termos da Sequência de Fibonacci
t1 = 0
t2 = 1
print(f'{t1} → {t2}', end = '')

# Loop para calcular e exibir os termos restantes da sequência
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(f' → {t3}', end = '')
    t1 = t2
    t2 = t3
    cont += 1

print(' → Fim')   