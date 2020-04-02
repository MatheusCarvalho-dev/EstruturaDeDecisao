# Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

num1 = float(input('Digite um número'))
if num1 == 0:
    print(num1, ' é neutro (0)')
if num1 > 0:
    print(num1, ' é positivo!')
if num1 < 0:
    print(num1, ' é negativo!')
