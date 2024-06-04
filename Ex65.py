num = soma = contador = maior = menor = 0
sair = False

while not sair:
    contador += 1
    num = int(input('Digite um número:'))
    soma += num
    if contador == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num 
    continuar = str(input('Quer continuar? [S/N]')).upper()
    if continuar == 'N':
        sair = True
    elif continuar == 'S': 
        continue
    else:
        print('Valor invalido.')
        continuar = str(input('Quer continuar? [S/N]')).upper()
        if continuar == 'N':
                sair = True
        elif continuar == 'S': 
            continue
media = soma / contador
print(f'Você digitou {contador} números, a soma foi {soma} e a média foi {media}')
print(f'O maior valor foi {maior} e o menor foi {menor}.')