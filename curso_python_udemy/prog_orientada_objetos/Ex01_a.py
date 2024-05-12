'''
Json (JavaScript Object Notation)

O módulo json em Python é usado para trabalhar com o formato JSON, que é um padrão para troca de dados entre sistemas. 

As principais funções incluem:
json.dump() e json.dumps(): Transformam dados do Python (como dicionários e listas) em JSON.
json.load() e json.loads(): Convertem dados em formato JSON de volta para estruturas de dados do Python.

dumps e loads > O "s" no final significa "string".


Classes

Classes em Python são estruturas que permitem a modelagem de objetos no paradigma de Programação Orientada a Objetos (POO). 
Elas funcionam como moldes para criar objetos que encapsulam dados e funções relacionados a esses dados. 
As classes podem conter atributos (dados) e métodos (funções) para definir o comportamento dos objetos.
'''

# Exercício - Salve sua classe em JSON

# Salve os dados da sua classe em JSON e depois crie novamente as instâncias da classe com os dados salvos.
# Faça em arquivos separados.

import json

# Definindo o caminho onde o arquivo JSON será salvo
CAMINHO_ARQUIVO = 'curso_python_udemy/prog_orientada_objetos/ex01.json'

# Definição da classe Pessoa com nome e idade como atributos
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

# Instanciando três objetos da classe Pessoa
pessoa_1 = Pessoa('João', 33)
pessoa_2 = Pessoa('Helena', 21)
pessoa_3 = Pessoa('Joana', 11)

# Criando uma lista de dicionários, onde cada dicionário representa os atributos de uma Pessoa
bd = [vars(pessoa_1), vars(pessoa_2), vars(pessoa_3)]

# Função para gravar a lista de dicionários em um arquivo JSON
def fazer_dump():
    with open(CAMINHO_ARQUIVO, 'w', encoding='utf8') as arquivo:
        json.dump(bd, arquivo, ensure_ascii=False, indent=2)

# Verificação se este script é o principal executado. Se for, executa o dump dos dados.
if __name__ == '__main__':
    print('Ele é o __main__')
    fazer_dump()
