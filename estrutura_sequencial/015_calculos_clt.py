"""
    Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
    Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para 
    o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
        a. salário bruto.
        b. quanto pagou ao INSS.
        c. quanto pagou ao sindicato.
        d. o salário líquido.
        e. calcule os descontos e o salário líquido, conforme a tabela abaixo:
            + Salário Bruto : R$
            - IR (11%) : R$
            - INSS (8%) : R$
            - Sindicato ( 5%) : R$
            = Salário Liquido : R$+
    Obs.: Salário Bruto - Descontos = Salário Líquido.
"""

ganho_hora = float(input('Informe quanto você ganha por hora: R$'))  
hora_trabalhada = float(input('Informe o número de horas trabalhadas no mês: '))
salario = ganho_hora * hora_trabalhada
ir = salario * 0.11
inss = salario * 0.08
sindicato = salario * 0.05
print(f'''+ Salário Bruto : R${salario:.2f}
- IR (11%) : R$ {ir:.2f}
- INSS (8%) : R$ {inss:.2f}
- Sindicato (5%) : R$ {sindicato:.2f}
= Salário Liquido : R$+ {salario - ir - inss - sindicato:.2f}
''' )