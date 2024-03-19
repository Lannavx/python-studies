#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

dinheiro = float(input('Informe quanto de dinheiro você tem: R$'))
valor_do_dolar = 3.27
dolar = dinheiro / valor_do_dolar
print(f'Com R${dinheiro:.2f} você pode comprar US${dolar:.2F}')