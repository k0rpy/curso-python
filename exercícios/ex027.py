# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
from rich import print

nome = str(input('Digite o seu nome completo: ')).strip()

n = nome.split()

primeironome = n[0]
ultimonome = n[-1]

print(f"""
Seu primeiro nome é {primeironome}
Seu último nome é {ultimonome}
""")