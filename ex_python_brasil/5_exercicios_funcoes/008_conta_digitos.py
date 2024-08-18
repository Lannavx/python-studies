# Faça uma função que informe a quantidade de dígitos de um determinado número inteiro informado.

def informar_quantidade(numero):
    '''Conta os dígitos de um número inteiro'''
    numero = abs(numero)  # Remove o sinal negativo se houver
    return len(str(numero))


# Solicita ao usuário um número inteiro
numero = int(input('Digite um número inteiro: '))

# Exibe o resultado
print(f'A quantidade de dígitos é de {informar_quantidade(numero)}')