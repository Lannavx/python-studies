'''Crie um programa que simule o funcionamento de um caixa eletrônico. 
No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.'''

print('=' * 20)
print('BANCO DO ESTUDANTE')
print('=' * 20)

cont_50 = 0
cont_20 = 0
cont_10 = 0
cont_1 = 0
valor = int(input('Qual valor você gostaria de sacar? R$'))
while valor > 0:  # O loop continuará até que o valor a ser sacado seja 0
    if valor >= 50:
        valor -= 50  
        cont_50 += 1  
    elif valor >= 20:
        valor -= 20  
        cont_20 += 1  
    elif valor >= 10:
        valor -= 10  
        cont_10 += 1 
    else:
        cont_1 += valor  # Todo o valor restante será em cédulas de R$1
        valor = 0  # Zera o valor para terminar o loop

# Após o término do loop, imprime o total de cédulas de cada valor
if cont_50 > 0:
    print(f'Total de {cont_50} cédulas de R$50')
if cont_20 > 0:
    print(f'Total de {cont_20} cédulas de R$20')
if cont_10 > 0:
    print(f'Total de {cont_10} cédulas de R$10')
if cont_1 > 0:
    print(f'Total de {cont_1} cédulas de R$1')
 
print('=' * 20)

#Forma Professor

valor = int(input('Qual valor você gostaria de sacar? R$'))
total = valor
cedula = 50
total_cedula = 0

while True:
    if total >= cedula:
        total -= cedula
        total_cedula += 1
    else:
        if total_cedula > 0:
            print(f'Total de {total_cedula} cédulas de R${cedula}')    
        # Atualiza o valor para a próxima nota de menor valor
        if  cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        # Reinicia o contador de cédulas para o novo valor de cédula
        total_cedula = 0
        # Saida do while
        if total == 0:
            break               