# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$ 0,50 por Km para viagens de até 200km e R$0,45 para viagens mais longas.
from rich import print

km = int(input('Digite a distância da sua viagem: '))

if km <= 200:
    print(f'O preço da passagem será de R${km*0.50}')
else:
    print(f'O preço da passagem será de R${km*0.45}')