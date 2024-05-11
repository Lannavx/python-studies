
'''
Introdução às funções (def) em Python

Funções são trechos de código usados para replicar determinada ação ao longo do seu código.
Elas podem receber valores para parâmetros (argumentos) e retornar um valor específico.
Por padrão, funções Python retornam None (nada).

Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)

Ao definir uma função, os parâmetros podem ter valores padrão. 
Caso o valor não seja enviado para o parâmetro, o valor padrão será usado.

'''

# Exercícios com funções

'''Crie uma função que multiplica todos os argumentos não nomeados recebidos.
Retorne o total para uma variável e mostre o valor da variável.'''

# Definindo a função 'multiplicar' que aceita um número variável de argumentos não nomeados
def multiplicar(*args):
    total = 1
    for numero in args:
        total *= numero
    return total # Após concluir a iteração sobre todos os números, retorna o 'total'
    
multiplicacao = multiplicar(5,8,3,6)
print(multiplicacao)

''' O *args é uma convenção em Python usada em definições de funções para permitir
que uma função aceite um número variável de argumentos não nomeados. '''