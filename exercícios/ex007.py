# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre sua média.
from rich import print

nota1 = int(input('Digite a primeira nota: ')) 
nota2 = int(input('Digite a segunda nota: '))

print(f'A sua média é {(nota1+nota2)/2}.')