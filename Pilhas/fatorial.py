def fatorial_usando_pilha(n: int) -> int:
    pilha = []

    # Simula as chamadas recursivas empilhando os valores
    for i in range(n, 0, -1):
        pilha.append(i)

    resultado = 1

    # Agora desempilha (como se estivesse retornando da recursão)
    while len(pilha) > 0:
        resultado *= pilha.pop()

    return resultado


numero = 5
print(f"Fatorial de {numero} é: {fatorial_usando_pilha(numero)}")
# Saída: Fatorial de 5 é: 120
