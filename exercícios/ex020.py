# O mesmo professor do desafio 019 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
import random
from rich import print

primeiroaluno = str(input('Digite o nome do primeiro aluno: '))
segundoaluno = str(input('Digite o nome do segundo aluno: '))
terceiroaluno = str(input('Digite o nome do terceiro aluno: '))
quartoaluno = str(input('Digite o nome do quarto aluno: '))

lista = [primeiroaluno, segundoaluno, terceiroaluno, quartoaluno]

random = random.shuffle(lista)

print(f'A ordem da apresentaçãos será {lista}')