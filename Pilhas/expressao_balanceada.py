def expressao_balanceada(expressao: str) -> bool:
    pilha = [] # Pilha para armazenar os símbolos de abertura
    pares = {')': '(', ']': '[', '}': '{'} # Dicionário com os pares de fechamento/abertura

    for i in range(len(expressao)):
        caractere = expressao[i]

        # Se for um símbolo de abertura, empilha

        if caractere in '([{':
            pilha.append(caractere)

         # Se for símbolo de fechamento, verifica se há algo na pilha e se o topo combina
        elif caractere in ')]}':
            if not pilha or pilha[-1] != pares[caractere]:
                return False
            pilha.pop()
# Se a pilha estiver vazia, todos os símbolos foram balanceados
    return len(pilha) == 0


print(expressao_balanceada("a + (b * c)"))       # True
print(expressao_balanceada("{[()]}"))            # True
print(expressao_balanceada("{[(])}"))            # False
print(expressao_balanceada("(((())))[]{}"))      # True
print(expressao_balanceada(")("))                # False
