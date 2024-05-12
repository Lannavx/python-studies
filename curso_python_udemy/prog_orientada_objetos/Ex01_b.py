import json

# Importando variáveis e funções do primeiro arquivo
from Ex01_a import CAMINHO_ARQUIVO, Pessoa

# Abrindo o arquivo JSON para leitura
with open(CAMINHO_ARQUIVO, 'r', encoding='utf-8') as arquivo:
    pessoas = json.load(arquivo)

    # Recriando os objetos da classe Pessoa a partir dos dados carregados
    p1 = Pessoa(**pessoas[0])
    p2 = Pessoa(**pessoas[1])
    p3 = Pessoa(**pessoas[2])

# Exibindo os nomes e idades das pessoas instanciadas
    print(p1.nome, p1.idade)
    print(p2.nome, p2.idade)
    print(p3.nome, p3.idade)                      

