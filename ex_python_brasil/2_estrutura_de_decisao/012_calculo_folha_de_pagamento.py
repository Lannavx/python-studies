'''Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, 
que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, 
mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. 
O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.

Desconto do IR:
Salário Bruto até 900 (inclusive) - isento
Salário Bruto até 1500 (inclusive) - desconto de 5%
Salário Bruto até 2500 (inclusive) - desconto de 10%
Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo. 

No exemplo o valor da hora é 5 e a quantidade de hora é 220.

        Salário Bruto: (5 * 220)        : R$ 1100,00
        (-) IR (5%)                     : R$   55,00  
        (-) INSS ( 10%)                 : R$  110,00
        FGTS (11%)                      : R$  121,00
        Total de descontos              : R$  165,00
        Salário Liquido                 : R$  935,00'''

valor_hora = float(input('Informe o valor da sua hora: R$ '))
horas_mes = int(input('Informe a quantidade de horas trabalhadas no mês: '))

salario_bruto = valor_hora * horas_mes
inss = salario_bruto * 0.10
fgts = salario_bruto * 0.11

if salario_bruto <= 900:
     imposto_renda = 0
     porcentagem = 0
elif salario_bruto <= 1500:
    porcentagem = 5
    imposto_renda = salario_bruto * (porcentagem / 100)
elif salario_bruto <= 2500:
     porcentagem = 10
     imposto_renda = salario_bruto * (porcentagem / 100)
else:
    porcentagem = 20
    imposto_renda = salario_bruto * (porcentagem / 100)

descontos =  imposto_renda + inss
salario_liquido = salario_bruto - descontos

print('=' * 36)

print(f'''
Salário Bruto:           R$ {salario_bruto:.2f}
(-) IR ({porcentagem}%):            R$ {imposto_renda:.2f}
(-) INSS (10%):          R$ {inss:.2f}
FGTS (11%):              R$ {fgts:.2f}
Total de descontos:      R$ {descontos:.2f}
Salário Líquido:         R$ {salario_liquido:.2f}
''') 
