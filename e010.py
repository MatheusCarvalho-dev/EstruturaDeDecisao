# Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou
# N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", 
# conforme o caso.


turno = str(input('Qual turno você é? Digite M-matutino ou V-Vespertino ou N- Noturno.'))
if turno == 'm':
    print('Bom dia!')
if turno == 'M':
    print('Bom dia!')
elif turno == 'v':
    print('Bom dia!')
elif turno == 'V':
    print('Boa tarde!')
elif turno == 'n':
    print('Boa noite!')
elif turno == 'NM':
    print('Boa noite!')
else:
    print('Valor Inválido!')
    
