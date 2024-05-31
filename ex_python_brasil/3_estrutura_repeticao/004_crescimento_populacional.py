'''Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3%
e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. 
Faça um programa que calcule e escreva o número de anos necessários para que a população do país A 
ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.'''

populacao_a = 80000  # População inicial do país A
populacao_b = 200000  # População inicial do país B
taxa_crescimento_a = 0.03  # Taxa de crescimento anual de 3% para o país A
taxa_crescimento_b = 0.015  # Taxa de crescimento anual de 1.5% para o país B

cont_anos = 0

while populacao_a < populacao_b:
    # Calcula o crescimento anual das populações
    populacao_a += populacao_a * taxa_crescimento_a
    populacao_b += populacao_b * taxa_crescimento_b
    # Incrementa o contador de anos
    cont_anos += 1

print(f'São necessários {cont_anos} anos para a população do país A ultrapassar ou se igualar ao país B!')
