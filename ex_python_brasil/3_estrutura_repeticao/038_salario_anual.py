'''Um funcionário de uma empresa recebe aumento salarial anualmente: 
Sabe-se que:
Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do percentual do ano anterior. 
Faça um programa que determine o salário atual desse funcionário. 
Após concluir isto, altere o programa permitindo que o usuário digite o salário inicial do funcionário.'''

import datetime

# Solicita ao usuário o salário inicial
salario = float(input('Informe o salário inicial do funcionário: R$'))

# Definindo o ano inicial e o aumento inicial 
aumento_percentual = 0.015
ano_inicial = 1997

# Aplica o primeiro aumento em 1996
salario += salario * aumento_percentual 

# Obtém o ano atual
ano_atual = datetime.datetime.now().year

# Aplica os aumentos de 1997 até o ano atual
for ano in range(ano_inicial, ano_atual + 1):
    aumento_percentual *= 2  # Dobra o aumento percentual a cada ano
    salario += salario * aumento_percentual  # Aplica o aumento ao salário

# Exibe o salário final após os aumentos
print(f'O salário atual do funcionário é R${salario:.2f}')

