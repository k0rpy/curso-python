# Crie um programa que faça o computador jogar Jokenpô com você.
from random import randint

itens = ['pedra', 'papel', 'tesoura']

print("""
Suas opções:
[ 1 ] PEDRA
[ 2 ] PAPEL
[ 3 ] TESOURA
""")

jogada = int(input('Qual é a sua jogada? '))
cpu = randint(1, 3)

if cpu == 1:
    if jogada == 1:
        print('VOCÊ ESCOLHEU: PEDRA')
        print('CPU ESCOLHEU: PEDRA\n')
        print('EMPATE')
    elif jogada == 2:
        print('VOCÊ ESCOLHEU: PAPEL')
        print('CPU ESCOLHEU: PEDRA\n')
        print('JOGADOR VENCEU!')
    elif jogada == 3:
        print('VOCÊ ESCOLHEU: TESOURA')
        print('CPU ESCOLHEU: PEDRA\n')
        print('CPU VENCEU!')
    else:
        print('Opção inválida.')
elif cpu == 2:
    if jogada == 1:
        print('VOCÊ ESCOLHEU: PEDRA')
        print('CPU ESCOLHEU: PAPEL\n')
        print('CPU VENCEU!')
    elif jogada == 2:
        print('VOCÊ ESCOLHEU: PEDRA')
        print('CPU ESCOLHEU: PAPEL\n')
        print('CPU VENCEU!')
    elif jogada == 3:
        print('VOCÊ ESCOLHEU: TESOURA')
        print('CPU ESCOLHEU: PAPEL\n')
        print('JOGADOR VENCEU!')
    else:
        print('Opção inválida.')
elif cpu == 3:
    if jogada == 1:
        print('VOCÊ ESCOLHEU: PEDRA')
        print('CPU ESCOLHEU: TESOURA\n')
        print('JOGADOR VENCEU!')
    elif jogada == 2:
        print('VOCÊ ESCOLHEU: PAPEL')
        print('CPU ESCOLHEU: TESOURA\n')
        print('CPU VENCEU!')
    elif jogada == 3:
        print('VOCÊ ESCOLHEU: TESOURA')
        print('CPU ESCOLHEU: PEDRA\n')
        print('CPU VENCEU!')
    else:
        print('Opção inválida.')