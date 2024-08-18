'''Faça um programa que use a função valorPagamento para determinar o valor a ser pago por uma prestação de uma conta. 
O programa deverá solicitar ao usuário o valor da prestação e o número de dias em atraso e passar estes valores para 
a função valorPagamento, que calculará o valor a ser pago e devolverá este valor ao programa que a chamou. 
O programa deverá então exibir o valor a ser pago na tela. 
Após a execução o programa deverá voltar a pedir outro valor de prestação e assim continuar até que seja informado
um valor igual a zero para a prestação. Neste momento o programa deverá ser encerrado, exibindo o relatório do dia, 
que conterá a quantidade e o valor total de prestações pagas no dia. O cálculo do valor a ser pago é feito da seguinte forma:

Para pagamentos sem atraso, cobrar o valor da prestação. Quando houver atraso, cobrar 3% de multa, mais 0,1% de juros por dia de atraso.'''


# Constantes para multa e juros
MULTA = 3
JUROS = 0.1

def valorPagamento(valor_prestacao, dias_em_atraso):
    """Calcula o valor a ser pago baseado no valor da prestação e nos dias em atraso."""
    if dias_em_atraso:
        valor_a_pagar = valor_prestacao + (valor_prestacao * MULTA / 100)
        valor_a_pagar += (valor_prestacao * dias_em_atraso * JUROS / 100)
        return valor_a_pagar
    else:
        return valor_prestacao  


# Variáveis para controle do relatório diário
total_prestacoes = 0
quantidade_prestacoes = 0

# Loop principal do programa
while True:
    valor_prestacao = float(input('Informe o valor da prestação: R$'))

    if valor_prestacao == 0:
        break   
    
    dias_em_atraso = int(input('Informe os dias em atraso: ')) 

    print(f'Valor a pagar: R${valorPagamento(valor_prestacao, dias_em_atraso):.2f}')

    # Acumula valores para o relatório
    total_prestacoes += valorPagamento(valor_prestacao, dias_em_atraso)
    quantidade_prestacoes += 1


# Exibe relatório 
print(f'\nRelatório do dia:')
print(f'Quantidade de prestações pagas: {quantidade_prestacoes}')
print(f'Valor total de prestações pagas: R${total_prestacoes:.2f}')