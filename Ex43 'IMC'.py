peso = float(input('Digite o seu peso?'))
alt = float(input('Digite a sua altura?'))

imc = peso / alt ** 2
print('O IMC é de {:.1f}.'.format(imc))

if imc > 40:
    print('Obesidade mórbida')
elif imc > 30:
    print('Obesidade')
elif imc > 25:
    print('Sobrepeso')
elif imc > 18.5:
    print('Peso ideal')
else:
    print('Abaixo do peso')
