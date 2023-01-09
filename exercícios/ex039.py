# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade: Se ele ainda vai se alistar ao serviço militar. Se é a hora de se alistar. Se já passou do tempo de alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import date

nascimento = int(input('Informe o ano de nascimento: '))

calculo = date.today().year - nascimento

if calculo == 18:
    print('Está na hora de se alistar!')
elif calculo < 18:
    print('Ainda não está na hora de se alistar.')
else:
    print('Passou da hora de se alistar.')