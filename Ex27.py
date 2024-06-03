n = str(input('Digite seu nome completo:')).strip()
print('Seu primeiro nome é {}'.format(n.split()[0]))
print('Seu ultimo nome é {}'.format(n.split()[len(n.split())-1]))
