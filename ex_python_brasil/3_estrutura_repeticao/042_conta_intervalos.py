''' Faça um programa que leia uma quantidade indeterminada de números positivos e 
conte quantos deles estão nos seguintes intervalos: [0-25], [26-50], [51-75] e [76-100]. 
A entrada de dados deverá terminar quando for lido um número negativo.'''

# Inicializa contadores para cada intervalo de números
cont_1 = cont_2 = cont_3 = cont_4 = 0

# Instrui o usuário sobre como terminar a entrada de dados
print('Digite um número negativo para encerrar a inserção de dados.')

while True:
    numeros = int(input('Informe um número aleatório positivo até 100: '))

    # Condição para finalizar o loop
    if numeros < 0:
        break

    # Condição para contabilizar os números nos intervalos mencionados     
    if 0 <= numeros <= 25:
        cont_1 += 1
    elif 26 <= numeros <= 50:
        cont_2 += 1    
    elif 51 <= numeros <= 75:
        cont_3 += 1      
    elif 76 <= numeros <= 100:
        cont_4 += 1   

    # Condição para números acima de 100
    if numeros > 100:
        print('São permitidos apenas números menores que 100!')
        

print()

# Exibe o resultado
print(f'Há {cont_1} números no intervalo de [0-25]')
print(f'Há {cont_2} números no intervalo de [26-50]')
print(f'Há {cont_3} números no intervalo de [51-75]')
print(f'Há {cont_4} números no intervalo de [76-100]')
