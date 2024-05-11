'''
Sets - Conjuntos em Python (tipo set)

Sets em Python são mutáveis, porém aceitam apenas tipos imutáveis como valor interno.
Criando um set: set(iterável) ou {1, 2, 3}

Sets são eficientes para remover valores duplicados de iteráveis.
    Não aceitam valores mutáveis;
    Seus valores serão sempre únicos;
    Não tem índexes;
    Não garantem ordem;
    São iteráveis (for, in, not in)

Métodos úteis: add, update, clear, discard

Operadores úteis:
    união | união (union) - Une
    intersecção & (intersection) - Itens presentes em ambos
    diferença - Itens presentes apenas no set da esquerda
    diferença simétrica ^ - Itens que não estão em ambos
'''

# Exercício usando set

'''
Crie uma função que encontra o primeiro duplicado considerando o segundo
número como a duplicação. Retorne a duplicação considerada.
Requisitos:
    A ordem do número duplicado é considerada a partir da segunda
    ocorrência do número, ou seja, o número duplicado em si.
    Exemplo:
        [1, 2, 3, ->3<-, 2, 1] -> 1, 2 e 3 são duplicados (retorne 3)
        [1, 2, 3, 4, 5, 6] -> Retorne -1 (não tem duplicados)
        [1, 4, 9, 8, ->9<-, 4, 8] (retorne 9)
    Se não encontrar duplicados na lista, retorne -1
'''

lista_de_listas_de_inteiros = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],
    [1, 3, 2, 2, 8, 6, 5, 9, 6, 7],
    [3, 8, 2, 8, 6, 7, 7, 3, 1, 9],
    [4, 8, 8, 8, 5, 1, 10, 3, 1, 7],
    [1, 3, 7, 2, 2, 1, 5, 1, 9, 9],
    [10, 2, 2, 1, 3, 5, 10, 5, 10, 1],
    [1, 6, 1, 5, 1, 1, 1, 4, 7, 3],
    [1, 3, 7, 1, 10, 5, 9, 2, 5, 7],
    [4, 7, 6, 5, 2, 9, 2, 1, 2, 1],
    [5, 3, 1, 8, 5, 7, 1, 8, 8, 7],
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
]


def primeiro_duplicado(lista_inteiros):
    numeros_checados = set()   # Inicializa um conjunto para armazenar os números já vistos e verificar duplicatas.
    primeiro_duplicado = -1    # O valor padrão -1 será retornado se não houver duplicatas na lista

    for numero in lista_inteiros:
        if numero in numeros_checados:       # Checa se o número já foi visto (está no conjunto numeros_checados).
            primeiro_duplicado = numero      # Se já foi visto, então é um duplicado. Atualiza primeiro_duplicado com esse número.
            break                            # Interrompe o loop, pois encontra o primeiro duplicado.

        numeros_checados.add(numero)         # Se não foi visto, adiciona o número ao conjunto para monitorar futuras ocorrências.


    return primeiro_duplicado                # Retorna o primeiro número duplicado encontrado, ou -1 se nenhum duplicado foi encontrado.
   
for lista in lista_de_listas_de_inteiros:    # Testa a função em todas as listas e imprime o resultado.
    print(lista, primeiro_duplicado(lista))

