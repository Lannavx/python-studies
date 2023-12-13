"""
    João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. 
    Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo 
    (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente.
     
    João precisa que você faça um programa que: 
        1. Leia a variável peso (peso de peixes) e calcule o excesso. 
        2. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. 
        3. Imprima os dados do programa com as mensagens adequadas.

"""
peso_peixe = float(input('Informe o peso adquirido hoje: '))
peso_limite = 50
taxa_multa = 4
if peso_peixe > peso_limite:
    diferença_peso = peso_peixe - peso_limite
    multa = diferença_peso * taxa_multa
    print(f'O peso de peixes excede {diferença_peso:.2f}kgs, logo será aplicado uma multa no total de R${multa:.2f}')
else:
    print('Peso dentro do regulamento!')    
print('Tenha um bom dia!')    