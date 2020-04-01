# Faça um Programa que leia três números e mostre o maior e o menor deles.
#testes: 1;2;3 ok// 1;3;2 ok// *2;1;3 erro// 2;3;1 ok//  3;2;1// 3;1;2

num1 = int(input('Digite um número'))
num2 = int(input('Digite um número'))
num3 = int(input('Digite um número'))

if num1 > num2 and num1 > num3:
    print(num1)
elif num2 > num1 and num2 > num3:
    print(num2)
elif num3 > num2 and num3 > num1:
    print(num3)

if num1 < num2 and num1 < num3:
    print(num1)
elif num2 < num1 and num2 < num3:
    print(num2)
elif num3 < num1 and num3 < num2:
    print(num3)
