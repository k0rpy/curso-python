# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
from rich import print

numero = int(input('Digite um número: '))

print(f"""
O dobro de {numero} vale {numero*2}
O triplo de {numero} vale {numero*3}
A raiz quadrada de {numero} vale {numero**(1/2)}
""")