# Escreva uma programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
from rich import print

import random

numero = random.randint(1, 5)

jogador = int(input('Qual o número que eu pensei? '))

if jogador == numero:
    print('Você acertou!')
else:
    print(f'Você errou, o número escolhido foi {numero}')