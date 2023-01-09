# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar. Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.
valor = float(input('Digite o valor da casa: R$'))
salario = float(input('Digite o salário do comprador: R$'))
anos = int(input('Digite em quantos anos ele vai pagar: '))

calculo = valor / (anos * 12)

if calculo >= (salario * 30 / 100):
    print('O empréstimo não foi aprovado!')
else:
    print('O empréstimo foi aprovado!')