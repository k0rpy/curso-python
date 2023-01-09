# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa
import math
from rich import print

oposto = float(input('Comprimento do cateto oposto: '))
adjacente = float(input('Comprimento do cateto adjacente: '))

conta = math.hypot(oposto, adjacente)

print(f'A hipotenusa vai medir {conta}')