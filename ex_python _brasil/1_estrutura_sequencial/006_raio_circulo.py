# Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

# Sempre que falamos de números quebrados, usamos "."
numero_de_pi = 3.14159

raio = float(input("Informe o raio de um círculo: "))

a = numero_de_pi * (raio**2)

print(f"O cálculo da área é: {a:.3f}")