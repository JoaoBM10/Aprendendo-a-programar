def calculo_area(l, c):
    a = l * c
    print(f'A área do terreno {l} x {c} é de {a}m².')


print(f'{'CONTROLE DE TERRENOS':^40}')
print('='*40)

largura = float(input('LARGURA (m):'))
comprimento = float(input('COMPRIMENTO (m):'))

calculo_area(largura, comprimento)