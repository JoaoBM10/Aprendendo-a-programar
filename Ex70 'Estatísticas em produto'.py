print('--'*20)
print(f'{'LOJA SUPER BARATÃO':^40}')
print('--'*20)

soma = maismil = contador = menorprod = menorval = 0

while True:
    contador += 1
    produto = str(input('Nome do produto:'))
    preco = float(input('Preço: R$'))
    soma += preco
    if preco >= 1000:
        maismil += 1
    if contador == 1:
        menorprod = produto
        menorval = preco
    if menorval > preco:
        menorval = preco
        menorprod = produto
    sair = ' '
    while sair not in 'SN':
        sair = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if sair == 'N':
        break
print(f'{' FIM DO PROGRAMA ':-^38}')
print(f'O total de compra foi de R${soma:.2f}')
print(f'Temos {maismil} produtos custando mais de R$1000,00 reais.')
print(f'O produto mais barato foi {menorprod} que custa R${menorval:.2f} reais')
