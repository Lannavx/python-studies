#Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

#Forma 1

multiplicador = 0
n1 = int(input('Digite um número para ver a sua tabuada: '))
for tabuada in range(0,10):
    multiplicador = multiplicador  + 1
    print(f'{n1} X {multiplicador } = {(n1 * multiplicador )}')

#Forma 2
    
n1 = int(input('Digite um número para ver a sua tabuada: '))
for multiplicador in range(1,11):
    print(f'{n1} X {multiplicador } = {(n1 * multiplicador )}')