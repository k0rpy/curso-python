# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.
from rich import print

algo = input('Digite algo: ')

print(f"""
O tipo primitivo é: {type(algo)}
É alfabetico? {algo.isalpha()}
É numérico? {algo.isnumeric()}
É espaços? {algo.isspace()}
Está em maíusculas? {algo.isupper()}
Está em minúsculas? {algo.islower()}
Apenas a primeira letra em maíusculas? {algo.istitle()}
""")