# Inverta um dicionário
# Dado um dicionário {chave: valor} , crie um novo dicionário {valor: chave} .
from collections import defaultdict

original = {'a': 1, 'b': 2, 'c': 1}
invertido = defaultdict(list)

for key, value in original.items():
    invertido[value].append(key)

print(dict(invertido))