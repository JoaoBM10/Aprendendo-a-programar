nome = input('Digite seu nome completo:').strip()
print('Analisando seu nome...')
print('Seu nome maiúsculo é {}.'.format(nome.upper()))
print('Seu nome minúsculo é {}.'.format(nome.lower()))
print('Seu nome tem ao todo {} letras.'.format(len(nome)-nome.count(' ')))
separar = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras.'.format(separar[0],len(separar[0])))

