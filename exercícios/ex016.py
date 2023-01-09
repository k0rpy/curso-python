# Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.
import math
from rich import print

num = float(input('Digite um número: '))

conta = math.floor(num)

print(conta)