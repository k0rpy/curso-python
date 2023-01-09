# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo: Abaixo de 18.5: Abaixo do Peso. Entre 18 e 25: Peso ideal. 25 até 30: 
peso = float(input('Qual é seu peso? '))
altura = float(input('Qual é sua altura? '))

imc = peso / (altura ** 2)

print(f'O IMC dessa pessoa é {imc}')

if imc < 18.5:
    print('Você está abaixo do peso!')
elif imc < 25:
    print('Você está no peso ideal!')
elif imc < 30:
    print('Você está com sobrepeso!')
elif imc < 40:
    print('Você está com obesidade!')
elif imc > 40:
    print('Você está com obesidade mórbida!')