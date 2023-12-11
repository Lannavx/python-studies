#Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
#(0 °C × 9/5) + 32 = 32 °F

celcius = float(input('Informe a temperatura em celcius: '))
conversao = (celcius * 9 / 5) + 32
print(f'A conversão de {celcius}°C para Fahrenheit é {conversao}°F')