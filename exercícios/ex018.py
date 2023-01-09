# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo
import math
from rich import print

ângulo = float(input('Digite o ângulo: '))

seno = math.sin(math.radians(ângulo))
cosseno = math.cos(math.radians(ângulo))
tangente = math.tan(math.radians(ângulo))

print(f'O ângulo de {ângulo} tem o seno de {seno}')
print(f'O ângulo de {ângulo} tem o cosseno de {cosseno}')
print(f'O ângulo de {ângulo} tem o tangente de {tangente}')