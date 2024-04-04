'''Faça uma lista de comprar com listas.
O usuário deve ter a possibilidade de inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com erros de índices inexistentes na lista. '''

lista = []

while True:
    print('Selecione uma opção:')
    opcao = input('[i]nserir [a]pagar [l]istar: ').lower().strip()[0]

    if opcao == 'i':
        valor = input('Valor: ')
        lista.append(valor)
    elif opcao == 'a':
        indice_str = input('Escolha um índice para apagar: ')
        
        try:
            indice_int = int(indice_str)
            del lista[indice_int]  
        except ValueError:
            print('Por favor, digite um número inteiro')
        except IndexError:
            print('Índice não existe na lista')    
    elif opcao == 'l':

        if len(lista) == 0:
            print('Não há itens para listar')

        for i, valor in enumerate(lista):
            print(i, valor)

    else: 
        print('Por favor, escolha i, a ou l')      
       


              

    