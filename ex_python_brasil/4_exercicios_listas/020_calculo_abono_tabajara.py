'''As Organizações Tabajara resolveram dar um abono aos seus colaboradores em reconhecimento ao bom resultado alcançado durante o ano que passou. 
Para isto contratou você para desenvolver a aplicação que servirá como uma projeção de quanto será gasto com o pagamento deste abono.
Após reuniões envolvendo a diretoria executiva, a diretoria financeira e os representantes do sindicato laboral, chegou-se a seguinte forma de cálculo:
a.Cada funcionário receberá o equivalente a 20% do seu salário bruto de dezembro; 
a.O piso do abono será de 100 reais, isto é, aqueles funcionários cujo salário for muito baixo, recebem este valor mínimo;
 Neste momento, não se deve ter nenhuma preocupação com colaboradores com tempo menor de casa, descontos, impostos ou outras particularidades. 
 Seu programa deverá permitir a digitação do salário de um número indefinido (desconhecido) de salários. 
 Um valor de salário igual a 0 (zero) encerra a digitação. Após a entrada de todos os dados o programa deverá calcular o valor do 
 abono concedido a cada colaborador, de acordo com a regra definida acima. Ao final, o programa deverá apresentar:
O salário de cada funcionário, juntamente com o valor do abono;
O número total de funcionário processados;
O valor total a ser gasto com o pagamento do abono;
O número de funcionário que receberá o valor mínimo de 100 reais;
O maior valor pago como abono; A tela abaixo é um exemplo de execução do programa, apenas para fins ilustrativos. 
Os valores podem mudar a cada execução do programa.
Projeção de Gastos com Abono
============================ 
 
Salário: 1000
Salário: 300
Salário: 500
Salário: 100
Salário: 4500
Salário: 0
 
Salário    - Abono     
R$ 1000.00 - R$  200.00
R$  300.00 - R$  100.00
R$  500.00 - R$  100.00
R$  100.00 - R$  100.00
R$ 4500.00 - R$  900.00
 
Foram processados 5 colaboradores
Total gasto com abonos: R$ 1400.00
Valor mínimo pago a 3 colaboradores
Maior valor de abono pago: R$ 900.00'''

print('Projeção de Gastos com Abono\n')


PORCENTAGEM = 0.2

salarios_abonos = [] # Lista para armazenar os pares de salário e abono 

# Contadores e acumuladores para armazenar dados
cont_colaborador_minimo = 0
total_abono = 0
cont_colaborador = 0
valor_maximo_abono = 0

# Laço para entrada de salários dos funcionários
while True:

    entrada_salarios = input('Informe o salário do funcionário ou ZERO para encerrar: R$')

    if entrada_salarios == '0':
        break

    # Trata erros de entrada    
    try:
        entrada_salarios = float(entrada_salarios)
    except ValueError:
        print('Valor inválido, por favor digite apenas números.')
        continue     

    # Calcula o abono dependendo do salário informado   
    if entrada_salarios < 1000:
        abono = 100
        cont_colaborador_minimo += 1
    else:
        abono = entrada_salarios * PORCENTAGEM

    # Armazena o par de salário e abono calculado
    salarios_abonos.append([entrada_salarios, abono])
    total_abono += abono
    cont_colaborador += 1

print()    

# Exibe todos os salários processados
for salario in salarios_abonos:
    print(f'Salário: {salario[0]}') 

# Exibe a relação salário-abono para cada entrada processada
print('\nSalário - Abono')
for salario, abono in salarios_abonos:
    print(f'R$ {salario:.2f} - R$ {abono:.2f}')
    
    if abono > valor_maximo_abono:
        valor_maximo_abono = abono
    
# Imprime estatísticas finais 
print(f'\nForam processados {cont_colaborador} colaboradores')
print(f'Total gasto com abonos: R$ {total_abono:.2f}')
print(f'Valor mínimo pago a {cont_colaborador_minimo} colaboradores')
print(f'Maior valor de abono pago: R$ {valor_maximo_abono}')