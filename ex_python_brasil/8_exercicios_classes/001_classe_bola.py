'''Classe Bola: Crie uma classe que modele uma bola:

a. Atributos: Cor, circunferência, material
b. Métodos: trocaCor e mostraCor'''

class Bola():
    def __init__(self, cor, circunferencia, material):
        self.cor = cor  
        self.circunferencia = circunferencia
        self.material = material

    def trocarCor (self, nova_cor):
        self.cor = nova_cor

    def mostrarCor (self):
        return self.cor

# Instancia um objeto da classe Bola
bola = Bola('Laranja', 27.2, 'Borracha')


print(f'Cor inicial da bola: {bola.mostrarCor()}')  

bola.trocarCor('Vermelho')  

print(f'Nova cor da bola: {bola.mostrarCor()}')     