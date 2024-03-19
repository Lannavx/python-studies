# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto

valor_produto = float(input('O preço do produto é: R$'))
desconto = valor_produto - (valor_produto*0.05)
print(f'O valor do produto com desconto de 5% é R${desconto:.2f}')

#Outra forma para fazer porcentagem: podemos pegar o valor, multiplicar pela porcentagem e dividir por 100
#Ex: eu tenho um valor de 10 reais, onde tenho 5% de desconto >> 10*5/100 = 0.5

valor_produto = float(input('O preço do produto é: R$'))
desconto = valor_produto - (valor_produto * 5 / 100)
print(f'O valor do produto com desconto de 5% é R${desconto:.2f}')