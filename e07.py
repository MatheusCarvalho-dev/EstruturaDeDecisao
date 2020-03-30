# Faça um Programa que leia três números e mostre o maior e o menor deles.

num1 = int(input('Digite um número'))
num2 = int(input('Digite um número'))
num3 = int(input('Digite um número'))

if num1 > num2 and num1 > num3:
    print(num1)
elif num1 < num2 and num2 > num3:
    print(num2)
elif num1 < num2 < num3:
    print(num3)
if num1 < num2 < num3:
    print(num1)
elif num2 < num1 < num3:
    print(num2)
elif num3 < num1 < num2:
    print(num3)
    
