'''Desenvolva um programa que faça a tabuada de um número qualquer inteiro que será digitado pelo usuário, 
mas a tabuada não deve necessariamente iniciar em 1 e terminar em 10, o valor inicial e final devem ser informados 
também pelo usuário, conforme exemplo abaixo:

Montar a tabuada de: 5
Começar por: 4
Terminar em: 7

Vou montar a tabuada de 5 começando em 4 e terminando em 7:
5 X 4 = 20
5 X 5 = 25
5 X 6 = 30
5 X 7 = 35
Obs: Você deve verificar se o usuário não digitou o final menor que o inicial.'''

# Inicia um loop para permitir múltiplas execuções do programa
while True:
    
    # Tratamento de erro no caso de valor inválido nas entradas solicitadas
    try:
        multiplicador = int(input('Informe um número para ver sua tabuada: '))
        inicio = int(input('Começar por: '))
        fim = int(input('Terminar em: '))

        # Verifica se o valor final é menor que o inicial.    
        while fim < inicio:
            print('O número final não deve ser menor que o inicial!')
            fim = int(input(f'Por favor, informe um número maior que {inicio} para finalizar a tabuada: '))

        print('-' * 10)

        print(f'Vou montar a tabuada de {multiplicador} começando em {inicio} e terminando em {fim}:')
        
        # Itera através do intervalo de números definido pelo usuário e imprime a tabuada
        for numero in range(inicio, fim + 1):
            print(f'{multiplicador} X {numero} = {multiplicador * numero}')

        print('-' * 10)    

    # Captura exceções se as entradas não forem numéricas
    except ValueError:
        print('Por favor, insira apenas números inteiros.')    

    # Pergunta se o usuário deseja repetir a operação.
    if input('Deseja criar outra tabuada? (s/n): ').strip().lower()[0] != 's':
        break  

print('Até breve!')