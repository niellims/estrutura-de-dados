# Crie um dicionário simples
dicionario_simples = {
    'Daniel': 24,
    'Joan': 55,
    'Joaquim': 80
}

# Acesse valores em um dicionário
print(dicionario_simples.get('Daniel'))

# Adicione e remova elementos
dicionario_simples['Sthefany'] = 25
dicionario_simples.pop('Joan')
print(dicionario_simples)

# Verifique a existência de uma chave
if 'Joan' in dicionario_simples:
    print('Existe')
else:
    print('Não existe')

# Itere sobre o dicionário
print(' ')
print(dicionario_simples.keys())
print(' ')
print(dicionario_simples.values())
print(' ')
print(dicionario_simples.items())
print(' ')
for key, value in dicionario_simples.items():
    print('A pessoa de nome {} tem {} anos'.format(key, value))


    