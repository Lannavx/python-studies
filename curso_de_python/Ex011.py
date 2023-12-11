'''Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, 
sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.'''

largura = float(input('Informe a largura da parede: '))
altura = float(input('Informe a altura da parede: '))

area = largura * altura
litros = area / 2

print(f'A sua parede tem {area:.2f}m², logo, são necessários {litros:.1f}L de tinta para pintar essa parede.')