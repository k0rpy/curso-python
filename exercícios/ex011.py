# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m².
from rich import print

altura = int(input('Digite a altura da parede: '))
largura = int(input('Digite a largura da parede: '))

area = altura * largura

print(f'A área da parede é {area}m²')

tinta = area / 2

print(f'Para pintar esta parede, você precisará de {tinta}l de tinta.')