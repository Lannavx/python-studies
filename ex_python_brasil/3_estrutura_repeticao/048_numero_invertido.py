'''Faça um programa que peça um numero inteiro positivo e em seguida mostre este numero invertido.

Exemplo:
  12376489
  => 98467321'''

# Lê um número inteiro positivo
numero = int(input('Informe um número inteiro positivo: '))

# Verifica se o número é negativo
while numero < 0:
    numero = int(input('Por favor, informe um número inteiro POSITIVO: '))

# Converte o número para string para facilitar a manipulação dos dígitos
numero_str = str(numero)

# Inicia a string que conterá o número invertido
numero_invertido = ''

# Laço para inverter os dígitos do número
for digito in numero_str:
    numero_invertido = digito + numero_invertido

# Exibe o resultado
print(f'{numero}')
print(f'=> {numero_invertido}')
