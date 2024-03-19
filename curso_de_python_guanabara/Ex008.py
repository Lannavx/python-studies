#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milimetros.

medida = float(input('Informe uma distância em metros: '))
centimetros = medida * 100
milimetros = medida * 1000
print(f'O metro informado em centímetros é: {centimetros}cm, já o metro informado em milimetros é {milimetros}mm')