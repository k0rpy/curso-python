# Crie um programa que leia o nome completo de uma pessoa e mostre: - O nome com todas as letras maiúsculas e minúsculas. - Quantas letras ao todo (sem considerar espaços). - Quantas letras tem o primeiro nome.
from rich import print

nome = str(input('Digite o seu nome completo: '))

separa = nome.split()
letras = len(nome)-nome.count(' ')

print(f'Todos os caracteres em letra maíuscula: {nome.upper()}')
print(f'Todos os caracteres em letra minúscula: {nome.lower()}')
print(f'Seu nome ao todo tem {letras} letras')
print(f'Seu primeiro nome é {separa[0]} e ele tem {len(separa[0])} letras')