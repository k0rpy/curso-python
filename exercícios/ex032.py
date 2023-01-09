# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
from datetime import date
from calendar import isleap
from rich import print

ano = int(input('Digite o ano, digite 0 para pegar o ano atual: '))

#Ano atual
if ano == 0:
    ano = date.today().year

if isleap(ano):
    print(f'O ano {ano} é bissexto.')
else:
    print(f'O ano {ano} não é bissexto.')