# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade: Até 9 anos: Mirim, Até 14 anos: Infantil, Até 19 anos: Júnior, Até 20 anos: Sênior, Acima: Master
from datetime import date

nascimento = int(input('Digite o ano de nascimento: '))

idade = date.today().year - nascimento

if idade <= 9:
    print('MIRIM')
elif idade <= 14:
    print('INFANTIL')
elif idade <= 19:
    print('JUNIOR')
elif idade <= 25:
    print('SÊNIOR')
elif idade > 25:
    print('MASTER')