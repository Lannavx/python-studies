'''Faça um programa com uma função chamada somaImposto. 
A função possui dois parâmetros formais: taxaImposto, que é a quantia de imposto sobre vendas expressa 
em porcentagem e custo, que é o custo de um item antes do imposto. 
A função “altera” o valor de custo para incluir o imposto sobre vendas.'''

def somaImposto(taxaImposto, custo):
    '''Calcula o valor do imposto com a porcentagem do custo'''
    valor_com_imposto = custo + (custo * taxaImposto / 100)  
    return valor_com_imposto

# Solicita ao usuário o valor do item e a taxa do imposto
custo = float(input('Informe o valor do item: R$'))
taxaImposto = float(input('Informe a quantia de imposto sobre vendas expressa em porcentagem: '))

# Chama a função e exibe o resultado com os valores fornecidos pelo usuário 
print(f'O valor do item com o imposto é de R${somaImposto(taxaImposto, custo):.2f}')