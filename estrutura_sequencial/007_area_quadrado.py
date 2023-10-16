# Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

lado_quadrado = float(input("Informe o tamanho dos lados do quadrado: "))

area_do_quadrado = (lado_quadrado ** 2)
dobro_do_quadrado = area_do_quadrado * 2

print(f"O dobro da área do quadrado é: {dobro_do_quadrado:.2f}")

