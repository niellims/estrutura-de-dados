# Mesclar dois dicionários
# Dado dois dicionários com dados de alunos (nome e nota), una os dois, somando as notas dos alunos repetidos.

alunos1 = {
    "Ana": 8.0,
    "Carlos": 7.5,
    "Marina": 9.0
}

alunos2 = {
    "Carlos": 6.5,
    "João": 8.0,
    "Marina": 7.0
}

alunos_mesclados = {}

# Primeiro adiciona todos os alunos do primeiro dicionário
for nome, nota in alunos1.items():
    alunos_mesclados[nome] = nota

# Depois adiciona os alunos do segundo dicionário, somando se já existir
for nome, nota in alunos2.items():
    if nome in alunos_mesclados:
        alunos_mesclados[nome] += nota
    else:
        alunos_mesclados[nome] = nota

print(alunos_mesclados)
