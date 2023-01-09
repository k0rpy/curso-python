# Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A", em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
from rich import print

frase = str(input('Digite uma frase: ')).upper()

count = frase.count('A')
primeiraposicao = frase.find('A') + 1
ultimaposicao = frase.rfind('A') + 1

print(f"""
A letra A aparece {count} vezes na frase.
A primeira letra A aparece na posição {primeiraposicao}
A última letra A aparece na posição {ultimaposicao}
""")