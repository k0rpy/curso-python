# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
from rich import print

carteira = float(input('Digite quanto de dinheiro você tem na carteira: '))

conversão = carteira / 3.27

print(f'Você pode comprar {conversão} dólares.')