def aumentar(preco = 0, taxa = 0, formatar = False):
    valor = preco + (preco * taxa/100)
    if formatar is False:
        return valor 
    else:
        return moeda(valor)


def diminuir(preco = 0, taxa = 0, formatar = False):
    valor = preco - (preco * taxa/100)
    if formatar is False:
        return valor
    else:
        return moeda(valor)


def dobro(preco = 0, formatar = False):
    valor = preco * 2
    if formatar is False:
        return valor
    else:
        return moeda(valor)


def metade(preco = 0, formatar = False):
    valor = preco / 2
    if formatar is False:
        return valor
    else:
        return moeda(valor)

def moeda(preco = 0, moeda = 'R$'):
    return f'{moeda}{preco:.2f}'.replace('.',',')


def resumo(preco = 0, taxa = 10, taxa2 = 5):
    print('='*32)
    print('RESUMO DO VALOR'.center(32))
    print('='*32)
    print(f'Preço analisado: \t{moeda(preco)}')
    print(f'Dobro do preço: \t{dobro(preco, True)}')
    print(f'Metade do preço: \t{metade(preco, True)}')
    print(f'Com {taxa}% de aumento: \t{aumentar(preco, taxa, True)}')
    print(f'Com {taxa2}% de redução: \t{diminuir(preco, taxa2, True)}')
    print('='*32)
