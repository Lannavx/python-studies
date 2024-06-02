''' Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número. 
Não utilize a função de potência da linguagem.'''

base = int(input('Informe um número (base): '))
expoente = int(input('Informe outro número (expoente): '))

# Inicializa potencia em 1 para garantir que o cálculo funcione corretamente inclusive para expoente 0
potencia = 1

# Se o expoente é positivo, realiza a potenciação
if expoente > 0:
    for _ in range(expoente):
        potencia *= base

# Se o expoente é negativo, realiza a potenciação e inverte o resultado
elif expoente < 0:
    for _ in range(-expoente):
        potencia *= base
    potencia = 1 / potencia     

print(f'O resultado de {base} elevado ao número {expoente} é de {potencia}')

