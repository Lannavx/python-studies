'''Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.'''

operacao = 0
num1 = int(input('Informe um valor: '))
num2 = int(input('Informe outro valor: '))
while operacao != '5':
    operacao = input('''[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
    Informe a opção desejada: ''')
    if operacao == '1':
        print(f'O soma entre {num1} + {num2} é = {num1 + num2}')
    elif operacao == '2':   
        print(f'O valor da multiplicação entre {num1} e {num2} é de {num1 * num2}')
    elif operacao == '3':
        if num1 > num2:
                print(f'Entre {num1} e {num2}, o maior número é o {num1}')
        elif num2 > num1:
                print(f'Entre {num1} e {num2}, o maior número é o {num2}')
        else:        
              print('Os números informados são iguais, logo, não há maior valor')
    elif operacao == '4':
            print('Informe os novos números desejados:')    
            num1 = int(input('Informe um valor: '))
            num2 = int(input('Informe outro valor: '))
    elif operacao == '5':
            print('Obrigada por usar nosso programa, até breve!')
    else:
            print('Opção inválida, tente novamente!')       





