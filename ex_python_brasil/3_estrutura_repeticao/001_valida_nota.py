''' Faça um programa que peça uma nota entre zero e dez. 
Mostre uma mensagem caso o valor seja inválido e continue pedindo até que
o usuário informe um valor válido.'''

nota = float(input('Informe uma nota entre zero e dez: '))

# Continua solicitando a nota enquanto ela estiver fora do intervalo permitido
while nota < 0 or nota > 10:
    nota = float(input('Valor incorreto! Informe uma nota entre zero e dez: '))

print(f'Você informou a nota {nota}.')