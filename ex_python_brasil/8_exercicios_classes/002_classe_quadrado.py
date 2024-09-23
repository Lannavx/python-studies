'''Classe Quadrado: Crie uma classe que modele um quadrado:

a. Atributos: Tamanho do lado
b. Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;'''

class Quadrado():
    def __init__(self, tamanho_lado: float):
        self.tamanho_lado = tamanho_lado

    def mudar_valor_lado(self, novo_valor: float):
        self.tamanho_lado = novo_valor

    def retornar_valor_lado(self):
        return self.tamanho_lado

    def calcular_area(self):
         return self.tamanho_lado ** 2


quadrado = Quadrado(4)

quadrado.mudar_valor_lado(8)

print(quadrado.retornar_valor_lado())
print(quadrado.calcular_area())