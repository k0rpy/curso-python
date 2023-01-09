# Crie um programa que leia um número e mostre na tela se ele é par ou ímpar.
from rich import print

numero = int(input('Digite um número: '))

if (numero % 2) == 0:
    print('O número é par.')
else:
    print('O número é impar.')