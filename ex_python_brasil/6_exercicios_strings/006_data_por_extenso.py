'''Data por extenso. Faça um programa que solicite a data de nascimento (dd/mm/aaaa) do usuário e imprima a data com o nome do mês por extenso.

Data de Nascimento: 29/10/1973
Você nasceu em  29 de Outubro de 1973.'''

# Configura a localização do ambiente garantindo que as datas sejam formatadas no idioma informado

from datetime import datetime

def validar_data(data):
    '''Valida a data informada pelo usuário.'''
    try:
        return datetime.strptime(data, '%d/%m/%Y')
    except ValueError:
        print('Data inválida. Por favor, insira a data no formato dd/mm/aaaa.')
    

def escrever_data_por_extenso(data):
    '''Escreve a data validada por extenso.'''
    data_validada = validar_data(data)
    
    if data_validada:
        lista_meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
                       'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')
        
        # Extrai dia, mês e ano
        dia = data_validada.day
        mes = data_validada.month
        ano = data_validada.year

        data_extenso = f'{dia} de {lista_meses[mes - 1]} de {ano}'
        print(f'Você nasceu em {data_extenso}')


# Solicita ao usuário uma data
data = input('Data de Nascimento (dd/mm/aaaa): ')

escrever_data_por_extenso(data)