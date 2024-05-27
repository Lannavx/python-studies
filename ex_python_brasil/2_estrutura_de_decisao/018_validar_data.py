# Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.

from datetime import datetime

data = input('Informe uma data no formato dd/mm/aaaa: ')

try:
    data_valida = datetime.strptime(data, '%d/%m/%Y')
    print('Data no formato correto e válida!')
except ValueError:
    print('Formato errado ou data inválida! Digite uma data no formato dd/mm/aaaa')



