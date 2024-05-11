'''
Introdução à função lambda (função anônima de uma linha)
A função lambda é uma função como qualquer outra em Python. 
Porém, são funções anônimas que contém apenas uma linha. Ou seja, tudo deve ser contido dentro de uma única expressão.


Shallow copy > copia as referências dos objetos contidos em uma estrutura de dados
Deep copy > cria cópias novas e independentes de todos os objetos contido


List comprehension é uma forma concisa de criar listas. 
Ela permite gerar novas listas aplicando uma expressão a cada elemento de uma sequência iterável, podendo também incorporar condições.


Empacotamento e desempacotamento em Python referem-se à manipulação de tuplas e listas. 
Empacotamento permite agrupar vários valores em uma única variável. 
Desempacotamento é o processo inverso, atribuindo os valores de uma tupla ou lista a variáveis individuais.
'''

# Exercícios

# Ex1. Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)

# Ex2. Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

# Ex3. Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)
 
import copy

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

'''A função copy.deepcopy() é usada antes de qualquer operação que modifique os produtos para garantir que a lista original não seja alterada. 
Isso é essencial em contextos onde a integridade dos dados originais precisa ser mantida.

A função round() é utilizada para garantir que o preço atualizado tenha apenas dois dígitos após a vírgula.
O que é comum em preços para manter a consistência e precisão monetária.'''

# Ex1.
novos_produtos = [
    {**produto, 'preco': round(produto['preco'] * 1.1, 2)}
    for produto in copy.deepcopy(produtos) 
]

# Ex2.
produtos_ordenados_por_nome = sorted(
    copy.deepcopy(produtos),
    key=lambda produto: produto['nome'],
    reverse=True
)
# O uso de reverse=True na função sorted() inverte a ordem padrão de ordenação (que seria crescente), permitindo assim a ordenação decrescente.

# Ex3.
produtos_ordenados_por_preco = sorted(
    copy.deepcopy(produtos), 
    key=lambda produto: produto['preco']
)

#Listas Finais

print('Lista Original',
       *produtos, sep='\n')
print()
print('Novos Produtos',
       *novos_produtos, sep='\n')
print()
print('Produtos Ordenados por Nome',
      *produtos_ordenados_por_nome, sep='\n')
print()
print('Produtos Ordenados por Preço',
      *produtos_ordenados_por_preco, sep='\n')