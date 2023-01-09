# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
from rich import print

metros = float(input('Digite a quantidade de metros: '))

milimetros = metros * 1000
centimetros = metros * 100

print(f'{metros*1000}m são {milimetros}mm e {centimetros*100}cm.')