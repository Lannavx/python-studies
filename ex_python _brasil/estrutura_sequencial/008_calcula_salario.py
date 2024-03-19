# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

mes = str(input("Informe o mês: "))
ganho_por_hora = float(input("Informe quanto você ganha por hora: "))
horas_trabalhadas = float(input(f"Informe o número das suas horas trabalhadas no mês de {mes}: "))
 

total_salario = ganho_por_hora * horas_trabalhadas

print(f"Seu salário total no mês de {mes} é: R${total_salario:.2F}")

