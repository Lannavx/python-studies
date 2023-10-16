"""

    Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
    Fórmula: C = 5 * ((F-32) / 9).

"""

fahrenheit = float(input("Informe a temperatura em F: "))

conversao_celsius = 5 * ((fahrenheit - 32) / 9)

print(f"Sua temperatura em graus Celsius é: {conversao_celsius:.1f}")