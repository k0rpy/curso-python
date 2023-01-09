# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$ 7,00 por cada Km acima do limite.
from rich import print

velocidade = float(input('Digite a velocidade do carro: '))
multa = (velocidade - 80) * 7

if velocidade <= 80:
    print('Você está abaixo da velocidade permitida.')
else :
    print(f'Você está acima da velocidade permitida, você deve pagar uma multa de R${multa}')