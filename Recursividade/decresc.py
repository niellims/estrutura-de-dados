def imprimir_decrescente(n: int):
    if n == 0:
        return
    print(n)
    return imprimir_decrescente(n - 1)


print(imprimir_decrescente(5))