# Strings são iteráveis
'''
Dizer que uma string é iterável significa que podemos percorrer, ou iterar,
cada um dos caracteres que compõem a string de forma sequencial. 
'''

# Iteração com loops
''' 
Por serem iteráveis, podemos usar loops (como for ou while) para acessar
e operar sobre cada caractere individualmente. 
'''

nome = 'Ana Lucia' 

indice = 0
novo_nome = ''
while indice < len(nome):   
    letra = nome[indice] # Acessa o caractere na posição 'indice' da string 'nome' e o atribui a 'letra'
    novo_nome += f'-{letra}' # Concatena um traço no caractere atual
    indice += 1 # Incrementa 'indice' em 1 para passar ao próximo caractere

novo_nome += '-'
print(novo_nome)    

'''
Cada caractere em uma string tem um índice associado, que pode ser positivo ou negativo.
Índices positivos começam em 0 e aumentam da esquerda para a direita.
Índices negativos começam em -1 e diminuem da direita para a esquerda.
'''

# Exemplo de índices
# Índices positivos: 012345678
#            nome = 'Ana Lucia'
# Índices negativos: 987654321