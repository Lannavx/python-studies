'''Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
- EQUILÁTERO: todos os lados iguais
- ISÓSCELES: dois lados iguais, um diferente
- ESCALENO: todos os lados diferentes'''

r1 = float(input('Informe o comprimento de uma reta: '))
r2 = float(input('Informe o comprimento de outra reta: '))
r3 = float(input('Informe o comprimento de mais uma reta: '))
if r1 < r2 + 3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('As retas podem formar um triângulo! ' , end='')
    if r1 == r2 == r3:
        print('Equilátero')
    elif r1 != r2 != r3 != r1:
        print('Escaleno') 
    else:
        print('Isósceles')       
else:
    print('As retas não podem formar um triângulo!')