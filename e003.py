#Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

v1= str(input('Digite F se for do sexo feminino e M se for do sexo masculino.'))

if v1 =='f':
    print('Feminino')
elif v1 =='m':
    print('Masculino')
else:
    print('Sexo Inválido.')
