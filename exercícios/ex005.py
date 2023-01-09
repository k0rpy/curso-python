# Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e o seu antecessor.
from rich import print 

numero = int(input('Digite um número inteiro: '))

antecessor = numero - 1
sucessor = numero + 1

print(f'O antecessor do número {numero} é {antecessor} e o sucessor é {sucessor}.')