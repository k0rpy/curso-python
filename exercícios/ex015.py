# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
from rich import print

km = int(input('Digite a quantidade de Km percorridos: '))
dias = int(input('Digite a quantidade de dias pelos quais o carro foi alugado: '))

conta = (km * 0.15) + (dias * 60)

print(f'O total a pagar é de R${conta}')