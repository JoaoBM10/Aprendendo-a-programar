contagem = ('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez',
            'onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito',
            'dezenove','vinte')

while True:
    valor = int(input('Digite um número entre 0 e 20:'))
    if valor > 20:
        print('Valor inválido.')
    else:
        break
print(f'Você digitou o número {contagem[valor]}.')