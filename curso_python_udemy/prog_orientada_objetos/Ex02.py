'''
Property
Uma property em Python é uma maneira de controlar o acesso a um atributo de uma classe. 
Ela permite definir métodos que podem ser acessados como se fossem atributos, facilitando a leitura 
e a escrita de dados, além de encapsular a lógica necessária para esses acesso

Getters
Um getter é um método que obtém (ou "pega") o valor de um atributo. 
Ele é usado para acessar o valor de um atributo privado ou protegido de uma classe. 
Em Python, é definido usando o decorador @property.

Setters
Um setter é um método que define (ou "seta") o valor de um atributo. 
Ele é usado para modificar o valor de um atributo privado ou protegido de uma classe. 
Em Python, é definido usando o decorador @<property_name>.setter.

Associação
Associação é um tipo de relacionamento entre duas classes onde os objetos de uma classe podem usar ou 
interagir com objetos de outra classe. É como uma conexão ou vínculo entre os objetos, 
mas eles podem existir de forma independente.
'''


# Exercício com classes

# 1 - Crie uma classe Carro (Nome)
# 2 - Crie uma classe Motor (Nome)
# 3 - Crie uma classe Fabricante (Nome)
# 4 - Faça a ligação entre Carro tem um Motor
#   Obs.: Um motor pode ser de vários carros
# 5 - Faça a ligação entre Carro e um Fabricante
#   Obs.: Um fabricante pode fabricar vários carros

# Exiba o nome do carro, motor e fabricante na tela


class Carro:
    def __init__(self, nome):
        self.nome = nome
        self._motor = None
        self._fabricante = None

    # Propriedade para acessar o motor do carro
    @property # Definindo o getter usando @property
    def motor(self):
        return self._motor    
    
    # Propriedade para definir o motor do carro
    @motor.setter # Definindo o setter usando @<property_name>.setter
    def motor(self, valor):
        self._motor  = valor

    # Propriedade para acessar o fabricante do carro
    @property # Definindo o getter usando @property
    def fabricante(self):
        return self._fabricante    
    
    # Propriedade para definir o fabricante do carro
    @fabricante.setter # Definindo o setter usando @<property_name>.setter
    def fabricante(self, valor):
        self._fabricante  = valor
    

class Motor:
    def __init__(self, nome):
        self.nome = nome


class Fabricante:
    def __init__(self, nome):
        self.nome = nome 


fiat_uno = Carro('Uno')                                              # Criação de um objeto Carro chamado fiat_uno
fiat = Fabricante('Fiat')                                            # Criação de um objeto Fabricante chamado fiat
motor_2 = Motor('2.0')                                               # Criação de um objeto Motor chamado motor_2
fiat_uno.fabricante = fiat                                           # Associação do fabricante fiat ao carro fiat_uno usando o setter
fiat_uno.motor = motor_2                                             # Associação do motor motor_2 ao carro fiat_uno usando o setter
print(fiat_uno.nome, fiat_uno.fabricante.nome, fiat_uno.motor.nome)

# Outros Exemplos

corolla = Carro('Corolla')
toyota = Fabricante('Toyota')
corolla.fabricante = toyota
corolla.motor = motor_2
print(corolla.nome, corolla.fabricante.nome, corolla.motor.nome)

nivus = Carro('Nivus')
volkswagen = Fabricante('Volkswagen')
motor_3 = Motor('3.0')
nivus.fabricante = volkswagen
nivus.motor = motor_3
print(nivus.nome, nivus.fabricante.nome, nivus.motor.nome)

gol = Carro('Gol')
gol.fabricante = fiat
gol.motor = motor_3
print(gol.nome, gol.fabricante.nome, gol.motor.nome)
