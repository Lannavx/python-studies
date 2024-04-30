'''
Uma closure é uma técnica onde uma função interna lembra as variáveis de seu ambiente de criação, 
mesmo depois de a função externa ter terminado. 
Isso permite que a função interna use essas variáveis em chamadas futuras.
'''

# Exercício - Adiando execução de funções

def soma(x, y):
    return x + y


def multiplica(x, y):
    return x * y


def criar_funcao(funcao, x):      # Função que cria uma closure. Ela recebe uma função e um valor 'x' como parâmetros.
    def interna (y):              # A função interna é definida aqui. Ela lembra 'funcao' e 'x' do escopo da função 'criar_funcao'.
        return funcao(x, y)       # Usa a função lembrada com 'x' fixo e 'y' passado na hora.
    return interna                # Retorna a função 'interna', que agora é uma closure que lembra 'funcao' e 'x'.
    

soma_com_cinco = criar_funcao(soma,5 )               
multiplica_por_dez = criar_funcao(multiplica, 10)    

print(soma_com_cinco(10))                      # Executa a closure 'soma_com_cinco' passando 10 como 'y'
print(multiplica_por_dez(10))                  # Executa a closure 'multiplica_por_dez' passando 10 como 'y'

'''
Esse uso de closures é particularmente útil para adiar a aplicação de uma função até que todos os argumentos 
necessários estejam disponíveis, permitindo também a reutilização de funções com diferentes parâmetros iniciais.
'''