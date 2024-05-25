'''As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e 
lhe contraram para desenvolver o programa que calculará os reajustes.
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
salários até R$ 280,00 (incluindo) : aumento de 20%
salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
salários de R$ 1500,00 em diante : aumento de 5% 

Após o aumento ser realizado, informe na tela:
o salário antes do reajuste;
o percentual de aumento aplicado;
o valor do aumento;
o novo salário, após o aumento.'''

salario = float(input('Informe seu salário R$: '))

if salario <= 280:
    percentual = '20%'
    valor_adicional = salario * 0.20
    novo_salario = salario + valor_adicional
elif salario > 280 and salario <= 700:
    percentual = '15%'
    valor_adicional = salario * 0.15
    novo_salario = salario + valor_adicional
elif salario > 700 and salario <= 1500:
    percentual = '10%'
    valor_adicional = salario * 0.10
    novo_salario = salario + valor_adicional
elif salario > 1500:
    percentual = '5%'
    valor_adicional = salario * 0.05
    novo_salario = salario + valor_adicional

print('=' * 36)

print(f'''Salário antes do reajuste: R${salario:.2f}
Percentual de aumento aplicado: {percentual}
Valor do aumento: R${valor_adicional:.2f}
Novo salário: R${novo_salario:.2f}''')   

