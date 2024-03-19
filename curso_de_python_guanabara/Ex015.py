'''Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. 
Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.'''

dias = int(input('Informe os dias que você alugou o carro: '))
km = float(input('Informe os km rodados: '))

pagamento = (60 * dias) + (0.15 * km)

print(f'O preço a pagar pelo carro alugado por {dias} dias e pelos {km}km percorridos é de R${pagamento:.2f}')