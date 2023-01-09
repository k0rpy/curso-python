# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal, 3 para hexadecimal.
numero = int(input('Digite um número inteiro: '))

binario = bin(numero)
octal = oct(numero)
hexadecimal = hex(numero)

print("""
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL
""")

opcao = int(input('Digite a sua opção: '))

if opcao == 1:
    print(binario)
elif opcao == 2:
    print(octal)
elif opcao == 3:
    print(hexadecimal)
else:
    print('Opção não existe.')