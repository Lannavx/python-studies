'''
Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
Dicas:
    Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
    Triângulo Equilátero: três lados iguais;
    Triângulo Isósceles: quaisquer dois lados iguais;
    Triângulo Escaleno: três lados diferentes;
'''

print('Informe os 3 lados de um triângulo: ')
primeiro_lado = float(input('Primeiro lado: '))
segundo_lado = float(input('Segundo lado: '))
terceiro_lado = float(input('Terceiro lado: '))

# Verifica se os lados podem formar um triângulo
if (primeiro_lado + segundo_lado > terceiro_lado and
    primeiro_lado + terceiro_lado > segundo_lado and
    segundo_lado + terceiro_lado > primeiro_lado):
    
    # Classifica os triângulos
    if primeiro_lado == segundo_lado and segundo_lado == terceiro_lado:
        print('Seu triângulo é um Triângulo Equilátero!')
    elif (primeiro_lado == segundo_lado or 
          segundo_lado == terceiro_lado or 
          primeiro_lado == terceiro_lado):
        print('Seu triângulo é um Triângulo Isósceles!')
    else:
        print('Seu triângulo é um Triângulo Escaleno!')
else:
    print('Os valores informados não podem formar um triângulo!') 
