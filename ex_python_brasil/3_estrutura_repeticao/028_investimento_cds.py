''' Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs 
e o valor médio gasto em cada um deles. O usuário deverá informar a quantidade de CDs e o valor para em cada um.'''

# Inicializa as variáveis necessárias para o cálculo
soma_valor = 0
contagem_cds = 0

print('Informe o valor de cada CD. Digite 0 para encerrar.')

# Loop infinito para coleta de dados até que o usuário decida encerrar
while True:
    valor_cd = float(input(f'Informe o valor do CD nº{contagem_cds + 1}: R$ '))

    # Verifica se o usuário digitou 0 para encerrar o loop
    if valor_cd == 0:
        break

    # Verifica se o valor informado é menor que zero e solicita uma nova entrada
    elif valor_cd < 0:
        print('Por favor, informe um valor válido maior que zero ou 0 para sair.') 

    # Adiciona o valor válido informado à soma total e incrementa o contador de CDs
    else:
        soma_valor += valor_cd
        contagem_cds += 1

# Verifica se algum CD foi registrado para evitar divisão por zero
if contagem_cds > 0:     
    media = soma_valor / contagem_cds
    print('-' * 10)
    print(f'O valor total investido na coleção de CDs foi de R${soma_valor:.2f}')
    print(f'E o valor médio gasto em cada um deles é de R${media:.2f}')    
else:
    print('Não há dados suficientes para calcular a média.')
