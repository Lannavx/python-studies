'''
Faça um programa que receba o valor de uma dívida e mostre uma tabela com os seguintes dados: 
valor da dívida, valor dos juros, quantidade de parcelas e valor da parcela.
Os juros e a quantidade de parcelas seguem a tabela abaixo:
Quantidade de Parcelas % de Juros sobre o valor inicial da dívida
1       0
3       10
6       15
9       20
12      25
Exemplo de saída do programa:
Valor da Dívida Valor dos Juros Quantidade de Parcelas  Valor da Parcela
R$ 1.000,00     0               1                       R$  1.000,00
R$ 1.100,00     100             3                       R$    366,00
R$ 1.150,00     150             6                       R$    191,67
'''

# Valor da dívida
valor_divida = float(input('Digite o valor da dívida: R$'))

# Listas com as opções de parcelamento e juros
parcelas = [1, 3, 6, 9, 12]
juros = [0, 10, 15, 20, 25]

print('Valor da Dívida\t\tValor dos Juros\t\tQuantidade de Parcelas\t\tValor da Parcela')

# Loop através dos índices das listas de parcelas e juros
for i in range(len(parcelas)):

    # Calcula o valor dos juros
    valor_juros = valor_divida * (juros[i] / 100)
    # Calcula o valor total com juros
    valor_total = valor_divida + valor_juros
    # Calcula o valor de cada parcela
    valor_parcela = valor_total / parcelas[i]
    
    # Exibe os resultados formatados em coluna com o caractere \t
    print(f'R$ {valor_total:.2f}\t\t{valor_juros:,.2f}\t\t\t{parcelas[i]}\t\t\t\tR$ {valor_parcela:,.2f}')
 
 