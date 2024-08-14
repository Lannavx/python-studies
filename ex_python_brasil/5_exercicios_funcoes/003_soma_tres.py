# Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.

def somar_valores(x,y,z):
    '''Soma três valores e retorna o resultado'''
    return x + y + z

# Solicita ao usuário 3 números inteiros
print('Informe três números inteiros para ver a soma deles.')
x = int(input('Informe o 1º número: '))
y = int(input('Informe o 2º número: '))
z = int(input('Informe o 3º número: '))

# Chama a função com os três números fornecidos e exibe o resultado
print(f'A soma dos números é de {somar_valores(x, y, z)}')