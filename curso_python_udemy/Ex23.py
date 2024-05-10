'''
Evitando uso de condicionais + Guard Clause

Evitar o uso de condicionais e aplicar o conceito de Guard Clauses ajuda a tornar o código mais legível e direto. 
Em vez de usar condicionais como if para controlar o fluxo, você usa Guard Clauses para lidar
com casos excepcionais ou erros no início de uma função. 
Isso reduz a profundidade de indentação e torna o código principal mais claro.
'''

# Código refatorado com uso de lambda

# Exercicio - Salvar a lista de tarefas em JSON

import json 

def listar(tarefas):
    print()
    if not tarefas:
        print('Nenhuma tarefa para listar')
        print()
        return

    print('Tarefas:')
    for tarefa in tarefas:
        print(f'\t{tarefa}')
    print()


def desfazer(tarefas, tarefas_refazer):
    print()
    if not tarefas:
        print('Nenhuma tarefa para desfazer')
        print()
        return

    tarefa = tarefas.pop()
    print(f'{tarefa=} removida da lista de tarefas.')
    tarefas_refazer.append(tarefa)
    print()
    listar(tarefas)


def refazer(tarefas, tarefas_refazer):
    print()
    if not tarefas_refazer:
        print('Nenhuma tarefa para refazer')
        print()
        return

    tarefa = tarefas_refazer.pop()
    print(f'{tarefa=} adicionada na lista de tarefas.')
    tarefas.append(tarefa)
    print()
    listar(tarefas)


def adicionar(tarefa, tarefas):
    print()
    tarefa = tarefa.strip()
    if not tarefa:
        print('Você não digitou uma tarefa.')
        return
    tarefas.append(tarefa)
    print()
    listar(tarefas)

# Função para ler as tarefas de um arquivo JSON
def ler(tarefas, caminho_arquivo):
    dados = []
    try:
        with open(caminho_arquivo, 'r', encoding='utf8') as arquivo:          # Tenta abrir o arquivo JSON para leitura
            dados = json.load(arquivo)                                        # Carrega os dados do arquivo JSON para a variável 'dados'
    except FileNotFoundError:
        print('Arquivo não existe')
        salvar(tarefas, caminho_arquivo)   # Chama a função salvar para criar um novo arquivo JSON com a lista de tarefas vazia ou existente
    return dados

# Função para salvar as tarefas em um arquivo JSON
def salvar(tarefas, caminho_arquivo):
    dados = tarefas
    with open(caminho_arquivo, 'w', encoding='utf8') as arquivo:              # Abre o arquivo JSON para escrita. Se o arquivo não existir, ele será criado.
        dados = json.dump(tarefas, arquivo, indent=2, ensure_ascii=False)     # Salva a lista de tarefas no arquivo JSON, formatando com indentação para melhor legibilidade
    return dados    


CAMINHO_ARQUIVO = 'ex23.json'
tarefas = ler([], CAMINHO_ARQUIVO)
tarefas_refazer = []

while True:
    print('Comandos: listar, desfazer e refazer')
    tarefa = input('Digite uma tarefa ou comando: ')

    comandos = {
        'listar': lambda: listar(tarefas),
        'desfazer': lambda: desfazer(tarefas, tarefas_refazer),
        'refazer': lambda: refazer(tarefas, tarefas_refazer),
        'adicionar': lambda: adicionar(tarefa, tarefas),
    }

    comando = comandos.get(tarefa) if comandos.get(tarefa) is not None else \
        comandos['adicionar']
    comando()
    salvar(tarefas, CAMINHO_ARQUIVO)    # Salva as alterações após cada comando  