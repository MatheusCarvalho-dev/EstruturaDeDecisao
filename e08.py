#Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

num1 = float(input('Digite o preço do produto'))
num2 = float(input('Digite o preço do produto'))
num3 = float(input('Digite o preço do produto'))

if num1 < num2 and num1 < num3:
    print(num1)
elif num2 < num1 and num2 < num3:
    print(num2)
elif num3 < num1 and num3 < num2:
    print(num3)
