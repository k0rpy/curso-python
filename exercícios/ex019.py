# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
import random
from rich import print

primeiroaluno = str(input('Primeiro aluno: '))
segundoaluno = str(input('Segundo aluno: '))
terceiroaluno = str(input('Terceiro aluno: '))
quartoaluno = str(input('Quarto aluno: '))

lista = [primeiroaluno, segundoaluno, terceiroaluno, quartoaluno]

print(f'O aluno escolhido foi {random.choice(lista)}')