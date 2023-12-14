'''Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
- à vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço formal
- 3x ou mais no cartão: 20% de juros'''

preço= float(input('Informe o valor do produto: R$'))
print('''[1] - À vista dinheiro / cheque')
[2] - À vista no cartão
[3] - Em até 2x no cartão
[4] - 3x ou mais no cartão''')
condição = input('Informe uma condição de pagamento conforme o menu: ')

if condição == '1':
    print(f'Você ganhou 10% de desconto! O valor do seu produto é de R${preço - (preço * 0.10):.2f}')
elif condição == '2':
    print(f'Você ganhou 5% de desconto! O valor do seu produto é de R${preço - (preço * 0.05):.2f}')
elif condição == '3':
    total = preço
    parcela = total / 2
    print(f'Sua compara será parcelada em 2x de R${parcela}')
    print(f'Você não ganha nenhum desconto! O valor do seu produto continua sendo de R${preço:.2f}')
elif condição == '4':
     total = preço + (preço * 0.20)
     total_parcelas = int(input('Quantas parcelas? '))  
     parcela = total / total_parcelas
     print(f'No parcelamento de {total_parcelas}x sua compara será parcelada em R${parcela:.2f}!')
     print(f'Você terá juros de 20%, logo seu produto passará a custar R${total:.2f}')
else:
    print('Opção inválida! Selecione a opção correta!')