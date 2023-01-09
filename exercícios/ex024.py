# Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".
from rich import print

cidade = str(input('Digite o nome da cidade em que você nasceu: ')).strip()

santo = cidade[:5].upper() == 'SANTO'

print(f'{santo}')