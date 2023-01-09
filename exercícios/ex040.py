# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida: Média abaixo de 5: reprovado, Média entre 5.0 e 6.9, recuperação e Média 7 ou superior, aprovado.
n1 = float(input('Digite uma nota: '))
n2 = float(input('Digite outra nota: '))

calculo = (n1 + n2) / 2

if calculo >= 7:
    print('APROVADO')
elif calculo >=5 and calculo < 7:
    print('RECUPERAÇÃO')
else:
    print('REPROVADO')