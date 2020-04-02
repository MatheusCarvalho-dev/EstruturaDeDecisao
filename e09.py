# Faça um Programa que leia três números e mostre-os em ordem decrescente. 312

num1 = int(input('Digite um número'))
num2 = int(input('Digite um número'))
num3 = int(input('Digite um número'))

if num1 < num2 and num2 < num3:
    print(num3), print(num2), print(num1) #123
if num1 < num3 and num3 < num2:
    print(num2), print(num3), print(1) #132

if num2 < num1 and num1 < num3:
    print(num3), print(num1), print(num2) #213 
if num3 < num1 and num1 < num2:
    print(num2), print(num1), print(num3) #231

if num2 < num3 and num3 < num1:
    print(num1), print(num3), print(num2) #321
if num3 < num2 and num2 < num1:
    print(num1), print(num2), print(num3)  #312
 
