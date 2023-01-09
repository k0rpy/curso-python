# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento. 
from rich import print

salario = float(input('Digite o salário do funcionário: '))

print(f'O salário do funcionário com o reajuste é R${salario+(salario*15/100)}')