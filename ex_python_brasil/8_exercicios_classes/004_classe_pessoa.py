'''Classe Pessoa: Crie uma classe que modele uma pessoa:

a. Atributos: nome, idade, peso e altura
b. Métodos: Envelhercer, engordar, emagrecer, crescer. 
Obs: Por padrão, a cada ano que nossa pessoa envelhece, sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm.'''

class Pessoa:
    def __init__(self, nome: str, idade: int, peso: float, altura: int):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura  # Altura em centímetros

    def envelhecer(self):
        if self.idade < 21:
            self.crescer(0.5)
        self.idade += 1

    def engordar(self, kg: float):
        self.peso += kg

    def emagrecer(self, kg: float):
        self.peso -= kg

    def crescer(self, cm: float):
        self.altura += cm

    def __str__(self):
        """
        Retorna uma representação em string dos atributos da pessoa.
        """
        return (f'Nome: {self.nome}\n'
                f'Idade: {self.idade} anos\n'
                f'Peso: {self.peso:.1f} kg\n'
                f'Altura: {self.altura:.1f} cm')


pessoa = Pessoa('João', 15, 70, 170)

anos_para_envelhecer = 10
for ano_atual in range(anos_para_envelhecer):
    pessoa.envelhecer()

    # A cada 2 anos, João engorda 2 kg
    if ano_atual % 2 == 0: 
        pessoa.engordar(2)
    # Nos anos ímpares, João emagrece 0,5 kg    
    else: 
        pessoa.emagrecer(0.5)

print('\nEstado final da pessoa:')
print(pessoa)
