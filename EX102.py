def fatorial(num, show=True):
    """
    Calcula o Fatorial de um número.
    :param num: O número a ser calculado.
    :param show: (opcional) Mostrar ou não o calculo feito.
    :return: O valor do Fatorial de um número num.
    """
    fat = 1
    for numero in range(num, 0, -1):
        fat *= numero
        if show:
            print(numero, end = '')
            if numero > 1:
                print(' x ', end = '')
            else:
                print(' = ', end = '')
    return fat

valor = int(input('Digite o valor para calcular seu fatorial:'))
print(fatorial(valor, True))
help(fatorial)