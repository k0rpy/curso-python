# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
from rich import print

salario = float(input('Digite o salário do funcionário: '))

if salario <= 1250:
    novosalario = salario + (salario * 15 / 100)
else:
    novosalario = salario + (salario * 10 / 100)

print(f'Quem ganhava R${salario} passa a ganhar R${novosalario} c   om o aumento.')