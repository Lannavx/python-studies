"""
    Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
        1. O produto do dobro do primeiro com metade do segundo .
        2. A soma do triplo do primeiro com o terceiro.
        3. O terceiro elevado ao cubo.
"""

numero_um = int(input('Informe um número: '))
numero_dois = float(input('Informe outro número: '))
numero_tres = int(input('Informe o terceiro número: '))

conta_um = (numero_um * 2) * (numero_dois / 2)
conta_dois = (numero_um * 3) + numero_tres
conta_tres = numero_tres **3

print(f'O produto do dobro do primeiro com metade do segundo é: {conta_um:.2f}')
print(f'A soma do triplo do primeiro com o terceiro é : {conta_dois}')
print(f'O terceiro elevado ao cubo é: {conta_tres}')