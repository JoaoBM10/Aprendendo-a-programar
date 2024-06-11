valores = list()

for contador in range(0,5):
    valor = int(input('Digite um valor:'))
    if contador == 0:
        valores.append(valor)
        print('O valor foi adicionado no inicio da lista.')
    elif valor > valores[-1]:
        valores.append(valor)
        print('O valor foi adicionado no final da lista.')
    else:
        posicao = 0
        while posicao < len(valores):
            if valor <= valores[posicao]:
                valores.insert(posicao, valor)
                print(f'O valor foi adicionado na posição {posicao}.')
                break
            posicao += 1
print(valores)