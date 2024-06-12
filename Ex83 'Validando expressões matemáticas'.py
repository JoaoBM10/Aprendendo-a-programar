expressao = str(input('Digite uma expressão matemática:'))
lista = []

for caracter in expressao:
    if caracter == '(':
        lista.append('(')
    elif caracter == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break
if len(lista) == 0:
    print('Sua expressão é válida.')
else:
    print('Sua expressão é inválida.')