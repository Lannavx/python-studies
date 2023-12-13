''''Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. 
Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. 
A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.'''


valor = float(input('Informe o valor da casa desejada: R$ '))
salario = float(input('Informe o seu salário: R$  '))
tempo = int(input('Em quantos anos você vai pagar esse imóvel? '))
prestação = (valor / (tempo * 12))
minimo = salario * 0.30
print(f'Para pagar uma casa de R${valor:.2F} em {tempo} anos, a prestação seria de R${prestação:.2F} ')
if prestação <= minimo:
    print('Empréstimo aprovado! Parabéns!')
else:
    print('Empréstimo Negado!') 