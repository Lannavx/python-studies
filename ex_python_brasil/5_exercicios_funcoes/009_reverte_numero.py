# Reverso do número. Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 127 -> 721.

def reverter_numero(numero):
    '''Reverte um número informado'''
    numero_revertido_str = str(abs(numero))[::-1]

    if numero < 0: # Se o número for negativo, adiciona o sinal negativo na frente
        numero_revertido_str = '-' + numero_revertido_str
    
    return numero_revertido_str

# Loop principal do programa que solicita ao usuário um número inteiro e exibe o resultado reverso até a parada 
while True:
    numero = int(input('Digite um número inteiro [0 para sair]: '))

    if numero == 0:
        break

    print(f'{numero} -> {reverter_numero(numero)}')