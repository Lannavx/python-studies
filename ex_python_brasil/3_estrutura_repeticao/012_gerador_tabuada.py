'''
Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 15. 
O usuário deve informar de qual numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:

Tabuada de 5:
5 X 1 = 5
5 X 2 = 10
...
5 X 10 = 50
'''


multiplicador = int(input('Qual numero você deseja ver a tabuada: '))

# Verificação de entrada
if 1 <= multiplicador <= 15:
    print('-' * 15)
    print(f'TABUADA DO {multiplicador}')
    print('-' * 15)
    for numero in range(1,11):
        print(f'{multiplicador} X {numero} = {multiplicador * numero}')
else:
    print('Por favor, insira um número entre 1 e 15.')