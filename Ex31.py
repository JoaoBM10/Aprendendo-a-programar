distancia_viagem = float(input('Qual é a distância da sua viagem?'))
print('Você está prestes a começar uma viagem de {}Km.'.format(distancia_viagem))

if distancia_viagem <= 200:
    valor_viagem = float(distancia_viagem * 0.5)
    print('E o preço da sua passagem será de R${}.'.format(valor_viagem))
else:
    valor_viagem = float(distancia_viagem * 0.5)
    desconto = float(valor_viagem - (valor_viagem * 0.1))
    print('E o preço da sua passagem será de R${:.2f}.'.format(desconto))

#Outro método

if distancia_viagem <= 200:
    valor = distancia_viagem * 0.5
else:
    valor = distancia_viagem * 0.45
print('E o preço da sua passagem será de R${:.2f}.'.format(valor))

#Outro método

valor = distancia_viagem * 0.5 if distancia_viagem <= 200 else distancia_viagem * 0.45
print('E o preço da sua passagem será de R${:.2f}.'.format(valor))