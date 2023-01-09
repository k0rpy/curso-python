# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
from rich import print

nome = str(input('Digite o nome: ')).strip()

silva = 'silva ' in nome.lower()

print(f'{silva}')