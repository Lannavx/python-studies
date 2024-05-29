'''Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. 
O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
    a. par ou ímpar;
    b. positivo ou negativo;
    c. inteiro ou decimal.'''

# Tratamento de erro no caso de valor inválido
try:
    num_um = float(input('Informe um número: '))
    num_dois = float(input('Informe outro número: '))
except ValueError:
    print('Por favor, insira números válidos.')
    exit()  # Encerra o programa se a entrada for inválida 

operacao = input('''Informe a operação que deseja realizar:
[1] Soma                
[2] Subtração  
[3] Divisão
[4] Multiplicação
Escolha: ''')

print('=' * 35)    

# Executa as operações conforme escolha do usuário
if operacao == '1':
    resultado = num_um + num_dois
    print(f'A soma de {num_um} + {num_dois} = {resultado:.2f}')
elif operacao == '2':
    resultado = num_um - num_dois
    print(f'A subtração de {num_um} - {num_dois} = {resultado:.2f}')
elif operacao == '3':
    # Verifica se o divisor não é zero
    if num_dois != 0:
        resultado = num_um / num_dois
        print(f'A divisão de {num_um} / {num_dois} = {resultado:.2f}')
    else:
        print('Divisão por zero não é permitida.')
        resultado = None
elif operacao == '4':
    resultado = num_um * num_dois
    print(f'A multiplicação de {num_um} * {num_dois} = {resultado:.2f}')
else:
    print('Opção inválida! Escolha entre 1 e 4 conforme operação desejada.')
    resultado = None

# Classificação do resultado da operação
if resultado is not None:
    if resultado > 0:
        print(f'{resultado:.2f} é um número positivo!')
    elif resultado < 0:
        print(f'{resultado:.2f} é um número negativo!')
    else:
        print(f'{resultado:.2f} é zero!')

    if resultado == round(resultado):
        print(f'{resultado:.2f} é um número inteiro!')
        if resultado % 2 == 0:
            print(f'{resultado:.2f} é um número par!')
        else:
            print(f'{resultado:.2f} é um número ímpar!')
    else:
        print(f'{resultado:.2f} é um número decimal!')
        print(f'Decimais não são classificados como par ou ímpar!')

