'''Um professor quer sortear um dos seus quatro alunos para apagar o quadro. 
Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.'''

import random
nome1 = input('Insira o nome do prinmeiro aluno: ')
nome2 = input('Insira o nome do segundo aluno: ')
nome3 = input('Insira o nome do terceiro aluno: ')
nome4 = input('Insira o nome do quarto aluno: ')
nomes = [nome1, nome2, nome3, nome4]
sorteio = random.choice(nomes)
print(f'O aluno escolhido foi: {sorteio}')