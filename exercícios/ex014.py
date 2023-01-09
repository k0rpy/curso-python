# Escreva um programa que converta uma temperatura digita em °C e converta para °F
from rich import print

celsius = float(input('Digite a temperatura em °C: '))

fahrenheit = ((9*celsius)/5)+32

print(f'{celsius}°C transformado em °F é {fahrenheit}')