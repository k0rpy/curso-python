# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição do pagamento: à vista/cheque: 10% de desconto, à vista no cartão: 5% de desconto, em até 2x no cartão: preço normal, 3x ou mais no cartão: 20% de juros.
preço = int(input('Preço das compras: R$'))

print("""
FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
""")

opção = int(input('Qual é a opção? '))

if opção == 1:
    desconto = (preço * 10 / 100) - preço
    print(f'Sua compra de R${preço} vai custar R${desconto} no final.')
elif opção == 2:
    desconto = (preço * 5 / 100) - preço
    print(f'Sua compra de R${preço} vai custar R${desconto} no final.')
elif opção == 3:
    print(f'Sua compra vai custar R${preço} (não tem desconto)')