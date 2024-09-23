'''Classe Retangulo: Crie uma classe que modele um retangulo:

Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
a. Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;
b.Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidades de um local. Depois, deve criar um objeto com as medidas e calcular a quantidade de pisos e de rodapés necessárias para o local.'''

class Retangulo():
    def __init__(self, comprimento: float, largura: float):
        self.comprimento = comprimento
        self.largura = largura

    def mudar_valor_lados(self, novo_valor_cumprimento: float, 
        novo_valor_largura: float):
        self.comprimento = novo_valor_cumprimento
        self.largura = novo_valor_largura

    def retornar_valor_lados(self):
       return self.comprimento, self.largura

    def calcular_area(self):
        return self.comprimento * self.largura

    def calcular_perimetro(self):
        return 2 * (self.comprimento + self.largura)         


# Solicita as medidas do local ao usuário
largura = float(input('Informe a largura do local: '))
comprimento = float(input('Informe o comprimento do local: '))

local = Retangulo(comprimento, largura)

area_local = local.calcular_area()
perimetro_local = local.calcular_perimetro()

print(f'\nÁrea do local: {area_local:.2f} m²')
print(f'Perímetro do local: {perimetro_local:.2f} m')