# Crie um programa que pergunte ao usuário o nome dele e em seguida dê boas vindas.
from rich import print

nome = input('Digite o seu nome: ')

print(f'Olá [blue]{nome}[/], seja bem vindo(a)!')