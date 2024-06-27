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