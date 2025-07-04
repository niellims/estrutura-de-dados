# 12. Detectar anagramas
# Dada uma lista de palavras, agrupe palavras que são anagramas entre si usando
# um dicionário.
def agrupar_anagramas(lista_palavras):
    grupos = {}

    for palavra in lista_palavras:
        letras_ordenadas = sorted(palavra)
        
        # Constrói a chave manualmente
        chave = ""
        for letra in letras_ordenadas:
            chave += letra  # concatena letra por letra

        # Adiciona no dicionário
        if chave in grupos:
            grupos[chave].append(palavra)
        else:
            grupos[chave] = [palavra]

    return grupos

palavras = ["amor", "roma", "carro", "corra", "ramo", "mora", "maro"]
resultado = agrupar_anagramas(palavras)

for chave, grupo in resultado.items():
    print(f"{chave}: {grupo}")
