''' Data com mês por extenso. 
Construa uma função que receba uma data no formato DD/MM/AAAA e devolva uma string no formato D de mesPorExtenso de AAAA. 
Opcionalmente, valide a data e retorne NULL caso a data seja inválida.'''

# Configura a localização do ambiente garantindo que as datas sejam formatadas no idioma informado
import locale
locale.setlocale(locale.LC_ALL, 'pt_BR.utf8')

from datetime import datetime

def validar_data(data):
    '''Valida a data informada pelo usuário'''
    try:
        return datetime.strptime(data, '%d/%m/%Y')
    except ValueError:
        return None

def escrever_data_extenso(data):
    '''Escreve a data por extenso, após verificação de data válida.'''
    data_validada = validar_data(data)
    if data_validada:
        return data_validada.strftime('%d de %B de %Y')
    else:
        return 'NULL'

# Solicita ao usuário uma data
data = input('Informe uma data no formato DD/MM/AAAA: ')

# Exibe a data por extenso ou 'NULL' no caso de data inválida
print(escrever_data_extenso(data))


