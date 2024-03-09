'''Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. 
O programa será interrompido quando o número solicitado for negativo. '''


while True:
    print('-' * 65)
    tabuada = int(input('Informe um número para exibir sua tabuada. (Negativo para parar): '))
    print('-' * 65)
    if tabuada < 0:
        break
    for multiplicador in range(1,11):
        print(f'{tabuada} X {multiplicador} = {(tabuada * multiplicador )}')
print('Programa encerrado')