# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
from rich import print

n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
n3 = int(input('Digite o terceiro valor: '))

# Menor
if n1 < n2 and n1 < n3:
    menor = n1
if n2< n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
# Maior 
if n1 > n2 and n1 > n3:
    maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3

print(f'O menor número é: {menor}')
print(f'O maior número é: {maior}')