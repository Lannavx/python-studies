# Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
# Fórmula = (0 °C × 9/5) + 32 = 32 °F

celsius = float(input("Informe a temperatura em C: "))

conversao_celsius = (celsius * (9/5) + 32)

print(f"Sua temperatura em Fahrenheit é: {conversao_celsius:.1f} °F")