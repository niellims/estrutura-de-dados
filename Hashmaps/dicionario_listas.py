# Dicionário com listas
# Crie um dicionário onde a chave seja o nome de um aluno e o valor seja uma lista
# de notas. Implemente uma função para calcular a média de cada aluno.

alunos = {
    "Ana": [8.0, 7.5, 9.0],
    "Carlos": [6.5, 7.0, 8.0],
    "Marina": [9.0, 8.5, 10.0],
    "João": []  # Exemplo com lista vazia
}

def calcular_medias(dicionario_alunos):
    for nome, notas in dicionario_alunos.items():
        if notas:  # Verifica se a lista de notas não está vazia
            media = sum(notas) / len(notas)
            print(f"{nome}: média = {media:.2f}")
        else:
            print(f"{nome}: sem notas registradas")

calcular_medias(alunos)