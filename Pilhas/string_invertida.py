def inverter_string(texto: str) -> str:
    pilha = []

    # Empilha cada caractere da string
    for i in range(len(texto)):
        pilha.append(texto[i])

    invertida = ""

    # Desempilha os caracteres e monta a string invertida
    while len(pilha) > 0:
        invertida += pilha.pop()

    return invertida


texto_original = "algoritmo"
texto_invertido = inverter_string(texto_original)
print(f"Invertida: {texto_invertido}")  # Saída: "omtirogla"
