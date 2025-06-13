def eh_palindromo(palavra: str) -> bool:
    pilha = []

    # Empilha cada caractere da palavra
    for i in range(len(palavra)):
        pilha.append(palavra[i])

    invertida = ""

    # Desempilha os caracteres para montar a palavra invertida
    while len(pilha) > 0:
        invertida += pilha.pop()

    # Compara a palavra original com a invertida
    return palavra == invertida


palavra = input('Digite uma palavra: ')
if (eh_palindromo(palavra)):
    print(f"{palavra} é palindromo.")
else:
    print(f"{palavra} não é palindromo.")