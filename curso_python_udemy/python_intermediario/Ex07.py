# Calculadora com o While

while True:
    
    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite outro número: ')
    operador = input('Digite o operador (+ - / *): ')

    # Inicialmente, assume-se que os números digitados podem ser inválidos.
    numeros_validos = None # None é usado como um valor inicial que indica que ainda não sabemos se os números são válidos
    num_1_float = 0
    num_2_float = 0

    # Tenta converter as entradas de string para float.
    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numeros_validos = True  # Se a conversão for bem-sucedida, marca os números como válidos
    except:
        numeros_validos = None  # Se a conversão falhar, mantém os números como inválidos.

    if numeros_validos is None:
        print('Um ou ambos os números digitados são inválidos!')
        continue

    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos:
        print('Operador inválido. Digite + - / ou *')
        continue

    if len(operador) > 1:
        print('Digite apenas um operador!')
        continue

    print('Confira o resultado da conta abaixo: ')    
    if operador == '+':
        print(f'{num_1_float} + {num_2_float} =', num_1_float + num_2_float)
    elif operador == '-':
        print(f'{num_1_float} - {num_2_float} =',num_1_float - num_2_float)
    elif operador == '/':
        print(f'{num_1_float} / {num_2_float} =',num_1_float / num_2_float) 
    else:
        print(f'{num_1_float} * {num_2_float} =',num_1_float * num_2_float)   

    sair = input('Deseja sair? [s]im / [n]ão: ').lower().startswith('s')

    if sair: # É a mesma coisa que if sair is True
        print('Volte sempre!')
        break
