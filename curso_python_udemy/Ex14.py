# Crie uma função que fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.

def identificador_par_impar(numero):
    multiplo_de_dois = numero % 2 == 0

    if multiplo_de_dois:
        return f'{numero} é par!'
    return f'{numero} é ímpar!'

print(identificador_par_impar(2))
print(identificador_par_impar(5))
print(identificador_par_impar(77))
print(identificador_par_impar(220)) 