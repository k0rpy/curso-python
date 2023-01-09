# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
from rich import print

produto = float(input('Digite o preço do produto: '))

print(f'O produto que custava {produto}R$ está custando {produto-(produto*5/100)}R$ com desconto de 5%.')