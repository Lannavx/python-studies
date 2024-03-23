# Exercício de programação com if e comparação 

primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')

if primeiro_valor >= segundo_valor:
    print(f'{primeiro_valor=} é maior ou igual ao {segundo_valor=}')
else:
    print(f'{segundo_valor=} é maior do que {primeiro_valor=}')

# print(f'{primeiro_valor=} --> f-string (strings formatadas)
# f-string imprime o nome da variável seguido pelo seu valor.
# É uma boa prática para debugging ou para deixar claro o que está sendo impresso.